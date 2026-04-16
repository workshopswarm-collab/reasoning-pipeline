---
type: evidence_map
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
research_run_id: 7fe6d653-7ef6-4529-91ad-c4c267299931
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchange-price
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/risk-manager.md"]
tags: ["evidence-map", "risk-manager", "timing"]
---

# Summary

The evidence supports a Yes lean, but the risk-manager net is that the market is slightly too confident because it is pricing current distance-from-strike more aggressively than timing-specific crypto downside risk.

## Question being evaluated

Will Binance SOL/USDT print a final 1-minute candle close above 80 at 12:00 ET on 2026-04-19?

## Current lean

Yes lean, but with lower confidence than the market.

## Prior / starting view

Starting view was that a market at 0.92 Yes likely reflected SOL already trading above 80, but that a date-specific noon candle several days out should still carry nontrivial path risk.

## Evidence supporting the claim

- **Binance current price and recent 1m candles above 80**  
  - Source: `2026-04-16-risk-manager-binance-price-verification.md`  
  - Why it matters causally: this is the same exchange family named in the contract and shows the underlying currently clearing the strike by roughly 6%+.  
  - Direct or indirect: direct.  
  - Weight: high.

- **CoinGecko cross-check around 85.23**  
  - Source: `2026-04-16-risk-manager-coingecko-context-check.md`  
  - Why it matters causally: reduces risk that Binance was showing an anomalous print versus the broader market.  
  - Direct or indirect: indirect/contextual.  
  - Weight: medium.

- **Polymarket strike ladder context**  
  - Source: `2026-04-16-risk-manager-polymarket-rules-and-market-state.md`  
  - Why it matters causally: nearby strike pricing suggests the market sees SOL near the low/mid 80s rather than near the threshold.  
  - Direct or indirect: indirect market-implied context.  
  - Weight: medium.

## Evidence against the claim

- **There are still ~84.7 hours to resolution**  
  - Source: direct time calculation recorded during verification.  
  - Why it matters causally: crypto can move more than 6% over that horizon without requiring an extraordinary catalyst.  
  - Direct or indirect: direct to timing risk, indirect to price direction.  
  - Weight: high.

- **Resolution depends on one exact one-minute close, not broad average price**  
  - Source: market rules note.  
  - Why it matters causally: a brief downdraft or local dislocation at the specific noon ET candle can defeat an otherwise bullish path.  
  - Direct or indirect: direct contract-interpretation risk.  
  - Weight: medium-high.

- **Extreme market confidence leaves little room for ordinary uncertainty**  
  - Source: market state note.  
  - Why it matters causally: 89%-92% implies relatively little residual risk even though several conditions still must hold jointly.  
  - Direct or indirect: indirect.  
  - Weight: medium.

## Ambiguous or mixed evidence

- Current price being well above 80 is clearly supportive, but how supportive depends on the volatility regime over the next several days.
- Binance API data is strongly relevant, though the contract text points users to the Binance UI candle view rather than to the API specifically.

## Conflict between inputs

There is no major factual conflict between sources. The main disagreement is interpretive: whether a current ~6% buffer with ~3.5 days remaining deserves near-90s confidence or merely high-70s/low-80s confidence.

## Key assumptions

- Current price location remains informative for the final noon ET print.
- No contract-interpretation edge case changes the plain reading of the market.
- Binance remains a reliable and observable source for the final candle.

## Key uncertainties

- Short-horizon realized volatility in SOL over the remaining window.
- Market-wide crypto sentiment into the weekend.
- Whether a sharp but temporary noon ET dip could decide the contract against the broader path.

## Disconfirming signals to watch

- Binance SOL/USDT losing the 80 level before April 19.
- Multiple closes compressing the buffer to near 80-82.
- Exchange-specific anomalies around the settlement window.

## What would increase confidence

- SOL holding above 83-84 through the next 24-48 hours.
- Reduced realized volatility and broad crypto stability into the weekend.
- Confirmation that Binance UI and public API candle outputs remain aligned around minute closes.

## Net update logic

The evidence kept the lean at Yes because direct Binance pricing is above the strike by a meaningful margin and a secondary source confirmed the broad level. But the run did not endorse market confidence fully because the contract is both date-specific and minute-specific. The most important downweight was not a bearish fundamental story; it was path-and-timing fragility.

## Suggested downstream use

Use this as an orchestrator synthesis input and as a guardrail against overstating confidence simply because current spot is above the strike.