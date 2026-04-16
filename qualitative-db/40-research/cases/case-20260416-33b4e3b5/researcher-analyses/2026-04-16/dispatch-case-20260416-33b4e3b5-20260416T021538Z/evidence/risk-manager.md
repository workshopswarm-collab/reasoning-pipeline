---
type: evidence_map
case_key: case-20260416-33b4e3b5
dispatch_id: dispatch-case-20260416-33b4e3b5-20260416T021538Z
research_run_id: 67c7c895-78bf-4dd2-bcde-7d6858f9f131
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-price-resolution
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 1-minute candle closing at 12:00 ET on 2026-04-19 be above 80?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-33b4e3b5/researcher-analyses/2026-04-16/dispatch-case-20260416-33b4e3b5-20260416T021538Z/personas/risk-manager.md"]
tags: ["evidence-map", "risk-manager", "timing-risk"]
---

# Summary

The evidence leans Yes because current Binance SOLUSDT trades materially above 80, but the risk-manager haircut comes from narrow settlement mechanics and short-horizon crypto volatility.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above 80?

## Current lean

Lean Yes, but with lower confidence than the market price suggests.

## Prior / starting view

Starting view from market price was that traders were treating the outcome as very likely given current SOL levels.

## Evidence supporting the claim

- **Current Binance SOLUSDT around 84.91**
  - Source: Binance API source note.
  - Why it matters: the asset is already several dollars above the threshold.
  - Direct or indirect: direct.
  - Weight: high.

- **Recent Binance 1-minute closes around 84.76-84.94**
  - Source: Binance API source note.
  - Why it matters: confirms the threshold is not being cleared by a razor-thin margin right now.
  - Direct or indirect: direct.
  - Weight: medium-high.

- **Short time to settlement**
  - Source: contract timing and assignment metadata.
  - Why it matters: fewer days remain for a large downside move to develop.
  - Direct or indirect: contextual.
  - Weight: medium.

## Evidence against the claim

- **Resolution is based on one exact 12:00 ET minute close on Binance**
  - Source: Polymarket rules / source note.
  - Why it matters: narrow timing creates path dependence and makes intraday volatility more dangerous than a broader end-of-day or average-price contract.
  - Direct or indirect: direct for rules, indirect for risk implication.
  - Weight: high.

- **Current cushion is meaningful but not enormous for a high-beta crypto asset**
  - Source: netting of Binance price versus 80 threshold.
  - Why it matters: an approximately 6% move over several days is plausible in crypto, especially into a weekend or risk-off tape.
  - Direct or indirect: indirect/contextual.
  - Weight: medium-high.

- **Venue-specific print risk**
  - Source: contract chooses Binance specifically rather than a broader index.
  - Why it matters: exchange-specific microstructure, outages, or isolated dislocations can matter at the exact resolution minute.
  - Direct or indirect: contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- Polymarket market price itself is mixed evidence: it aggregates trader information, but at 89.5% it may also embed more confidence than the evidence set justifies for a single-minute crypto close.

## Conflict between inputs

There is no major factual conflict in the checked sources. The main disagreement is weighting-based: how much to penalize the market for timing/path fragility versus giving credit to the current several-dollar cushion above 80.

## Key assumptions

- The current buffer above 80 survives normal volatility into Apr 19 noon ET.
- Binance remains a clean and representative venue at settlement time.
- No sharp macro or crypto-specific selloff occurs before resolution.

## Key uncertainties

- Whether SOL can hold above 80 through the exact settlement minute.
- Whether weekend trading adds outsized downside volatility.
- Whether Binance-specific conditions diverge from broader market behavior at noon ET.

## Disconfirming signals to watch

- SOLUSDT falling toward 82 or lower before Apr 19.
- Repeated intraday prints near or below 80.
- Binance operational anomalies close to the resolution window.

## What would increase confidence

- Additional Binance checks showing SOL holding a wider buffer above 80 closer to settlement.
- Broad crypto tape remaining stable or supportive into Apr 19.

## Net update logic

The direct price evidence supports Yes, but the contract wording forces a downward confidence adjustment because settlement depends on one exact venue-specific minute close. That timing fragility is the main reason not to simply mirror the market’s high-80s probability.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why the risk-manager view is modestly below the market rather than outright bearish.