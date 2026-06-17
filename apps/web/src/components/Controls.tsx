import { useEffect, useState } from "react";

import type { Lever } from "../api";

interface Props {
  sectors: string[];
  regions: string[];
  selectedRegion: string | null;
  levers: Lever[];
  onChange: (levers: Lever[]) => void;
  onHelp?: () => void;
}

export function Controls({ sectors, regions, selectedRegion, levers, onChange, onHelp }: Props) {
  const [sector, setSector] = useState("");
  const [scope, setScope] = useState<string>("");

  // When a region is clicked on the map, default new levers to that region.
  useEffect(() => {
    if (selectedRegion) setScope(selectedRegion);
  }, [selectedRegion]);

  const addLever = () => {
    if (!sectors.includes(sector)) return;
    const region = scope || null;
    if (levers.some((l) => l.sector === sector && (l.region ?? null) === region)) return;
    onChange([...levers, { sector, region, reduction: 0.3 }]);
    setSector("");
  };

  const updateReduction = (i: number, reduction: number) => {
    const next = levers.slice();
    next[i] = { ...next[i], reduction };
    onChange(next);
  };

  const removeLever = (i: number) => onChange(levers.filter((_, j) => j !== i));

  return (
    <section className="controls">
      <h2>
        Demand-reduction levers
        {onHelp && <button className="help-btn" onClick={onHelp} title="Guide">?</button>}
      </h2>
      <p className="hint">
        Reductions only — the seed never adds demand. Pick a sector, optionally scope it to a
        region, then set how much of its final demand to remove.
      </p>

      <div className="add-lever">
        <input
          list="sector-list"
          placeholder="Search a sector…"
          value={sector}
          onChange={(e) => setSector(e.target.value)}
        />
        <datalist id="sector-list">
          {sectors.map((s) => (
            <option key={s} value={s} />
          ))}
        </datalist>
        <select value={scope} onChange={(e) => setScope(e.target.value)}>
          <option value="">All regions</option>
          {regions.map((r) => (
            <option key={r} value={r}>
              {r}
            </option>
          ))}
        </select>
        <button onClick={addLever} disabled={!sectors.includes(sector)}>
          Add
        </button>
      </div>

      {levers.length === 0 && <p className="empty">No levers yet — add one to simulate.</p>}

      <ul className="lever-list">
        {levers.map((lever, i) => (
          <li key={`${lever.sector}::${lever.region ?? "all"}`}>
            <div className="lever-head">
              <span className="lever-sector" title={lever.sector}>
                {lever.sector}
              </span>
              <span className="lever-scope">{lever.region ?? "all"}</span>
              <button className="remove" onClick={() => removeLever(i)} aria-label="remove">
                ×
              </button>
            </div>
            <div className="lever-slider">
              <input
                type="range"
                min={0}
                max={100}
                value={Math.round(lever.reduction * 100)}
                onChange={(e) => updateReduction(i, Number(e.target.value) / 100)}
              />
              <span className="lever-pct">−{Math.round(lever.reduction * 100)}%</span>
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
}
