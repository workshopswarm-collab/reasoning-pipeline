---
type: evidence_map
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
research_run_id: 727e240c-327b-4b32-8699-6e38a29953db
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: will-the-binance-sol-usdt-12-00-et-1-minute-candle-close-be-above-80-on-april-19-2026
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close be above 80 on April 19, 2026?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/market-implied.md"]
tags: ["evidence-map", "crypto", "sol", "polymarket"]
---

# Summary

Netting the evidence favors `Yes` at a high but not extreme-certainty level because the source-of-truth venue already has SOL comfortably above 80 and the remaining horizon is short, but crypto volatility and exact-minute settlement mechanics keep this from being near-certain.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle for 12:00 ET on April 19, 2026 close strictly above 80?

## Current lean

Lean `Yes`, high probability.

## Prior / starting view

Starting from the market, the prior was 91.5% `Yes` from the quoted market price.

## Evidence supporting the claim

- **Direct Binance spot above threshold by meaningful cushion**  
  - Source: `2026-04-16-market-implied-binance-solusdt-spot-and-contract-source.md`  
  - Why it matters causally: the governing venue already has SOL around 85.27, so `Yes` requires maintenance more than fresh upside.  
  - Direct or indirect: direct to the governing exchange, indirect to final settlement.  
  - Weight: high.

- **Recent 1-minute Binance candles clustered in mid-85s**  
  - Source: same Binance source note.  
  - Why it matters causally: shows the level is not just a single print; recent microstructure is also above 80.  
  - Direct or indirect: direct exchange context, indirect to settlement.  
  - Weight: medium-high.

- **Secondary market cross-check aligned with Binance**  
  - Source: `2026-04-16-market-implied-coingecko-cross-check.md`  
  - Why it matters causally: lowers odds the direct read was stale or exchange-specific noise.  
  - Direct or indirect: contextual.  
  - Weight: medium.

- **Short time to expiry relative to cushion over strike**  
  - Source: market rules plus current spot observations.  
  - Why it matters causally: only a moderate drawdown over ~3.5 days is needed for `No`, but absent a catalyst the market often prices hold-above-threshold contracts efficiently from current distance to strike.  
  - Direct or indirect: inferential.  
  - Weight: medium-high.

## Evidence against the claim

- **Crypto volatility can erase a 6% cushion quickly**  
  - Source: general market structure and contract timing.  
  - Why it matters causally: SOL is a high-beta asset and can trade below 80 at the exact settlement minute even if it spends most of the period above it.  
  - Direct or indirect: contextual.  
  - Weight: high.

- **Exact-minute settlement risk**  
  - Source: market rules.  
  - Why it matters causally: the contract is about one specific 1-minute Binance close, not a daily close or average.  
  - Direct or indirect: direct contract interpretation.  
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Positive 24-hour move is supportive, but short-horizon momentum can reverse quickly in crypto and is not by itself durable evidence.

## Conflict between inputs

There is no strong factual conflict between sources. The main tension is weighting: whether the current ~$5 cushion over the strike justifies a >90% probability given exact-minute and weekend-style volatility risk.

## Key assumptions

- Current pricing on Binance remains broadly representative through expiry.
- No major negative Solana-specific or crypto-wide shock occurs before the settlement minute.
- The noon ET candle can be mapped cleanly from Binance’s time series without hidden timezone ambiguity.

## Key uncertainties

- Short-term realized volatility between now and April 19.
- Whether any weekend/event-driven move hits the exact settlement minute.
- Whether the market may be slightly underweighting path volatility because spot is already above strike.

## Disconfirming signals to watch

- SOL breaks back below 82 and fails to recover.
- Major crypto selloff emerges before the relevant noon ET window.
- Binance-specific dislocation or unusual wick behavior into the settlement minute.

## What would increase confidence

- Continued Binance trading above 83–84 into April 18–19.
- Absence of major market-wide risk-off catalysts.
- Another direct verification closer to settlement showing spot still comfortably above strike.

## Net update logic

The evidence keeps the view close to the market because the strongest market logic is simple and credible: the governing venue already has SOL well above 80, so the contract mostly asks whether that cushion persists for a few more days. I downweight near-certainty because the contract is exact-minute and crypto drawdowns of this size are not rare.

## Suggested downstream use

Use as orchestrator synthesis input and as a quick audit trail for why the market-implied lane did not take a reflexively contrarian stance.