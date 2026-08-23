#!/usr/bin/env python3
"""Builds dashboard.html — the walkthrough page — from the prompt files in this folder.

The page carries the same prompt text the .md files carry. Editing a prompt file and
forgetting the page is the drift this script exists to stop. Run it after any prompt edit:

    python3 build_page.py

The <style> block is the page's own; everything below STYLE is content.
"""
import html
import pathlib
import re

HERE = pathlib.Path(__file__).parent
STYLE = (HERE / "page.css").read_text()

# Per agent: how you set it up, how you know it worked, and the one trap.
# The prompt body itself is read from the sibling .md file — never retyped here.
AGENTS = [
    dict(
        file="01-market-researcher-prompt.md",
        steps=[
            "Open a <strong>new chat</strong> inside your Outbound Stack project.",
            "Copy the prompt below and paste it in. Press enter.",
            "It works in five steps and shows each one as it finishes. Let it run.",
            "Read the brief. <strong>Delete every fact that has no date on it.</strong>",
            "Keep the top three sub-segments. You build for one of them at a time.",
        ],
        works="Every number in the brief has a source and a date you can click.",
        trap="A section that comes back empty and calm means a site blocked it. Ask which sources returned data and which refused.",
        needs=["A Claude account", "Free scraper", "Search key"],
        mins="15 min",
    ),
    dict(
        file="02-buyer-psychologist-prompt.md",
        steps=[
            "New chat, same project. The agent 1 brief has to be above it in the same conversation.",
            "Paste the prompt.",
            "<strong>Open three of the quotes it returns.</strong> Check they exist.",
            "Copy the top five phrases into your business block, on the &ldquo;words my buyers actually use&rdquo; line.",
            "Update the project knowledge so every later agent reads them.",
        ],
        works="One phrase makes you think &ldquo;I would never have written that.&rdquo; That is the one to build on.",
        trap="A quote with no URL is an invented quote. Delete it and make it redo that section.",
        needs=["A Claude account", "Free scraper", "Search key"],
        mins="20 min",
    ),
    dict(
        file="03-offer-writer-prompt.md",
        steps=[
            "New chat, same project.",
            "Paste the prompt.",
            "You want <strong>one</strong> promise back, with one number. If it gives you three, tell it to pick.",
            "Read every slot it pinned. Ask: could two people fill this two ways and both be right?",
            "Any slot that fails, send it back to be pinned harder before you move on.",
        ],
        works="You could hand the slot list to somebody else and get the same email back.",
        trap="&ldquo;Personalise this&rdquo; is not a pin. An unpinned slot gets invented differently every single time.",
        needs=["A Claude account"],
        mins="20 min",
    ),
    dict(
        file="04-list-builder-prompt.md",
        steps=[
            "New chat, same project.",
            "Paste the prompt. Give it your target: industry, size, country, job titles.",
            "<strong>Start with 200 leads. Not 5,000.</strong>",
            "When it comes back, read the BIN list first. That is where your search was wrong.",
            "Fix the search, run it again, then keep the KEEP list.",
        ],
        works="Things got binned, and you agree with why.",
        trap="A bad list at 5,000 costs you your sending domain. At 200 it costs you an afternoon.",
        needs=["Free scraper", "One contact tool"],
        mins="45 min",
    ),
    dict(
        file="05-contact-finder-prompt.md",
        steps=[
            "New chat, same project. Paste the KEEP list from agent 4.",
            "Paste the prompt.",
            "Check the source column. If every email came from one tool it never ran the order &mdash; send it back.",
            "<strong>Run every address through a verifier.</strong> Not just the guessed ones.",
            "Drop the invalids. Park catch-alls in their own list, never mixed into the main send.",
        ],
        works="Every row can tell you where the person came from and where the email came from.",
        trap="<code>info@</code> is not a person. Find the named human or drop the row.",
        needs=["One contact tool", "Email verifier", "Search key"],
        mins="30 min",
    ),
    dict(
        file="06-signal-finder-prompt.md",
        steps=[
            "New chat, same project. Paste the verified list.",
            "Paste the prompt.",
            "It filters for fit on free data <strong>first</strong>. Check that it did, before anything got enriched.",
            "<strong>Open five signals yourself.</strong> Read the date on the page, not the date on the filter.",
            "Split the list. Live signal &rarr; campaign. No signal &rarr; watch list. Re-run it weekly.",
        ],
        works="Most of your list did not make it, and you can name what changed at every company that did.",
        trap="&ldquo;They are an accounting firm&rdquo; is not a signal. A signal is a change, with a date.",
        needs=["Free scraper", "Search key", "One contact tool"],
        mins="45 min",
    ),
    dict(
        file="07-email-writer-prompt.md",
        steps=[
            "New chat, same project. Paste the signalled list.",
            "Paste the prompt.",
            "<strong>Count the words on email 1 yourself.</strong> Under 64, or cut.",
            "Make the thing your follow-up offers, <strong>before</strong> you send. It has to actually exist.",
            "Load it as its own campaign with its own list. Two emails, day one and day two. Then it stops.",
        ],
        works="Line one names what changed. Line two is what that means for them.",
        trap="Never load signal-routed copy as variants. Sending tools rotate variants at random, so the wrong email reaches the wrong lead and nothing tells you.",
        needs=["A Claude account", "Sending tool"],
        mins="30 min",
    ),
    dict(
        file="08-inbox-agent-prompt.md",
        steps=[
            "New chat, same project. Paste the prompt. Leave the tab open all day.",
            "Paste your two real open call times in each morning.",
            "When a reply lands, paste it in with the email it answers.",
            "Read the colour and the draft. Change what you want. <strong>You</strong> press send.",
            "Only once that works by hand: wire the webhook so the draft is already waiting.",
        ],
        works="You paste a reply and would only change a word or two of what comes back.",
        trap="Set every automated message step to create a <strong>draft</strong>, never to send.",
        needs=["A Claude account", "Sending tool"],
        mins="10 min",
    ),
]

BLOCK = re.compile(r"```\n(.*?)\n```", re.S)


def read_agent(spec):
    text = (HERE / spec["file"]).read_text()
    n, title = re.search(r"^# Agent (\d) — (.+)$", text, re.M).groups()
    lead = re.search(r"^\*\*What it answers:\*\* (.+)$", text, re.M).group(1)
    prompt = BLOCK.search(text).group(1)
    return {**spec, "n": n, "title": title, "lead": lead, "prompt": prompt}


def prompt_block(agent):
    body = html.escape(agent["prompt"])
    return f"""      <div class="promptbox">
        <div class="hd">
          <span class="subj">the prompt &mdash; paste it whole</span>
          <button class="copybtn" type="button">Copy</button>
        </div>
        <pre class="bd">{body}</pre>
      </div>"""


def agent_section(agent):
    steps = "\n".join(f"            <li>{s}</li>" for s in agent["steps"])
    needs = "\n".join(
        f'            <span class="tool">{n}</span>' for n in agent["needs"]
    )
    return f"""    <article class="arow" id="a{agent['n']}">
      <div class="idx">0{agent['n']}</div>
      <div>
        <h3>{agent['title']}</h3>
        <p class="does">Answers {agent['lead']}</p>
        <div class="adetail">
          <div class="acol">
            <h4>Set it up &mdash; {agent['mins']}</h4>
            <ol class="steps">
{steps}
            </ol>
          </div>
          <div class="acol">
            <h4>What you need open</h4>
            <div class="toolrow">
{needs}
            </div>
            <div class="grp">
              <span>You know it worked when</span>
              <p class="wintext">{agent['works']}</p>
            </div>
          </div>
        </div>
{prompt_block(agent)}
        <p class="fact"><strong>The trap:</strong> {agent['trap']}</p>
      </div>
    </article>"""


agents = [read_agent(a) for a in AGENTS]

BUSINESS_BLOCK = BLOCK.search((HERE / "claude-md-snippet.md").read_text()).group(1)

nav = "\n".join(
    f'        <a class="node" href="#a{a["n"]}"><span class="n">0{a["n"]}</span>'
    f'<span class="t">{a["title"]}</span><span class="d">{a["mins"]}</span></a>'
    for a in agents
)

body = f"""<title>The Eight Agents</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;450;500&display=swap">

{STYLE}

<div class="topbar">
  <div class="wrap">
    <span class="brandmark">GAP &middot; Build Vault</span>
    <div class="chips">
      <div class="chip"><span class="v">8</span><span class="k">agents</span></div>
      <div class="chip"><span class="v">25 min</span><span class="k">to the first one</span></div>
      <div class="chip"><span class="v">No code</span><span class="k">nothing to install</span></div>
    </div>
  </div>
</div>

<main>

<section>
  <div class="wrap">
    <p class="eyebrow">Build it yourself &middot; <b>free, no sign-up</b></p>
    <h1>Set up all eight.<br>One at a time.</h1>
    <p class="sub">This is the install, not the pitch. Every agent below has the steps, the prompt to paste, and the one thing that goes wrong. <strong>Start at the top and do them in order</strong> &mdash; agent 7 does not work without agent 2.</p>
    <p class="sub">Nothing to install. No code. Four of the six tools you need, you almost certainly already pay for.</p>
    <div class="phases navgrid">
{nav}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">First &middot; <b>15 minutes, once</b></p>
    <h2>What you need open before you start.</h2>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Tool</th><th>What it does here</th><th>Cost</th></tr></thead>
        <tbody>
          <tr><td><strong>Claude</strong></td><td>Runs all eight prompts</td><td>Free to start</td></tr>
          <tr><td><strong>A free scraper</strong></td><td>Opens and reads company sites, forums, review pages</td><td>Free</td></tr>
          <tr><td><strong>A search key</strong></td><td>Finds the threads, the job ads, the people</td><td>Free tier is enough to begin</td></tr>
          <tr><td><strong>One contact tool</strong></td><td>Finds the person and their email</td><td>You probably already pay for one</td></tr>
          <tr><td><strong>An email verifier</strong></td><td>Checks every address before anything is sent to it</td><td>100 free, then about $1.80 per 1,000</td></tr>
          <tr><td><strong>A sending tool</strong></td><td>Sends the two emails, catches the replies</td><td>Whatever you already use</td></tr>
        </tbody>
      </table>
    </div>
    <p class="after"><strong>You can run agents 1, 2, 3 and 8 with nothing but a Claude account.</strong> That is half the stack, and agent 8 is the fastest win on this page. Start there if you want to see it work before you set anything else up.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Step 0 &middot; <b>do this before agent 1</b></p>
    <h2>Teach it your business, once.</h2>
    <p class="sub">Every one of the eight reads this block. Fill it in one time and you never type any of it again.</p>
    <div class="setup">
      <div class="sstep"><span class="sn">1</span><div><b>Make the project</b><p>Open <a class="link" href="https://claude.ai">claude.ai</a>, sign in, click <strong>Projects</strong> in the left sidebar, then <strong>New project</strong>. Name it <code>Outbound Stack</code>.</p></div></div>
      <div class="sstep"><span class="sn">2</span><div><b>Fill in the block below</b><p>Every bracket. If you do not have the thing, write what you do have. An empty slot is where an agent invents a price or a client result, and that reaches a real buyer.</p></div></div>
      <div class="sstep"><span class="sn">3</span><div><b>Paste it in as knowledge</b><p>Inside the project, find <strong>Project knowledge</strong> on the right. Click <strong>Add content</strong>, then <strong>Add text</strong>. Paste it. Save.</p></div></div>
      <div class="sstep"><span class="sn">4</span><div><b>Check it took</b><p>Open a new chat in the project and ask &ldquo;what do I sell and who do I sell it to&rdquo;. It should answer with your real offer and your real buyer, not a generic description.</p></div></div>
    </div>
    <div class="promptbox">
      <div class="hd">
        <span class="subj">your business block</span>
        <button class="copybtn" type="button">Copy</button>
      </div>
      <pre class="bd">{html.escape(BUSINESS_BLOCK)}</pre>
    </div>
    <p class="fact">Leave the <strong>&ldquo;words my buyers actually use&rdquo;</strong> line blank for now. Agent 2 fills it in, and it is the most valuable line on the page.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Step 0.5 &middot; <b>15 minutes, once</b></p>
    <h2>Get the six logins first.</h2>
    <p class="sub">Do this in one sitting, before agent 1. Stopping halfway through a build to go and make an account is how people put this page down and never come back.</p>
    <p class="sub">Open a plain text file. Every time you get a key, paste it in with the name of the tool next to it. You will need four of them again later.</p>
    <div class="setup">
      <div class="sstep"><span class="sn">1</span><div><b>Claude &mdash; runs all eight</b>
        <p><strong>Sign up:</strong> <a class="link" href="https://claude.ai">claude.ai</a>. <strong>Free tier:</strong> free works to start &mdash; you will hit limits on the long research runs. Pro is $20 a month, or $17 if you pay for the year, and buys you higher limits. <strong>No key needed:</strong> you use it in the browser. <strong>Check it worked:</strong> you can open a new chat and it answers.</p></div></div>
      <div class="sstep"><span class="sn">2</span><div><b>Scrapling &mdash; the free scraper</b>
        <p><strong>Get it:</strong> <a class="link" href="https://github.com/D4Vinci/Scrapling">github.com/D4Vinci/Scrapling</a>, free and open source. <strong>Install:</strong> <code>pip install "scrapling[fetchers]"</code> then <code>scrapling install</code>. <strong>No key.</strong> <strong>Check it worked:</strong> run <code>scrapling shell</code> &mdash; if it opens, you are done. If <code>pip</code> is not a command on your machine, install Python first from <a class="link" href="https://python.org">python.org</a>.</p></div></div>
      <div class="sstep"><span class="sn">3</span><div><b>Serper &mdash; the search key</b>
        <p><strong>Sign up:</strong> <a class="link" href="https://serper.dev">serper.dev</a>, no card. <strong>Free tier:</strong> 2,500 searches. That is plenty for the first niche. <strong>The key:</strong> log in, open the <strong>API Key</strong> page in the dashboard, copy the string. <strong>Where it goes:</strong> your text file, and later into the tool that does the searching. <strong>Check it worked:</strong> the dashboard shows your credit balance and it is not zero.</p></div></div>
      <div class="sstep"><span class="sn">4</span><div><b>A contact tool &mdash; finds the person</b>
        <p><strong>Use what you already pay for.</strong> Apollo, Clay, ZoomInfo, Lusha &mdash; any of them. Most people reading this already have one. <strong>If you have none:</strong> start with <a class="link" href="https://apollo.io">apollo.io</a>, which has a free plan you can search on. <strong>The key:</strong> in Apollo it is under <strong>Settings &rarr; Integrations &rarr; API</strong>; API access is not on every plan, so check yours before you plan to script it. <strong>Check it worked:</strong> search one company you know and see a real name come back.</p></div></div>
      <div class="sstep"><span class="sn">5</span><div><b>MillionVerifier &mdash; the email verifier</b>
        <p><strong>Sign up:</strong> <a class="link" href="https://www.millionverifier.com">millionverifier.com</a>. <strong>Free tier:</strong> 100 credits on signup, no card. <strong>Cost after that:</strong> from about $1.80 per 1,000, cheaper in bulk, and credits do not expire. <strong>The key:</strong> log in, open <strong>API</strong> in the left menu. <strong>Check it worked:</strong> paste your own email address into the single-email checker and it comes back good.</p>
        <p>One thing that catches people out: if you call it from a script, send a normal browser user-agent header. It returns a 403 without one, and a 403 looks exactly like a dead key.</p></div></div>
      <div class="sstep"><span class="sn">6</span><div><b>A sending tool &mdash; sends the two emails</b>
        <p><strong>Whatever you already use</strong> &mdash; Smartlead, Instantly, Lemlist, Apollo. <strong>Two things have to be true of it:</strong> it can hold a sequence of two emails, and it can fire a webhook when somebody replies. Almost all of them can. <strong>Check it worked:</strong> send one email to yourself, reply to it, and confirm the reply shows up in the tool.</p></div></div>
    </div>
    <p class="eyebrow" style="margin-top:38px">Before agent 1 &middot; <b>tick all six</b></p>
    <div class="checks">
      <label class="check"><input type="checkbox"><span>Claude account, signed in, project made</span></label>
      <label class="check"><input type="checkbox"><span>Scrapling installed &mdash; <code>scrapling shell</code> opens</span></label>
      <label class="check"><input type="checkbox"><span>Serper key copied, balance shows 2,500</span></label>
      <label class="check"><input type="checkbox"><span>Contact tool logged in, one test search returned a real name</span></label>
      <label class="check"><input type="checkbox"><span>MillionVerifier key copied, my own address came back good</span></label>
      <label class="check"><input type="checkbox"><span>Sending tool connected, test reply landed in it</span></label>
      <label class="check"><input type="checkbox"><span>All my keys are in one text file with the tool name beside each</span></label>
    </div>
    <p class="fact">Six boxes ticked and the rest of this page is just pasting prompts. <strong>Agents 1, 2, 3 and 8 need nothing but the first box</strong> &mdash; if you only have 20 minutes tonight, do box one and go to agent 8.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">The eight &middot; <b>in order</b></p>
    <h2>Each one, start to finish.</h2>
    <p class="sub">Do not skip to agent 7. The research is what produced the subject line, and you cannot work backwards to it.</p>
    <div class="agents">
{chr(10).join(agent_section(a) for a in agents)}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Your first week &middot; <b>four days</b></p>
    <h2>Do it in this order and it takes four evenings.</h2>
    <div class="setup">
      <div class="sstep"><span class="sn">1</span><div><b>Day one &mdash; the block, then learn</b><p>Step 0, then agents 1 and 2. Delete every fact with no date. Check three quotes yourself. Put the top five phrases back in your block.</p></div></div>
      <div class="sstep"><span class="sn">2</span><div><b>Day two &mdash; build the list</b><p>Agents 3, 4 and 5. Two hundred leads, not five thousand. Read the bin list. Verify every address.</p></div></div>
      <div class="sstep"><span class="sn">3</span><div><b>Day three &mdash; time it</b><p>Agent 6. Check five signals at the source. Split the list into campaign and watch list.</p></div></div>
      <div class="sstep"><span class="sn">4</span><div><b>Day four &mdash; send and answer</b><p>Agents 7 and 8. Count the words. Make the follow-up&rsquo;s offer before you send. Test a reply on yourself.</p></div></div>
      <div class="sstep"><span class="sn">5</span><div><b>Then, every Friday &mdash; 20 minutes</b><p>Reply rate <strong>per signal type</strong>, never blended. Re-run agent 6 on the watch list, because signals expire. Write down what you changed and the date you changed it.</p></div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Do not skip these &middot; <b>the gates</b></p>
    <h2>Seven checks, and one that holds up the rest.</h2>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Gate</th><th>Where</th><th>What happens without it</th></tr></thead>
        <tbody>
          <tr><td><strong>Every fact carries its date</strong></td><td class="num">Agent 1</td><td>You act on an 18-month-old market as if it were today</td></tr>
          <tr><td><strong>Quotes are sourced or dropped</strong></td><td class="num">Agent 2</td><td>An invented phrase reaches a buyer and reads as invented</td></tr>
          <tr><td><strong>Every slot is pinned</strong></td><td class="num">Agent 3</td><td>The same line ships four different ways and it looks like a writer problem</td></tr>
          <tr><td><strong>Somebody opens and reads the sites</strong></td><td class="num">Agent 4</td><td>A quarter of your list is the wrong kind of company</td></tr>
          <tr><td><strong>Every address verified</strong></td><td class="num">Agent 5</td><td>Bounces, then your domain</td></tr>
          <tr><td><strong>Signal confirmed at the source</strong></td><td class="num">Agent 6</td><td>You open with a change that never happened</td></tr>
          <tr><td><strong>Word count on email 1</strong></td><td class="num">Agent 7</td><td>It becomes a pitch, and it gets deleted</td></tr>
          <tr><td><strong>A human presses send</strong></td><td class="num">Agent 8</td><td>Eventually it sends something you would not have</td></tr>
          <tr><td><strong>A block fails loudly</strong></td><td class="num">All eight</td><td>An empty result looks exactly like &ldquo;nothing to find&rdquo;, and you ship a decision built on it</td></tr>
        </tbody>
      </table>
    </div>
    <p class="after">That last one holds up everything else. When a site blocks an agent, it has to say so out loud. An agent that returns an empty list on a block is the most expensive thing in this build, because <strong>nothing looks wrong</strong>.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta">
      <h2>That is the whole build. Take it.</h2>
      <p>Every prompt on this page is also a file in the public folder, with the troubleshooting tables that did not fit here. No sign-up, no email wall, nothing to unsubscribe from.</p>
      <p><strong>The folder:</strong> <a class="link" href="https://github.com/gary-chakraborty/gap-build-vault/tree/main/builds/outbound-agent-stack">github.com/gary-chakraborty/gap-build-vault</a> &rarr; <code>builds/outbound-agent-stack</code></p>
      <p>If you would rather we built it inside your company &mdash; or your pipeline is stuck &mdash; that is what we do. One niche, one signal, two emails, and <strong>15 to 25 qualified sales calls a month</strong> with people actually looking for what you sell.</p>
      <a class="ctabtn" href="https://form.jotform.com/262194392563059">Tell us how this went &rarr;</a>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="wrap">GAP Build Vault &middot; the outbound agent stack &middot; the prompts on this page are the same text as the files in the folder</div>
</footer>

<script>
(function () {{
  document.querySelectorAll(".copybtn").forEach(function (btn) {{
    btn.addEventListener("click", function () {{
      var pre = btn.closest(".promptbox").querySelector(".bd");
      navigator.clipboard.writeText(pre.innerText).then(function () {{
        btn.textContent = "Copied";
        btn.classList.add("done");
        setTimeout(function () {{
          btn.textContent = "Copy";
          btn.classList.remove("done");
        }}, 1600);
      }}).catch(function () {{}});
    }});
  }});
}})();
</script>
"""

(HERE / "dashboard.html").write_text(body)
print(f"dashboard.html written — {len(agents)} agents, {len(body)} bytes")
