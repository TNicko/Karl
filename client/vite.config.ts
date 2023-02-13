import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import viteTsconfigPaths from "vite-tsconfig-paths";
import svgrPlugin from "vite-plugin-svgr";

// https://vitejs.dev/config/
export default defineConfig({
  server: { host: "0.0.0.0", port: 5173 },
  plugins: [react(), viteTsconfigPaths(), svgrPlugin()],
});
