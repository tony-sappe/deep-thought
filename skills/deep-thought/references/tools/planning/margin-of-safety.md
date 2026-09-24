# Margin of safety

**Job.** Design the plan so it still works when your estimate is wrong by a stated amount.

**Not this.** Padding added without a stated error. A round number on a date is not a margin until you say which mistake it absorbs. Also not redundancy of paths (slack). Margin is distance between the load you expect and the load that breaks the plan.

**Diagram.** The estimate, the break point, and the gap between them labeled with the error it covers.

**Steps.**
1. Name the estimate the plan depends on (demand, time, load, skill, price, failure rate).
2. Name the break point: the value at which the plan fails in a way you care about.
3. State how wrong you have been on this kind of estimate before. If you have no history, the margin has to be wider and you should say the history is missing.
4. Place the plan's operating point far enough from the break point to cover that error. If you cannot, change the plan or decline the commitment.
5. Do not spend the margin on purpose in the next planning round. A margin that is immediately consumed was a wish.

**Source.** Benjamin Graham, *The Intelligent Investor*: in investing, a margin of safety is buying far enough below value that you can be wrong and still be all right. The engineering factor of safety is older and separate. This page uses the shared idea, an operating point short of a stated break, not Graham's net-asset calculation. Farnam Street and James Clear are indexes.
