# Install paths

Canonical skill instructions live under `skills/deep-thought/`. That folder is the installable unit: `SKILL.md` plus the reference pages it routes to. Host adapters are thin. Plugin manifests point at `skills/`, or discovery folders symlink the skill.

Identical skill bytes. No per-host fork inside `SKILL.md`.

## Host matrix

| Host | How to install | Discovery / adapter | Map |
| --- | --- | --- | --- |
| **Grok Build** | `grok plugin marketplace add tony-sappe/deep-thought` then `grok plugin install deep-thought --trust` — or `grok plugin install tony-sappe/deep-thought --trust` | `.grok-plugin/marketplace.json` (plugin `source` is the git URL) + root `plugin.json` → `skills/` | Merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` |
| **Codex** | `codex plugin marketplace add tony-sappe/deep-thought` then `codex plugin add deep-thought@deep-thought` — or marketplace-add a local checkout path | `.codex-plugin/plugin.json` + `.agents/plugins/marketplace.json` → `skills/` | Same snippet |
| **Claude Code** | `/plugin marketplace add tony-sappe/deep-thought` then `/plugin install deep-thought@deep-thought` — or `claude --plugin-dir /path/to/deep-thought` | `.claude-plugin/plugin.json` (+ `marketplace.json`) → `skills/` | Same snippet |
| **GitHub CLI** | `gh skill install tony-sappe/deep-thought --all` | Discovers `skills/*/SKILL.md` via [agentskills.io](https://agentskills.io) / `gh skill` | Same snippet |
| **Cursor** | Open this repo, or use the canonical-folder link/copy commands in [Install](README.md#cursor--windsurf) | `.cursor/skills/deep-thought` → `skills/deep-thought` (also discovers `.agents/skills/`) | Same snippet |
| **Windsurf** | Open this repo, or use the canonical-folder link/copy commands in [Install](README.md#cursor--windsurf) | `.windsurf/skills/deep-thought` → `skills/deep-thought` | Same snippet |
| **Generic / no plugin** | Link the canonical skill folder by absolute path or copy `skills/deep-thought` using [Install](README.md#cursor--windsurf) | Prefer `.agents/skills/` when the host scans it | Same snippet |

## Adapter layout (this repo)

```text
plugin.json                          # Grok plugin identity (repo root)
skills/deep-thought/SKILL.md         # canonical skill
skills/deep-thought/references/      # taxonomy, overlap rules, tool pages
.agents/skills/deep-thought          # symlink → ../../skills/deep-thought
.cursor/skills/deep-thought          # symlink → ../../skills/deep-thought
.windsurf/skills/deep-thought        # symlink → ../../skills/deep-thought
.claude-plugin/plugin.json           # Claude Code plugin identity
.codex-plugin/plugin.json            # Codex plugin identity
.grok-plugin/marketplace.json        # Grok marketplace entry
.agents/plugins/marketplace.json
```

## Verify without installing a host

```bash
./scripts/validate.sh
```

Install the Python/PyYAML development requirements first; see [validation setup](README.md#validate-no-host-clis-required). The validator checks manifests, frontmatter, declared paths, local references, the tool index, adapters, and the no-hooks policy. Structural PASS is not host-runtime proof.

## Notes

- **Windows:** git symlinks need symlink privilege or Developer Mode. If links arrive as plain text files, use the PowerShell canonical-folder copy procedure in [Install](README.md#cursor--windsurf). Never copy the relative adapter links into another project.
- **On demand:** Deep Thought does not ship `.cursor/rules` or `.windsurf/rules` copies. The skill loads when invoked. The `AGENTS.md` snippet tells the host not to route ordinary work here.
