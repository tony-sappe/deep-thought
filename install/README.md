# Install

Human notes only. The skill ships with its reference pages. Hosts still control discovery, tool permissions, and instruction following. See [`paths.md`](paths.md) for the host matrix.

Usage and the four moves: root [`README.md`](../README.md).

## Grok Build

```bash
grok plugin marketplace add tony-sappe/deep-thought
grok plugin install deep-thought --trust
```

Or from a local checkout:

```bash
grok plugin install /path/to/deep-thought --trust
```

Enable the plugin if it stays off (`/plugins` → Space, or `[plugins] enabled = ["deep-thought"]` in `~/.grok/config.toml`).

Start a **new session** (or reload) after install so the skill appears.

## Codex

Two steps: add the **marketplace**, then install the **plugin**. `deep-thought@deep-thought` fails if the marketplace was never added.

```bash
codex plugin marketplace add tony-sappe/deep-thought
codex plugin add deep-thought@deep-thought
```

Equivalent marketplace source:

```bash
codex plugin marketplace add https://github.com/tony-sappe/deep-thought.git
```

**From a local checkout** (no GitHub fetch):

```bash
codex plugin marketplace add /absolute/path/to/deep-thought
codex plugin add deep-thought@deep-thought
```

**Confirm:**

```bash
codex plugin marketplace list
codex plugin list --marketplace deep-thought
```

Expect `deep-thought@deep-thought` → installed, enabled, version `0.1.0`. Codex reads that version from `.codex-plugin/plugin.json`.

**Update later:**

```bash
codex plugin marketplace upgrade deep-thought
```

If the VERSION column stays stale after a release, remove and re-add the plugin (`codex plugin remove deep-thought@deep-thought` then `codex plugin add deep-thought@deep-thought`).

Start a **new thread/session** after install.

## Claude Code

```text
/plugin marketplace add tony-sappe/deep-thought
/plugin install deep-thought@deep-thought
```

Local checkout for one session, without a persistent install:

```bash
claude --plugin-dir /path/to/deep-thought
```

## GitHub CLI (Agent Skills)

```bash
gh skill install tony-sappe/deep-thought --all
```

Non-interactive defaults are `--agent github-copilot` and `--scope project` (the current repo). Pass `--agent` for another host and `--scope user` to install for every project. Several agents, including Copilot, Cursor, and Codex, share `.agents/skills/` at project scope. Claude Code, Grok, and Windsurf do not. Preview with `gh skill preview tony-sappe/deep-thought deep-thought`.

## Cursor / Windsurf

This repo already contains `.cursor/skills/` and `.windsurf/skills/` (symlinks into `skills/`). Opening the checkout is enough for discovery.

To use Deep Thought inside another project, link the **canonical skill folder** from a retained checkout. Do not copy this repository's relative adapter symlink into another project: its target depends on this repository's layout. Substitute your absolute paths below. These commands assume the destination name is unused; they do not overwrite an existing skill.

<!-- acceptance: symlink -->
```bash
deep_thought_repo="/absolute/path/to/deep-thought"
project="/absolute/path/to/project"
mkdir -p "$project/.cursor/skills"
for skill in "$deep_thought_repo"/skills/*; do
  destination="$project/.cursor/skills/$(basename "$skill")"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    echo "Destination already exists: $destination" >&2
    exit 1
  fi
  ln -s "$skill" "$destination"
done
```

Use `.windsurf/skills` or `.agents/skills` in place of `.cursor/skills` for those hosts. Keep the source checkout at the same absolute path while using links.

For a standalone copy that does not depend on the checkout location:

<!-- acceptance: copy -->
```bash
deep_thought_repo="/absolute/path/to/deep-thought"
project="/absolute/path/to/project"
mkdir -p "$project/.cursor/skills"
for skill in "$deep_thought_repo"/skills/*; do
  destination="$project/.cursor/skills/$(basename "$skill")"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    echo "Destination already exists: $destination" >&2
    exit 1
  fi
  cp -R "$skill" "$destination"
done
```

Windows PowerShell (copies avoid symlink privileges):

```powershell
$deepThoughtRepo = 'C:\src\deep-thought'
$project = 'C:\src\my-project'
$skillsRoot = Join-Path $project '.cursor/skills'
New-Item -ItemType Directory -Force -Path $skillsRoot | Out-Null
Get-ChildItem -Directory (Join-Path $deepThoughtRepo 'skills') | ForEach-Object {
    $destination = Join-Path $skillsRoot $_.Name
    if (Test-Path $destination) { throw "Destination already exists: $destination" }
    Copy-Item -Recurse -LiteralPath $_.FullName -Destination $destination
}
```

Validate a destination with the source checkout's validator:

```bash
python3 /absolute/path/to/deep-thought/scripts/validate.py --installed-skills /absolute/path/to/project/.cursor/skills
```

The destination check expects only this plugin's skill folder. For a mixed host root, check a separate temporary copy of that folder. Merge the AGENTS snippet below when you want the always-on "do not auto-run" note.

## AGENTS.md

Copy or merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` (prepend preferred). The snippet tells the agent to load this skill only when the user invokes it.

## Validate (no host CLIs required)

Python 3.9+ and PyYAML are development dependencies. Installing or reading the skill does not require them.

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
./scripts/validate.sh
python3 -m unittest discover -s tests -v
```

Tool pages are authored under `skills/deep-thought/references/`. There is no generated copy to sync. Validation parses JSON/YAML, checks declared paths, local reference closure, the tool index, adapters, and hook declarations. It is a structural gate, not a host-runtime or model-behavior proof.

Behavioral cases live in [`tests/behavioral.md`](../tests/behavioral.md).
