import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { FORM_URL } from "../config";
import { getBuild } from "../lib/builds.mjs";
import Markdown from "./Markdown";

export function buildMetadata(slug: string): Metadata {
  const build = getBuild(slug);
  if (!build) return {};
  return { title: build.title, description: build.oneliner };
}

export default function BuildPage({ slug }: { slug: string }) {
  const build = getBuild(slug);
  if (!build) notFound();

  return (
    <div className="shell">
      <Link href="/" className="back-link">
        Back to all builds
      </Link>

      <div className="build-head">
        <h1>{build.title}</h1>
        {build.oneliner ? <p>{build.oneliner}</p> : null}
        <div className="card-meta">
          {build.tags.map((tag) => (
            <span key={tag} className="tag">
              {tag}
            </span>
          ))}
          {build.keyword ? (
            <span className="keyword">{build.keyword}</span>
          ) : null}
        </div>
      </div>

      <Markdown content={build.content} slug={build.slug} />

      <div className="feedback">
        <h2>Used this build?</h2>
        <p>
          Tell me how it went. Two minutes, five questions:{" "}
          <a href={FORM_URL} target="_blank" rel="noreferrer">
            open the form
          </a>
          .
        </p>
      </div>
    </div>
  );
}
