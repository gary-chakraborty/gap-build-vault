import type { Metadata } from "next";
import Link from "next/link";
import {
  AUTHOR_NAME,
  AUTHOR_URL,
  BOOKING_URL,
  REPO_URL,
  SITE_NAME,
  TAGLINE,
} from "../config";
import "./globals.css";

export const metadata: Metadata = {
  title: SITE_NAME,
  description: TAGLINE,
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
              {SITE_NAME}
            </Link>
            <a
              className="header-link"
              href={REPO_URL}
              target="_blank"
              rel="noreferrer"
            >
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
              <a href={BOOKING_URL} target="_blank" rel="noreferrer">
                Work with GAP
              </a>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
