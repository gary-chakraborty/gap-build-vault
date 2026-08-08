"use client";

import { isValidElement, useRef, type ReactNode } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { REPO_URL } from "../config";
import { slugify } from "../lib/toc";
import CodeBlock from "./CodeBlock";
import Mermaid from "./Mermaid";
import { Alert, Bulb, Flag, Info, Stop } from "./icons";

// Links inside a README point at files in the same build folder.
// Send those to GitHub so people can open and download them.
function resolveHref(href: string, slug: string): string {
  if (!href) return href;
  if (/^(https?:|mailto:|tel:|#)/i.test(href)) return href;
  const clean = href.replace(/^\.\//, "");
  return `${REPO_URL}/blob/main/builds/${slug}/${clean}`;
}

/* ---------- GitHub alert blocks -> callout boxes ---------- */

const CALLOUTS = {
  note: { label: "Note", Icon: Info },
  tip: { label: "Tip", Icon: Bulb },
  important: { label: "Important", Icon: Flag },
  warning: { label: "Watch out", Icon: Alert },
  caution: { label: "Do not", Icon: Stop },
} as const;

type CalloutKind = keyof typeof CALLOUTS;

type MdNode = {
  type?: string;
  value?: string;
  children?: MdNode[];
  data?: Record<string, unknown>;
};

// `> [!TIP]` and friends are not part of GFM, so lift them here: mark the
// blockquote as a callout and strip the marker out of the text.
function remarkCallouts() {
  return (tree: MdNode) => {
    walk(tree);
  };

  function walk(node: MdNode) {
    if (!node.children) return;
    for (const child of node.children) {
      if (child.type === "blockquote") convert(child);
      walk(child);
    }
  }

  function convert(quote: MdNode) {
    const first = quote.children?.[0];
    if (!first || first.type !== "paragraph") return;
    const text = first.children?.[0];
    if (!text || text.type !== "text" || typeof text.value !== "string") return;

    const match = /^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\][ \t]*\r?\n?/i.exec(
      text.value
    );
    if (!match) return;

    const kind = match[1].toLowerCase() as CalloutKind;
    text.value = text.value.slice(match[0].length);

    // Marker was on its own line: drop the now-empty paragraph.
    if (!text.value.trim() && (first.children?.length ?? 0) === 1) {
      quote.children = quote.children?.slice(1);
    }

    quote.data = {
      ...(quote.data ?? {}),
      hName: "div",
      hProperties: {
        className: `callout callout-${kind}`,
        "data-callout": kind,
      },
    };
  }
}

function Callout({
  kind,
  children,
}: {
  kind: CalloutKind;
  children: ReactNode;
}) {
  const { label, Icon } = CALLOUTS[kind];
  return (
    <div className={`callout callout-${kind}`}>
      <p className="callout-head">
        <Icon />
        {label}
      </p>
      {children}
    </div>
  );
}

/* ---------- helpers ---------- */

function textOf(children: ReactNode): string {
  if (children == null || typeof children === "boolean") return "";
  if (typeof children === "string" || typeof children === "number") {
    return String(children);
  }
  if (Array.isArray(children)) return children.map(textOf).join("");
  if (isValidElement(children)) {
    return textOf((children.props as { children?: ReactNode }).children);
  }
  return "";
}

function fenceOf(children: ReactNode): { code: string; language: string } {
  const child = Array.isArray(children) ? children[0] : children;
  let language = "";
  if (isValidElement(child)) {
    const className = String(
      (child.props as { className?: string }).className ?? ""
    );
    language = /language-([\w+-]+)/.exec(className)?.[1] ?? "";
  }
  return { code: textOf(children).replace(/\n$/, ""), language };
}

export default function Markdown({
  content,
  slug,
}: {
  content: string;
  slug: string;
}) {
  // Heading ids must match the in-page nav exactly, duplicates included.
  const seen = useRef(new Map<string, number>());
  seen.current = new Map();

  const headingId = (children: ReactNode) => {
    const base = slugify(textOf(children));
    if (!base) return undefined;
    const count = seen.current.get(base) ?? 0;
    seen.current.set(base, count + 1);
    return count === 0 ? base : `${base}-${count}`;
  };

  return (
    <div className="prose">
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkCallouts]}
        components={{
          h2({ children, ...props }) {
            return (
              <h2 {...props} id={headingId(children)}>
                {children}
              </h2>
            );
          },
          h3({ children, ...props }) {
            return (
              <h3 {...props} id={headingId(children)}>
                {children}
              </h3>
            );
          },
          a({ href, children, ...props }) {
            const target = resolveHref(String(href ?? ""), slug);
            const external = /^https?:/i.test(target);
            return (
              <a
                {...props}
                href={target}
                {...(external ? { target: "_blank", rel: "noreferrer" } : {})}
              >
                {children}
              </a>
            );
          },
          table({ children, ...props }) {
            return (
              <div className="table-wrap" tabIndex={0} role="group">
                <table {...props}>{children}</table>
              </div>
            );
          },
          pre({ children }) {
            const { code, language } = fenceOf(children);
            if (language === "mermaid") return <Mermaid chart={code} />;
            return <CodeBlock code={code} language={language} />;
          },
          div({ children, ...props }) {
            const kind = (props as Record<string, unknown>)[
              "data-callout"
            ] as CalloutKind | undefined;
            if (kind && kind in CALLOUTS) {
              return <Callout kind={kind}>{children}</Callout>;
            }
            return <div {...props}>{children}</div>;
          },
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
