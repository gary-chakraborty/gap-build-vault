import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { FORM_URL } from "../config";
import { getBuild } from "../lib/builds.mjs";
import { getSections } from "../lib/toc";
import Markdown from "./Markdown";
import Toc from "./Toc";
import { ArrowLeft } from "./icons";

export function buildMetadata(slug: string): Metadata {
  const build = getBuild(slug);
  if (!build) return {};
  return { title: build.title, description: build.oneliner };
}

export default function BuildPage({ slug }: { slug: string }) {
  const build = getBuild(slug);
  if (!build) notFound();

  const sections = getSections(build.content);

  return (
    <div className="shell build-shell">
      <Link href="/" className="back-link">
        <ArrowLeft />
        All builds
      </Link>

      <header className="build-head">
        <h1>{build.title}</h1>
        {build.oneliner ? <p className="build-line">{build.oneliner}</p> : null}
        <div className="build-meta">
          {build.keyword ? (
            <span className="keyword">{build.keyword}</span>
          ) : null}
          {build.tags.length > 0 ? (
            <div className="card-tags">
              {build.tags.map((tag: string) => (
                <span key={tag}>{tag}</span>
              ))}
            </div>
          ) : null}
        </div>
      </header>

      <div className="build-layout">
        <article>
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
        </article>

        <Toc sections={sections} />
      </div>
    </div>
  );
}
