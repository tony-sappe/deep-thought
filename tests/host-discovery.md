# Host discovery and routing

Recorded 2026-09-24 from this checkout. Structural package tests do not count as a host pass. A result below is only what that command actually did.

| Host | Discovery | Routing |
| --- | --- | --- |
| Grok Build 1.0.41 | `grok plugin validate` on this checkout: manifest valid, version 0.1.0, one skill directory. `grok plugin list` does not include deep-thought. The plugin is not installed. | `grok -p` in this checkout, model `grok-4.7-build`, headless. The checkout's `AGENTS.md` was visible. Incomplete prompt asked what happened or what is stuck and did not emit the template. The twelve-question rewrite prompt routed to Frame, primary Eigenquestions, one complement, with sources and a diagram. |
| Codex 0.155.0-alpha.16.4 | `codex plugin list`: `deep-thought@deep-thought` installed, enabled, version 0.1.0, source this checkout. | `codex exec --ephemeral --sandbox read-only` saw the skill name, then failed closed. The code-mode host binary is missing, and disabling `code_mode_host` failed the same way. The incomplete prompt asked for a situation without loading the skill body. Tool-page routing was not exercised. |
| Claude Code | No `claude` binary on this machine. `.claude-plugin/plugin.json` is present and covered by the package validator. | Not run. |
| Cursor | No `cursor` binary. `.cursor/skills/deep-thought` is a symlink to `skills/deep-thought` and `SKILL.md` resolves. | Not run. |
| Windsurf | No `windsurf` binary. `.windsurf/skills/deep-thought` resolves the same way. | Not run. |
| GitHub CLI 2.101.0 | `gh skill list` finds `deep-thought` at `skills/deep-thought`, scope `project`, host `published`. It does not list a copy installed into the Cursor, Codex, Claude, or Grok skill directories. | Not run. `gh skill preview` fetches from GitHub rather than this working tree. |

Incomplete-input cases and the per-family prompts are in `behavioral.md`. Only the two Grok prompts above were run on a host.
