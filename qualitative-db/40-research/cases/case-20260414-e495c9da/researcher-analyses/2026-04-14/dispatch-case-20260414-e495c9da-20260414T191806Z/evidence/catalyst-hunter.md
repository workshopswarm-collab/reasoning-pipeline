---
type: evidence_map
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
research_run_id: ddc2c912-7662-421b-a988-702b790c0ee0
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-19
question: "Will the price of Bitcoin be above $70,000 on April 19?"
driver: operational-risk
date_created: 2026-04-14
agent: catalyst-hunter
status: complete
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["macro-event-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-e495c9da/researcher-analyses/2026-04-14/dispatch-case-20260414-e495c9da-20260414T191806Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "bitcoin", "catalyst"]
---

# Summary

The evidence nets to a high-probability Yes lean, but the catalyst lens argues against treating 90%+ as fully locked because the contract settles on one exact Binance minute close and BTC can still move several percent on short notice.

## Question being evaluated

Will Binance BTCUSDT close above 70,000 on the 12:00 ET one-minute candle on April 19, 2026?

## Current lean

Lean Yes, with the main residual risk coming from a sharp downside catalyst or exchange-specific pricing issue close to the observation window.

## Prior / starting view

Starting from the market baseline of 89.5%, the initial expectation was that Yes was likely but required extra verification because the market was already at an extreme probability and the contract wording is narrow.

## Evidence supporting the claim

- Live Binance BTCUSDT spot around 74,267 at research time.
  - Source: Binance ticker price fetch and source note.
  - Why it matters causally: the market starts with a cushion of roughly 4,267 above threshold.
  - Direct or indirect: direct.
  - Weight: high.

- Binance 24h low around 72,599.9, still above 70,000.
  - Source: Binance 24h ticker fetch and source note.
  - Why it matters causally: shows recent realized downside has not yet threatened the threshold.
  - Direct or indirect: direct.
  - Weight: high.

- Polymarket rule clearly keys settlement to Binance BTC/USDT noon ET 1-minute close.
  - Source: Polymarket event page and source note.
  - Why it matters causally: removes ambiguity about other exchanges or broader BTC reference prices.
  - Direct or indirect: direct for contract interpretation.
  - Weight: high.

## Evidence against the claim

- Bitcoin can move more than 5% within a few days or even intraday, so the current cushion is meaningful but not decisive.
  - Source: market structure inference from live volatility range and general BTC behavior.
  - Why it matters causally: a single sharp risk-off event could erase the cushion before the exact observation minute.
  - Direct or indirect: indirect/contextual.
  - Weight: medium-high.

- The contract is path-insensitive except for one exact minute close.
  - Source: Polymarket rule text.
  - Why it matters causally: even if BTC trades above 70k most of the week, a noon ET downtick on April 19 still resolves No.
  - Direct or indirect: direct for settlement logic.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- No confirmed high-information catalyst calendar item was established in this run because general web search failed, limiting confidence on event-specific timing.
- The Binance API verification is strong on mechanics and current state, but not the exact web UI surface referenced by Polymarket.

## Conflict between inputs

There is little factual conflict. The main issue is weighting-based: whether the existing 4k-plus cushion should justify a probability near the market's 89.5% or a bit lower because of narrow single-minute settlement risk.

## Key assumptions

- No major downside macro or crypto shock arrives before the observation window.
- Binance BTCUSDT remains a reliable settlement surface without abnormal dislocation.
- Current spot cushion is informative for five-day-ahead risk.

## Key uncertainties

- Whether a specific scheduled macro or crypto catalyst falls close enough to resolution to matter.
- Whether weekend liquidity conditions increase downside gap risk into Sunday noon ET.
- Whether Binance-specific price behavior diverges meaningfully from broader BTC spot.

## Disconfirming signals to watch

- BTC falls through the low-72k area and starts testing 71k-70k.
- A major negative regulatory, ETF-flow, liquidation, or macro surprise appears.
- Binance operational or pricing irregularities emerge.

## What would increase confidence

- Continued trading above 72k into late April 18 or early April 19.
- Additional verification of no major scheduled risk catalyst near the resolution window.
- Cross-exchange stability showing no Binance-specific weakness.

## Net update logic

The decisive evidence is not a new bullish catalyst but the combination of a clear resolution rule and a sizable current cushion above threshold. I downweighted generic bullish narrative because the contract cares about one exact minute. That makes downside shock timing the only serious remaining mechanism.

## Suggested downstream use

Use as an orchestrator synthesis input and as a forecast update input, with emphasis on monitoring downside catalysts and Sunday noon ET settlement mechanics rather than searching for more generic BTC-bullish evidence.