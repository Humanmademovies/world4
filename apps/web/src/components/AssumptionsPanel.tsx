import { useEffect, useState } from "react";

import { getAssumptions, type AssumptionInfo } from "../api";

interface Props {
  values: Record<string, number>;
  onChange: (values: Record<string, number>) => void;
  onHelp?: () => void;
}

const pct = (x: number) => `${(x * 100).toFixed(1)}%`;

// Anti-mathwashing panel: each entry is a *contested hypothesis*, not a lever.
// The slider travels over the published range only, the citation is one click
// away, and the whole panel is styled distinctly (dashed border) so assumption
// never masquerades as accounting.
export function AssumptionsPanel({ values, onChange, onHelp }: Props) {
  const [catalog, setCatalog] = useState<AssumptionInfo[]>([]);

  useEffect(() => {
    getAssumptions()
      .then(setCatalog)
      .catch(() => setCatalog([]));
  }, []);

  if (!catalog.length) return null;

  const toggle = (a: AssumptionInfo, on: boolean) => {
    const next = { ...values };
    if (on) next[a.key] = a.default;
    else delete next[a.key];
    onChange(next);
  };

  return (
    <section className="assumptions">
      <h2>
        Assumptions <span className="assumptions-flag">contested — sourced</span>
        {onHelp && (
          <button className="help-btn" onClick={onHelp} title="Guide">
            ?
          </button>
        )}
      </h2>
      <p className="hint">
        Not accounting: each slider is a disputed hypothesis with a published range. Results it
        touches are shown as a band, never as a single hard number.
      </p>

      <ul className="assumption-list">
        {catalog.map((a) => {
          const active = a.key in values;
          const value = values[a.key] ?? a.default;
          return (
            <li key={a.key} className={active ? "assumption on" : "assumption"}>
              <label className="assumption-head">
                <input
                  type="checkbox"
                  checked={active}
                  onChange={(e) => toggle(a, e.target.checked)}
                />
                <span className="assumption-label">{a.label}</span>
                {active && <span className="assumption-value">{pct(value)}</span>}
              </label>
              <p className="assumption-desc">{a.description}</p>
              {active && (
                <div className="assumption-slider">
                  <span className="assumption-bound">{pct(a.low)}</span>
                  <input
                    type="range"
                    min={Math.round(a.low * 1000)}
                    max={Math.round(a.high * 1000)}
                    value={Math.round(value * 1000)}
                    onChange={(e) =>
                      onChange({ ...values, [a.key]: Number(e.target.value) / 1000 })
                    }
                  />
                  <span className="assumption-bound">{pct(a.high)}</span>
                </div>
              )}
              <div className="assumption-range">
                published range {pct(a.low)}–{pct(a.high)} · default {pct(a.default)}
              </div>
              <details className="assumption-source">
                <summary>source</summary>
                <p>{a.source}</p>
                {a.note && <p className="assumption-note">{a.note}</p>}
              </details>
            </li>
          );
        })}
      </ul>
    </section>
  );
}
