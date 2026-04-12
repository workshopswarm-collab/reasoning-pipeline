---
type: evidence_map
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
research_run_id: 0262fd61-c199-415c-a863-b45386315277
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-for-12-00-pm-et-on-2026-04-09-close-above-70000
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-09 close above 70000?"
driver: operational-risk
date_created: 2026-04-09
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/market-implied.md"]
tags: ["market-implied", "settlement", "binance", "timestamp"]
---

# Summary

The market price looks directionally reasonable: BTC was already trading above 70k by a meaningful margin, but the contract still carries real intraday price-path risk plus modest timestamp/source-surface risk, so sub-100% pricing is defensible.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-09 close above 70,000?

## Current lean

Lean yes, with probability in the low-to-mid 80s rather than near certainty.

## Prior / starting view

Start from the market at 78.5%, which already implies traders think the threshold is likely but not locked.

## Evidence supporting the claim

- Binance live BTC/USDT spot was above 71,000 during analysis, giving more than a 1,000-point cushion over the threshold.
  - direct/current market evidence
  - high weight because the contract resolves on Binance BTC/USDT specifically
- The governing source is a single official venue and a single 1-minute close, reducing interpretive ambiguity relative to multi-source markets.
  - direct/rules evidence
  - medium-high weight
- Polymarket order flow already priced the 70k line at 78.5%, suggesting crowd consensus that the threshold is more likely than not to hold into noon.
  - indirect but highly relevant aggregation evidence
  - medium weight

## Evidence against the claim

- BTC can move more than 1k intraday, so the current cushion is meaningful but not decisive over several remaining hours.
  - direct contextual market-risk evidence
  - high weight
- Exact settlement depends on one minute and one venue, creating operational sensitivity to brief spikes, reversals, or surface inconsistencies.
  - direct rules/mechanics evidence
  - medium-high weight
- Small discrepancies across Binance public API hosts on a recent live candle show that not every public surface is perfectly identical in real time.
  - direct verification evidence
  - medium weight

## Ambiguous or mixed evidence

- The Polymarket page scrape showed 86% on the public page while assignment metadata said current_price 0.785, implying either small feed lag or page/state mismatch. This does not change the directional view much but reduces confidence in treating any single non-runtime price snapshot as exact.

## Conflict between inputs

There is no major factual conflict on rules. The main conflict is weighting-based: how much intraday downside risk remains versus how much the current >70k spot level should dominate the estimate.

## Key assumptions

- Noon ET maps to 16:00 UTC on Binance for this date.
- The relevant candle is the candle identified by open time 16:00:00 UTC.
- Current Binance BTC/USDT level remains the best short-horizon anchor for the noon close probability.

## Key uncertainties

- Intraday BTC volatility over the remaining hours.
- Any last-minute Binance surface inconsistency around the governing close.

## Disconfirming signals to watch

- BTC falling back toward or below 70.5k before noon.
- Clarification that the market uses a different minute bucket than the open-time mapping.
- Observable divergence between Binance UI close and API-reported close near settlement.

## What would increase confidence

- A continued BTC cushion above 71k closer to noon ET.
- Confirmation from Binance UI or settlement precedent that the relevant candle is the 16:00 UTC open-time candle.

## Net update logic

The market prior already captured most of the story. Direct Binance spot being clearly above 70k pushed me slightly more bullish than the 78.5% assigned market price, but not to certainty because the contract is path-dependent on one minute and a volatile asset.

## Suggested downstream use

Use as orchestrator synthesis input and settlement-mechanics audit trail.