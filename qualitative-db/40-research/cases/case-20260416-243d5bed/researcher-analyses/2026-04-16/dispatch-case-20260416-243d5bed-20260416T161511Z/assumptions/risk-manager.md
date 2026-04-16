---
type: assumption_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
research_run_id: 3f8e7a4e-ff0a-42a1-9cfa-290069d73894
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-300-on-april-17
question: "Will the price of Ethereum be above $2,300 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-17 12:00 ET"
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/risk-manager.md"]
tags: ["threshold-risk", "timing-risk", "settlement-mechanics"]
---

# Assumption

ETH will remain sufficiently above 2300 into the April 17 noon ET Binance 1 minute settlement candle such that normal intraday volatility does not push the final relevant Close below the threshold.

## Why this assumption matters

The current Yes case depends less on long-horizon ETH direction and more on short-horizon path stability around one exact minute. If ETH revisits or dips below 2300 near noon ET on April 17, the market resolves No even if ETH traded above 2300 for most of the surrounding day.

## What this assumption supports

- A Yes-lean above 50%
- The interpretation that current spot above 2300 is meaningful evidence rather than noise
- The judgment that market pricing in the mid-70s is broadly reasonable but somewhat confidence-heavy

## Evidence or logic behind the assumption

- Binance direct spot and recent 1 minute klines during research were around 2338, giving a cushion of roughly 38 dollars above the threshold.
- The market itself priced the 2300 line around 71-75%, implying traders also view the threshold as more likely than not to hold by settlement.
- ETH is not sitting only a few cents above the line; there is at least some buffer.

## What would falsify it

- ETH trading back below 2300 on Binance during the hours before noon ET April 17.
- A sharp macro or crypto-specific selloff that erases the current cushion.
- Exchange-specific dislocation in Binance ETH/USDT relative to broader ETH pricing.

## Early warning signs

- ETH losing the 2320-2330 area before the final morning.
- Repeated minute closes drifting toward the threshold.
- Sudden divergence between Binance ETH/USDT and broad ETH spot references.

## What changes if this assumption fails

The case flips quickly from modest Yes-lean to No-lean or at least near-coinflip, because the contract only cares about one exact minute close rather than average daily trading level.

## Notes that depend on this assumption

- The main persona finding
- The evidence map for this run
