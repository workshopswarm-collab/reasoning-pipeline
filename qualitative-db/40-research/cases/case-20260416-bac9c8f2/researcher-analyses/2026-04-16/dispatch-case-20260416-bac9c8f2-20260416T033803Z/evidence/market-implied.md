---
type: evidence_map
case_key: case-20260416-bac9c8f2
dispatch_id: dispatch-case-20260416-bac9c8f2-20260416T033803Z
research_run_id: 75ecccba-c083-431c-aa2c-7157b5bd39a2
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: reliability
date_created: 2026-04-15T23:41:00-04:00
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: medium
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-bac9c8f2/researcher-analyses/2026-04-16/dispatch-case-20260416-bac9c8f2-20260416T033803Z/personas/market-implied.md"]
tags: ["market-implied", "threshold-market", "binance", "auditability"]
---

# Summary

The market's roughly 71%-73% Yes price looks broadly efficient: BTC is currently above the threshold on the named exchange, but not by enough to justify near-certainty given ordinary one-day BTC volatility and one-minute-candle settlement risk.

## Question being evaluated

Will the Binance BTC/USDT one-minute candle for 12:00 ET on April 17, 2026 close above 74,000?

## Current lean

Moderate Yes lean, broadly in line with the market.

## Prior / starting view

Starting from the market-implied baseline of 0.71, the main task was to test whether that price under- or overstates the significance of BTC already trading above the threshold.

## Evidence supporting the claim

- Direct Binance price and recent one-minute klines were around 74,986 to 75,030 during the run.
  - Source: `researcher-source-notes/2026-04-16-market-implied-binance-btcusdt-price-and-klines.md`
  - Why it matters causally: the contract resolves off Binance BTC/USDT itself.
  - Direct or indirect: direct.
  - Weight: high.

- Polymarket neighboring strikes were internally coherent: 72k around 94%, 74k around 72%-73%, 76k around 32%.
  - Source: `researcher-source-notes/2026-04-16-market-implied-polymarket-rules-and-ladder.md`
  - Why it matters causally: suggests the market is pricing a plausible short-horizon BTC distribution rather than a stale isolated binary.
  - Direct or indirect: indirect for outcome, direct for market-implied view.
  - Weight: medium-high.

- Threshold distance is positive but modest, roughly 1.3%-1.4% above 74,000 at observation time.
  - Source: derived from Binance direct prints.
  - Why it matters causally: supports Yes but leaves enough downside room for failure.
  - Direct or indirect: direct.
  - Weight: medium-high.

## Evidence against the claim

- BTC can move more than 1% in less than a day with little warning, so current spot being above the line does not guarantee the noon ET print.
  - Source: contextual crypto volatility logic; reflected indirectly by the market not pricing Yes near 90%+.
  - Why it matters causally: one adverse move can flip the contract.
  - Direct or indirect: indirect/contextual.
  - Weight: high.

- The contract is resolved by one exact one-minute Binance candle close at 12:00 ET, which increases sensitivity to timing noise and exchange-specific prints.
  - Source: Polymarket rules note.
  - Why it matters causally: even if BTC is generally above 74k, a settlement-minute dip or Binance-specific wick could resolve No.
  - Direct or indirect: direct on mechanics.
  - Weight: high.

## Ambiguous or mixed evidence

- Coingecko and generic BTC summaries are directionally consistent with Binance being around 75k, but they are not the settlement source and add limited marginal value.
- The Polymarket webpage scrape is useful for rules and ladder context, but not itself authoritative for final settlement beyond quoting the contract.

## Conflict between inputs

There is little true factual conflict. The main tension is weighting-based: how much confidence should one assign to current price being above the threshold versus the fragility introduced by a one-minute time-specific close.

## Key assumptions

- Binance API prints are a good proxy for the exchange surface named in settlement rules.
- No major downside move or exchange-specific anomaly occurs before April 17 noon ET.
- The current market has already incorporated ordinary volatility risk reasonably well.

## Key uncertainties

- Short-horizon BTC volatility between now and settlement.
- Whether there is any pending catalyst or overnight risk not visible from a quick rules-plus-price pass.
- Exact alignment between Binance public API outputs and the GUI candle used at settlement.

## Disconfirming signals to watch

- BTCUSDT loses 74,500 and begins closing repeatedly below it.
- Cross-exchange weakness is concentrated on Binance.
- Any evidence that the settlement minute is likely to coincide with a known macro event or exchange-specific operational issue.

## What would increase confidence

- Another verification pass closer to settlement still showing BTC comfortably above 74,000.
- Continued internal coherence of adjacent strike prices.
- Additional confirmation that Binance API and GUI candle values match closely enough for practical settlement interpretation.

## Net update logic

The evidence did not justify a big move away from the market. Direct Binance prices support Yes, but the narrow, time-specific settlement mechanic keeps No meaningfully alive. That makes a low-70s probability more plausible than either a coinflip or a near-lock.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input; little additional research is needed unless price regime changes materially before settlement.