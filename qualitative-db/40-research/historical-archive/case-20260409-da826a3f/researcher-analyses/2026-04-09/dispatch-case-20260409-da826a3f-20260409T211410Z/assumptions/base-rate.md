---
type: assumption_note
case_key: case-20260409-da826a3f
dispatch_id: dispatch-case-20260409-da826a3f-20260409T211410Z
research_run_id: feeb63a1-2d29-41b4-bdb8-391af0c0becd
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: btc-daily-close
entity: bitcoin
topic: bitcoin-above-68k-on-april-10
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-10 close above 68000?"
driver: operational-risk
date_created: 2026-04-09
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-da826a3f/researcher-analyses/2026-04-09/dispatch-case-20260409-da826a3f-20260409T211410Z/personas/base-rate.md"]
tags: ["assumption", "timezone", "binance", "settlement"]
---

# Assumption

The relevant settlement candle is the Binance BTC/USDT 1-minute bar **opened at 12:00 ET / 16:00 UTC** on 2026-04-10, and Binance’s API/UI timezone handling is consistent enough that this identifies the same candle Polymarket intends.

## Why this assumption matters

If the wrong minute is selected because ET is mapped incorrectly or the candle timing convention is misunderstood, the analysis could be directionally right about BTC level but still mis-handle the actual settlement rule.

## What this assumption supports

- The claim that rule ambiguity is low enough to treat this mainly as a price-level question.
- The claim that 68k is currently far enough below spot that “Yes” should remain the dominant base-rate outcome.

## Evidence or logic behind the assumption

- Polymarket explicitly specifies the Binance BTC/USDT 1-minute candle for 12:00 ET.
- Binance docs say klines are uniquely identified by open time.
- Binance docs also say `timeZone` changes interval interpretation while `startTime`/`endTime` remain UTC.
- 2026-04-10 12:00 ET is 16:00 UTC because New York is on EDT.

## What would falsify it

- Evidence that Polymarket historically interprets these contracts using a different candle boundary than the 1-minute bar opened at 12:00 ET.
- Evidence that Binance’s web UI candle selection for ET noon differs from the API interpretation in a way material to settlement.

## Early warning signs

- Conflicting examples from similar Polymarket crypto close markets.
- A Binance UI display convention that appears to label the bar by close time rather than open time.

## What changes if this assumption fails

The probability estimate should be reduced modestly because the case would carry more rule-resolution risk than price risk alone suggests, and further contract-interpretation work would be needed before trusting a high-confidence view.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-da826a3f/researcher-analyses/2026-04-09/dispatch-case-20260409-da826a3f-20260409T211410Z/personas/base-rate.md
