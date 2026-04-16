---
type: assumption_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: c6ed34d1-4a34-4db6-a398-47e7b8116f25
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: "current-above-threshold does not equal guaranteed noon-close-above-threshold"
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle on April 17 close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-variant-view-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-variant-view-binance-live-price-and-candles.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/variant-view.md"]
tags: ["assumption-note", "ethereum", "binance", "resolution-timing"]
---

# Assumption

Being roughly $98 above the threshold on April 16 morning ET is strong evidence for Yes, but it does not make the April 17 12:00 ET Binance 1-minute close mechanically safe because a single overnight drawdown of about 4-5% would still flip the contract to No.

## Why this assumption matters

The variant view depends on separating “currently above threshold” from “final governing minute close above threshold.” If that distinction is wrong or immaterial, the market’s 91% price is too conservative rather than slightly rich.

## What this assumption supports

- A modestly below-market Yes estimate rather than simply matching or exceeding the market.
- The claim that the market may be somewhat overconfident because traders can anchor on current spot rather than the exact future settlement minute.

## Evidence or logic behind the assumption

- The contract settles on one specific Binance 1-minute close at noon ET on April 17, not on any trade above 2200.
- Binance context shows ETH is above the line, but only by about 4.4%.
- ETH moved about 100 points within the observed 48-hour Binance context window, showing that nontrivial downside movement within a day is plausible.

## What would falsify it

- Evidence that ETH volatility has collapsed enough that a drop below 2200 by the settlement minute is extremely unlikely.
- Strong additional direct evidence of persistent support well above 2200 into late April 16 / early April 17.

## Early warning signs

- ETH holds above 2300 through multiple additional hourly closes.
- The April 17 pre-noon market remains comfortably above 2250 with low realized volatility.
- Market-implied probability rises toward the high 90s on stable price action rather than only sentiment.

## What changes if this assumption fails

If the noon-close-specific reversal risk is smaller than assumed, the correct probability should move closer to or above the market’s low-90s pricing.

## Notes that depend on this assumption

- Main finding for variant-view persona in this dispatch.