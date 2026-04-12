---
type: evidence_map
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
research_run_id: b1bd99f0-882e-480f-929a-51b75f160793
analysis_date: 2026-04-11
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1m-candle-for-2026-04-11-12-00-et-close-above-72000
question: "Will the Binance BTC/USDT 1m candle for 2026-04-11 12:00 ET close above 72000?"
driver: operational-risk
date_created: 2026-04-10
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
downstream_uses: ["risk-manager finding"]
tags: ["btc", "binance", "evidence-netting"]
---

# Summary

The evidence nets to a moderate Yes lean, but the risk-manager view is less confident than the market because the threshold cushion is small and the contract depends on exact Binance minute-candle interpretation.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 2026-04-11 12:00 ET close above 72,000?

## Current lean

Lean Yes, but with meaningful residual downside from ordinary intraday volatility and narrow resolution mechanics.

## Prior / starting view

Starting point was the market price near 0.7125, implying a clear Yes favorite but not certainty.

## Evidence supporting the claim

- Binance BTCUSDT last trade and 24h ticker place spot around 72.9k, already above the threshold by roughly 1.2%. Direct, high weight.
- CoinGecko, Coinbase, and Kraken broadly confirm BTC near the same level, reducing concern that Binance is materially out of line at research time. Indirect/contextual, medium weight.
- Recent 1-minute Binance sample showed roughly 80% of closes above 72k in the sampled window, which is directionally supportive even if not a formal forecast. Direct to venue but only contextual to future resolution, medium-low weight.

## Evidence against the claim

- Binance 24h low near 71.4k shows the threshold has been penetrated recently; a sub-72k print by the exact noon ET minute is fully plausible. Direct, high weight.
- The contract depends on a single 1-minute candle close rather than a broader time average, making path timing risk important. Structural/contractual, high weight.
- There is mild source-of-truth ambiguity because Polymarket cites the Binance website chart UI, not a specific API call, leaving a small operational interpretation tail. Structural, medium weight.

## Ambiguous or mixed evidence

- Cross-exchange alignment is reassuring on general price level but does not settle Binance-specific minute-close behavior.
- A simple realized-volatility projection from recent Binance minute data suggested a probability in the mid-70s for finishing above 72k by the target minute, which roughly supports Yes but is model-sensitive and should not be treated as a precise forecast.

## Conflict between inputs

There was no major factual conflict across the checked sources. The main disagreement is not factual but weighting-based: how much to discount the current above-threshold spot level because the market resolves on one precise future minute.

## Key assumptions

- Noon ET maps to 16:00 UTC on 2026-04-11.
- The relevant candle is the one identified by open time at 16:00 UTC, with field 4 close price being decisive.
- Cross-exchange spot parity remains close enough that outside venues are useful contextual checks.

## Key uncertainties

- Exact BTC price path into the resolution minute.
- Whether Binance UI presentation could create a subtle interpretation mismatch versus API mechanics.
- Whether overnight or morning macro/crypto flow shocks hit before noon ET.

## Disconfirming signals to watch

- BTCUSDT losing 72k and failing to reclaim it during the US morning.
- Binance-specific weakness versus other spot venues.
- Any evidence that Polymarket/ Binance label the noon ET candle differently than expected.

## What would increase confidence

- Seeing BTC hold materially above 72k, ideally 72.5k-73k+, through the late morning ET window.
- A direct check of the Binance chart UI near resolution confirming the expected candle mapping.

## Net update logic

The evidence pulled the view slightly above the market-neutral baseline because BTC is already above 72k on the actual venue that matters. But the update stops well short of near-certainty because recent realized range shows the cushion is not large, and the contract's one-minute settlement design amplifies timing and interpretation risk.

## Suggested downstream use

Use this as synthesis input for a mildly contrarian risk adjustment: the base case is still Yes, but confidence should be tempered relative to a casual "price is already above the line" reading.