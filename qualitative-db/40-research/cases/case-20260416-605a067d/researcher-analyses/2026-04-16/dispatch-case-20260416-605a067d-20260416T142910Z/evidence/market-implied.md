---
type: evidence_map
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: 68f599bc-70db-4afc-921d-575b6a9e57c6
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: "Netting live Binance cushion against exact noon-close path risk"
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle close on April 17 be above 2200?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: final
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-market-implied-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-market-implied-binance-klines-and-docs.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/market-implied.md"]
tags: ["evidence-map", "crypto", "market-implied"]
---

# Summary

The evidence supports Yes as the base case because Binance ETH/USDT is already several percent above 2200. But because this is an exact future one-minute close contract rather than a touch contract, the market’s high-80s confidence still deserves a modest discount for path and timing risk.

## Question being evaluated

Will the Binance ETH/USDT 12:00 ET one-minute candle on April 17 have a final close above 2200?

## Current lean

Lean Yes, with probability in the low 80s rather than at the market’s upper-80s quote.

## Prior / starting view

Start from the market prior around 87.1% Yes because the market is pricing current cushion and crowd information.

## Evidence supporting the claim

- Live Binance ETHUSDT around 2298 at the time of check.
  - Source: Binance live API note.
  - Causal importance: gives direct cushion of roughly 98 points above threshold.
  - Direct vs indirect: direct contextual evidence, though not yet the settlement minute.
  - Weight: high.
- Recent sampled one-minute candles and 24h low remained above 2200.
  - Source: Binance live API note.
  - Causal importance: suggests 2200 is not merely barely crossed but comfortably inside recent trading range.
  - Direct vs indirect: direct contextual evidence.
  - Weight: medium-high.
- Cross-strike Polymarket ladder was internally coherent: 2100 near certainty, 2200 high confidence, 2300 near balanced, 2400 low.
  - Source: Polymarket rules and market-state note.
  - Causal importance: suggests traders are not obviously mispricing the distribution shape.
  - Direct vs indirect: indirect but information-rich market evidence.
  - Weight: medium.

## Evidence against the claim

- The contract settles on one exact future 12:00 ET one-minute close, not current spot and not any intraday touch.
  - Source: Polymarket rules note.
  - Causal importance: means a late selloff can flip the market even if ETH stays above 2200 most of the time.
  - Direct vs indirect: direct rule evidence.
  - Weight: high.
- The last hour before capture showed downside drift from about 2345 to about 2298.
  - Source: Binance live API note.
  - Causal importance: shows price is not static and some cushion has already been eroded.
  - Direct vs indirect: direct contextual evidence.
  - Weight: medium.
- Crypto can move more than 4% in 24 hours without extraordinary news.
  - Source: market-structure context inferred from observed volatility; not a separate source note.
  - Causal importance: keeps No nontrivial despite current cushion.
  - Direct vs indirect: contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- The Binance API and Binance UI are likely aligned for candle data, but the Polymarket rule names the UI surface specifically; this is close to resolved but not zero-ambiguity.
- The market may be incorporating order-flow or tacit sentiment not visible in a short manual check, but no specific hidden catalyst was identified.

## Conflict between inputs

There is little factual conflict. The disagreement is mostly weighting-based: how much to discount a comfortable current cushion for the fact that only one exact future minute close matters.

## Key assumptions

- Binance ETHUSDT will remain above 2200 through the relevant noon ET minute on April 17.
- Binance UI and API candle representations are functionally consistent for practical verification.
- No major macro or crypto-specific shock arrives before settlement.

## Key uncertainties

- Exact price path into the settlement minute.
- Whether a fast selloff near noon ET narrows or erases the current cushion.
- Whether the market is embedding unseen information that justifies its higher confidence.

## Disconfirming signals to watch

- ETH trading back toward or below 2240 on Binance during April 17 morning.
- Sharp broad crypto drawdown before noon ET.
- Any evidence of settlement-surface inconsistency on Binance.

## What would increase confidence

- Fresh April 17 morning Binance checks still showing ETH comfortably above 2200.
- Stability above 2200 across the final hours before noon ET.
- Direct UI capture of the governing candle once near completion.

## Net update logic

The market prior starts strong because the line is already in-the-money by several percent. I keep a modest discount versus market because the contract is close-above at one exact minute, not touch-above, and recent price action shows nontrivial but not dominant downside path risk.

## Suggested downstream use

Use as synthesis input for a mildly market-below but still clearly Yes-leaning interpretation, with emphasis on exact settlement-minute risk rather than thesis-level bearishness.