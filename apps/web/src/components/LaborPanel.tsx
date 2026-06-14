import { useEffect, useState } from "react";

import {
  getWorkTime,
  solveWorkTime,
  type Lever,
  type SolveFor,
  type SolveResult,
  type WorkTime,
  type WorkTimeParams,
} from "../api";

interface Props {
  region: string | null;
  available: boolean; // region has demography (labour view possible)
  levers: Lever[]; // current demand-reduction scenario
}

const DEFAULTS: WorkTimeParams = {
  start_age: 20,
  retirement_age: 65,
  non_employment_rate: 0.2,
  weeks_per_year: 52,
};

function Slider(props: {
  label: string;
  value: number;
  min: number;
  max: number;
  step: number;
  fmt: (v: number) => string;
  onChange: (v: number) => void;
}) {
  return (
    <label className="wt-slider">
      <span className="wt-label">{props.label}</span>
      <input
        type="range"
        min={props.min}
        max={props.max}
        step={props.step}
        value={props.value}
        onChange={(e) => props.onChange(Number(e.target.value))}
      />
      <span className="wt-val">{props.fmt(props.value)}</span>
    </label>
  );
}

export function LaborPanel({ region, available, levers }: Props) {
  const [params, setParams] = useState<WorkTimeParams>(DEFAULTS);
  const [forward, setForward] = useState<WorkTime | null>(null);
  const [target, setTarget] = useState(32);
  const [solveFor, setSolveFor] = useState<SolveFor>("retirement_age");
  const [solved, setSolved] = useState<SolveResult | null>(null);

  const usable = Boolean(region) && available;
  const set = (patch: Partial<WorkTimeParams>) => setParams((p) => ({ ...p, ...patch }));

  useEffect(() => {
    if (!usable || !region) {
      setForward(null);
      return;
    }
    const h = setTimeout(() => {
      getWorkTime(region, params, levers).then(setForward).catch(() => setForward(null));
    }, 200);
    return () => clearTimeout(h);
  }, [region, usable, params, levers]);

  useEffect(() => {
    if (!usable || !region) {
      setSolved(null);
      return;
    }
    const h = setTimeout(() => {
      solveWorkTime(region, target, solveFor, params, levers)
        .then(setSolved)
        .catch(() => setSolved(null));
    }, 200);
    return () => clearTimeout(h);
  }, [region, usable, params, target, solveFor, levers]);

  if (!usable) {
    return (
      <section className="labor">
        <h2>Work time</h2>
        <p className="hint">
          Click a country with demography on the map to explore its work-time trade-offs.
        </p>
      </section>
    );
  }

  const solvedText = () => {
    if (!solved) return "…";
    if (!solved.feasible || solved.value === null) return "not achievable with these settings";
    if (solved.solve_for === "retirement_age") return `retire at ${solved.value.toFixed(1)} yrs`;
    if (solved.solve_for === "non_employment_rate") return `n = ${(solved.value * 100).toFixed(1)}%`;
    return `start at ${solved.value.toFixed(1)} yrs`;
  };

  return (
    <section className="labor">
      <h2>Work time — {region}</h2>

      <Slider label="Start age" value={params.start_age} min={14} max={30} step={1}
        fmt={(v) => `${v}`} onChange={(v) => set({ start_age: v })} />
      <Slider label="Retirement age" value={params.retirement_age} min={55} max={80} step={1}
        fmt={(v) => `${v}`} onChange={(v) => set({ retirement_age: v })} />
      <Slider label="Non-employment n%" value={params.non_employment_rate} min={0} max={0.5} step={0.01}
        fmt={(v) => `${Math.round(v * 100)}%`} onChange={(v) => set({ non_employment_rate: v })} />
      <Slider label="Weeks / year" value={params.weeks_per_year} min={40} max={52} step={1}
        fmt={(v) => `${v}`} onChange={(v) => set({ weeks_per_year: v })} />

      <div className="wt-result">
        <div className="wt-big">
          {forward ? forward.weekly_hours_per_worker.toFixed(1) : "…"}
          <span className="wt-unit"> h/week</span>
        </div>
        <div className="wt-sub">
          {forward
            ? `${(forward.employed / 1e6).toFixed(1)} M workers · ${(forward.production_hours / 1e9).toFixed(1)} G·hr/yr to produce`
            : ""}
        </div>
        {forward && forward.production_hours_delta < 0 && (
          <div className="wt-freed">
            ▼ {(-forward.production_hours_delta / 1e6).toFixed(0)} M·hr/yr freed by your levers (
            {((forward.production_hours_delta / forward.baseline_production_hours) * 100).toFixed(2)}%)
          </div>
        )}
      </div>

      <div className="wt-target">
        <div className="wt-target-row">
          <span>Target</span>
          <input type="number" min={1} max={80} step={0.5} value={target}
            onChange={(e) => setTarget(Number(e.target.value))} />
          <span>h/week →</span>
          <select value={solveFor} onChange={(e) => setSolveFor(e.target.value as SolveFor)}>
            <option value="retirement_age">retirement age</option>
            <option value="non_employment_rate">n%</option>
            <option value="start_age">start age</option>
          </select>
        </div>
        <div className={`wt-solved ${solved && solved.feasible ? "ok" : "no"}`}>{solvedText()}</div>
      </div>
    </section>
  );
}
