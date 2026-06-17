// Loads the bilingual wiki markdown bundled under content/wiki/{lang}/{slug}.md.

const modules = import.meta.glob("./wiki/**/*.md", {
  query: "?raw",
  import: "default",
  eager: true,
}) as Record<string, string>;

export type Lang = "en" | "fr";

export interface WikiPage {
  slug: string;
  title: Record<Lang, string>;
}

// Page order + localized titles for the navigation.
export const WIKI_PAGES: WikiPage[] = [
  { slug: "overview", title: { en: "Overview", fr: "Vue d'ensemble" } },
  { slug: "levers", title: { en: "Demand levers", fr: "Leviers de demande" } },
  { slug: "work-time", title: { en: "Work time", fr: "Temps de travail" } },
  { slug: "targets", title: { en: "Targets", fr: "Cibles" } },
  { slug: "glossary", title: { en: "Glossary", fr: "Glossaire" } },
];

const pages: Record<Lang, Record<string, string>> = { en: {}, fr: {} };
for (const [path, raw] of Object.entries(modules)) {
  const match = path.match(/\/wiki\/(en|fr)\/(.+)\.md$/);
  if (match) pages[match[1] as Lang][match[2]] = raw;
}

export function wikiMarkdown(lang: Lang, slug: string): string {
  return pages[lang][slug] ?? pages.en[slug] ?? `# ${slug}\n\n(missing)`;
}

// French labels for the headline impacts (data labels arrive in English from the API).
export const IMPACT_LABEL_FR: Record<string, string> = {
  co2_combustion: "CO2 — combustion",
  water_blue: "Eau — bleue",
  land_use: "Usage des sols",
  material: "Extraction de matières",
  energy: "Usage d'énergie",
  employment_hours: "Emploi — heures",
};
