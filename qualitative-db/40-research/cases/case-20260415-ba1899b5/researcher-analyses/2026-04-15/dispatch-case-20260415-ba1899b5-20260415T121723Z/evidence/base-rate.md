---
type: evidence_map
case_key: case-20260415-ba1899b5
dispatch_id: dispatch-case-20260415-ba1899b5-20260415T121723Z
research_run_id: 01206f1c-852a-4730-b773-49f495722729
analysis_date: 2026-04-15
persona: base-rate
domain: culture
subdomain: streaming
entity: netflix
topic: will-netflix-inc-nflx-beat-quarterly-earnings
question: "Will Netflix Inc (NFLX) beat quarterly earnings?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low-direct-conflict-high-missing-primary
action_relevance: high
related_entities: ["netflix"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["base-rate-finding"]
tags: ["evidence-map", "earnings", "netflix", "base-rate"]
---

# Summary

This evidence map nets a very bullish market price against a less bullish outside-view prior built from contract mechanics, date verification, and recent realized diluted EPS history.

## Question being evaluated

Will Netflix report diluted GAAP EPS above $0.76 in the relevant next quarterly earnings release, within the timing and source rules in the contract?

## Current lean

Lean Yes, but much less strongly than the market.

## Prior / starting view

Starting prior was that a mega-cap, consistently profitable company can beat a modest-looking threshold reasonably often, but a 94.5% implied probability is unusually aggressive for an unsolved earnings threshold market unless the strike is clearly beneath current-quarter consensus.

## Evidence supporting the claim

- Polymarket contract shows a simple threshold event with no extra hidden conditions beyond timing, source, and rounding. This reduces operational complexity once the release occurs. Direct. Moderate weight.
- Netflix is a mature, consistently profitable company rather than a fragile or distressed issuer. That lowers tail risk of a catastrophic miss or reporting disruption. Indirect/contextual. Moderate weight.
- The estimated earnings date is imminent, April 16, 2026, so there is limited time left for new negative developments to emerge before resolution. Direct for timing. Low-to-moderate weight.

## Evidence against the claim

- Macrotrends historical diluted EPS series shows Netflix below $0.76 in every listed 2024 and 2025 quarter, including $0.66, $0.72, $0.59, and $0.56 in 2025. Direct historical context. High weight.
- Because the strike is above the recent realized range, Yes appears to require a real profitability step-up, not mere maintenance of recent performance. Interpretive, grounded in the historical series. High weight.
- Primary-source verification of the current-quarter official setup was incomplete because Netflix investor-relations pages were Cloudflare-blocked in this environment. That missing direct verification should compress confidence and keep the estimate away from extreme certainty. Direct process limitation. Moderate weight.

## Ambiguous or mixed evidence

- Nasdaq's earnings page was accessible but mostly data-poor in this environment; it indicates an earnings page exists but does not provide a reliable current-quarter consensus read here.
- The market itself may contain information from traders who have access to fresher consensus data, but using market price as proof of its own correctness would be circular.

## Conflict between inputs

There is no strong factual conflict among accessible sources. The main conflict is between market pricing near certainty and the weaker accessible outside-view evidence. This is primarily a weighting-based disagreement under source scarcity.

## Key assumptions

- Recent realized diluted EPS is a useful prior for the next quarter.
- No hidden current-quarter consensus revision has moved comfortably above $0.76.
- Netflix will report on or near the estimated date, making the 45-day delayed-release clause unlikely to matter.

## Key uncertainties

- Current-quarter sell-side consensus level.
- Whether Netflix has provided direct guidance or other evidence pointing above $0.76.
- Whether the relevant quarter has a seasonal or accounting feature making recent-quarter comparisons misleading.

## Disconfirming signals to watch

- Official release or credible pre-release coverage showing diluted GAAP EPS consensus well above $0.76.
- Direct investor-relations materials indicating a current-quarter outlook materially above recent realized levels.

## What would increase confidence

- Access to Netflix official investor-relations materials for the exact upcoming quarter.
- One clean independent consensus source showing the current-quarter GAAP EPS estimate.
- Historical beat-rate data versus consensus for Netflix using a reliable source.

## Net update logic

The base-rate prior starts with a profitable large-cap company and therefore does not point to No. But the accessible historical diluted EPS series keeps the prior from moving anywhere near the market's 94.5% confidence because the strike sits above every listed recent quarter. The result is a moderate Yes lean rather than a near-certain Yes.

## Suggested downstream use

- Orchestrator synthesis input.
- Decision-maker review, especially if another persona has fresher direct consensus evidence.
- Follow-up investigation focused narrowly on official IR materials and one reliable current-quarter consensus source.