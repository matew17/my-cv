import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createInterface } from "node:readline/promises";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const mode = process.argv[2];
if (!["check", "status", "login"].includes(mode)) {
  console.error("Usage: node scripts/linkedin_session.mjs check|status|login");
  process.exit(1);
}

const client = new Client({ name: "my-cv-linkedin-session", version: "1.0.0" });
const transport = new StdioClientTransport({
  command: process.execPath,
  args: [resolve(root, "scripts/linkedin_mcp.mjs")],
  cwd: root,
});

async function call(name, args) {
  const result = await client.callTool({ name, arguments: args });
  if (result.isError) {
    throw new Error(result.content.filter(part => part.type === "text").map(part => part.text).join("\n"));
  }
  return result;
}

try {
  await client.connect(transport);
  const { tools } = await client.listTools();
  for (const name of ["browser_navigate", "browser_snapshot", "browser_fill_form", "browser_file_upload", "browser_take_screenshot"]) {
    if (!tools.some(tool => tool.name === name)) throw new Error(`Missing browser tool: ${name}`);
  }
  console.log(`MCP connected; ${tools.length} browser tools available.`);
  if (mode === "check") console.log(tools.map(tool => tool.name).join(", "));
  if (mode === "check") {
    await call("browser_navigate", { url: "about:blank" });
    console.log("Dedicated Chrome browser started successfully. No LinkedIn profile accessed.");
  } else if (mode === "login") {
    await call("browser_navigate", { url: "https://www.linkedin.com/login" });
    console.log("Sign in yourself in the dedicated Chrome window, including any MFA.");
    console.log("Do not paste your password or cookies into OpenCode. This session stays local to the project.");
    const terminal = createInterface({ input: process.stdin, output: process.stdout });
    try {
      await terminal.question("After LinkedIn shows your signed-in page, press Enter here to finish: ");
    } finally {
      terminal.close();
    }
    const result = await call("browser_evaluate", { function: "() => ({ url: location.href, loginForm: !!document.querySelector('input[type=password]') })" });
    const text = result.content.filter(part => part.type === "text").map(part => part.text).join("\n");
    if (/\/(login|checkpoint|authwall)\b|\"loginForm\":\s*true/.test(text)) {
      throw new Error("Login is still incomplete or LinkedIn requires a checkpoint. Rerun npm run linkedin:login.");
    }
    const session = await call("browser_run_code_unsafe", {
      code: "async page => { const cookies = await page.context().cookies('https://www.linkedin.com'); return { hasSession: cookies.some(cookie => cookie.name === 'li_at' && cookie.value.length > 0) }; }",
    });
    const sessionText = session.content.filter(part => part.type === "text").map(part => part.text).join("\n");
    if (!/\"hasSession\":\s*true/.test(sessionText)) {
      throw new Error("No LinkedIn session is present yet. Rerun npm run linkedin:login.");
    }
    console.log("Login session detected. Run /linkedin-review to verify access to your own profile.");
  } else {
    await call("browser_navigate", { url: "about:blank" });
    const result = await call("browser_run_code_unsafe", {
      code: "async page => { const cookies = await page.context().cookies('https://www.linkedin.com'); return { hasSession: cookies.some(cookie => cookie.name === 'li_at' && cookie.value.length > 0) }; }",
    });
    const text = result.content.filter(part => part.type === "text").map(part => part.text).join("\n");
    console.log(/\"hasSession\":\s*true/.test(text)
      ? "LinkedIn session present. Live validity and profile ownership still require /linkedin-review."
      : "No LinkedIn login session yet. Run npm run linkedin:login, or sign in during /linkedin-review.");
  }
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
} finally {
  try { await client.callTool({ name: "browser_close", arguments: {} }); } catch {}
  await client.close();
}
