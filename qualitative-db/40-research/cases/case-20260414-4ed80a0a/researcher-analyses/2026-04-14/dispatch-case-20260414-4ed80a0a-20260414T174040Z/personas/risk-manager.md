---
type: agent_finding
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: c66d2b88-d6ed-44c7-ad54-6594d87a8cb8
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2-400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-14
agent: orchestrator
stance: yes-already-likely-achieved
certainty: high
importance: medium
novelty: medium
time_horizon: intrawindow
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-market-data-integrity"]
upstream_inputs: []
downstream_uses: []
tags: ["risk-manager", "eth", "polymarket", "binance", "threshold-market"]
---

# Claim

Ethereum has very likely already satisfied this contract’s $2,400 trigger, so the main remaining risk is not directional ETH price risk but source-of-truth / settlement-path risk. My view is effectively **Yes at 99%**.

## Market-implied baseline

Assignment metadata gave `current_price: 0.916`, implying **91.6%**. That is already a high-confidence market view. On an additional verification pass, the Polymarket event page data for this exact ladder showed the $2,400 line at **1.0 / 100% Yes** when checked later on 2026-04-14, so the market appears to have moved from very high confidence to practical certainty.

**Embedded confidence assessment:** even the initial 91.6% price looked highly confident for a contract that can hinge on one wick print and one named venue; after direct verification, that confidence now looks mostly justified.

## Own probability estimate

**99%**.

I am leaving a small residual 1% for operational edge cases: Binance data-surface inconsistency, timezone/window interpretation error, or an unusual settlement dispute.

## Agreement or disagreement with market

I **roughly agree, then converge upward** after verification.

- Versus the assignment baseline of 91.6%, I am modestly more bullish on `Yes`, mostly because the condition appears already realized.
- Versus the later page check at 100%, I am directionally aligned but keep a tiny haircut for settlement mechanics and source-path ambiguity.
- The difference is mostly about residual uncertainty, not directional disagreement.

## Implication for the question

For decision purposes, this looks less like an open forecast and more like a verification/settlement case. Once a qualifying Binance 1-minute high has already printed inside the Apr 13-19 ET window, future ETH path matters much less unless the observed print is somehow invalidated.

## Key sources used

**Primary / authoritative contract source**
- Polymarket event page and embedded market data for `What price will Ethereum hit April 13-19?` and the specific `$2,400` submarket.
- Source note: `qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-source-notes/2026-04-14-risk-manager-polymarket-rules-binance-threshold.md`
- Direct for contract interpretation / source-of-truth.

**Primary / direct verification source**
- Binance ETH/USDT 1-minute kline data and 24hr ticker data.
- Source note: `qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-source-notes/2026-04-14-risk-manager-binance-price-verification.md`
- Direct for whether the trigger condition occurred.

**Supporting audit artifacts**
- Assumption note: `qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/assumptions/risk-manager.md`
- Evidence map: `qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/evidence/risk-manager.md`

**Evidence-floor compliance**
- Met with **two meaningful sources**: (1) Polymarket rule text / market structure, (2) direct Binance minute-level market data.
- Additional verification pass performed because the market was already at an extreme probability and source-of-truth ambiguity was explicitly flagged.

## Supporting evidence

- Polymarket’s rule text says the market resolves `Yes` if **any Binance ETH/USDT 1-minute candle high** in the Apr 13 00:00 ET to Apr 19 23:59 ET window is `>= 2400`.
- Binance direct data check found a **1-minute high of 2415.5** during the qualifying window, with the max observed candle opening at **2026-04-14 10:32 ET**.
- The threshold was exceeded by **$15.5**, so this is not a borderline touch that depends on rounding.
- Binance 24hr ticker data independently showed `highPrice: 2415.5`, matching the kline-based conclusion.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **not** a bearish ETH thesis. It is the possibility of a **resolution-path problem**:
- Binance API output might differ from the exact chart/UI surface Polymarket expects.
- A timezone/window interpretation mistake could invalidate the check.
- A rare settlement dispute could emerge around a suspect wick or data anomaly.

This is the main thing that keeps me at 99% instead of 100%.

## Resolution or source-of-truth interpretation

This section is decisive for the case.

**Governing source of truth:** Binance ETH/USDT 1-minute candle **highs**, as specified on the Polymarket market page.

What counts:
- any Binance ETH/USDT 1-minute candle in the Apr 13-19 ET window
- final candle **High** `>= 2400`

What does **not** count:
- prices from other exchanges
- different trading pairs
- generic spot-price aggregators like CoinGecko
- closing price if the intraminute high already met the threshold

Because this is a narrow, date-specific threshold market, that source-of-truth mapping matters more than general ETH market commentary.

## Key assumptions

- Binance API data accurately reflects the operative Binance ETH/USDT 1-minute highs relevant to settlement.
- The ET-to-UTC window conversion used in verification is correct.
- No special exception or dispute invalidates the observed >2400 print.

## Why this is decision-relevant

This is a good example of where markets can look extremely confident for the right reason: the event may already have happened. The risk-manager takeaway is that once direct evidence exists on the named venue, macro narratives and general crypto sentiment should be downweighted sharply. The residual risk is mostly procedural.

## What would falsify this interpretation / change your mind

I would revise materially downward if any of the following appeared:
- Binance chart/UI evidence showing the relevant qualifying candle did **not** in fact print above 2400
- official Polymarket clarification that the observed print is ineligible or disputed
- proof that my checked time window was misaligned with the contract’s ET window

If instead I saw archived Binance chart evidence or an official Polymarket acknowledgement confirming the hit, I would move from 99% to effectively 100%.

## Source-quality assessment

- **Primary source used:** Polymarket’s own rule text for the market and Binance direct market data.
- **Most important secondary/contextual source:** none was needed for the core claim; contextual external price trackers were intentionally downweighted because they do not govern settlement.
- **Evidence independence:** medium-high. The two key sources are not fully independent because the contract names Binance, but they are independent in role: one defines the rule and the other tests whether the rule condition occurred.
- **Source-of-truth ambiguity:** low after verification, though not zero because I used Binance API data rather than an archived screenshot from the chart UI.

## Verification impact

- **Additional verification pass performed:** yes.
- **Material change from verification:** yes.
- **How it changed the view:** it moved the case from “high-probability forward threshold hit” to “threshold appears already achieved on the named venue,” which is a qualitatively stronger conclusion.

## Reusable lesson signals

- Possible durable lesson: for crypto threshold ladder markets, the right question is often “has the named exchange already printed the trigger?” rather than “is spot likely to get there?”
- Possible missing or underbuilt driver: `binance-market-data-integrity` / exchange-specific settlement-path risk for rule-sensitive crypto contracts.
- Possible source-quality lesson: direct venue data should outrank generic aggregators when the contract names one exchange and one candle definition.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- one-sentence reason: exchange-specific settlement-path risk seems reusable across similar crypto wick/threshold contracts, but this single case is probably not enough for canon promotion yet.

## Recommended follow-up

- Optional final confirmation: archive or inspect the Binance chart UI for the qualifying minute if a belt-and-suspenders settlement record is desired.
- Otherwise, treat the contract as functionally settled pending ordinary market resolution mechanics.