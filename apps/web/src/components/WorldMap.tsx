import maplibregl from "maplibre-gl";
import { useEffect, useRef } from "react";

interface Props {
  values: Record<string, number>;
  selectedRegion: string | null;
  onSelectRegion: (iso: string) => void;
  globe: boolean;
}

// Inline MapLibre style: no external tiles (offline), just our country polygons.
// Cast to any to avoid fighting MapLibre's strict expression literal types.
const STYLE: any = {
  version: 8,
  sources: {
    countries: { type: "geojson", data: "/countries.geojson", promoteId: "iso" },
  },
  layers: [
    { id: "bg", type: "background", paint: { "background-color": "#08121a" } },
    {
      id: "country-fill",
      type: "fill",
      source: "countries",
      paint: {
        "fill-color": [
          "interpolate",
          ["linear"],
          ["coalesce", ["feature-state", "t"], 0],
          0, "#0b1f2a",
          0.25, "#0e4a4f",
          0.5, "#1f7a5a",
          0.75, "#74c043",
          1, "#f2f25a",
        ],
        "fill-opacity": 0.92,
      },
    },
    {
      id: "country-line",
      type: "line",
      source: "countries",
      paint: {
        "line-color": [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          "#ffffff",
          "#2b4a5a",
        ],
        "line-width": [
          "case",
          ["boolean", ["feature-state", "selected"], false],
          2.5,
          0.4,
        ],
      },
    },
  ],
};

function applyValues(map: maplibregl.Map, values: Record<string, number>): void {
  const finite = Object.values(values).filter((v) => Number.isFinite(v) && v > 0);
  const max = finite.length ? Math.max(...finite) : 0;
  for (const [iso, value] of Object.entries(values)) {
    const t = max > 0 ? Math.pow(Math.max(value, 0) / max, 0.4) : 0;
    try {
      map.setFeatureState({ source: "countries", id: iso }, { t });
    } catch {
      // region without geometry (RoW aggregates, Malta) — ignore.
    }
  }
}

export function WorldMap({ values, selectedRegion, onSelectRegion, globe }: Props) {
  const containerRef = useRef<HTMLDivElement>(null);
  const mapRef = useRef<maplibregl.Map | null>(null);
  const readyRef = useRef(false);
  const prevSelected = useRef<string | null>(null);

  // Create the map once.
  useEffect(() => {
    if (!containerRef.current) return;
    const map = new maplibregl.Map({
      container: containerRef.current,
      style: STYLE,
      center: [10, 25],
      zoom: 1.3,
      attributionControl: false,
    });
    mapRef.current = map;
    map.addControl(new maplibregl.NavigationControl({ showCompass: false }), "top-right");

    map.on("load", () => {
      readyRef.current = true;
      applyValues(map, values);
    });
    map.on("click", "country-fill", (e) => {
      const iso = e.features?.[0]?.properties?.iso as string | undefined;
      if (iso) onSelectRegion(iso);
    });
    map.on("mouseenter", "country-fill", () => (map.getCanvas().style.cursor = "pointer"));
    map.on("mouseleave", "country-fill", () => (map.getCanvas().style.cursor = ""));

    return () => {
      map.remove();
      mapRef.current = null;
      readyRef.current = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Recolor when values change.
  useEffect(() => {
    const map = mapRef.current;
    if (map && readyRef.current) applyValues(map, values);
  }, [values]);

  // Highlight the selected region.
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !readyRef.current) return;
    if (prevSelected.current) {
      map.setFeatureState({ source: "countries", id: prevSelected.current }, { selected: false });
    }
    if (selectedRegion) {
      try {
        map.setFeatureState({ source: "countries", id: selectedRegion }, { selected: true });
      } catch {
        // no geometry for this region
      }
    }
    prevSelected.current = selectedRegion;
  }, [selectedRegion]);

  // Toggle globe / mercator projection (MapLibre GL JS v5).
  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const set = () => map.setProjection({ type: globe ? "globe" : "mercator" });
    if (readyRef.current) set();
    else map.once("load", set);
  }, [globe]);

  return <div ref={containerRef} className="map" />;
}
