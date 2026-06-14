// Display helpers.

const compact = new Intl.NumberFormat("en", { notation: "compact", maximumSignificantDigits: 3 });
const percent = new Intl.NumberFormat("en", { style: "percent", maximumFractionDigits: 1 });

export function fmtValue(value: number, unit: string): string {
  if (!Number.isFinite(value)) return "n/a";
  return `${compact.format(value)} ${unit}`;
}

export function fmtPercent(fraction: number): string {
  if (!Number.isFinite(fraction)) return "n/a";
  return percent.format(fraction);
}

// Coverage flag -> visual treatment (rigour vs uncertainty must be distinct).
export function coverageColor(coverage: string): string {
  switch (coverage) {
    case "good":
      return "#3fb950";
    case "partial":
      return "#d29922";
    case "poor":
      return "#f85149";
    default:
      return "#8b949e";
  }
}

// Sequential ramp for the choropleth (dark -> bright), t in [0, 1].
export const RAMP: [number, string][] = [
  [0.0, "#0b1f2a"],
  [0.25, "#0e4a4f"],
  [0.5, "#1f7a5a"],
  [0.75, "#74c043"],
  [1.0, "#f2f25a"],
];
