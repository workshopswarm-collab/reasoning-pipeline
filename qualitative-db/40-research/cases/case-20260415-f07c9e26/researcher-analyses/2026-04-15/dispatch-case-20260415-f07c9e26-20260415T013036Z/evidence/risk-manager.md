---
type: evidence_map
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
research_run_id: ac1c7e60-d279-413d-b028-3d7d6bfb216a
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
driver: operational-risk
date_created: 2026-04-15
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-f07c9e26/researcher-analyses/2026-04-15/dispatch-case-20260415-f07c9e26-20260415T013036Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "risk-manager"]
---

# Summary

The evidence nets to a strong Yes lean, but the market's 90%+ confidence looks slightly too high because this contract is determined by one exchange-specific one-minute close and BTC still only has a modest cushion over the threshold.

## Question being evaluated

Will Binance BTC/USDT's 12:00 ET one-minute candle on April 16, 2026 close above 72,000?

## Current lean

Yes, with high but not near-certain probability.

## Prior / starting view

Starting view was that the market was probably right directionally because BTC was already above 72k, but the narrow timestamp mechanics likely made 90%+ confidence somewhat fragile.

## Evidence supporting the claim

- **Direct Binance last price around 74.7k**  
  - Source: `researcher-source-notes/2026-04-15-risk-manager-binance-direct-data.md`  
  - Why it matters: gives a current cushion of roughly 2.67k above the threshold.  
  - Direct or indirect: direct.  
  - Weight: high.

- **Recent Binance 24h low still above 72k**  
  - Source: same source note.  
  - Why it matters: recent realized range has not yet breached the threshold.  
  - Direct or indirect: direct.  
  - Weight: medium-high.

- **Recent daily closes mostly above 72k**  
  - Source: same source note.  
  - Why it matters: supports that the threshold is not far above the current trading regime.  
  - Direct or indirect: direct/contextual hybrid.  
  - Weight: medium.

## Evidence against the claim

- **Single-minute-close path risk**  
  - Source: `researcher-source-notes/2026-04-15-risk-manager-polymarket-contract.md`  
  - Why it matters: the contract can fail on one sharp move at the exact settlement minute even if BTC trades above 72k for most of the period.  
  - Direct or indirect: direct contract evidence.  
  - Weight: high.

- **Cushion is only about 3.6%**  
  - Source: combination of Binance last price and threshold.  
  - Why it matters: BTC can move that much on a normal volatile session; this is not an absurd downside tail.  
  - Direct or indirect: direct.  
  - Weight: medium-high.

- **Exchange-specific settlement mechanics**  
  - Source: contract note and Binance note.  
  - Why it matters: other exchanges or broader crypto strength do not save a Yes outcome if Binance BTC/USDT alone closes below the line.  
  - Direct or indirect: direct contract evidence.  
  - Weight: medium.

## Ambiguous or mixed evidence

- The current market price itself is informative and suggests broad trader confidence, but it may also embed underpriced overconfidence because it compresses timing and operational nuance into a single number.

## Conflict between inputs

No major factual conflict between inputs. The main issue is weighting: current spot level strongly supports Yes, while the contract's one-minute resolution structure argues against treating the outcome as nearly locked.

## Key assumptions

- BTC does not suffer a >3.6% downside move into the exact settlement minute.
- Binance spot data remains operational and representative at the relevant time.
- No contract-interpretation edge case overrides the straightforward reading of the rule text.

## Key uncertainties

- Overnight macro / crypto risk between now and noon ET April 16.
- Whether a brief selloff could coincide specifically with the settlement minute.
- Residual UI/API settlement implementation ambiguity.

## Disconfirming signals to watch

- BTC breaks below 73k before the morning ET session.
- Realized volatility accelerates with broad crypto weakness.
- Binance operational issues emerge near the resolution window.

## What would increase confidence

- BTC remaining comfortably above 74k into the late-morning ET window on April 16.
- Another direct verification of Binance 1m candle behavior close to the resolution time.

## Net update logic

Direct exchange data supports a high-probability Yes outcome, but the risk adjustment comes from recognizing that this is not a daily-close or average-price market. The exact one-minute-close mechanic and modest percentage cushion are the main reasons to shade below the market rather than simply echo it.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review