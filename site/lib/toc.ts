// One slug function, used by both the in-page nav and the heading renderer,
// so every nav link always lands on a heading that exists.

export type Section = { id: string; title: string };

export function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/[`*_~]/g, "")
    .replace(/[^\w\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

/** Top level (##) headings of a README, in document order, skipping fenced code. */
export function getSections(markdown: string): Section[] {
  const sections: Section[] = [];
  const seen = new Map<string, number>();
  let inFence = false;

  for (const rawLine of markdown.split("\n")) {
    const line = rawLine.trimEnd();

    if (/^\s{0,3}(```|~~~)/.test(line)) {
      inFence = !inFence;
      continue;
    }
    if (inFence) continue;

    const match = /^##\s+(.+)$/.exec(line);
    if (!match) continue;

    const title = match[1].replace(/#+\s*$/, "").trim();
    const base = slugify(title);
    if (!base) continue;

    const count = seen.get(base) ?? 0;
    seen.set(base, count + 1);
    sections.push({ id: count === 0 ? base : `${base}-${count}`, title });
  }

  return sections;
}
