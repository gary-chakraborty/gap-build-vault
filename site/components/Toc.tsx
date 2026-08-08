"use client";

import { useEffect, useState } from "react";
import type { Section } from "../lib/toc";

// Marks the section you are reading. Falls back to plain links if the browser
// has no IntersectionObserver — the nav still works, it just stops tracking.
export default function Toc({ sections }: { sections: Section[] }) {
  const [active, setActive] = useState(sections[0]?.id ?? "");

  useEffect(() => {
    if (typeof IntersectionObserver === "undefined") return;

    const headings = sections
      .map((section) => document.getElementById(section.id))
      .filter((el): el is HTMLElement => Boolean(el));
    if (headings.length === 0) return;

    const observer = new IntersectionObserver(
      () => {
        const line = window.scrollY + 140;
        let current = headings[0];
        for (const heading of headings) {
          if (heading.offsetTop <= line) current = heading;
        }
        setActive(current.id);
      },
      { rootMargin: "-100px 0px -60% 0px", threshold: [0, 1] }
    );

    for (const heading of headings) observer.observe(heading);
    return () => observer.disconnect();
  }, [sections]);

  if (sections.length < 3) return null;

  return (
    <nav className="toc" aria-label="Sections of this build">
      <p className="toc-label">On this page</p>
      <ol>
        {sections.map((section) => (
          <li key={section.id}>
            <a
              href={`#${section.id}`}
              data-active={active === section.id}
              aria-current={active === section.id ? "true" : undefined}
            >
              {section.title}
            </a>
          </li>
        ))}
      </ol>
    </nav>
  );
}
