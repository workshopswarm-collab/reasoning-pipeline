---
type: evidence_map
case_key: case-20260416-ec675d33
dispatch_id: dispatch-case-20260416-ec675d33-20260416T073538Z
research_run_id: 6f87b0a6-0e6b-49ba-890c-64618d3af2a6
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on 2026-04-20?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["timing-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-ec675d33/researcher-analyses/2026-04-16/dispatch-case-20260416-ec675d33-20260416T073538Z/personas/risk-manager.md"]
tags: ["evidence-map", "settlement-risk", "crypto"]
---

# Summary

The evidence nets to a Yes lean because current Binance BTC/USDT is already well above 72,000 and recent closes are mostly above the threshold, but the market may be a bit overconfident because the contract resolves on a single Binance minute close rather than a broad daily level.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 20, 2026 be strictly above 72,000?

## Current lean

Lean Yes, but with more timing fragility than the 84.5% market price suggests.

## Prior / starting view

Starting view was modest Yes because current spot was above strike and only four days remained, but I expected the single-minute settlement mechanic to create nontrivial downside tail risk.

## Evidence supporting the claim

- Binance direct ticker around 74,888.68 on April 16.
  - Source: source note on Binance price context.
  - Why it matters: current level is roughly 4% above threshold with limited time to settlement.
  - Direct or indirect: direct.
  - Weight: high.
- Recent Binance daily closes mostly above 72,000.
  - Source: same Binance note.
  - Why it matters: suggests threshold is not being barely held by one anomalous print.
  - Direct or indirect: direct contextual.
  - Weight: medium-high.
- Polymarket rules explicitly settle to Binance BTC/USDT, reducing cross-exchange ambiguity.
  - Source: Polymarket rules note.
  - Why it matters: the governing source is clear even if outcome remains uncertain.
  - Direct or indirect: direct for contract interpretation.
  - Weight: medium.

## Evidence against the claim

- The contract resolves on one exact minute close at 12:00 ET, not on spot now or daily close later.
  - Source: Polymarket rules note.
  - Why it matters: narrow timing windows increase path and wick risk.
  - Direct or indirect: direct.
  - Weight: high.
- Recent Binance data still showed a close near 70,740.98 within the short lookback.
  - Source: Binance note.
  - Why it matters: demonstrates that sub-72k outcomes are still plausible over a few days.
  - Direct or indirect: direct contextual.
  - Weight: medium.
- Current market price implies substantial confidence rather than just a directional edge.
  - Source: assignment current_price and Polymarket market page.
  - Why it matters: any hidden timing/volatility risk is magnified when the market is already pricing near 85%.
  - Direct or indirect: direct for market baseline.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Short time-to-settlement helps the Yes case if current spot stays stable, but it also leaves less time to recover from a sudden drawdown before the exact noon ET print.

## Conflict between inputs

No major factual conflict. The main issue is weighting: how much confidence should current >72k spot justify when the contract is a narrow single-minute event.

## Key assumptions

- BTC remains broadly above 72,000 into April 20.
- Binance settlement-minute behavior is representative rather than anomalous.
- No exchange-specific operational or microstructure event distorts the relevant print.

## Key uncertainties

- Intraday volatility between now and April 20.
- Noon ET price behavior specifically.
- Whether a sharp but temporary downside move occurs close to settlement.

## Disconfirming signals to watch

- BTC losing 72k decisively before April 20.
- Frequent intraday whipsaws around 72k.
- Binance-specific price irregularity or outage.

## What would increase confidence

- Continued Binance trading above 74k into the weekend.
- Additional evidence that noon ET prints have not been unusually weak or volatile.
- Reduced realized volatility approaching settlement.

## Net update logic

The direct exchange data keeps the case on the Yes side, but the contract wording prevents treating this as a near-lock. The market seems directionally right and slightly rich on confidence because it prices the event more like a broad daily-above-threshold question than a single-minute settlement test.

## Suggested downstream use

Use as an orchestrator synthesis input and as a caution against over-weighting the raw market price without adjusting for settlement-window fragility.