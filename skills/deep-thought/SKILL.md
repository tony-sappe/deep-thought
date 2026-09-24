---
name: deep-thought
description: "Route an explicit thinking problem to one primary tool and at most two complements. Use only when the user invokes Deep Thought, deep thought, thinking tools, systems thinking, frame this, eigenquestion, or /deep-thought to frame a problem. Mentions, quotations, and ordinary editing requests are not invocations."
license: MIT
metadata:
  collection: deep-thought
  version: "0.1.0"
---

> The answer is useless without the question.

## When it runs

Only when the user invokes Deep Thought, deep thought, thinking tools, systems thinking, frame this, or eigenquestion, or runs `/deep-thought`.

The user must be asking for this thinking workflow. Quoted text, names in documents, and requests to edit or review the plugin are not invocations. Neither is an unrelated use such as "frame this image".

If this skill loaded for any other reason, say you are not routing and do the user's actual ask. Do not classify it.

## Incomplete input

A situation is a concrete stake already in the prompt: what happened, what is stuck, or the options and facts in dispute. The skill name, a trigger phrase, and a tool name are not a situation.

Ask one question — what happened, or what is stuck — and stop. Do not read the taxonomy. Do not emit the output template. Do not invent an event, a domain, a layer, a tool, or facts. This is the whole reply when:

- The prompt is only an invocation: `Deep Thought`, `Deep Thought: frame this.`, or `/deep-thought`.
- The prompt names a tool and nothing else: `Deep Thought: run a premortem.`
- The prompt is only a domain phrase: `thinking tools` or `systems thinking`.

Continue when a situation is present, even if it is short. `Deep Thought: frame this. The team has twelve open questions and no decision.` is enough. So is a named disagreement or a set of options with facts.

## Protocol

Read `references/taxonomy.md` before you classify. Then stop at these moves:

1. Restate the raw prompt as an event. What happened, or what is stuck. No solution in that sentence.
2. Name one domain: Frame, Diagnose, Systems, Decide, Prioritize, Plan, or Communicate.
3. Name one iceberg layer: Events, Patterns, Structure, Mental models, or Goals/paradigm.
4. State the eigenquestion. The question whose answer collapses the rest.
5. Pick one primary tool and at most two complements from `references/tools/_index.md`. Read those pages. Do not read the rest of the guide.
6. For each chosen tool, write the job, when not to use it, and 3–6 steps on **this** problem. Cite the source on the page. Use the problem's nouns. Do not paste the page's generic steps unchanged.
7. Name the next physical action and the diagram to draw. Use the diagram named on the primary page.

If two tools seem to fit, read `references/overlap-map.md` and keep the one whose axis matches the event.

The bias overlay (`references/bias-overlay.md`) may be named in one line when a listed bias is distorting the frame. It is never the primary tool and never a complement that displaces a real tool.

If the user asks for the full guide, the lattice, or "all the tools", point at `references/tools/_index.md`. Do not recite it.

Canon and indexes: `references/sources.md`. Do not add a tool that is not on the index. If the user names a discarded tool, route the underlying event to a page that exists.

## Output

```text
Event:
Domain:
Layer:
Eigenquestion:
Primary: <tool> — <job on this problem>
Not when: <one sentence>
Steps:
1. ...
Source: <as on the page>
Complements: <none, or one or two in the same shape>
Next: <physical action and the diagram named on the primary page>
```

Three tools is the ceiling. Zero complements is normal.

## Anti-patterns

- A catalogue dump
- A tool that is not on the index
- Bias overlay as the main move
- Generic steps that could apply to any problem
- A solution smuggled into the event line
- A separate page for a merged name (Pugh matrix, a generic "feedback loop"). Use the page that absorbed it.
- Five Whys pushed through a loop or a multi-cause mess
