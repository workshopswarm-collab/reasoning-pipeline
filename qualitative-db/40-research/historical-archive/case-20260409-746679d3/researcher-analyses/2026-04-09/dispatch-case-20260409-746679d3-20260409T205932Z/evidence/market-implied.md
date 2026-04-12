---
type: evidence_map
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: b29230d1-9199-41b0-bfbe-3521de8f43e7
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity:
topic: eth-above-2100-apr-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/market-implied.md"]
tags: ["evidence-map", "settlement", "market-implied"]
---

# Summary

The market already appears to be pricing the contract largely correctly: ETHUSDT is currently trading well above 2100 on Binance, nearby strike pricing is internally coherent, and the remaining risk is mostly contract-timing or overnight drawdown risk rather than a hidden information gap.

## Question being evaluated

Will the Binance ETH/USDT 1-minute candle for 12:00 ET on Apr 10, 2026 have a final close above 2100?

## Current lean

Lean Yes, high probability but not certainty.

## Prior / starting view

Start from market price 0.94 and assume the market may already be efficiently summarizing both current spot level and contract-specific timing mechanics.

## Evidence supporting the claim

- **Live Binance 1m klines show ETHUSDT around 2211-2213 on Apr 9 afternoon ET**  
  - source: Binance live API note  
  - why it matters: current spot is roughly 5% above the strike with less than a day remaining  
  - direct/indirect: direct for current level, indirect for next-day noon settlement  
  - weight: high

- **Polymarket nearby strike ladder is coherent**  
  - source: Polymarket rules/price note  
  - why it matters: 2000 near certainty, 2100 very high, 2200 near coinflip-to-moderately-favored, 2300 low; this is exactly the shape expected if spot is in low 2200s  
  - direct/indirect: indirect but highly relevant market-structure evidence  
  - weight: medium-high

- **Binance kline mechanics are straightforward**  
  - source: Binance docs and API note  
  - why it matters: there is no complex benchmark basket or disputed oracle; one exchange and one candle reduces interpretive noise  
  - direct/indirect: direct for settlement mechanics  
  - weight: high

## Evidence against the claim

- **Single-minute settlement creates jump risk**  
  - source: contract wording itself  
  - why it matters: a brief drawdown below 2100 at the exact target minute is enough for No even if ETH is otherwise strong  
  - direct/indirect: direct  
  - weight: high

- **Small residual ambiguity around candle labeling**  
  - source: comparison between Polymarket wording and Binance documentation  
  - why it matters: an off-by-one-minute interpretation is unlikely but not impossible  
  - direct/indirect: direct contract-interpretation risk  
  - weight: low-medium

## Ambiguous or mixed evidence

- The assignment baseline price is 0.94 while the fetched event page showed about 0.974 for the 2100 line. This likely reflects time drift or page scrape timing rather than substantive disagreement.

## Conflict between inputs

There is no major factual conflict. The only mild conflict is between assignment metadata and fetched page price, which is best treated as timing drift in a fast market.

## Key assumptions

- The relevant candle is the 12:00 ET bar opened at 16:00 UTC.
- ETHUSDT remains roughly near current spot regime through tomorrow noon.

## Key uncertainties

- Overnight crypto volatility.
- Exact minute-level print at settlement.
- Whether Polymarket would use any UI-specific interpretation if the API/UI labeling looked odd.

## Disconfirming signals to watch

- ETHUSDT falling back toward 2120 or lower before the target window.
- Any Polymarket clarification changing candle interpretation.
- Exchange disruption or chart anomaly around the target minute.

## What would increase confidence

- A fresh check tomorrow morning showing ETHUSDT still comfortably above 2150.
- Confirmation from Binance UI that the noon-ET candle label aligns with the API open-time convention.

## Net update logic

The market-implied prior already captured most of the information. Direct exchange data did not reveal a hidden contradiction; instead it reinforced that the contract is mostly a one-minute threshold bet with ETH starting from a comfortable cushion above 2100. That makes a high-90s Yes price directionally sensible, though I trim slightly below near-certainty because one-minute resolution and crypto volatility still matter.

## Suggested downstream use

Use as synthesis input supporting a high-probability Yes lean, with explicit caveat that the residual risk is timing-specific rather than thesis-breaking.