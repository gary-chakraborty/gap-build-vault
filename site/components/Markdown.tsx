"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { REPO_URL } from "../config";

// Links inside a README point at files in the same build folder.
// Send those to GitHub so people can open and download them.
function resolveHref(href: string, slug: string): string {
  if (!href) return href;
  if (/^(https?:|mailto:|tel:|#)/i.test(href)) return href;
  const clean = href.replace(/^\.\//, "");
  return `${REPO_URL}/blob/main/builds/${slug}/${clean}`;
}

export default function Markdown({
  content,
  slug,
}: {
  content: string;
  slug: string;
}) {
  return (
    <div className="prose">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
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
              <div className="table-wrap">
                <table {...props}>{children}</table>
              </div>
            );
          },
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
