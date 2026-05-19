import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "node:path";

export default defineConfig({
  plugins: [react()],
  base: "/equity_research/",
  build: {
    outDir: "dist",
  },
  server: {
    fs: {
      allow: [path.resolve(__dirname, "..")],
    },
  },
});
