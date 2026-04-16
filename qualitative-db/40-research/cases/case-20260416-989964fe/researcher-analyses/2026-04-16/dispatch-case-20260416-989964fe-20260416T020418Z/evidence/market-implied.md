---
type: evidence_map
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
research_run_id: bc1386c8-af21-4134-ab96-549437c00cbc
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: will-the-binance-eth-usdt-12-00-et-one-minute-candle-close-on-2026-04-17-be-above-2200
question: "Will the Binance ETH/USDT 12:00 ET one-minute candle close on 2026-04-17 be above 2200?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance global exchange venue / exact canonical slug uncertain"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/market-implied.md"]
tags: ["crypto", "ethereum", "evidence-map", "market-implied"]
---

# Summary

The current market price looks mostly efficient: ETH is comfortably above the strike, the contract mechanics are clear, and the residual No probability seems to reflect ordinary short-horizon downside and settlement-minute execution risk rather than a hidden fundamental dispute.

## Question being evaluated

Will the Binance ETH/USDT 12:00 ET one-minute candle close on 2026-04-17 be above 2200?

## Current lean

Lean Yes with high but not absolute confidence.

## Prior / starting view

Starting view was that a 95.5 percent market-implied probability deserved respect because the threshold sat materially below current ETH spot, but it required verification given the extreme probability and precise settlement mechanics.

## Evidence supporting the claim

- Binance spot and recent 1m candles show ETH around 2354 to 2356.
  - Source: 2026-04-16-market-implied-binance-polymarket-resolution-and-spot.md
  - Why it matters: the settlement source itself is currently well above the threshold.
  - Direct or indirect: direct for current level, indirect for tomorrow's noon close.
  - Weight: high.

- Polymarket rules specify a single Binance 12:00 ET one-minute close above 2200.
  - Source: 2026-04-16-market-implied-binance-polymarket-resolution-and-spot.md
  - Why it matters: reduces ambiguity about what must happen for Yes.
  - Direct or indirect: direct on contract interpretation.
  - Weight: high.

- CoinGecko cross-check places ETH near 2354 and recent day trading in the low-to-mid 2300s.
  - Source: 2026-04-16-market-implied-coingecko-crosscheck.md
  - Why it matters: suggests Binance is not showing an isolated, unusual price premium.
  - Direct or indirect: contextual.
  - Weight: medium.

## Evidence against the claim

- Crypto can move several percent in less than 24 hours, so a roughly 6.6 to 7 percent drop into the settlement minute is not impossible.
  - Source: inferred from the short-horizon structure and the need for only one specific minute close.
  - Why it matters: this is the main reason No still deserves nonzero weight.
  - Direct or indirect: indirect.
  - Weight: medium.

- The contract is keyed to one exchange and one exact minute close, so exchange-specific microstructure or operational issues could matter.
  - Source: Polymarket rules plus exchange-specific settlement design.
  - Why it matters: even if broad ETH market stays strong, Binance-specific anomalies can affect settlement.
  - Direct or indirect: direct on mechanics, indirect on realized probability.
  - Weight: low-to-medium.

## Ambiguous or mixed evidence

- CoinGecko confirms broad level but not exact Binance noon ET close; useful cross-check but not decisive.
- Recent spot strength supports Yes but short-dated crypto thresholds remain path-sensitive.

## Conflict between inputs

No material factual conflict across sources. The main uncertainty is weighting-based: how much residual probability to assign to a sharp downside move or settlement-minute anomaly.

## Key assumptions

- ETH does not suffer a large downside move before noon ET on April 17.
- Binance remains a functioning, representative venue at settlement.

## Key uncertainties

- Overnight and morning crypto volatility.
- Exact Binance print at the one-minute settlement window.

## Disconfirming signals to watch

- ETH trading in the low 2200s or below ahead of U.S. morning.
- Binance-specific disruptions or visible divergence from other ETH/USD markets.

## What would increase confidence

- Fresh Binance and broad-market spot checks closer to settlement still showing ETH materially above 2200.
- Stable market conditions overnight with no exchange-specific issues.

## Net update logic

The extra verification pass did not uncover hidden rule complexity or price-level disagreement. Instead it confirmed that the market's extreme Yes pricing is mostly explained by a large cushion above the threshold plus clear settlement mechanics. That keeps the price looking efficient, though slightly rich because one exact-minute close on a volatile asset always retains some tail risk.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why the market-respecting lane stayed close to, but a bit below, the live market.