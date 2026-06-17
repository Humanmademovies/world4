import { marked } from "marked";
import { useEffect, useMemo, useState } from "react";

import { getWikiSector, getWikiSectors, type SectorInfo, type SectorProfile } from "../api";
import { IMPACT_LABEL_FR, type Lang, WIKI_PAGES, wikiMarkdown } from "../content/wiki";

export type WikiTarget = { kind: "page"; slug: string } | { kind: "sectors" };

interface Props {
  open: boolean;
  onClose: () => void;
  lang: Lang;
  onLang: (lang: Lang) => void;
  region: string | null;
  target: WikiTarget | null;
}

type View = { kind: "page"; slug: string } | { kind: "sectors" } | { kind: "sector"; name: string };

const T = {
  en: { guide: "Guide", sectors: "Sectors", search: "Search a sector…", back: "← all sectors",
        forRegion: "for", drives: "of footprint", labour: "labour tied up", pick: "Pick a sector." },
  fr: { guide: "Guide", sectors: "Secteurs", search: "Chercher un secteur…", back: "← tous les secteurs",
        forRegion: "pour", drives: "de l'empreinte", labour: "travail mobilisé", pick: "Choisis un secteur." },
};

export function WikiDrawer({ open, onClose, lang, onLang, region, target }: Props) {
  const [view, setView] = useState<View>({ kind: "page", slug: "overview" });
  const [sectors, setSectors] = useState<SectorInfo[]>([]);
  const [query, setQuery] = useState("");
  const [profile, setProfile] = useState<SectorProfile | null>(null);
  const t = T[lang];

  useEffect(() => {
    if (open && sectors.length === 0) getWikiSectors().then(setSectors).catch(() => setSectors([]));
  }, [open, sectors.length]);

  // Follow deep-link targets (the ⓘ buttons / the Guide button).
  useEffect(() => {
    if (target) setView(target.kind === "sectors" ? { kind: "sectors" } : target);
  }, [target]);

  useEffect(() => {
    if (view.kind !== "sector") return;
    setProfile(null);
    getWikiSector(view.name, region ?? "").then(setProfile).catch(() => setProfile(null));
  }, [view, region]);

  const matches = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return [];
    return sectors.filter((s) => s.sector.toLowerCase().includes(q)).slice(0, 40);
  }, [query, sectors]);

  const driverLabel = (key: string, label: string) =>
    lang === "fr" ? (IMPACT_LABEL_FR[key] ?? label) : label;

  return (
    <aside className={`wiki ${open ? "wiki-open" : ""}`} aria-hidden={!open}>
      <header className="wiki-head">
        <strong>{t.guide}</strong>
        <div className="wiki-head-right">
          <button className={`wiki-lang ${lang === "en" ? "on" : ""}`} onClick={() => onLang("en")}>EN</button>
          <button className={`wiki-lang ${lang === "fr" ? "on" : ""}`} onClick={() => onLang("fr")}>FR</button>
          <button className="wiki-close" onClick={onClose} aria-label="close">×</button>
        </div>
      </header>

      <nav className="wiki-nav">
        {WIKI_PAGES.map((p) => (
          <button
            key={p.slug}
            className={view.kind === "page" && view.slug === p.slug ? "on" : ""}
            onClick={() => setView({ kind: "page", slug: p.slug })}
          >
            {p.title[lang]}
          </button>
        ))}
        <button className={view.kind !== "page" ? "on" : ""} onClick={() => setView({ kind: "sectors" })}>
          {t.sectors}
        </button>
      </nav>

      <input
        className="wiki-search"
        placeholder={t.search}
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onFocus={() => view.kind === "page" && setView({ kind: "sectors" })}
      />

      <div className="wiki-body">
        {query && matches.length > 0 && (
          <ul className="wiki-results">
            {matches.map((s) => (
              <li key={s.sector}>
                <button onClick={() => { setView({ kind: "sector", name: s.sector }); setQuery(""); }}>
                  {s.sector} <span className="wiki-cat">{s.category}</span>
                </button>
              </li>
            ))}
          </ul>
        )}

        {view.kind === "page" && (
          <div className="wiki-md" dangerouslySetInnerHTML={{ __html: marked.parse(wikiMarkdown(lang, view.slug)) as string }} />
        )}

        {view.kind === "sectors" && !query && (
          <ul className="wiki-sector-list">
            {sectors.map((s) => (
              <li key={s.sector}>
                <button onClick={() => setView({ kind: "sector", name: s.sector })}>
                  {s.sector} <span className="wiki-cat">{s.category}</span>
                </button>
              </li>
            ))}
          </ul>
        )}

        {view.kind === "sector" && (
          <div className="wiki-sector">
            <button className="wiki-back" onClick={() => setView({ kind: "sectors" })}>{t.back}</button>
            <h3>{view.name}</h3>
            {profile ? (
              <>
                <p className="wiki-meta">
                  {profile.category} · {profile.code} · {t.forRegion} <strong>{profile.region}</strong>
                </p>
                {profile.labour_hours_in_region != null && (
                  <p className="wiki-labour">
                    {t.labour}: {(profile.labour_hours_in_region / 1e6).toFixed(0)} M·hr
                  </p>
                )}
                <ul className="wiki-drivers">
                  {profile.drivers.map((d) => (
                    <li key={d.key}>
                      <div className="wiki-driver-head">
                        <span>{driverLabel(d.key, d.label)}</span>
                        <span className="wiki-share">{(d.share * 100).toFixed(1)}% {t.drives}</span>
                      </div>
                      <div className="wiki-driver-bar">
                        <div style={{ width: `${Math.min(Math.abs(d.share), 1) * 100}%` }} />
                      </div>
                    </li>
                  ))}
                </ul>
              </>
            ) : (
              <p className="hint">…</p>
            )}
          </div>
        )}
      </div>
    </aside>
  );
}
