import type { Metadata } from "next";
import Link from "next/link";
import "@fontsource-variable/inter/wght.css";
import "@fontsource-variable/space-grotesk/wght.css";
import "@fontsource-variable/jetbrains-mono/wght.css";
import {
  AUTHOR_NAME,
  AUTHOR_URL,

  REPO_URL,
  SITE_NAME,
  TAGLINE,
} from "../config";
import { Github } from "../components/icons";
import "./globals.css";

export const metadata: Metadata = {
  title: SITE_NAME,
  description: TAGLINE,
};

export const viewport = {
  themeColor: "#0d1117",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <div className="shell">
            <Link href="/" className="wordmark">
              <span className="wordmark-mark" aria-hidden="true" />
              {SITE_NAME}
            </Link>
            <a
              className="header-link"
              href={REPO_URL}
              target="_blank"
              rel="noreferrer"
            >
              <Github />
              Code on GitHub
            </a>
          </div>
        </header>

        <main>{children}</main>

        <footer className="site-footer">
          <div className="shell">
            <div className="footer-links">
              <a href={REPO_URL} target="_blank" rel="noreferrer">
                GitHub repo
              </a>
              <a href={AUTHOR_URL} target="_blank" rel="noreferrer">
                {AUTHOR_NAME}
              </a>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
