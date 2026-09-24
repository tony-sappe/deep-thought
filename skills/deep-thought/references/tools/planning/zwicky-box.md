# Zwicky box

**Job.** Generate options by crossing parameters, including combinations nobody brainstormed.

**Not this.** A way to choose among options you already have (decision matrix). Also not a prompt to implement the wildest cell. Generation and selection are separate.

**Diagram.** A grid. One column per parameter. Cells are the values that parameter can take. A handful of combinations circled, including at least one that surprises you.

**Steps.**
1. Name the parameters that define a solution in this problem (channel, user, timing, mechanism, constraint). Keep them independent enough to cross.
2. Under each parameter, list the real values available. Include the current value. Include one value that is legal and usually ignored.
3. Form combinations by taking one value from each column. You do not have to enumerate the full cartesian product in the reply. Sample deliberately: the current design, a neighbor, and a combination you would not have proposed in a meeting.
4. Strike combinations that violate a hard constraint. Mark the ones that are merely unfamiliar.
5. Hand the survivors to a decision tool. Do not pick a winner inside the grid by vibe.

**Source.** Fritz Zwicky, morphological analysis. Worksheet form: [Untools](https://untools.co).
