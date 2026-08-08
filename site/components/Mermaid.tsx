"use client";

import { useEffect, useId, useState } from "react";
import { Diagram } from "./icons";

// Mermaid is loaded on demand, in the browser only, so the static export never
// tries to render a diagram at build time and the library stays out of the
// bundle for pages that have no diagrams.
const THEME = {
  theme: "base" as const,
  darkMode: true,
  fontFamily:
    '"Inter Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
  themeVariables: {
    background: "transparent",
    primaryColor: "#1b2330",
    primaryTextColor: "#edf1f7",
    primaryBorderColor: "#3b82f6",
    secondaryColor: "#161d27",
    secondaryTextColor: "#edf1f7",
    secondaryBorderColor: "#3f4b5b",
    tertiaryColor: "#12181f",
    tertiaryTextColor: "#a7b2c0",
    tertiaryBorderColor: "#3f4b5b",
    lineColor: "#5a6878",
    textColor: "#dbe3ec",
    mainBkg: "#1b2330",
    nodeBorder: "#3b82f6",
    clusterBkg: "rgba(255,255,255,0.02)",
    clusterBorder: "#303b48",
    edgeLabelBackground: "#0d1117",
    titleColor: "#edf1f7",
    noteBkgColor: "#161d27",
    noteTextColor: "#dbe3ec",
    noteBorderColor: "#3f4b5b",
    actorBkg: "#1b2330",
    actorBorder: "#3b82f6",
    actorTextColor: "#edf1f7",
    signalColor: "#a7b2c0",
    signalTextColor: "#dbe3ec",
    labelBoxBkgColor: "#1b2330",
    labelBoxBorderColor: "#3b82f6",
    labelTextColor: "#edf1f7",
    loopTextColor: "#dbe3ec",
    sectionBkgColor: "#161d27",
    sectionBkgColor2: "#12181f",
    altSectionBkgColor: "#12181f",
    gridColor: "#303b48",
    taskBkgColor: "#1b2330",
    taskTextColor: "#edf1f7",
    taskTextOutsideColor: "#dbe3ec",
    taskBorderColor: "#3b82f6",
    activeTaskBkgColor: "#3b82f6",
    activeTaskBorderColor: "#7aa9fb",
    doneTaskBkgColor: "#232b36",
    doneTaskBorderColor: "#3f4b5b",
    pie1: "#3b82f6",
    pie2: "#7aa9fb",
    pie3: "#34d399",
    pie4: "#a78bfa",
  },
};

function naturalSize(svg: string): string {
  const viewBox = /viewBox="([\d.\-\s]+)"/.exec(svg)?.[1];
  const width = viewBox ? Number(viewBox.trim().split(/\s+/)[2]) : NaN;
  const out = svg.replace(/max-width:\s*[\d.]+px;?/g, "");
  if (!Number.isFinite(width) || width <= 0) return out;
  return out.replace(/width="100%"/, `width="${Math.round(width)}"`);
}

export default function Mermaid({ chart }: { chart: string }) {
  const reactId = useId();
  const [svg, setSvg] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    let cancelled = false;
    const domId = `mermaid-${reactId.replace(/[^a-zA-Z0-9]/g, "")}`;

    (async () => {
      try {
        const mermaid = (await import("mermaid")).default;
        mermaid.initialize({
          startOnLoad: false,
          securityLevel: "strict",
          ...THEME,
        });
        const { svg: rendered } = await mermaid.render(domId, chart);
        // Mermaid ships the svg at width="100%" with a max-width, so it
        // stretches on a wide screen and shrinks to an unreadable thumbnail on
        // a phone. Pin it to the size it was drawn at and let the frame scroll.
        if (!cancelled) setSvg(naturalSize(rendered));
      } catch (err) {
        // A broken diagram must say so, not vanish.
        if (!cancelled) {
          setError(err instanceof Error ? err.message : "Diagram failed to render.");
        }
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [chart, reactId]);

  return (
    <figure className="diagram">
      <div className="diagram-head">
        <Diagram />
        Diagram
      </div>
      {svg ? (
        <div
          className="diagram-body"
          role="img"
          aria-label="Flow diagram for this build"
          dangerouslySetInnerHTML={{ __html: svg }}
        />
      ) : error ? (
        <pre className="diagram-error">
          Diagram could not be drawn: {error}
          {"\n\n"}
          {chart}
        </pre>
      ) : (
        <div className="diagram-pending">Drawing diagram…</div>
      )}
    </figure>
  );
}
