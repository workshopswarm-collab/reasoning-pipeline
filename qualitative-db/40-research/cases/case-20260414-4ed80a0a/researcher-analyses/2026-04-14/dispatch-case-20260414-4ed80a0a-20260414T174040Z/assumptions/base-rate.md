---
type: assumption_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: 23445208-5ef6-4cd8-978c-62c7f846d319
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: eth-price-threshold
question: "Will Ethereum reach $2,400 April 13-19?"
date_created: 2026-04-14
agent: orchestrator
status: active
certainty: high
importance: medium
time_horizon: days
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-venue-specific-price-threshold-resolution"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/base-rate.md"]
tags: ["assumption", "source-of-truth", "binance", "resolution"]
driver:
---

# Assumption

The economically relevant question is fully captured by the contract's venue-specific rule: a Binance ETH/USDT 1-minute candle High at or above $2,400 inside the stated ET window is sufficient regardless of broader cross-exchange dispersion.

## Why this assumption matters

The analysis becomes mostly a rules-and-verification exercise rather than a broader judgment about ETH's generalized market level. If this assumption were wrong, the case would require much more cross-venue or methodology analysis.

## What this assumption supports

- Treating Polymarket's Binance-specific rule as the governing source of truth.
- Giving very high probability / effective certainty to Yes once Binance data confirms a high above $2,400.
- Downweighting other exchange prices except as context.

## Evidence or logic behind the assumption

- The Polymarket market metadata explicitly names Binance ETH/USDT 1-minute candle High as the resolution source.
- The market description also explicitly excludes other exchanges, trading pairs, and spot references from consideration.

## What would falsify it

- Evidence that Polymarket used a different settlement source in practice.
- Evidence that the quoted API description was stale or mismatched to the actual resolving contract.
- Evidence that Binance's reported high did not occur inside the stated Apr 13-19 ET window.

## Early warning signs

- Inconsistency between Polymarket metadata and displayed rules text.
- Dispute, correction, or reversal in Polymarket settlement status.
- Binance 1-minute chart inspection showing no qualifying candle despite summary endpoints suggesting otherwise.

## What changes if this assumption fails

Confidence would fall sharply and the run would need a fresh resolution-mechanics audit, probably with lower confidence and more emphasis on timestamp-specific exchange data.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/base-rate.md
- qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-source-notes/2026-04-14-base-rate-polymarket-rules-and-state.md
- qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-source-notes/2026-04-14-base-rate-binance-24h-ticker.md