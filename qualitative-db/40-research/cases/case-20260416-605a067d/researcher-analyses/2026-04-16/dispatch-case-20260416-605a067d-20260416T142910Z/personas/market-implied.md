---
type: agent_finding
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: 68f599bc-70db-4afc-921d-575b6a9e57c6
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: "ETH above 2200 on April 17 noon ET close"
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle on April 17 have a final close above 2200?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
stance: yes-lean
certainty: medium
importance: high
novelty: low
time_horizon: 24h
related_entities: ["binance", "polymarket", "ethereum"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-market-implied-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-market-implied-binance-klines-and-docs.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/assumptions/market-implied.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/evidence/market-implied.md"]
downstream_uses: []
tags: ["market-implied", "ethereum", "polymarket", "binance", "close-market"]
---

# Claim

The market’s Yes case is broadly sensible because ETH is already trading comfortably above 2200 on Binance, but the current quote still looks a bit rich for a contract that settles on one exact future one-minute close rather than a touch. I land at **0.83 Yes** versus the market-implied **0.871 Yes**.

**Evidence-floor compliance:** met with two meaningful sources plus an extra verification pass: (1) Polymarket rule text / market state and (2) Binance primary documentation plus live Binance ETHUSDT pricing checks.

## Market-implied baseline

The assignment’s current price of **0.871** implies **87.1% Yes**.

A live Polymarket page check was directionally consistent and showed the 2200 line around **91%-91.5% Yes** at capture time, which suggests the market was still pricing this as comfortably in-the-money.

## Own probability estimate

**83% Yes.**

## Agreement or disagreement with market

**Roughly agree on direction, mildly disagree on confidence.**

I agree with the market that Yes should be favored because live Binance ETH/USDT was about **2298** around 10:30 ET on April 16, roughly **4.5% above** the 2200 threshold, and even the sampled 24h low near **2285.1** remained above the line.

I disagree modestly with the market’s upper-80s confidence because this is a **close-above** market on **one exact future minute**: the Binance ETH/USDT **12:00 ET 1-minute candle on April 17 must have a final Close above 2200**. That is a narrower and less forgiving mechanism than a touch/high contract. The market may be slightly underweighting exact-minute path risk.

## Implication for the question

The current price looks mostly efficient rather than badly wrong. The market appears to be correctly pricing that 2200 is already below current spot by a meaningful cushion. My adjustment is not bearish in thesis terms; it is a mechanism discount for the exact settlement minute.

## Key sources used

**Primary / direct contract source**
- Polymarket event page and rules for the April 17 ETH threshold ladder, including the explicit settlement rule and displayed pricing: `researcher-source-notes/2026-04-16-market-implied-polymarket-rules-and-market-state.md`

**Primary / direct contextual source**
- Binance Spot API kline documentation plus live ETHUSDT API checks showing current one-minute closes, recent 60-minute range, and 24h ticker stats: `researcher-source-notes/2026-04-16-market-implied-binance-klines-and-docs.md`

**Supporting provenance artifacts**
- Assumption note: `researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/assumptions/market-implied.md`
- Evidence map: `researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/evidence/market-implied.md`

**Governing source of truth explicitly identified**
- The governing source of truth is **Binance ETH/USDT 1-minute candle data for the 12:00 ET minute on April 17**, as displayed on Binance’s ETH/USDT trading surface with 1m candles selected. The operative field is the candle’s **final Close**.

## Supporting evidence

- Live Binance ETH/USDT was around **2298.33** during this run, leaving about a **98-point cushion** above 2200.
- A recent 60-minute sample still had a **minimum low near 2285.1**, above the threshold.
- Polymarket cross-strike pricing was internally coherent: 2100 near certain, 2200 high confidence, 2300 much closer to balanced, 2400 low. That distribution shape fits a spot level around the high 2200s / low 2300s.
- The market’s high Yes price therefore has a strong efficient-markets explanation: traders do not need fresh bullish news if the asset is already materially above the strike and only needs to avoid a sharp one-day drawdown.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that **current spot above 2200 does not settle the contract**. ETH had also drifted down from about **2345** to about **2298** over the sampled recent hour, showing that downside path risk is real. In crypto, a roughly **4%+** cushion can disappear over 24 hours without requiring a bizarre catalyst.

## Resolution or source-of-truth interpretation

This section matters a lot because the contract is date-sensitive and mechanism-specific.

**Material conditions that must all hold for Yes**
1. The relevant instrument is **Binance ETH/USDT**, not another venue or pair.
2. The relevant bar is the **12:00 ET** one-minute candle on **April 17, 2026**.
3. The contract uses the candle’s **final Close**, not the high, low, average, current spot, or any earlier minute.
4. That final Close must be **higher than 2200**.

**Date / timezone verification**
- The market closes and resolves at **2026-04-17 12:00 PM America/New_York** per assignment context.
- Binance API documentation confirms 1-minute kline mechanics and supports timezone-aware interval interpretation, though Polymarket specifically cites the Binance trading surface.

**Reviewed mechanism-specific check**
- I directly verified the primary resolution source named by the contract: Binance ETH/USDT 1m candles.
- I captured governing-source proof of the rule and the practical candle semantics, but the event itself is **not yet verified** because the relevant April 17 noon ET candle has **not yet occurred**. This is an explicit “not yet occurred,” not merely “occurred but not yet verified.”

**Canonical mapping check**
- Clean canonical slug confirmed: `ethereum`.
- Clean driver slug confirmed: `reliability`.
- Structurally important but not cleanly confirmed from provided canonical files for frontmatter use here: `binance`, `polymarket` -> recorded under `proposed_entities` instead of forced canonical linkage.
- No important missing driver slug discovered in this run.

## Key assumptions

- ETH avoids a sharp selloff into April 17 noon ET.
- Binance UI candle display and practical API candle output remain aligned enough that the live API check is a valid extra-verification proxy.
- No late macro or crypto-specific shock changes the regime before settlement.

## Why this is decision-relevant

This is a useful market-respecting case: the market does not look stupid or stale. It looks mostly efficient, with only a moderate overconfidence risk from contract mechanics. That means a contrarian No stance would need stronger evidence than “crypto is volatile.”

## What would falsify this interpretation / change your mind

- Fresh Binance checks on April 17 morning showing ETH back near or below **2240**, especially with negative momentum into noon ET.
- Evidence that the Binance settlement surface being used by traders differs materially from API-observed candles.
- A crypto-wide risk-off shock large enough to make a sub-2200 noon close plausible.

## Source-quality assessment

- **Primary source used:** Polymarket contract rules plus Binance primary market-data documentation and live Binance ETHUSDT data.
- **Key secondary/contextual source used:** the live Polymarket cross-strike ladder itself as an information-rich market context surface.
- **Evidence independence:** **medium**. The sources are distinct in function (contract surface vs exchange data) but both center on the same underlying market state.
- **Source-of-truth ambiguity:** **low-to-medium**. The contract clearly names Binance ETH/USDT 1m candles and the final Close, but it references the Binance trading UI specifically, so API checks are strong verification rather than absolute settlement finality.

## Verification impact

Yes, an **additional verification pass** was performed because the market probability was extreme (>85%) and the case is date-sensitive.

That extra pass **did not materially change** the directional view. It strengthened confidence that the market’s bullish stance is grounded in real current cushion above 2200, while also preserving my modest discount for exact-minute close risk.

## Reusable lesson signals

- Possible durable lesson: short-dated crypto **close-above** markets deserve a smaller confidence boost than touch-style markets when the asset is above the line but settlement depends on one exact minute.
- Possible missing or underbuilt driver: none from this single run.
- Possible source-quality lesson: when Polymarket cites a UI-specific exchange surface, API checks are excellent verification but should still be labeled as proxy verification unless the exact settlement UI snapshot is captured.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: Binance and Polymarket were structurally important here but were left in `proposed_entities` because I did not confirm clean canonical slugs from the provided entity files.

## Recommended follow-up

If this case is rerun closer to settlement, do one short April 17 morning Binance recheck and then a near-noon governing-surface capture. The main thing that can still move the estimate is whether downside momentum emerges into the exact settlement minute.