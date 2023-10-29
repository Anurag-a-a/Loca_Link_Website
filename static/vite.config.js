import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes("tinymce/skins/content/default/content.min.css")) {
            return "content-css"; // 为 content.min.css 文件创建一个单独的 chunk
          }
        },
      },
    },
  },
  css: {
    preprocessorOptions: {
      scss: {},
    },
  },
  resolve: {
    alias: {
      "@": resolve("./src"),
    },
  },

  plugins: [react()],
  server: {
    open: true,
  },
});
