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
