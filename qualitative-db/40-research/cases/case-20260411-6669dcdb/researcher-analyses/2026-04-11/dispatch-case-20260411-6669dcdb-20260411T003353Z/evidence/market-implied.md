---
type: evidence_map
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
research_run_id: c3087e03-beb2-4c56-963a-a1700409c4c3
analysis_date: 2026-04-11
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-11
question: "Will the price of Bitcoin be above $72,000 on April 11?"
driver: operational-risk
date_created: 2026-04-10
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "bitcoin", "polymarket", "binance"]
---

# Summary

The market price looks directionally justified because live Binance BTCUSDT already traded above 72k during the run, making Yes the natural base case. The main remaining work is contract mechanics rather than macro thesis.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 11, 2026 close above 72,000?

## Current lean

Lean Yes, with the market broadly efficient and possibly even slightly conservative if live Binance spot remains materially above 72k.

## Prior / starting view

Start from the assignment baseline of 71.25% Yes and test whether that underestimates how close the event is to a simple near-spot threshold check.

## Evidence supporting the claim

- Live Binance BTCUSDT spot around research time was roughly 72.86k to 72.87k.
  - Source: Binance API source note.
  - Why it matters causally: only a drop of roughly 1.2% is needed to flip the market to No by ET noon.
  - Direct or indirect: direct.
  - Weight: high.

- Polymarket rules explicitly use Binance BTC/USDT, not another exchange or pair.
  - Source: Polymarket rules note.
  - Why it matters causally: reduces cross-exchange basis risk and makes live Binance spot highly relevant.
  - Direct or indirect: direct.
  - Weight: high.

- ET-to-UTC mapping is straightforward under DST: ET noon on Apr. 11 corresponds to 16:00 UTC.
  - Source: Binance server time plus API docs.
  - Why it matters causally: supports that this is a clearly timed minute event, not a vague daily-close market.
  - Direct or indirect: direct/mechanical.
  - Weight: medium.

## Evidence against the claim

- The event is still unresolved and BTC can move more than 1% in a crypto session before noon ET.
  - Source: inference from 24h high-low range in Binance data.
  - Why it matters causally: threshold is only modestly below spot, so volatility can still break Yes.
  - Direct or indirect: contextual.
  - Weight: high.

- The assignment snapshot (71.25%) and live page (~90.8%) diverged sharply.
  - Source: assignment plus live market page fetch.
  - Why it matters causally: introduces stale-price risk in the baseline and reminds us that sentiment can move fast.
  - Direct or indirect: direct on pricing, indirect on resolution.
  - Weight: medium.

- Contract points to Binance UI rather than a clean official settlement API endpoint.
  - Source: Polymarket rules and Binance docs.
  - Why it matters causally: creates mild source-of-truth ambiguity and operational risk.
  - Direct or indirect: direct on settlement mechanics.
  - Weight: medium.

## Ambiguous or mixed evidence

- Binance API `timeZone` parameter confirms interval interpretation mechanics, but the market resolves using what is "currently available" on the Binance web interface. Those should usually align, but the contract leaves a small UI-versus-API ambiguity.

## Conflict between inputs

The only meaningful conflict is not factual about price but procedural about the current market price snapshot: assignment metadata shows 71.25%, while the live webpage appeared closer to 90.8%. This is timing-based rather than thesis-based.

## Key assumptions

- Relevant candle is the 12:00 ET minute by open-time labeling.
- Binance UI and API will align on the close value used for resolution.
- No large downside move occurs before ET noon.

## Key uncertainties

- Short-term BTC volatility between now and noon ET.
- Exact settlement practice if UI/API or timestamp labeling were disputed.

## Disconfirming signals to watch

- BTCUSDT trading back below 72k on Binance before the decision minute.
- Any evidence that Polymarket or Binance interprets the candle boundary differently from the API convention.
- An overnight macro or crypto-specific shock causing >1% downside.

## What would increase confidence

- A later pre-noon Binance price check still comfortably above 72k.
- Visual confirmation from Binance UI that the same minute labeling matches the API expectation.

## Net update logic

The strongest update versus the assignment baseline is that live Binance BTCUSDT is already above 72k by a visible margin and the contract is tightly tied to that same pair. That pulls the case toward a high-probability Yes. What stops the estimate from going to the high 90s is simple: BTC can still move more than the needed amount in a short window, and the contract has mild UI-versus-API settlement ambiguity.

## Suggested downstream use

Use this as orchestrator synthesis input and as an audit trail for why the market-implied persona did not fade a high Yes price simply because the event remains technically unresolved.