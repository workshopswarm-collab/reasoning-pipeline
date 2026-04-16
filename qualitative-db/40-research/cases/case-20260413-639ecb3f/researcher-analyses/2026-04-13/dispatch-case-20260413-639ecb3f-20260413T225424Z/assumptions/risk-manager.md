---
type: assumption_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
research_run_id: a10e6d3e-9efd-4494-9641-024a999073f7
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
driver: liquidity
date_created: 2026-04-13
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "1 week"
related_entities: ["ethereum"]
related_drivers: ["liquidity", "sentiment"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "weekly-price-target", "crypto"]
---

# Assumption

The main working assumption is that ETH's remaining gap to $2,400 is small enough that normal one-week crypto volatility makes a touch more likely than not, even without a major new catalyst.

## Why this assumption matters

The probability estimate depends less on a strong bullish thesis than on path mechanics: if ordinary volatility is enough, the market's high probability is defensible; if realized volatility compresses or turns sharply negative, the thesis weakens fast.

## What this assumption supports

- A high but not near-certain probability estimate for ETH touching $2,400 during April 13-19.
- A view that the market is directionally right but somewhat overconfident.
- A risk framing that the disagreement is mostly about uncertainty and path risk, not about the basic direction.

## Evidence or logic behind the assumption

- Spot checks placed ETH around $2348-$2361, only about 1.6%-2.2% below the target.
- Weekly crypto moves of that size are common enough that the barrier is plausible without requiring an exceptional regime change.
- Cross-venue spot prices were consistent, reducing the odds that the market is reacting to a single anomalous print.

## What would falsify it

- Evidence that the market's rules require a stricter or different source than the contextual spot feeds and that source remains materially below $2,400 when others do not.
- A fast downside break that moves ETH materially away from the threshold early in the week.
- New evidence that realized volatility has collapsed enough that a further ~2% upside touch is no longer routine.

## Early warning signs

- ETH repeatedly failing near the mid/high-2300s and selling off on each approach.
- Widening divergence across exchanges or between settlement source and major spot venues.
- Broad crypto risk-off conditions that pull ETH materially below current levels.

## What changes if this assumption fails

If this assumption weakens, the correct move is not just trimming probability slightly; it means the market may be meaningfully underpricing path risk and hidden contract mechanics, which would justify moving well below the current 0.76 market price.

## Notes that depend on this assumption

- Main finding: `personas/risk-manager.md`
- Evidence map: `evidence/risk-manager.md`