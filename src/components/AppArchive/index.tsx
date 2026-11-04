import React, {useState, type ReactNode} from 'react';
import Link from '@docusaurus/Link';
import archive from '@site/src/data/app-archive.json';
import styles from './styles.module.css';

type File = {platform: string; label: string; url: string; size: string};
type Version = {version: string; date: string; dateLabel: string; files: File[]};

const PLATFORMS = ['Windows x64', 'Windows Arm64', 'macOS'];
const INITIAL = 6;

function anchor(version: string): string {
  return '/updates/app-release-notes#v' + version.replace(/\./g, '-');
}

function VersionCard({v, latest}: {v: Version; latest: boolean}): ReactNode {
  return (
    <article className={latest ? `${styles.card} ${styles.latest}` : styles.card}>
      <header className={styles.head}>
        <h3 className={styles.version} id={'v' + v.version.replace(/\./g, '-')}>
          {v.version}
          {latest && <span className={styles.badge}>Latest</span>}
        </h3>
        <span className={styles.date}>{v.dateLabel}</span>
        <Link className={styles.notes} to={anchor(v.version)}>
          Release notes →
        </Link>
      </header>
      <div className={styles.platforms}>
        {PLATFORMS.map((p) => {
          const files = v.files.filter((f) => f.platform === p);
          if (files.length === 0) return null;
          return (
            <div key={p} className={styles.platform}>
              <span className={styles.platformName}>{p}</span>
              <div className={styles.buttons}>
                {files.map((f) => (
                  <a key={f.url} className={styles.download} href={f.url} rel="nofollow">
                    <span>{f.label}</span>
                    <span className={styles.size}>{f.size}</span>
                  </a>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </article>
  );
}

export default function AppArchive(): ReactNode {
  const versions = archive.versions as Version[];
  const [showAll, setShowAll] = useState(false);
  const shown = showAll ? versions : versions.slice(0, INITIAL);
  return (
    <div className={styles.archive}>
      {shown.map((v, i) => (
        <VersionCard key={v.version} v={v} latest={i === 0} />
      ))}
      {versions.length > INITIAL && (
        <button type="button" className={styles.more} onClick={() => setShowAll(!showAll)}>
          {showAll ? 'Show fewer versions' : `Show all ${versions.length} versions`}
        </button>
      )}
    </div>
  );
}
