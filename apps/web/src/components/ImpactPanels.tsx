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
          return (
            <article className="impact-card" key={impact.key}>
              <header>
                <span className="impact-label">{impact.label}</span>
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
              <div className="impact-abs">{fmtValue(impact.delta, impact.unit)}</div>
              <div className="bar">
                <div className="bar-fill" style={{ width: `${magnitude * 100}%` }} />
              </div>
            </article>
          );
        })}
      </div>
    </section>
  );
}
