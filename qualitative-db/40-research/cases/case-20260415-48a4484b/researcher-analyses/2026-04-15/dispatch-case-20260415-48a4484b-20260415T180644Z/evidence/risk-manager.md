---
type: evidence_map
case_key: case-20260415-48a4484b
dispatch_id: dispatch-case-20260415-48a4484b-20260415T180644Z
research_run_id: 4e9d7e90-67e2-4b1c-ad3c-93d512c9f74f
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-on-2026-04-16-close-above-72000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "timing", "binance"]
---

# Summary

The evidence leans Yes because the named settlement source currently prices BTC/USDT well above 72,000, but the risk-manager view discounts the market’s very high confidence because this is a narrow, time-specific close condition rather than a broad daily average.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-16 have a final close above 72,000?

## Current lean

Lean Yes, but with meaningful path/timing risk that makes sub-95% confidence more appropriate than near-certainty.

## Prior / starting view

Starting view was that market pricing near 93.5% likely reflects BTC already trading comfortably above the threshold, but that a risk pass should test whether the market is underpricing timing-specific volatility or contract mechanics.

## Evidence supporting the claim

- **Polymarket rules + Binance direct price check**
  - Source: `2026-04-15-risk-manager-binance-polymarket-resolution-check.md`
  - Why it matters causally: this pairs the exact contract condition with the current level on the named settlement venue.
  - Direct vs indirect: direct.
  - Weight: very high.

- **Recent Binance 1-minute kline closes around 74.2k**
  - Source: same note.
  - Why it matters causally: confirms the current spot observation is not a stale one-off print and that the market is trading materially above threshold.
  - Direct vs indirect: direct.
  - Weight: high.

## Evidence against the claim

- **The market settles on one exact minute close, not on current spot or broad daily level**
  - Source: same note / Polymarket rules.
  - Why it matters causally: a temporary selloff at the relevant minute is enough to resolve No.
  - Direct vs indirect: direct contract interpretation.
  - Weight: high.

- **A roughly 3% downside move would erase the current cushion**
  - Source: derived from Binance spot level versus 72k threshold.
  - Why it matters causally: BTC can move several percent inside a day; the threshold is not so far away that failure is negligible.
  - Direct vs indirect: indirect/analytical.
  - Weight: medium.

## Ambiguous or mixed evidence

- Secondary contextual source checking was weak because the fetched CoinDesk page did not yield a strong timestamped quote. This modestly reduces independent confirmation quality, though it does not challenge the primary Binance-based view.

## Conflict between inputs

No major factual conflict. The tension is between a strongly favorable current spot level and the nontrivial risk introduced by the contract’s narrow settlement timing.

## Key assumptions

- Binance API spot/kline behavior is a reasonable proxy for the eventual web-surface candle used in settlement.
- No major market shock drives BTC below 72k before noon ET on Apr 16.

## Key uncertainties

- Overnight / morning BTC volatility into the settlement window.
- Whether any exchange-specific microstructure behavior on Binance could matter around the precise minute close.

## Disconfirming signals to watch

- BTC moving back toward 73k or lower before the final hours.
- A rapid selloff near the settlement window.
- Any Binance-specific price anomaly.

## What would increase confidence

- BTC holding above 74k into the morning of Apr 16.
- Another direct Binance check closer to settlement still showing a comfortable cushion.

## Net update logic

The direct evidence is strong enough to justify a Yes lean, but the risk adjustment comes from contract structure: current spot >72k is necessary evidence, not sufficient certainty. The market’s 93.5% price looks directionally sensible yet slightly too complacent about a narrow one-minute settlement condition.

## Suggested downstream use

- Orchestrator synthesis input
- forecast update
- decision-maker review