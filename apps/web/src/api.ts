// Typed client for the World4 API. Mirrors apps/api/src/world4_api/schemas.py.
// (A generated OpenAPI client is a planned enhancement; kept hand-written + small
// for now so the front has no extra build step.)

export interface ModelInfo {
  name: string;
  regions: string[];
  sectors: string[];
  products: number;
  extensions: string[];
  has_footprints: boolean;
}

export interface ImpactInfo {
  key: string;
  label: string;
  extension: string;
  unit: string;
  coverage: string;
}

export interface RegionValues {
  impact: string;
  unit: string;
  coverage: string;
  values: Record<string, number>;
}

export interface Lever {
  sector: string;
  region?: string | null;
  reduction: number;
}

export interface SimImpact {
  key: string;
  label: string;
  unit: string;
  coverage: string;
  baseline: number;
  delta: number;
  relative: number;
}

export interface SimResult {
  scenario: string;
  model: string;
  impacts: SimImpact[];
}

const BASE = `${import.meta.env.BASE_URL.replace(/\/+$/, "")}/api`;

async function getJson<T>(path: string): Promise<T> {
  const response = await fetch(BASE + path);
  if (!response.ok) throw new Error(`${response.status} on GET ${path}`);
  return response.json() as Promise<T>;
}

export const getModelInfo = () => getJson<ModelInfo>("/model/info");
export const getImpacts = () => getJson<ImpactInfo[]>("/impacts");
export const getImpactByRegion = (key: string) =>
  getJson<RegionValues>(`/impacts/${encodeURIComponent(key)}/by-region`);

export async function simulate(levers: Lever[]): Promise<SimResult> {
  const response = await fetch(BASE + "/simulate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: "ui", levers }),
  });
  if (!response.ok) throw new Error(`${response.status} on POST /simulate`);
  return response.json() as Promise<SimResult>;
}

// --- Work-time (labour) -----------------------------------------------------

export interface LaborCatalog {
  year: number;
  regions: string[]; // region codes that have demography
}

export interface WorkTimeParams {
  start_age: number;
  retirement_age: number;
  non_employment_rate: number;
  weeks_per_year: number;
}

export interface WorkTime {
  region: string;
  production_hours: number; // scenario-adjusted
  baseline_production_hours: number;
  production_hours_delta: number; // <= 0
  working_age_population: number;
  employed: number;
  weekly_hours_per_worker: number;
}

export type SolveFor = "retirement_age" | "non_employment_rate" | "start_age";

export interface SolveResult {
  region: string;
  solve_for: SolveFor;
  target_weekly_hours: number;
  value: number | null;
  feasible: boolean;
}

async function postJson<T>(path: string, body: unknown): Promise<T> {
  const response = await fetch(BASE + path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!response.ok) throw new Error(`${response.status} on POST ${path}`);
  return response.json() as Promise<T>;
}

export const getLaborCatalog = () => getJson<LaborCatalog>("/labor");

// --- Sustainability targets -------------------------------------------------

export interface TargetInfo {
  impact_key: string;
  label: string;
  unit: string;
  allocation: string;
  source: string;
  note: string;
  presets: string[];
  default_preset: string;
}

export interface RegionTargetItem {
  impact_key: string;
  label: string;
  unit: string;
  preset: string;
  boundary: number;
  per_capita_footprint: number;
  overshoot_ratio: number;
  overshoot_day: number | null;
  source: string;
  note: string;
}

export interface RegionTargets {
  region: string;
  items: RegionTargetItem[];
}

export const getTargetsCatalog = () => getJson<TargetInfo[]>("/targets");

// --- Wiki (computed sector profiles) ---------------------------------------

export interface SectorInfo {
  sector: string;
  code: string;
  category: string;
}

export interface SectorDriver {
  key: string;
  label: string;
  unit: string;
  share: number;
}

export interface SectorProfile {
  sector: string;
  region: string;
  code: string;
  category: string;
  drivers: SectorDriver[];
  labour_hours_in_region: number | null;
}

export const getWikiSectors = () => getJson<SectorInfo[]>("/wiki/sectors");

export const getWikiSector = (sector: string, region: string) =>
  getJson<SectorProfile>(
    `/wiki/sector/${encodeURIComponent(sector)}?region=${encodeURIComponent(region)}`,
  );

export const getRegionTargets = (region: string, co2Preset: string) =>
  getJson<RegionTargets>(
    `/targets/region/${encodeURIComponent(region)}?co2_preset=${encodeURIComponent(co2Preset)}`,
  );

// Work-time queries carry the current levers so the result reflects the scenario
// (production hours fall as the chosen industries shrink).
export const getWorkTime = (region: string, p: WorkTimeParams, levers: Lever[]) =>
  postJson<WorkTime>(`/labor/${encodeURIComponent(region)}/worktime`, { ...p, levers });

export const solveWorkTime = (
  region: string,
  targetWeeklyHours: number,
  solveFor: SolveFor,
  p: WorkTimeParams,
  levers: Lever[],
) =>
  postJson<SolveResult>(`/labor/${encodeURIComponent(region)}/solve`, {
    ...p,
    target_weekly_hours: targetWeeklyHours,
    solve_for: solveFor,
    levers,
  });
