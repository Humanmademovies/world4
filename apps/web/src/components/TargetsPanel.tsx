import { useEffect, useState } from "react";

import { getRegionTargets, type ImpactInfo, type RegionTargetItem } from "../api";

interface Props {
  region: string | null;
  available: boolean; // region has demography (per-capita possible)
  impacts: ImpactInfo[]; // full impact catalog, to flag those without a target
  targetKeys: string[]; // impact keys that have a sourced target
  onHelp?: () => void;
}

const CO2_PRESETS = [
  { value: "2C", label: "2 °C (O'Neill)" },
  { value: "1.5C-2030", label: "1.5° 2030 (Hot or Cool)" },
  { value: "1.5C-2050", label: "1.5° 2050" },
];

function fmt(value: number): string {
  return value >= 100 ? value.toFixed(0) : value.toFixed(2);
}

function Row({ item }: { item: RegionTargetItem }) {
  const over = item.overshoot_ratio > 1;
  const fill = Math.min(item.overshoot_ratio, 3) / 3; // 0..1 on a 0..3x scale
  return (
    <li className="tg-row" title={item.source + (item.note ? ` — ${item.note}` : "")}>
      <div className="tg-head">
        <span className="tg-label">{item.label}</span>
        <span className={`tg-ratio ${over ? "over" : "ok"}`}>×{item.overshoot_ratio.toFixed(2)}</span>
      </div>
      <div className="tg-bar">
        <div className={`tg-fill ${over ? "over" : "ok"}`} style={{ width: `${fill * 100}%` }} />
        <div className="tg-mark" style={{ left: `${(1 / 3) * 100}%` }} title="target (×1)" />
      </div>
      <div className="tg-sub">
        {fmt(item.per_capita_footprint)} vs <span className="tg-target">{fmt(item.boundary)}</span>{" "}
        {item.unit} ({item.preset})
        {over && item.overshoot_day ? ` · overshoot day ${Math.round(item.overshoot_day)}` : ""}
      </div>
    </li>
  );
}

export function TargetsPanel({ region, available, impacts, targetKeys, onHelp }: Props) {
  const [items, setItems] = useState<RegionTargetItem[]>([]);
  const [co2Preset, setCo2Preset] = useState("2C");

  const usable = Boolean(region) && available;

  useEffect(() => {
    if (!usable || !region) {
      setItems([]);
      return;
    }
    getRegionTargets(region, co2Preset)
      .then((r) => setItems(r.items))
      .catch(() => setItems([]));
  }, [region, usable, co2Preset]);

  if (!usable) {
    return (
      <section className="targets">
        <h2>
          Targets
          {onHelp && <button className="help-btn" onClick={onHelp} title="Guide">?</button>}
        </h2>
        <p className="hint">Click a country with demography to see each limit vs its fair-share target.</p>
      </section>
    );
  }

  const withoutTarget = impacts.filter((i) => !targetKeys.includes(i.key)).map((i) => i.label);

  return (
    <section className="targets">
      <h2>
        Targets — {region}
        {onHelp && <button className="help-btn" onClick={onHelp} title="Guide">?</button>}
      </h2>
      <label className="tg-preset">
        Carbon ambition:{" "}
        <select value={co2Preset} onChange={(e) => setCo2Preset(e.target.value)}>
          {CO2_PRESETS.map((p) => (
            <option key={p.value} value={p.value}>
              {p.label}
            </option>
          ))}
        </select>
      </label>
      <ul className="tg-list">
        {items.map((item) => (
          <Row key={item.impact_key} item={item} />
        ))}
      </ul>
      {withoutTarget.length > 0 && (
        <p className="tg-none">
          No per-capita planetary boundary: {withoutTarget.join(", ")}.
        </p>
      )}
      <p className="hint">Footprint = rigorous; target line = sourced &amp; contestable (hover for source).</p>
    </section>
  );
}
