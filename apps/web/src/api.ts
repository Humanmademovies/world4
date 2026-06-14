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

const BASE = "/api";

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
  production_hours: number;
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

export const getLaborCatalog = () => getJson<LaborCatalog>("/labor");

function query(params: Record<string, string | number>): string {
  return new URLSearchParams(
    Object.fromEntries(Object.entries(params).map(([k, v]) => [k, String(v)])),
  ).toString();
}

export const getWorkTime = (region: string, p: WorkTimeParams) =>
  getJson<WorkTime>(`/labor/${encodeURIComponent(region)}?${query({ ...p })}`);

export const solveWorkTime = (
  region: string,
  targetWeeklyHours: number,
  solveFor: SolveFor,
  p: WorkTimeParams,
) =>
  getJson<SolveResult>(
    `/labor/${encodeURIComponent(region)}/solve?${query({
      target_weekly_hours: targetWeeklyHours,
      solve_for: solveFor,
      ...p,
    })}`,
  );
