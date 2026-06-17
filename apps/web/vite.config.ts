import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// Dev: Vite serves the SPA and proxies the JSON API to the FastAPI server.
// Prod: `vite build` emits to dist/, which FastAPI serves at "/" (single origin).
// The dev proxy target follows WORLD4_API_PORT (default 8000) so it lines up with
// the port you start the API on (8000 is reserved on some Windows setups).
const apiPort = process.env.WORLD4_API_PORT ?? "8537";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": `http://127.0.0.1:${apiPort}`,
    },
  },
  build: {
    outDir: "dist",
  },
});
