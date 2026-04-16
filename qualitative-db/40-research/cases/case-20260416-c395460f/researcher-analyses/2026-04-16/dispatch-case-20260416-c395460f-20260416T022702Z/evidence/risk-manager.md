---
type: evidence_map
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
research_run_id: 7f9a8867-43dc-4458-b821-f20241efeedb
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: threshold-market
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 1-minute candle at 12:00 PM ET on 2026-04-19 close above 80?"
driver: operational-risk
date_created: 2026-04-15T22:28:00-04:00
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/risk-manager.md"]
tags: ["evidence-map", "threshold", "timing-risk"]
---

# Summary

The evidence leans Yes because Binance SOL/USDT is already above 80 and has recently traded above that level, but the market's 89% confidence likely understates timing-specific and path-dependent failure modes.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle corresponding to 12:00 PM ET on 2026-04-19 have a final close above 80?

## Current lean

Lean Yes, but with less confidence than the market.

## Prior / starting view

Starting view was that an 89% market on a short-dated crypto threshold looked directionally plausible but potentially too confident given crypto volatility and the exact-candle settlement rule.

## Evidence supporting the claim

- **Binance direct price context** — source note: `researcher-source-notes/2026-04-16-risk-manager-binance-context.md`
  - Current SOLUSDT fetched at 85.33 on Binance.
  - Causally matters because the contract settles on Binance SOL/USDT.
  - Direct evidence.
  - Weight: high.

- **Recent Binance daily range above strike** — same source note.
  - Recent sample daily lows remained above 80 in the returned window.
  - Matters because it suggests the strike is not merely barely touched at one moment.
  - Direct but imperfect evidence for the exact future minute.
  - Weight: medium-high.

- **Polymarket pricing at ~89-90% Yes** — source note: `researcher-source-notes/2026-04-16-risk-manager-polymarket-rules.md`
  - Matters as a crowd baseline and a check that the market broadly sees the strike as already in the money.
  - Indirect evidence.
  - Weight: medium.

## Evidence against the claim

- **Exact timestamp risk** — Polymarket rules source note.
  - The contract depends on one specific noon ET 1-minute close, not daily close or average price.
  - This matters because even a brief drawdown can flip resolution.
  - Direct contract-interpretation risk.
  - Weight: high.

- **Buffer above strike is real but not huge** — Binance context note.
  - 85.33 is only about 6.7% above 80, within normal crypto move size over several days.
  - Matters because the market is pricing near-certainty despite a cushion small enough to be erased by routine volatility.
  - Direct context.
  - Weight: high.

- **Venue-specific / operational edge risk** — rules and venue dependence.
  - Binance SOL/USDT specifically governs, so non-Binance strength would not save the trade if Binance underperforms or prints a brief adverse move.
  - Direct source-of-truth risk.
  - Weight: medium.

## Ambiguous or mixed evidence

- The recent Binance daily sample is supportive, but daily candles smooth over intraday noon-ET noise.
- Market pricing may reflect informed traders, but it may also compress uncertainty too aggressively on short-dated in-the-money threshold contracts.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting-based: how much to trust current >80 context versus how much to penalize exact-minute settlement risk.

## Key assumptions

- Current Binance >80 context remains broadly intact into April 19.
- There is no major weekend crypto drawdown.
- The noon ET minute is not unusually adverse relative to broader price action.

## Key uncertainties

- How volatile SOL will be over the remaining days.
- Whether the Binance noon ET minute could briefly print below 80 even if broader trend remains constructive.
- Whether market participants are underpricing precise settlement-minute risk.

## Disconfirming signals to watch

- SOL falling back toward 82 or lower on Binance before the event.
- A broad crypto risk-off move.
- Repeated failure to hold above 80 on intraday retests.

## What would increase confidence

- Sustained Binance SOL/USDT trading several dollars above 80 closer to April 19.
- Additional venue-specific intraday data showing stable support well above the threshold.

## Net update logic

The direct exchange data keeps the lean on Yes. The risk-manager haircut comes from the mismatch between an 89% market price and a settlement rule that depends on one precise minute only a few days away. The key downweight is not a bearish SOL thesis; it is concern that the market may be overconfident about timing fragility.

## Suggested downstream use

Use this as an orchestrator synthesis input and as a caution against treating the current in-the-money spot level as equivalent to a near-certain final resolution.