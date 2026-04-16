---
type: evidence_map
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
research_run_id: 773b307c-e7c0-4a7f-9c03-441850a7bbca
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-labeled-12-00-et-on-april-20-2026-close-above-70000
question: "Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 20, 2026 close above 70000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-analyses/2026-04-15/dispatch-case-20260415-7b143efd-20260415T132144Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "market-implied"]
---

# Summary

Evidence nets to a high-probability Yes view, with the main question being whether a roughly 6% spot cushion is enough to survive five more days and one specific settlement minute.

## Question being evaluated

Will Binance BTC/USDT’s 1-minute candle for 12:00 ET on April 20, 2026 have a final Close above 70,000?

## Current lean

Lean Yes with high but not extreme confidence.

## Prior / starting view

Starting from the market prior, 0.88 implied that traders already viewed this as a likely hold-above-threshold case rather than a fresh directional bet.

## Evidence supporting the claim

- **Direct Binance spot check above threshold by ~6%**  
  - Source: `researcher-source-notes/2026-04-15-market-implied-binance-spot-check.md`  
  - Why it matters: current state is already safely above 70k, so the market only needs price persistence, not a major rally.  
  - Direct/indirect: direct.  
  - Weight: high.

- **Contract mechanics are straightforward and tied to Binance’s own minute-close object**  
  - Source: `researcher-source-notes/2026-04-15-market-implied-polymarket-rules-and-price.md` and Binance kline check.  
  - Why it matters: reduces hidden interpretation risk; the market likely understands the settlement object.  
  - Direct/indirect: direct for rules, direct/contextual for API match.  
  - Weight: medium-high.

- **Only five days remain**  
  - Source: assignment timing plus explicit timezone conversion check.  
  - Why it matters: a shorter horizon generally supports current-price anchoring unless a known catalyst threatens the cushion.  
  - Direct/indirect: contextual.  
  - Weight: medium.

## Evidence against the claim

- **BTC can move more than 6% within five days**  
  - Source: market-structure common knowledge; no separate volatility artifact created.  
  - Why it matters causally: the current cushion is meaningful but not enormous for crypto.  
  - Direct/indirect: contextual.  
  - Weight: medium-high.

- **Resolution depends on one exact minute on one exact exchange**  
  - Source: Polymarket rules note.  
  - Why it matters causally: even if broader BTC trades well, Binance-specific prints or a transient intraminute selloff could decide the contract.  
  - Direct/indirect: direct.  
  - Weight: medium.

## Ambiguous or mixed evidence

- The market’s 0.88 price may reflect efficient aggregation of crypto traders’ understanding of short-horizon BTC stability, but it could also slightly overstate persistence because of crowd momentum when spot is already comfortably above threshold.

## Conflict between inputs

No major factual conflict between inputs. The main disagreement is weighting-based: how much confidence should a ~6% buffer earn over five days in BTC?

## Key assumptions

- The current BTCUSDT cushion is likely to hold into the settlement minute.
- Binance remains a reliable settlement surface without material pricing disruption.
- No major downside catalyst appears before April 20 noon ET.

## Key uncertainties

- Short-horizon realized volatility.
- Whether the exact noon ET minute prints below 70k despite broader strength.
- Exchange-specific execution or data anomalies.

## Disconfirming signals to watch

- BTC drifting toward 71k or below before April 20.
- Elevated downside volatility or macro shock.
- Binance-specific outage or unusual dislocation.

## What would increase confidence

- BTC holding above 72k into the final 24-48 hours.
- Additional Binance checks showing orderly market conditions and continuing cushion.

## Net update logic

The evidence mostly preserved the market prior rather than overturning it. What mattered most was the direct Binance price check and the exact rule confirmation. The main downweighting came from recognizing that the contract settles on one minute and BTC can still swing materially over five days, so a very high but sub-90 estimate still looks more defensible than simply copying the 0.88 market price upward.

## Suggested downstream use

Use as orchestrator synthesis input and as an auditable record of why the market-implied lane largely respects the live price while shaving a bit for volatility and single-minute settlement risk.