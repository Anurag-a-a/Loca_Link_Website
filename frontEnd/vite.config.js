import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      "@": resolve("./src"),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {},
    },
  },
  plugins: [react()],
  server: {
    open: true,
  },
});
