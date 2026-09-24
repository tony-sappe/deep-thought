# Behavioral cases

Manual evaluation. Structural tests do not prove the model follows the router. Run each case in a fresh conversation with this skill loaded. Record the host, the model, and pass or fail.

A pass includes the output shape from `SKILL.md`: event, domain, layer, eigenquestion, one primary, at most two complements, steps that use this problem's nouns, a source, and a next diagram. A catalogue recital is a fail.

| Case | Prompt | Required result |
| --- | --- | --- |
| Invocation | `Deep Thought: frame this. The team has twelve open questions about the rewrite and no decision.` | Domain Frame. Eigenquestion present. One to three tools. No tour of the index. |
| Recurrence | `Deep Thought: why does this keep happening? We add reviewers and the queue still grows.` | Domain Diagnose or Systems. Not 5 Whys alone if the reply itself calls the story a loop. A systems page is primary or a complement. |
| Lattice request | `Deep Thought: list every tool you have.` | Points at `references/tools/_index.md`. Does not paste the catalogue. |
| Merged name | `Deep Thought: run a Pugh matrix on these three vendors.` | Uses the decision-matrix page. Does not invent a Pugh tool. |
| Discarded name | `Deep Thought: do an Ikigai for our platform team.` | Says that tool is not in the guide. Still classifies the event and routes to a page that exists. |
| Bias bait | `Deep Thought: I think we're just being biased about this launch. Confirmation, maybe.` | Bias overlay is at most one line. Some other page is primary. |
| Wrong tool for the shape | `Deep Thought: five-why this. Every fix speeds the team up, which brings more work, which makes the next fix more urgent.` | Does not finish a single Why-chain as the whole answer. Switches or complements toward a reinforcing or limits story. |
| Not invoked | `Rename this function and ship the one-line fix.` with this skill loaded by mistake. | Says it is not routing. Does the rename. No domain block. |
