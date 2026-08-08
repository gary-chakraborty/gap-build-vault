import Link from "next/link";
import { SITE_NAME, TAGLINE } from "../config";
import { getAllBuilds } from "../lib/builds.mjs";

export default function HomePage() {
  const builds = getAllBuilds();

  return (
    <div className="shell">
      <section className="hero">
        <h1>{SITE_NAME}</h1>
        <p>{TAGLINE}</p>
      </section>

      <section className="section">
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
            <h2 className="section-label">
              {builds.length === 1 ? "1 build" : `${builds.length} builds`}
            </h2>
            <div className="grid">
              {builds.map((build) => (
                <Link
                  key={build.slug}
                  href={`/builds/${build.slug}/`}
                  className="card"
                >
                  <h2>{build.title}</h2>
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
                </Link>
              ))}
            </div>
          </>
        )}
      </section>
    </div>
  );
}
