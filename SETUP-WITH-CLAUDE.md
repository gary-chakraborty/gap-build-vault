# Set this up by talking to Claude

Every build in this vault is prompts, checklists and one small script. You do not have to code. You do have to give
Claude the files and answer its questions.

Two ways in. Pick one. Option A needs nothing but a browser. Option B is faster once you have more than one build
running, and it can run the script for you.

---

## Option A: in your browser, no code at all

1. Open https://github.com/gary-chakraborty/gap-build-vault, click the green **Code** button, then **Download ZIP**.
   Unzip it.
2. Go to https://claude.ai and sign in. Free works to start.
3. In the left sidebar click **Projects**, then **New project**. Name it after the build, for example `Booking Desk`.
4. On the right, find **Project knowledge**, click **Add content**, and upload every `.md` file from that build's
   folder.
5. Open a new chat inside the project and paste this:

```text
You have the files for one build from the GAP Build Vault in your project knowledge.

Read all of them first. Then:
1. Tell me in five lines what this build does and what it needs from me.
2. Ask me the questions you need answered about my business, one at a time, and wait
   for each answer before asking the next.
3. When you have enough, give me the first thing I have to do today, with the exact
   text to paste or send.

Do not skip a question because you can guess the answer. If I give you a vague answer,
ask again with a question that needs a number or a name.
```

6. Work through its questions. Keep the chat open: it is the project's memory.

**You know this worked when:** it asks you something specific about your own business in the first reply.

---

## Option B: in your editor, with Claude Code

Claude Code reads the whole folder itself, edits files in place and runs the scripts. It works in VS Code, Cursor,
Antigravity, JetBrains, or a plain terminal.

1. Install it: https://claude.com/claude-code. In VS Code, Cursor or Antigravity, install the Claude Code extension
   from the extension panel and sign in with your Claude account.
2. Get the folder on your machine:

```bash
git clone https://github.com/gary-chakraborty/gap-build-vault.git
cd gap-build-vault
```

3. Open that folder in your editor. Open Claude Code in it (in VS Code and Antigravity it is a panel on the side; in a
   terminal, type `claude`).
4. Paste this:

```text
This folder is the GAP Build Vault. Read README.md, then read every file in
builds/<the build you want>.

Then:
1. Tell me in five lines what this build does and what it needs from me.
2. Ask me the questions you need answered about my business, one at a time, and wait
   for each answer.
3. Write my answers into a file called my-setup.md in this folder, so we do not lose
   them, and show me the first thing to do today with the exact text to paste or send.

Rules: never invent a number, a price or a client result for me. If you do not have a
fact, ask me for it or write "missing" and move on.
```

5. From then on, ask it for the work in plain English: "split this list by lane", "write today's call list from these
   threads", "run the scoreboard and tell me what moved".

**You know this worked when:** `my-setup.md` exists and has your real answers in it, not brackets.

---

## What Claude does, and what stays yours

| Claude does this | You still do this |
|---|---|
| Reads the build and asks what it needs | Answer with real numbers, not guesses |
| Sorts lists, drafts messages, builds the call list | Read the first ten before any of it goes out |
| Runs the scoreboard and explains the numbers | Decide what to change next week |
| Writes your answers down so the next chat has them | Keep your API keys out of the chat, in your own file |

Never paste an API key into a chat message. In Option B, put keys in a `.env` file in the folder and tell Claude the
file name. It can read the file without the key ever appearing in the conversation.

---

## When you get stuck

| What you see | What to do |
|---|---|
| It answers in generalities about your market | Your answers were general. Give it one real client, one real number |
| It writes a message you would never send | Paste a message you actually sent and tell it to match that voice |
| It invents a price or a result | Tell it the real one, or "we do not have that yet". Then check the last thing it wrote |
| A script stops with `STOPPED:` and a reason | Paste the whole line into the chat. That message names the fix |
| A long chat starts drifting | Start a new one. In Option A the project knowledge reloads; in Option B point it at `my-setup.md` |
