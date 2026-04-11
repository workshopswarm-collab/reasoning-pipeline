# Decision-Maker Planner

Planner code for the Decision-Maker stage should prepare the smallest deterministic input bundle needed for final judgment.

Likely responsibilities:
- locate canonical synthesis artifacts for a case
- resolve market / quote context inputs
- resolve optional portfolio context inputs
- build a compact decision-context bundle for the runtime step

Design rule:
- keep planner work deterministic
- keep prompts small
- include only the context needed to make a decision
- prefer structured inputs over large raw re-inlining
