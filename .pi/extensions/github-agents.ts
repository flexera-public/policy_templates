/**
 * github-agents.ts
 *
 * Pi extension that loads agent instruction files from .github/agents/ and
 * injects them into the system prompt on every agent turn.
 *
 * Install (project-local, committed to repo):
 *   mkdir -p .pi/extensions
 *   cp github-agents.ts .pi/extensions/
 *
 * Pi auto-discovers extensions in .pi/extensions/ so no config needed.
 * Every contributor who runs `pi` from this repo gets the agents loaded.
 */

import type { ExtensionAPI, ExtensionContext } from "@mariozechner/pi-coding-agent";
import * as fs from "node:fs";
import * as path from "node:path";

interface AgentFile {
  name: string;
  content: string;
}

interface LoadResult {
  agentsDir: string;
  files: AgentFile[];
  errors: string[];
}

export default function (pi: ExtensionAPI) {
  let cached: LoadResult = { agentsDir: "", files: [], errors: [] };

  function loadAgentFiles(): LoadResult {
    const agentsDir = path.join(process.cwd(), ".github", "agents");

    if (!fs.existsSync(agentsDir)) {
      return { agentsDir, files: [], errors: [] };
    }

    let filenames: string[];
    try {
      filenames = fs
        .readdirSync(agentsDir)
        .filter((f) => f.endsWith(".md") || f.endsWith(".txt"))
        .sort();
    } catch (err) {
      return { agentsDir, files: [], errors: [`Could not read .github/agents/: ${(err as Error).message}`] };
    }

    const files: AgentFile[] = [];
    const errors: string[] = [];

    for (const name of filenames) {
      try {
        const content = fs.readFileSync(path.join(agentsDir, name), "utf-8").trim();
        if (content.length === 0) continue; // skip empty files
        files.push({ name, content });
      } catch (err) {
        errors.push(`Could not read .github/agents/${name}: ${(err as Error).message}`);
      }
    }

    return { agentsDir, files, errors };
  }

  function buildSystemPromptAppendix(files: AgentFile[]): string {
    const sections = files.map(({ name, content }) => `<!-- .github/agents/${name} -->\n${content}`);
    return `\n\n---\n<!-- Project agent instructions from .github/agents/ -->\n\n${sections.join("\n\n---\n\n")}`;
  }

  function reload(ctx: ExtensionContext, notify: boolean) {
    cached = loadAgentFiles();
    const { agentsDir, files, errors } = cached;

    // Always surface errors, but only when notifying — avoids surprise
    // red toasts during silent session switches
    if (notify) {
      for (const err of errors) {
        ctx.ui.notify(`github-agents: ${err}`, "error");
      }

      if (files.length === 0 && errors.length === 0) {
        ctx.ui.notify(`github-agents: .github/agents/ not found or empty — extension inactive`, "warning");
      } else if (files.length > 0) {
        ctx.ui.notify(
          `github-agents: loaded ${files.length} file${files.length !== 1 ? "s" : ""}: ${files.map((f) => f.name).join(", ")}`,
          "info"
        );
      }
    }
  }

  pi.on("session_start", (event, ctx) => {
    const shouldNotify = event.reason === "startup" || event.reason === "reload";
    reload(ctx, shouldNotify);
  });

  pi.registerCommand("github-agents-reload", {
    description: "Reload files from .github/agents/ without restarting pi",
    handler: (_args, ctx) => {
      reload(ctx, true);
    },
  });

  pi.registerCommand("github-agents-status", {
    description: "Show currently loaded .github/agents/ files and their content preview",
    handler: (_args, ctx) => {
      const { agentsDir, files, errors } = cached;

      const lines: string[] = [];

      if (files.length === 0 && errors.length === 0) {
        lines.push(`No files loaded. Looked in: ${agentsDir}`);
      } else {
        lines.push(`${files.length} file${files.length !== 1 ? "s" : ""} loaded from ${agentsDir}`);
        lines.push("");
        for (const { name, content } of files) {
          const previewLines = content.split("\n").slice(0, 3);
          const preview = previewLines.join(" ↵ ");
          const truncated = content.split("\n").length > 3 ? " …" : "";
          lines.push(`• ${name} (${content.length} chars): ${preview}${truncated}`);
        }
      }

      if (errors.length > 0) {
        lines.push("");
        lines.push("Errors:");
        for (const err of errors) {
          lines.push(`• ${err}`);
        }
      }

      pi.sendMessage({
        customType: "github-agents-status",
        content: lines.join("\n"),
        display: true,
      });
    },
  });

  pi.on("before_agent_start", (event, _ctx) => {
    if (cached.files.length === 0) return;

    return {
      systemPrompt: event.systemPrompt + buildSystemPromptAppendix(cached.files),
    };
  });
}
