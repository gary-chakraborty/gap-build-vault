#!/usr/bin/env python3
"""llm_router_example.py — one AI call, three providers, and it fails loudly.

Order: Claude -> Gemini -> OpenAI. A provider with no key, no credit, a bad key or a
rate limit is skipped and the reason is printed. If every provider fails, it RAISES.
It never returns an empty string, because an empty answer looks like "it checked and
found nothing", and nothing tells you it was really a failure.

Keys: read from environment variables, or from secrets/<name>.env files next to this
script (one line each: ANTHROPIC_API_KEY=..., GEMINI_API_KEY=..., OPENAI_API_KEY=...).

Models are set by environment variable so you can change them without editing code:
  CLAUDE_MODEL (default claude-sonnet-5), GEMINI_MODEL (default gemini-2.5-flash),
  OPENAI_MODEL (default gpt-4.1-mini)

Use:
  python3 llm_router_example.py "Say hello in five words"
  from llm_router_example import ask; text = ask("...")
"""
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
SECRETS = HERE / "secrets"


class RouterError(RuntimeError):
    """Every provider failed. The message lists why, provider by provider."""


def _key(name: str) -> str | None:
    if os.environ.get(name):
        return os.environ[name]
    for f in SECRETS.glob("*.env") if SECRETS.exists() else []:
        for line in f.read_text().splitlines():
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip().strip('"')
    return None


def _post(url: str, headers: dict, body: dict, timeout: int = 60) -> dict:
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST")
    # Some APIs block the default Python user agent. Send a normal one.
    req.add_header("User-Agent", "Mozilla/5.0 (llm-router-example)")
    req.add_header("Content-Type", "application/json")
    for k, v in headers.items():
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def _claude(prompt: str, max_tokens: int) -> str:
    key = _key("ANTHROPIC_API_KEY")
    if not key:
        raise LookupError("no ANTHROPIC_API_KEY")
    d = _post("https://api.anthropic.com/v1/messages",
              {"x-api-key": key, "anthropic-version": "2023-06-01"},
              {"model": os.environ.get("CLAUDE_MODEL", "claude-sonnet-5"),
               "max_tokens": max_tokens,
               "messages": [{"role": "user", "content": prompt}]})
    return "".join(b.get("text", "") for b in d.get("content", []) if b.get("type") == "text")


def _gemini(prompt: str, max_tokens: int) -> str:
    key = _key("GEMINI_API_KEY")
    if not key:
        raise LookupError("no GEMINI_API_KEY")
    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    d = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
              {"x-goog-api-key": key},
              {"contents": [{"parts": [{"text": prompt}]}],
               "generationConfig": {"maxOutputTokens": max_tokens}})
    parts = (d.get("candidates") or [{}])[0].get("content", {}).get("parts", [])
    return "".join(p.get("text", "") for p in parts)


def _openai(prompt: str, max_tokens: int) -> str:
    key = _key("OPENAI_API_KEY")
    if not key:
        raise LookupError("no OPENAI_API_KEY")
    d = _post("https://api.openai.com/v1/chat/completions",
              {"Authorization": f"Bearer {key}"},
              {"model": os.environ.get("OPENAI_MODEL", "gpt-4.1-mini"),
               "max_tokens": max_tokens,
               "messages": [{"role": "user", "content": prompt}]})
    return d["choices"][0]["message"]["content"] or ""


PROVIDERS = [("claude", _claude), ("gemini", _gemini), ("openai", _openai)]


def ask(prompt: str, max_tokens: int = 1024) -> str:
    reasons = []
    for name, call in PROVIDERS:
        try:
            text = call(prompt, max_tokens).strip()
        except LookupError as e:
            reasons.append(f"{name}: skipped ({e})")
            continue
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")[:200]
            # 401/403 bad key, 402 no credit, 429 rate limit or quota, 400 "credit balance too low"
            reasons.append(f"{name}: HTTP {e.code} {body}")
            continue
        except (urllib.error.URLError, TimeoutError, KeyError, IndexError, ValueError) as e:
            reasons.append(f"{name}: {type(e).__name__} {e}")
            continue
        if not text:
            reasons.append(f"{name}: empty answer (treated as a failure)")
            continue
        if reasons:
            print("router: fell through -> " + " | ".join(reasons), file=sys.stderr)
        print(f"router: answered by {name}", file=sys.stderr)
        return text
    raise RouterError("every provider failed -> " + " | ".join(reasons))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('usage: python3 llm_router_example.py "your prompt"')
    try:
        print(ask(sys.argv[1]))
    except RouterError as e:
        print(f"FAILED LOUDLY: {e}", file=sys.stderr)
        sys.exit(2)
