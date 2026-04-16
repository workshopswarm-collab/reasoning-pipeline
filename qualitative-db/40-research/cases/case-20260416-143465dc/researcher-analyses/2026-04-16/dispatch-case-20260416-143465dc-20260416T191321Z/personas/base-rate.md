---
type: agent_finding
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
research_run_id: 6d25cb26-798a-4d9e-8725-d5c2a662051b
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: prediction-markets
entity: sol
topic: will-solana-reach-90-april-13-19
question: "Will Solana reach $90 April 13-19?"
date_created: 2026-04-16
agent: Orchestrator
stance: modestly_bearish_vs_market
certainty: medium
importance: high
novelty: medium
time_horizon: "2026-04-13 to 2026-04-19 ET"
related_entities: ["sol", "solana"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["crypto-short-horizon-momentum-threshold-touch"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-base-rate-binance-resolution-source.md", "qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-base-rate-binance-price-check.md", "qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/assumptions/base-rate.md", "qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/evidence/base-rate.md"]
downstream_uses: []
tags: ["base-rate", "sol", "polymarket", "binance", "touch-market"]
driver:
---

# Claim

Base-rate view: **Yes is slightly more likely than No, but not by as much as the market implies.** My estimate is **68%** that Binance SOL/USDT prints at least one 1-minute candle High of **$90.00+** before April 19 11:59 PM ET.

This is a touch market, so the governing mechanism is short-horizon volatility and wick risk, not a durable repricing above 90. The outside-view reason to lean Yes is simple: SOL is already trading within roughly 1-2% of the barrier with several days left. The outside-view reason not to fully follow the market is equally simple: the event has **not** happened yet on the governing source, and the last two weeks have repeatedly stopped short of 90.

## Market-implied baseline

Current market price is **0.74**, implying about **74%** for Yes.

## Own probability estimate

**68% Yes / 32% No.**

## Agreement or disagreement with market

I **roughly disagree** with the market: same direction, lower confidence. The market is pricing a near-threshold touch as fairly likely, which is sensible, but 74% looks a bit rich for a contract that still depends on a brief future spike that has not yet occurred.

Base-rate framing:
- bullish adjustment from prior: the asset is already close enough that one ordinary crypto intraday extension could settle the market
- bearish adjustment versus market: round-number thresholds often look inevitable when price is nearby, but many near-touch setups fail, and the direct governing data still says no touch so far

## Implication for the question

Interpret this as a **live but not near-certain** Yes path. The contract is meaningfully more likely to resolve Yes than a generic "close above 90" framing would suggest, because a brief wick is enough. But it should not be treated as effectively done until Binance prints the qualifying 1-minute High.

## Key sources used

Primary / direct / governing source:
- `qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-base-rate-binance-resolution-source.md` — Polymarket rules page stating the exact source of truth: Binance SOL/USDT 1-minute candle Highs.

Primary / direct empirical verification:
- `qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-base-rate-binance-price-check.md` — direct Binance kline and ticker checks showing no qualifying touch yet, with current observed maximum at 89.15 during the live window so far.

Supporting audit artifacts:
- `qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/assumptions/base-rate.md`
- `qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/evidence/base-rate.md`

## Supporting evidence

- **Direct contract mechanics favor Yes more than a close-based intuition would.** What counts is any Binance 1-minute High >= 90, so a short-lived wick is sufficient.
- **Direct Binance verification shows proximity.** The highest checked 1-minute High during the live window so far was **89.15** on Apr 16, and the live 24h ticker at research time showed SOL around **88.96**.
- **Recent regime still contains 90-touch precedent.** In the last 30 daily candles, Binance daily highs were >= 90 on **8 of 30** days. That is not dominant, but it does show 90 is not some remote outlier level.
- **Several days remain.** With Apr 17-19 still ahead at research time, a 1-2% upside extension is structurally plausible for a volatile crypto asset.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is also direct: **Binance has not printed the required 90 touch yet in the checked April 13-16 portion of the window**, despite multiple days of opportunity, and the **last 14 daily candles had zero highs >= 90**. That says the threshold is close, but not trivially easy in the current local regime.

## Resolution or source-of-truth interpretation

**Governing source of truth:** Binance SOL/USDT 1-minute candle **High** values, as specified on the Polymarket rules page.

What counts:
- any Binance SOL/USDT 1-minute candle during Apr 13 12:00 AM ET through Apr 19 11:59 PM ET with final High >= 90.00

What does **not** count:
- prices from other exchanges
- prices from other pairs
- generic "spot price" references
- daily closes or highs on non-governing venues
- being merely close to 90 without a qualifying Binance 1-minute High

Why the wording matters:
- this contract is easier to resolve Yes than a daily-close contract, because a brief spike is enough
- but it is also narrower than a generic crypto-price question, because only the specified Binance series counts

## Key assumptions

- Near-threshold crypto markets can still generate brief upside wicks even without a sustained breakout.
- Current SOL volatility remains high enough over the remaining days for a 1-2% extension to be realistic.
- My Binance API verification is a faithful operational check of the same underlying series referenced in the contract.

## Why this is decision-relevant

This is exactly the kind of market where narrative can outrun base rate. Once traders see 88-89 against a 90 barrier, "basically there" thinking can push probabilities too high. The base-rate correction is that many near-threshold touch markets remain unresolved because the final marginal move still has to happen on the exact governing series.

## What would falsify this interpretation / change your mind

I would move **up** materially if:
- a fresh verification pass shows a qualifying touch already occurred, or
- SOL keeps trading above roughly 89 with expanding highs and broader crypto strength

I would move **down** materially if:
- SOL reverses back toward the low 80s,
- repeated attempts fail below 89-90 with narrowing range, or
- a cleaner historical/structural check suggests my wick probability is too generous for this setup

## Source-quality assessment

- **Primary source used:** Polymarket rules page for exact resolution mechanics
- **Most important secondary/contextual source used:** direct Binance kline/ticker API checks for the governed series
- **Evidence independence:** **medium** — the two core sources are independent in function (contract rules vs exchange data) but both center on the same governed venue
- **Source-of-truth ambiguity:** **low after explicit interpretation** — the contract wording is narrow but clear once read carefully

## Verification impact

**Additional verification pass performed: yes.**

I did an explicit extra pass by checking direct Binance 1-minute klines over the relevant live-window portion and then cross-checking with Binance recent daily klines and 24h ticker data. It **did not materially change the directional view**, but it **did** keep me below the market because the strongest direct fact remained: no qualifying touch yet, max observed high 89.15.

## Reusable lesson signals

- possible durable lesson: touch markets near round numbers are easy to overprice when traders confuse "close" with "brief wick"
- possible missing or underbuilt driver: short-horizon crypto threshold-touch dynamics may deserve a dedicated driver note; recorded in `proposed_drivers` as `crypto-short-horizon-momentum-threshold-touch`
- possible source-quality lesson: for exclusion-heavy crypto touch markets, preserve governing-source proof and a direct exchange check in the artifact set
- confidence that any lesson here is reusable: **medium**

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- one-sentence reason: this case repeatedly highlights a reusable pattern where touch-market probability is driven by exact wick mechanics and venue-specific rules rather than broader price narratives.

## Recommended follow-up

- Re-run the direct Binance 1-minute check closer to Apr 19 if the contract is still unresolved.
- In synthesis, compare this base-rate lane against any catalyst-driven bullish lane; the key dispute should be about wick probability, not long-run SOL fundamentals.

## Compliance with case checklist / evidence floor

- market-implied probability stated: **yes (74%)**
- own probability stated: **yes (68%)**
- strongest disconfirming evidence named explicitly: **yes**
- what could change my mind stated: **yes**
- governing source of truth identified explicitly: **yes**
- canonical-mapping check performed: **yes**; used canonical entities `sol` and `solana`, and recorded unresolved structural driver as proposed instead of forcing a weak canonical driver fit
- source-quality assessment included: **yes**
- verification impact included: **yes**
- reusable lesson signals included: **yes**
- Orchestrator review suggestions included: **yes**
- evidence floor met: **yes — two meaningful sources used (1 primary governing rules source + 1 direct governing exchange data source), with additional verification pass preserved in supporting artifacts**
- provenance legibility: **yes — source notes, assumption note, and evidence map make the reasoning auditable**