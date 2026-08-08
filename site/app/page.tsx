import Link from "next/link";
import { SITE_NAME, TAGLINE } from "../config";
import { getAllBuilds } from "../lib/builds.mjs";
import { ArrowRight } from "../components/icons";

type Build = {
  slug: string;
  title: string;
  oneliner: string;
  tags: string[];
  date: string;
  keyword: string;
};

function BuildCard({
  build,
  index,
  featured,
}: {
  build: Build;
  index: number;
  featured?: boolean;
}) {
  return (
    <Link
      href={`/builds/${build.slug}/`}
      className={`card${featured ? " card-featured" : ""}`}
      style={{ "--i": index } as React.CSSProperties}
    >
      <h2 className="card-title">{build.title}</h2>
      {build.oneliner ? <p className="card-line">{build.oneliner}</p> : null}
      {build.tags.length > 0 ? (
        <div className="card-tags">
          {build.tags.map((tag) => (
            <span key={tag}>{tag}</span>
          ))}
        </div>
      ) : null}
      <div className="card-foot">
        {build.keyword ? (
          <span className="keyword">{build.keyword}</span>
        ) : (
          <span />
        )}
        <span className="card-go">
          Open the build
          <ArrowRight />
        </span>
      </div>
    </Link>
  );
}

export default function HomePage() {
  const builds = getAllBuilds() as Build[];
  const [newest, ...rest] = builds;

  return (
    <div>
      <section className="hero">
        <div className="shell hero-inner">
          <h1>{SITE_NAME}</h1>
          <p className="hero-lead">{TAGLINE}</p>
          {builds.length > 0 ? (
            <p className="hero-facts">
              <span>
                <b>{builds.length}</b>{" "}
                {builds.length === 1 ? "build" : "builds"}
              </span>
              <span>Prompts, scripts and steps included</span>
              {newest?.date ? <span>Updated {newest.date}</span> : null}
            </p>
          ) : null}
        </div>
      </section>

      <section className="section">
        <div className="shell">
          {builds.length === 0 ? (
            <div className="empty-state">
              <h2>First builds land this week.</h2>
              <p>
                Each one comes as a full folder: the prompts, the scripts, the
                workflow files, and steps you can follow start to finish.
              </p>
              <p>Nothing to sign up for. Nothing held back.</p>
            </div>
          ) : (
            <>
              <div className="section-head">
                <h2 className="section-label">Every build</h2>
                <p className="section-note">Newest first</p>
              </div>
              <div className="grid">
                <BuildCard build={newest} index={0} featured />
                {rest.map((build, i) => (
                  <BuildCard key={build.slug} build={build} index={i + 1} />
                ))}
              </div>
            </>
          )}
        </div>
      </section>
    </div>
  );
}
