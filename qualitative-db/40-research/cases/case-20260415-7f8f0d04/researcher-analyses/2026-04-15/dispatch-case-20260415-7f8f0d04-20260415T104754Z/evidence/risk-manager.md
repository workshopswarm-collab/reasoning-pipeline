---
type: evidence_map
case_key: case-20260415-7f8f0d04
dispatch_id: dispatch-case-20260415-7f8f0d04-20260415T104754Z
research_run_id: 648e92f4-33bd-43e9-be14-3526acd379d5
analysis_date: 2026-04-15
persona: risk-manager
domain: tech-ai
subdomain: model-rankings
entity:
topic: "top-model resolution risk netting"
question: "Will claude-opus-4-6-thinking be the top AI model on April 17, 2026 (Style Control On)?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: mild
action_relevance: high
related_entities: ["anthropic", "claude"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["lm-arena-text-leaderboard", "claude-opus-4-6-thinking"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["risk-manager finding"]
tags: ["evidence-map", "top-model", "resolution-risk", "leaderboard"]
---

# Summary

The current evidence supports a YES lean, but the main risk is that the market may be pricing `Anthropic is probably near the top` as if it were equivalent to `the exact string claude-opus-4-6-thinking will be first at noon ET on April 17 under style control on`.

## Question being evaluated

Will `claude-opus-4-6-thinking` be the top model on the relevant LM Arena style-control-on text leaderboard when checked on April 17, 2026 at 12:00 PM ET?

## Current lean

YES lean, but less confident than the market.

## Prior / starting view

Starting view from the market price was that traders were treating this as very likely, around 87.4%.

## Evidence supporting the claim

- LM Arena fetch showed an Anthropic model currently ranked #1 around score 1502 ± 5.
  - Direct source: LM Arena leaderboard source note.
  - Why it matters causally: current leadership makes YES plausible.
  - Direct vs indirect: direct on current board state, indirect on exact future resolution.
  - Weight: high.

- The next listed competitor scores in the fetch were close but still below the top Anthropic row.
  - Why it matters: suggests current edge rather than trailing position.
  - Direct vs indirect: direct.
  - Weight: medium.

- Polymarket contract clearly names the same leaderboard family and the exact future check procedure.
  - Why it matters: confirms that current LM Arena state is the right resolution arena to monitor.
  - Direct vs indirect: direct on contract mechanics.
  - Weight: high.

## Evidence against the claim

- The fetched LM Arena text did not cleanly expose exact model strings, so exact mapping from current top row to `claude-opus-4-6-thinking` is not fully verified.
  - Why it matters causally: this market resolves on an exact string, not on vendor family.
  - Direct vs indirect: direct limitation of the evidence.
  - Weight: high.

- The leaderboard is tightly clustered near the top, so two days of movement could plausibly change first place.
  - Why it matters causally: even if the named model is first now, persistence to the check time is not guaranteed.
  - Direct vs indirect: indirect but material.
  - Weight: medium-high.

- Tie handling can hurt the `-thinking` suffix variant because alphabetical order is the tiebreaker.
  - Why it matters causally: a tied score may not favor the contract model.
  - Direct vs indirect: direct from contract wording.
  - Weight: medium.

## Ambiguous or mixed evidence

- Market price itself is evidence that many traders think the named model is likely top, but it may partly reflect broad Anthropic confidence rather than exact contract auditing.

## Conflict between inputs

There is no hard factual conflict between sources. The conflict is between broad directional support (Anthropic appears top) and insufficiently clean exact-string verification for the specific contract target.

## Key assumptions

- Current top Anthropic row is the exact named model.
- Style-control-on state in the fetched leaderboard aligns with contract interpretation.
- No rival model overtakes before the noon ET check.

## Key uncertainties

- Exact current model-string identity of the top row.
- Magnitude of near-term leaderboard churn.
- Whether any tie or near-tie will matter at the resolution timestamp.

## Disconfirming signals to watch

- Cleaner primary-source verification that another model string is currently first.
- Any update showing another model overtaking or tying the named model.
- Evidence of style-control-on/off confusion.

## What would increase confidence

- A cleaner capture of the live LM Arena table with full model names visible.
- A second independent verification pass closer to the resolution timestamp.
- Confirmation that the top row’s exact model string is `claude-opus-4-6-thinking`.

## Net update logic

The evidence keeps the thesis in YES territory because the primary source suggests Anthropic is currently leading. But the risk adjustment comes from contract exactness, imperfect model-name extraction, and close-enough competition that a future check is not the same as a current one.

## Suggested downstream use

Use as synthesis input with explicit emphasis on overconfidence risk, exact-string mapping risk, and time-of-check risk rather than pure directional disagreement.