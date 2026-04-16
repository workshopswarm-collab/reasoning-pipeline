---
type: evidence_map
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
research_run_id: 415584b8-57d1-4833-a6d9-41f2cd595fdb
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: threshold-close-markets
entity: sol
topic: "SOL above 80 on Apr 19 via Binance noon ET 1m close"
question: "Will the price of Solana be above $80 on April 19?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "sol"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-source-notes/2026-04-16-market-implied-polymarket-rules-and-binance-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/market-implied.md"]
tags: ["evidence-map", "sol", "polymarket", "binance"]
---

# Summary

The market's high Yes price is broadly defensible because Binance SOL/USDT is currently well above 80 and recent contextual price history also sits above that threshold. The main reason not to simply match the market is that this resolves on one exact noon ET one-minute close several days from now, so current price dominance can still be reversed by ordinary crypto volatility.

## Question being evaluated

Will the Binance SOL/USDT 12:00 ET one-minute candle on Apr 19 have a final Close strictly above 80?

## Current lean

Lean Yes, with probability high but a bit below market.

## Prior / starting view

Start from the live market prior of 88.5% Yes because the contract is exchange-specific but mechanically straightforward and SOL is already above the threshold.

## Evidence supporting the claim

- Direct contract/rules check shows the governing source is Binance SOL/USDT and the threshold is 80 at one exact minute. Weight: high. Direct on mechanism.
- Direct Binance API check showed SOL/USDT around 84.70 with recent one-minute closes near 84.7 on Apr 15 evening ET. Weight: high. Direct on current exchange-specific state.
- Independent CoinGecko 48-hour context showed roughly 82.96-87.34 range with latest around 84.73. Weight: medium. Contextual, but supports that 80 is below recent trading range.

## Evidence against the claim

- This is a point-in-time close market, not a touch market. A temporary breakdown at the governing minute is enough for No even if SOL trades above 80 most of the time. Weight: high. Directly mechanism-relevant.
- Crypto weekend volatility can produce several-percentage-point moves in short windows, and current cushion above 80 is meaningful but not overwhelming. Weight: medium.
- Exchange-specific settlement means Binance-specific dislocations or negative exchange-level issues could matter more than generic SOL strength. Weight: low-to-medium.

## Ambiguous or mixed evidence

- Recent price action has been above 80, but without a strong catalyst that can be read either as healthy buffer or as a condition vulnerable to routine mean reversion.
- The market's 88.5% may reflect good aggregation, but it may also partially compress the distinction between a current-above-threshold state and a future exact-minute close state.

## Conflict between inputs

No major factual conflict. The disagreement is mainly weighting-based: how much to discount the current-above-80 evidence for remaining path risk into Apr 19 noon ET.

## Key assumptions

- Current market price mostly reflects short-horizon volatility math rather than hidden information.
- Binance-specific settlement surface will behave normally.
- No major crypto-wide downside shock arrives before the event.

## Key uncertainties

- How much realized volatility SOL will see between now and Apr 19 noon ET.
- Whether weekend trading weakens altcoins enough to put 80 back in play.
- Whether Binance-specific prints diverge from broader spot references at settlement.

## Disconfirming signals to watch

- SOL revisiting 81-82 and failing to hold.
- Broad crypto risk-off move before the deadline.
- Any Binance operational issue affecting SOL/USDT pricing visibility.

## What would increase confidence

- Continued Binance SOL/USDT trading above 84 into Apr 18-19.
- Stable broader crypto sentiment.
- A fresh direct check closer to settlement confirming the noon-ET mapping and price cushion.

## Net update logic

The market prior already captures most of the obvious bullish evidence, and the direct Binance check supports it. I only net slightly below the market because the contract is a future exact-close condition rather than a touch condition, so some path-risk discount remains warranted.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why the market-implied lane was broadly supportive of the live price while still preserving a modest exact-timestamp discount.