<p align="center">
  <img src="./assets/deep-thought-full.jpg" width="720" alt="Deep Thought">
</p>

<h1 align="center">Deep Thought</h1>

<p align="center">
  <em>The answer is useless without the question.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-1-0E4D5C?style=flat-square&labelColor=111111" alt="1 skill">
  <img src="https://img.shields.io/badge/tools-66-0E4D5C?style=flat-square&labelColor=111111" alt="66 tools">
  <img src="https://img.shields.io/badge/hosts-Grok%20%7C%20Codex%20%7C%20Claude%20%7C%20Cursor%20%2B-111111?style=flat-square" alt="Works across coding agents">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license"></a>
</p>

<p align="center">
  <a href="skills/deep-thought/SKILL.md">[deep-thought]</a>
</p>

<p align="center">
  <sub>The guide, by family</sub><br>
  <a href="skills/deep-thought/references/tools/_index.md#framing">[Framing]</a>
  &middot;
  <a href="skills/deep-thought/references/tools/_index.md#diagnosis">[Diagnosis]</a>
  &middot;
  <a href="skills/deep-thought/references/tools/_index.md#systems">[Systems]</a>
  &middot;
  <a href="skills/deep-thought/references/tools/_index.md#decision">[Decision]</a>
  <br>
  <a href="skills/deep-thought/references/tools/_index.md#prioritization">[Prioritization]</a>
  &middot;
  <a href="skills/deep-thought/references/tools/_index.md#planning">[Planning]</a>
  &middot;
  <a href="skills/deep-thought/references/tools/_index.md#communication">[Communication]</a>
</p>

---

<p align="center">
  <strong>Classify. Ask the question that collapses the rest. Hand over the tool.</strong><br>
  <sub>A router for thinking tools. Systems thinking is the spine. Everything else is an instrument you pick up on purpose.</sub>
</p>

Deep Thought does not run unless you invoke it. It does not recite the guide. The pages are for the agent to open one at a time.

## Install

Works as a plugin on **Grok Build**, **Codex**, and **Claude Code**. Other agents discover the skill from this repo (Cursor, Windsurf, and anything that scans `.agents/skills/`).

Commands and the host matrix: [`install/README.md`](install/README.md) · [`install/paths.md`](install/paths.md)

```bash
# Grok Build
grok plugin marketplace add tony-sappe/deep-thought
grok plugin install deep-thought --trust

# Codex
codex plugin marketplace add tony-sappe/deep-thought
codex plugin add deep-thought@deep-thought

# Agent Skills via GitHub CLI
gh skill install tony-sappe/deep-thought --all
```

Claude Code: `/plugin marketplace add tony-sappe/deep-thought` then `/plugin install deep-thought@deep-thought`.

Local checkout and non-plugin hosts: [`install/`](install/).

Start a **new session** (or reload) after install so the skill appears.

## Usage

Say the name, then the problem:

```text
Deep Thought: what should we even ask?
Deep Thought: why does this keep happening?
Deep Thought: frame this.
```

These also invoke it: `deep thought`, `thinking tools`, `systems thinking`, `eigenquestion`, `/deep-thought`.

Ordinary work is not a trigger. If you did not point at the skill, it should stay out of the way.

When it runs, it does five things and stops:

1. Restates the prompt as an event, with no solution in that sentence.
2. Names the domain and the iceberg layer.
3. States the eigenquestion.
4. Hands you one primary tool and at most two complements, with steps for this problem.
5. Tells you which diagram to draw next.

If you want the whole guide, ask for the index. The agent should point at [`references/tools/_index.md`](skills/deep-thought/references/tools/_index.md), not paste it.

| Family | Reach for it when |
| --- | --- |
| [Framing](skills/deep-thought/references/tools/_index.md#framing) | Deadlock, too many questions, the wrong altitude |
| [Diagnosis](skills/deep-thought/references/tools/_index.md#diagnosis) | Why this happened, and the cause might be a chain, a category, or a belief |
| [Systems](skills/deep-thought/references/tools/_index.md#systems) | It keeps happening. Loops, delays, policy resistance |
| [Decision](skills/deep-thought/references/tools/_index.md#decision) | You are choosing among options |
| [Prioritization](skills/deep-thought/references/tools/_index.md#prioritization) | Too much work. What first |
| [Planning](skills/deep-thought/references/tools/_index.md#planning) | Sequence, risk, capacity, invention |
| [Communication](skills/deep-thought/references/tools/_index.md#communication) | Explain, enroll, or give feedback |

Labels and layer definitions: [`references/taxonomy.md`](skills/deep-thought/references/taxonomy.md). What was merged, kept, or left out: [`references/overlap-map.md`](skills/deep-thought/references/overlap-map.md).

## Contributing

Python 3.9+ and PyYAML are development dependencies. Reading the skill does not require them.

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
./scripts/validate.sh
python3 -m unittest discover -s tests -v
```

Tool pages are authored in [`skills/deep-thought/references/tools/`](skills/deep-thought/references/tools/). Each page needs a job, when not to use it, a diagram, steps, and a source. Add a page to the index in the same change. Do not add a second copy of a page that [overlap-map.md](skills/deep-thought/references/overlap-map.md) already folded in.

[Behavioral cases](tests/behavioral.md) are manual. The validator checks structure and that every page is reachable. It does not prove an agent will route well.

〔[MIT](LICENSE)〕
