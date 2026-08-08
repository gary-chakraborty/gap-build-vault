import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";

/**
 * @typedef {Object} Build
 * @property {string} slug
 * @property {string} title
 * @property {string} oneliner
 * @property {string[]} tags
 * @property {string} date
 * @property {string} keyword
 * @property {string} status
 * @property {string} content
 */

// The builds folder sits next to the site folder in the repo. Some deploys
// flatten the tree, so check that shape too. If neither exists, stop the build
// loudly. An empty grid must never hide a missing folder.
function buildsDir() {
  const candidates = [
    path.join(process.cwd(), "..", "builds"),
    path.join(process.cwd(), "builds"),
  ];
  for (const dir of candidates) {
    if (fs.existsSync(dir) && fs.statSync(dir).isDirectory()) return dir;
  }
  throw new Error(
    `builds folder not found. Looked in: ${candidates.join(", ")}. ` +
      `Refusing to render an empty site from a missing folder.`
  );
}

/** @param {unknown} value @returns {string} */
function asString(value) {
  return typeof value === "string" ? value.trim() : "";
}

/** @param {unknown} value @returns {string[]} */
function asTags(value) {
  if (!Array.isArray(value)) return [];
  return value.map((tag) => String(tag).trim()).filter(Boolean);
}

/** @param {unknown} value @returns {string} */
function asDate(value) {
  if (value instanceof Date) return value.toISOString().slice(0, 10);
  return asString(value);
}

/** @returns {Build[]} every build with status: live, newest first */
export function getAllBuilds() {
  const dir = buildsDir();
  const slugs = fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .filter((name) => !name.startsWith("."));

  /** @type {Build[]} */
  const builds = [];

  for (const slug of slugs) {
    const readme = path.join(dir, slug, "README.md");
    if (!fs.existsSync(readme)) continue;

    const parsed = matter(fs.readFileSync(readme, "utf8"));
    const data = /** @type {Record<string, unknown>} */ (parsed.data);

    builds.push({
      slug,
      title: asString(data.title) || slug,
      oneliner: asString(data.oneliner),
      tags: asTags(data.tags),
      date: asDate(data.date),
      keyword: asString(data.keyword),
      status: asString(data.status).toLowerCase(),
      content: parsed.content,
    });
  }

  return builds
    .filter((build) => build.status === "live")
    .sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
}

/** @param {string} slug @returns {Build | undefined} */
export function getBuild(slug) {
  return getAllBuilds().find((build) => build.slug === slug);
}
