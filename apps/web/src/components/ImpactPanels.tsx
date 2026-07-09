import type { SimImpact } from "../api";
import { coverageColor, fmtPercent, fmtValue } from "../format";

interface Props {
  impacts: SimImpact[];
  loading: boolean;
}

// No single aggregate index: every impact is shown side by side with its own
// metric, unit and an explicit coverage flag (rigour vs uncertainty stays visible).
export function ImpactPanels({ impacts, loading }: Props) {
  return (
    <section className="impacts">
      <h2>
        Impacts {loading && <span className="spin">…</span>}
      </h2>
      <div className="impact-grid">
        {impacts.map((impact) => {
          const reduced = impact.delta < 0;
          const magnitude = Math.min(1, Math.abs(impact.relative));
          // Assumption-dependent result: show the published-range band and style
          // the card distinctly — a hypothesis must never look like accounting.
          const assumed = impact.relative_low != null && impact.relative_high != null;
          const bandLow = assumed ? Math.min(1, Math.abs(impact.relative_low ?? 0)) : 0;
          const bandHigh = assumed ? Math.min(1, Math.abs(impact.relative_high ?? 0)) : 0;
          return (
            <article className={`impact-card${assumed ? " assumed" : ""}`} key={impact.key}>
              <header>
                <span className="impact-label">{impact.label}</span>
                {assumed && (
                  <span className="assumed-flag" title="Depends on an active assumption">
                    ≈ hypothesis
                  </span>
                )}
                <span
                  className="coverage"
                  style={{ backgroundColor: coverageColor(impact.coverage) }}
                  title={`Coverage: ${impact.coverage}`}
                >
                  {impact.coverage}
                </span>
              </header>
              <div className="impact-baseline">
                baseline {fmtValue(impact.baseline, impact.unit)}
              </div>
              <div className={`impact-delta ${reduced ? "down" : "flat"}`}>
                {reduced ? "▼ " : ""}
                {fmtPercent(impact.relative)}
              </div>
              {assumed ? (
                <div className="impact-band">
                  {fmtPercent(impact.relative_low ?? 0)} … {fmtPercent(impact.relative_high ?? 0)}{" "}
                  over the published range
                </div>
              ) : (
                <div className="impact-abs">{fmtValue(impact.delta, impact.unit)}</div>
              )}
              <div className="bar">
                {assumed && (
                  <div
                    className="bar-band"
                    style={{
                      left: `${Math.min(bandLow, bandHigh) * 100}%`,
                      width: `${Math.abs(bandHigh - bandLow) * 100}%`,
                    }}
                  />
                )}
                <div className="bar-fill" style={{ width: `${magnitude * 100}%` }} />
              </div>
            </article>
          );
        })}
      </div>
    </section>
  );
}
