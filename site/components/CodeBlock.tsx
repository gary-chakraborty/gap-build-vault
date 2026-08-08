"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Check, Copy } from "./icons";

// Prompts are the product on these pages, so every block hands itself over in
// one click. If the clipboard API is blocked the button says so instead of
// pretending it worked.
export default function CodeBlock({
  code,
  language,
}: {
  code: string;
  language?: string;
}) {
  const [state, setState] = useState<"idle" | "copied" | "failed">("idle");
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    return () => {
      if (timer.current) clearTimeout(timer.current);
    };
  }, []);

  const copy = useCallback(async () => {
    try {
      if (navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(code);
      } else {
        throw new Error("clipboard unavailable");
      }
      setState("copied");
    } catch {
      setState("failed");
    }
    if (timer.current) clearTimeout(timer.current);
    timer.current = setTimeout(() => setState("idle"), 2200);
  }, [code]);

  const label =
    state === "copied" ? "Copied" : state === "failed" ? "Press Ctrl+C" : "Copy";

  return (
    <div className="code-block">
      <div className="code-head">
        <span className="code-lang">{language || "text"}</span>
        <button
          type="button"
          className="copy-btn"
          onClick={copy}
          data-copied={state === "copied"}
          aria-label={
            state === "copied" ? "Copied to clipboard" : "Copy code to clipboard"
          }
        >
          {state === "copied" ? <Check /> : <Copy />}
          {label}
        </button>
      </div>
      <pre>
        <code>{code}</code>
      </pre>
    </div>
  );
}
