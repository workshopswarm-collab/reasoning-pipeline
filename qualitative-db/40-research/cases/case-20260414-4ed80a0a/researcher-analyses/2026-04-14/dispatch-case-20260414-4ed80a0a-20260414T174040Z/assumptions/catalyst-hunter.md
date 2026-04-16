---
type: assumption_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: d66c734c-2974-4d14-8528-3843c0bbd96e
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-14
agent: catalyst-hunter
status: active
certainty: medium
importance: medium
time_horizon: immediate
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-threshold-touch-resolution"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/catalyst-hunter.md"]
tags: ["assumption", "timing", "resolution", "binance"]
---

# Assumption

The decisive catalyst for this market is a brief Binance ETH/USDT threshold touch on a 1-minute candle, and once that happened the remaining week no longer mattered for the Yes/No outcome.

## Why this assumption matters

This assumption shifts the analysis away from broad week-ahead ETH direction and toward whether a qualifying intraperiod spike had already occurred under the exact rules.

## What this assumption supports

- A high probability estimate for Yes despite ETH later trading back below $2,400.
- The view that the most important catalyst was already realized rather than still upcoming.
- The interpretation that current sub-$2,400 spot quotes are not meaningful disconfirmation.

## Evidence or logic behind the assumption

- The extracted Polymarket rules explicitly say the market resolves Yes immediately if any Binance 1-minute candle high reaches the threshold during the date window.
- The page source for the `↑ 2,400` outcome showed it as closed and resolved with Yes priced at 1.
- Independent contextual exchange data (Kraken daily high above $2,400) makes a same-day threshold breach plausible rather than anomalous.

## What would falsify it

- Evidence that the extracted rules text was stale or not actually operative for this outcome.
- Evidence that the page source state was stale or erroneous and the contract later reopened or reversed.
- Direct Binance historical candle data showing no qualifying 1-minute high in the relevant ET window.

## Early warning signs

- A contradiction between Polymarket’s visible settlement state and Binance historical candles.
- A dispute or reversal on the Polymarket/UMA resolution path.
- Discovery that the market referred to a different price source than Binance ETH/USDT 1m highs.

## What changes if this assumption fails

If this assumption fails, the analysis would revert to a normal week-ahead catalyst question focused on whether ETH still had enough upside and volatility to trade above $2,400 before April 19.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/catalyst-hunter.md`