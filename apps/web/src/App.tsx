import { useEffect, useMemo, useState } from "react";

import {
  getImpactByRegion,
  getImpacts,
  getLaborCatalog,
  getModelInfo,
  simulate,
  type ImpactInfo,
  type Lever,
  type ModelInfo,
  type RegionValues,
  type SimResult,
} from "./api";
import { Controls } from "./components/Controls";
import { ImpactPanels } from "./components/ImpactPanels";
import { LaborPanel } from "./components/LaborPanel";
import { WorldMap } from "./components/WorldMap";
import { coverageColor, fmtValue, RAMP } from "./format";

const NO_GEOMETRY = "Rest-of-World aggregates (WA, WL, WE, WF, WM) and Malta have no map geometry.";

export function App() {
  const [info, setInfo] = useState<ModelInfo | null>(null);
  const [impacts, setImpacts] = useState<ImpactInfo[]>([]);
  const [mapImpact, setMapImpact] = useState<string>("");
  const [regionValues, setRegionValues] = useState<RegionValues | null>(null);
  const [selectedRegion, setSelectedRegion] = useState<string | null>(null);
  const [levers, setLevers] = useState<Lever[]>([]);
  const [sim, setSim] = useState<SimResult | null>(null);
  const [simLoading, setSimLoading] = useState(false);
  const [globe, setGlobe] = useState(false);
  const [laborRegions, setLaborRegions] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);

  // Initial load.
  useEffect(() => {
    Promise.all([getModelInfo(), getImpacts()])
      .then(([modelInfo, impactList]) => {
        setInfo(modelInfo);
        setImpacts(impactList);
        if (impactList.length) setMapImpact(impactList[0].key);
      })
      .catch((e) => setError(String(e)));
    // Labour view is optional (needs the labour artifact); empty list if absent.
    getLaborCatalog()
      .then((c) => setLaborRegions(c.regions))
      .catch(() => setLaborRegions([]));
  }, []);

  // Map colouring follows the chosen impact.
  useEffect(() => {
    if (!mapImpact) return;
    getImpactByRegion(mapImpact)
      .then(setRegionValues)
      .catch((e) => setError(String(e)));
  }, [mapImpact]);

  // Debounced simulation whenever the levers change.
  useEffect(() => {
    setSimLoading(true);
    const handle = setTimeout(() => {
      simulate(levers)
        .then(setSim)
        .catch((e) => setError(String(e)))
        .finally(() => setSimLoading(false));
    }, 250);
    return () => clearTimeout(handle);
  }, [levers]);

  const values = regionValues?.values ?? {};
  const maxValue = useMemo(() => {
    const finite = Object.values(values).filter((v) => Number.isFinite(v) && v > 0);
    return finite.length ? Math.max(...finite) : 0;
  }, [values]);

  if (error) return <div className="fatal">Error: {error}</div>;
  if (!info) return <div className="loading">Loading World4…</div>;

  const activeImpact = impacts.find((i) => i.key === mapImpact);

  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <strong>World4</strong>
          <span className="model">{info.name}</span>
        </div>
        <div className="topbar-controls">
          <label>
            Map impact:{" "}
            <select value={mapImpact} onChange={(e) => setMapImpact(e.target.value)}>
              {impacts.map((i) => (
                <option key={i.key} value={i.key}>
                  {i.label} ({i.unit})
                </option>
              ))}
            </select>
          </label>
          <label className="toggle">
            <input type="checkbox" checked={globe} onChange={(e) => setGlobe(e.target.checked)} />
            Globe
          </label>
        </div>
      </header>

      <main className="layout">
        <div className="map-pane">
          <WorldMap
            values={values}
            selectedRegion={selectedRegion}
            onSelectRegion={setSelectedRegion}
            globe={globe}
          />
          <div className="legend">
            {activeImpact && (
              <>
                <div className="legend-title">
                  {activeImpact.label}
                  <span
                    className="coverage"
                    style={{ backgroundColor: coverageColor(activeImpact.coverage) }}
                  >
                    {activeImpact.coverage}
                  </span>
                </div>
                <div
                  className="legend-ramp"
                  style={{
                    background: `linear-gradient(90deg, ${RAMP.map(
                      ([t, c]) => `${c} ${t * 100}%`,
                    ).join(", ")})`,
                  }}
                />
                <div className="legend-scale">
                  <span>0</span>
                  <span>{fmtValue(maxValue, activeImpact.unit)}</span>
                </div>
                <div className="legend-note">
                  Baseline consumption footprint per region. {NO_GEOMETRY}
                </div>
              </>
            )}
            {selectedRegion && regionValues && (
              <div className="selected">
                <strong>{selectedRegion}</strong>:{" "}
                {fmtValue(regionValues.values[selectedRegion] ?? NaN, regionValues.unit)}
              </div>
            )}
          </div>
        </div>

        <aside className="side">
          <Controls
            sectors={info.sectors}
            regions={info.regions}
            selectedRegion={selectedRegion}
            levers={levers}
            onChange={setLevers}
          />
          <LaborPanel
            region={selectedRegion}
            available={selectedRegion !== null && laborRegions.includes(selectedRegion)}
          />
          <ImpactPanels impacts={sim?.impacts ?? []} loading={simLoading} />
        </aside>
      </main>
    </div>
  );
}
