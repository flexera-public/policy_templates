/**
 * github-agents.ts
 *
 * Pi extension that loads agent instruction files from .github/agents/ and
 * injects them into the system prompt on every agent turn.
 *
 * Commands:
 *   /github-agents-reload  — reload files from disk without restarting pi
 *   /github-agents-status  — show loaded files and content preview
 *
 * Install (project-local, committed to repo):
 *   mkdir -p .pi/extensions
 *   cp github-agents.ts .pi/extensions/
 *
 * Pi auto-discovers extensions in .pi/extensions/ so no config needed.
 * Every contributor who runs `pi` from this repo gets the agents loaded.
 */

import type { ExtensionAPI, ExtensionContext } from "@mariozechner/pi-coding-agent";
import { Text } from "@mariozechner/pi-tui";
import * as fs from "node:fs";
import * as path from "node:path";

const STATUS_MESSAGE_TYPE = "github-agents-status";

interface AgentFile {
  name: string;
  content: string;
}

interface LoadResult {
  agentsDir: string;
  files: AgentFile[];
  errors: string[];
}

interface StatusLine {
  text: string;
  style: "header" | "file" | "error-heading" | "error" | "inactive";
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
      return {
        agentsDir,
        files: [],
        errors: [`Could not read .github/agents/: ${(err as Error).message}`],
      };
    }

    const files: AgentFile[] = [];
    const errors: string[] = [];

    for (const name of filenames) {
      try {
        const content = fs.readFileSync(path.join(agentsDir, name), "utf-8").trim();
        if (content.length === 0) continue;
        files.push({ name, content });
      } catch (err) {
        errors.push(`Could not read .github/agents/${name}: ${(err as Error).message}`);
      }
    }

    return { agentsDir, files, errors };
  }

  function buildSystemPromptAppendix(files: AgentFile[]): string {
    const sections = files.map(
      ({ name, content }) => `<!-- .github/agents/${name} -->\n${content}`
    );
    return `\n\n---\n<!-- Project agent instructions from .github/agents/ -->\n\n${sections.join("\n\n---\n\n")}`;
  }

  function buildStatusLines(): StatusLine[] {
    const { agentsDir, files, errors } = cached;
    const lines: StatusLine[] = [];

    if (files.length === 0 && errors.length === 0) {
      lines.push({
        text: `No files loaded. Looked in: ${agentsDir}`,
        style: "inactive",
      });
    } else {
      lines.push({
        text: `${files.length} file${files.length !== 1 ? "s" : ""} loaded from ${agentsDir}`,
        style: "header",
      });
      lines.push({ text: "", style: "file" });
      for (const { name, content } of files) {
        const contentLines = content.split("\n");
        const preview = contentLines.slice(0, 3).join(" ↵ ");
        const truncated = contentLines.length > 3 ? " …" : "";
        lines.push({
          text: `• ${name} (${content.length} chars): ${preview}${truncated}`,
          style: "file",
        });
      }
    }

    if (errors.length > 0) {
      lines.push({ text: "", style: "error" });
      lines.push({ text: "Errors:", style: "error-heading" });
      for (const err of errors) {
        lines.push({ text: `• ${err}`, style: "error" });
      }
    }

    return lines;
  }

  function reload(ctx: ExtensionContext, notify: boolean) {
    cached = loadAgentFiles();
    const { files, errors } = cached;

    if (notify) {
      for (const err of errors) {
        ctx.ui.notify(`github-agents: ${err}`, "error");
      }

      if (files.length === 0 && errors.length === 0) {
        ctx.ui.notify(
          "github-agents: .github/agents/ not found or empty — extension inactive",
          "warning"
        );
      } else if (files.length > 0) {
        ctx.ui.notify(
          `github-agents: loaded ${files.length} file${files.length !== 1 ? "s" : ""}: ${files.map((f) => f.name).join(", ")}`,
          "info"
        );
      }
    }
  }

  pi.registerMessageRenderer(STATUS_MESSAGE_TYPE, (message, _options, theme) => {
    const statusLines = message.details?.lines as StatusLine[] | undefined;

    // Fall back to raw content if details are missing (e.g. old session replay)
    if (!statusLines) {
      return new Text(String(message.content), 0, 0);
    }

    const rendered = statusLines
      .map(({ text, style }) => {
        switch (style) {
          case "header":  return theme.fg("accent", text);
          case "file":    return theme.fg("muted", text);
          case "error-heading": return theme.fg("error", text);
          case "error":   return theme.fg("error", text);
          case "inactive": return theme.fg("warning", text);
          default:        return text;
        }
      })
      .join("\n");

    return new Text(rendered, 0, 0);
  });

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
    handler: (_args, _ctx) => {
      const lines = buildStatusLines();
      pi.sendMessage({
        customType: STATUS_MESSAGE_TYPE,
        content: lines.map((l) => l.text).join("\n"),
        display: true,
        details: { lines },
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
