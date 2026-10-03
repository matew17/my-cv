import { mkdirSync } from "node:fs";
import { spawn } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const profile = resolve(root, ".local/linkedin/browser-profile");
const output = resolve(root, "output/linkedin");
mkdirSync(profile, { recursive: true, mode: 0o700 });
mkdirSync(output, { recursive: true, mode: 0o700 });

const server = spawn(process.execPath, [
  resolve(root, "node_modules/@playwright/mcp/cli.js"),
  "--browser", "chrome",
  "--user-data-dir", profile,
  "--output-dir", output,
  "--no-webmcp",
], { cwd: root, stdio: "inherit" });

for (const signal of ["SIGINT", "SIGTERM"]) {
  process.on(signal, () => server.kill(signal));
}
server.on("error", (error) => {
  console.error(`LinkedIn browser could not start: ${error.message}`);
  process.exitCode = 1;
});
server.on("exit", (code) => {
  process.exitCode = code ?? 1;
});
