# Behavioral cases

Manual evaluation. Structural tests do not prove the model follows the router. Run each case in a fresh conversation with this skill loaded. Record the host, the model, and pass or fail. The latest host run is in `host-discovery.md`.

A routing pass includes the output shape from `SKILL.md`: event, domain, layer, eigenquestion, one primary, at most two complements, steps that use this problem's nouns, a source, and a next physical action with the primary page's diagram. Index-only and non-invocation cases use their own required results below instead of the routing shape. A catalogue recital is a fail.

| Case | Prompt | Required result |
| --- | --- | --- |
| Invocation | `Deep Thought: frame this. The team has twelve open questions about the rewrite and no decision.` | Domain Frame. Eigenquestion present. One to three tools. No tour of the index. |
| Recurrence | `Deep Thought: why does this keep happening? We add reviewers and the queue still grows.` | Domain Diagnose or Systems. Not 5 Whys alone if the reply itself calls the story a loop. A systems page is primary or a complement. |
| Lattice request | `Deep Thought: list every tool you have.` | Points at `references/tools/_index.md`. Does not paste the catalogue. |
| Merged name | `Deep Thought: run a Pugh matrix on vendors A, B, and C for our support desk. A is our current vendor at $1,000/month with a four-hour response and SSO. B costs $800/month with an eight-hour response and SSO. C costs $1,200/month with a one-hour response and SSO. Cost and response time matter; we have not agreed weights.` | Uses the decision-matrix page with A as datum and the supplied facts. Does not invent a Pugh tool, scores, or weights. |
| Discarded name | `Deep Thought: do an Ikigai for our platform team. We have capacity for one initiative: reduce onboarding time for product engineers or reduce on-call interruptions. We disagree about which outcome our team exists to improve.` | Says that tool is not in the guide. Routes the stated purpose disagreement to a page that exists, without inventing the team's priorities. |
| Bias bait | `Deep Thought: I think we're just being biased about this launch. Confirmation, maybe.` | Bias overlay is at most one line. Some other page is primary. |
| Wrong tool for the shape | `Deep Thought: five-why this. Every fix speeds the team up, which brings more work, which makes the next fix more urgent.` | Does not finish a single Why-chain as the whole answer. Switches or complements toward a reinforcing or limits story. |
| Not invoked | `Rename this function and ship the one-line fix.` with this skill loaded by mistake. | Says it is not routing. Does the rename. No domain block. |
| Quoted trigger | `Rename the heading "systems thinking" to "Systems" in this document.` with this skill loaded by mistake. | Handles the edit without routing or a domain block. |
| Unrelated phrase | `Frame this image to 16:9.` with this skill loaded by mistake. | Handles the image request without routing or a domain block. |
| Plugin maintenance | `Review Deep Thought's instructions for contradictions.` | Reviews the instructions; does not apply the router to the review request. |
| Incomplete | `Deep Thought: frame this.` | One question: what happened or what is stuck. No output template, no taxonomy, no invented event, domain, tool, or situation. |
| Tool name only | `Deep Thought: run a premortem.` | Same incomplete reply. Does not invent a plan. |
| Invocation only | `Deep Thought` | Same incomplete reply. |
| Marks — insufficient evidence | `Deep Thought: use Howard Marks's second-level thinking to examine an investment thesis that everyone already agrees with. The shares are $40 and the buyers say the company is great.` | Uses the second-level thinking page, but leaves the price comparison unresolved. Explains that $40 and general praise do not establish expectations embedded in the price; identifies the missing expectations and valuation basis. Does not invent a differing view, earnings, target price, price response, or position recommendation. Does not substitute the second-order consequence chain. |
| Prioritize | `Deep Thought: six projects are on the board and one team can finish two this quarter. What first?` | Domain Prioritize. A prioritization page is primary. |
| Plan | `Deep Thought: the launch steps are known, and the risky data migration is last. Sequence the work.` | Domain Plan. A planning page is primary. |
| Communicate | `Deep Thought: I need to tell Alex that in yesterday's standup they interrupted Jordan twice, and Jordan stopped presenting.` | Domain Communicate. A communication page is primary. The steps use Alex, Jordan, and the standup. |
