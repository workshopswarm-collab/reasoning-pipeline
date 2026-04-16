---
type: evidence_map
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
research_run_id: 0c2cbef2-5728-4527-9793-376dd5cb38dd
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET one-minute candle close on 2026-04-19 be above 80?"
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-540d9abf/researcher-analyses/2026-04-15/dispatch-case-20260415-540d9abf-20260415T234706Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "catalyst-hunter", "crypto"]
---

# Summary

The case currently leans Yes because the direct settlement source already shows SOL/USDT comfortably above the strike, but the key risk is that the contract resolves on a single exact minute and therefore remains vulnerable to a fast drawdown before noon ET on April 19.

## Question being evaluated

Will the Binance SOL/USDT one-minute candle at 12:00 ET on April 19, 2026 close above $80?

## Current lean

Lean Yes, high but not near-certainty.

## Prior / starting view

Starting view was that a 90% market price might be too confident unless current Binance pricing was materially above the strike and the rules were clean.

## Evidence supporting the claim

- Binance direct price check during this run showed SOLUSDT around 84.99.
  - Direct evidence.
  - High weight because Binance is the named settlement source.
- Recent Binance daily closes were mostly above 80 and recent highs reached the mid-to-high 80s.
  - Direct evidence.
  - Medium-high weight because it shows the current regime is above the threshold, not a one-tick anomaly.
- Recent 1h and 4h Binance candles on April 15 mostly traded between roughly 83 and 85.8.
  - Direct evidence.
  - Medium weight because it shows near-term buffer and intraday stability.
- Contract mechanics are straightforward: only Binance SOL/USDT 1m close at 12:00 ET matters.
  - Direct rule evidence.
  - High weight because it limits interpretive ambiguity.

## Evidence against the claim

- The resolution depends on a single exact one-minute close, not average price, so path dependence is high.
  - Direct rule implication.
  - High weight.
- SOL is only about five dollars above the threshold, which is meaningful but still reachable in a volatile weekend crypto selloff.
  - Direct plus contextual.
  - Medium-high weight.
- No strong independent scheduled positive catalyst was identified that would add much new upside informationally before resolution.
  - Contextual evidence.
  - Medium weight because the best Yes argument is mostly current level persistence, not an upcoming bullish event.

## Ambiguous or mixed evidence

- General crypto market tone could help or hurt, but without a specific scheduled macro event identified here it mostly functions as background volatility rather than a clean catalyst.
- Solana-specific news flow could emerge unexpectedly; absence of an identified catalyst is not proof of calm.

## Conflict between inputs

No major factual conflict was found. The main tension is weighting-based: whether current buffer above $80 deserves a probability in the low 90s or something a bit lower because of single-minute contract fragility.

## Key assumptions

- No sharp risk-off move or Solana-specific negative shock before the resolution minute.
- Binance market structure remains normal enough that the observed price path is representative at settlement.

## Key uncertainties

- Weekend crypto volatility into the exact timestamp.
- Possible unscheduled Solana reliability or exchange-specific disruption.

## Disconfirming signals to watch

- SOL losing the low-80s area before April 19.
- Broad BTC/ETH weakness dragging altcoins lower.
- Solana outage, exploit, or significant negative operational headline.

## What would increase confidence

- Continued Binance SOL/USDT trading above 83-84 into April 18-19.
- Lack of exchange or network reliability issues.
- Additional confirmation closer to expiry that the noon ET timing maps cleanly to the relevant Binance candle.

## Net update logic

The key update was that direct Binance pricing and recent klines show SOL already above the strike by a usable margin, making the default path Yes. I downweighted unsupported narrative catalysts because no identified event looked more informative than the simple current-level buffer. I also refused to push to near-certainty because the single-minute settlement design makes a fast late drawdown the central disconfirming mechanism.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with a note that this is primarily a contract-mechanics-plus-current-level case rather than a rich multi-catalyst calendar case.