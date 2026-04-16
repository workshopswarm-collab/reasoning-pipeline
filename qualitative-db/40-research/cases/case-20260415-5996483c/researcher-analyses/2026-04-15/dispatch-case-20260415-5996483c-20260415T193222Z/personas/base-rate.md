---
type: agent_finding
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
research_run_id: 7cdd1985-3b77-475d-8d68-f5d0894a3b41
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "Binance noon close above 70000 on 2026-04-20"
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
stance: yes-lean
certainty: medium
importance: high
novelty: low
time_horizon: 2026-04-20
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-5996483c/researcher-source-notes/2026-04-15-base-rate-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260415-5996483c/researcher-source-notes/2026-04-15-base-rate-binance-and-cross-venue-price-context.md", "qualitative-db/40-research/cases/case-20260415-5996483c/researcher-analyses/2026-04-15/dispatch-case-20260415-5996483c-20260415T193222Z/assumptions/base-rate.md"]
downstream_uses: []
tags: ["base-rate", "btc", "binance", "threshold", "noon-close", "evidence-floor-met"]
---

# Claim

Base-rate view: **Yes is more likely than not by a wide margin, but the market still looks somewhat too confident.** My estimate is **86%** that the Binance BTC/USDT 1-minute candle at **12:00 ET on Apr 20** closes above **70,000**.

Compliance note: evidence floor met with **two meaningful sources plus an extra verification pass**: (1) Polymarket contract rules / market state as primary mechanism source, (2) Binance spot + recent daily context with Coinbase and CoinGecko cross-checks as contextual price evidence, and (3) extra verification pass focused on governing-source wording, noon ET timing, and cross-venue/current-price consistency.

## Market-implied baseline

The assigned current price was **0.895**, implying **89.5%** Yes. The fetched Polymarket event page also showed the 70,000 line around **92-93% Yes**, so the market baseline is clearly in the high-80s / low-90s range.

## Own probability estimate

**86% Yes.**

## Agreement or disagreement with market

I **roughly agree directionally** with the market that Yes is the favorite, but I **disagree modestly on magnitude**. My outside-view estimate is a bit lower than the market because this is not a touch market or a generic end-of-day price market. It requires **one specific Binance 1-minute close at noon ET on Apr 20** to be above 70,000.

The bullish base rate is strong: BTC is already trading around **74.9k**, roughly **6-7% above** the threshold, and recent Binance daily closes have generally held above 70k after the breakout. In ordinary crypto price-regime terms, that setup usually favors an above-threshold close a few days later.

But the contract is narrow enough that some probability mass should still be reserved for a sub-70k move by the exact resolving minute. A high-80s estimate fits the outside view better than a low-90s one unless there is stronger case-specific evidence that the above-70k regime is unusually locked in.

## Implication for the question

The main implication is straightforward: **the threshold is currently comfortably in-the-money, so Yes should be favored**, but the decisive mechanism is **level persistence into one exact minute**, not whether BTC can merely remain strong overall. The contract can still resolve No if BTC dips below 70k at the relevant Binance noon close even after spending much of the next few days above that line.

## Key sources used

Primary / direct / authoritative for mechanism:
- `qualitative-db/40-research/cases/case-20260415-5996483c/researcher-source-notes/2026-04-15-base-rate-polymarket-rules-and-market-state.md`
  - Based on the Polymarket event page: https://polymarket.com/event/bitcoin-above-on-april-20
  - Governing source of truth identified there as **Binance BTC/USDT with 1m candles selected**.

Secondary / contextual:
- `qualitative-db/40-research/cases/case-20260415-5996483c/researcher-source-notes/2026-04-15-base-rate-binance-and-cross-venue-price-context.md`
  - Binance API current price and recent daily candles
  - Coinbase spot and CoinGecko spot used as cross-checks

Direct vs contextual distinction:
- **Direct for settlement mechanics:** Polymarket rule text naming Binance BTC/USDT 1-minute candle close at 12:00 ET.
- **Contextual for probability:** current Binance spot level, recent Binance daily closes, and cross-venue price agreement.

## Supporting evidence

- Binance spot was about **74,887**, giving BTC a substantial cushion above 70,000.
- Binance daily data showed BTC not just tagging 70k but posting several recent closes above it, which supports the idea of a regime shift rather than a one-candle anomaly.
- Cross-venue spot checks from Coinbase and CoinGecko were closely aligned with Binance, reducing concern that the observed level is just an exchange-specific artifact.
- For a liquid 24/7 asset already trading materially above the strike several days before resolution, the base rate usually favors staying above the threshold at a randomly selected later minute unless volatility regime shifts materially.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **contract narrowness plus crypto volatility**: this market is settled by **one exact Binance minute close at noon ET on Apr 20**, not by whether BTC trades above 70k most of the week. A 6-7% cushion is meaningful but not invulnerable in BTC over several days, especially if macro or crypto-specific risk sentiment reverses.

## Resolution or source-of-truth interpretation

**Primary governing source:** Binance BTC/USDT, specifically the **1-minute candle close** for **12:00 ET (noon) on Apr 20, 2026**.

Material conditions that must all hold for a Yes resolution:
1. The relevant venue must be **Binance**.
2. The relevant pair must be **BTC/USDT**.
3. The relevant timestamp is the **12:00 ET** one-minute candle on **Apr 20, 2026**.
4. The relevant field is the candle's final **Close** price.
5. That Close must be **higher than 70,000**.

What does **not** by itself count:
- BTC trading above 70k on Coinbase, CoinGecko, or another venue.
- BTC touching or exceeding 70k earlier in the day but not closing the relevant Binance minute above it.
- BTC closing above 70k on a daily candle or at a different intraday minute.

Date/timing check:
- I explicitly verified the contract wording uses **ET timezone** and **noon**, which matters because this is a narrow time-specific market.

Near-complete-event proof status:
- **Not yet occurred / not yet verifiable**, because the resolving Apr 20 noon ET minute has not happened yet.
- This is distinct from “may already have occurred but not yet verified”; that distinction does not apply here because the resolution timestamp is still in the future.

Canonical-mapping check:
- Clean canonical slugs available and used: `btc`, `reliability`, `operational-risk`.
- No additional causally important entity or driver required a proposed slug for this memo.

## Key assumptions

- BTC remains in a post-breakout regime where trading above 70k is persistent rather than a temporary overshoot.
- No major market shock or Binance-specific dislocation occurs before the resolving minute.
- Recent above-70k daily closes contain some signal for the Apr 20 noon minute despite the contract's narrower mechanism.

## Why this is decision-relevant

At high market probabilities, the main decision question is usually not direction but **whether the contract is too mechanically narrow for the quoted confidence**. This memo says the answer is: somewhat, but not dramatically. The setup still strongly favors Yes.

## What would falsify this interpretation / change your mind

What could still change my mind:
- BTC quickly falling back below 72k and then below 70k over the next few sessions.
- Evidence that the recent move above 70k was fragile or flow-driven in a way likely to mean-revert by Apr 20.
- Any sign of Binance-specific pricing dislocation or contract-surface ambiguity around the relevant minute.

If BTC is back near or below 70k on Apr 19-20, I would cut the estimate materially because this contract is resolved at one exact minute rather than over a broad window.

## Source-quality assessment

- **Primary source used:** Polymarket event page and contract wording naming Binance BTC/USDT 1-minute close at 12:00 ET.
- **Key secondary/contextual source used:** Binance current-price and recent daily-candle data, cross-checked with Coinbase and CoinGecko spot.
- **Evidence independence:** **medium**. Binance is primary for settlement, while Coinbase/CoinGecko provide partial independent confirmation of broad market level but are still all measuring the same asset state.
- **Source-of-truth ambiguity:** **low-to-medium**. The contract wording is fairly explicit, but markets of this type still require care because exact venue, pair, time, and field (close vs high) all matter.

## Verification impact

- **Additional verification pass performed:** yes.
- I performed an extra pass because the market is already at an extreme probability and the contract is date/time-specific.
- The pass focused on: exact rule wording, governing source identification, ET/noon timing, and cross-venue/current-price consistency.
- **Did it materially change the view?** No material directional change. It reinforced that Yes is favored, but it also confirmed the market is on a narrower mechanism than a casual glance might suggest.

## Reusable lesson signals

- Possible durable lesson: narrow time-specific **close** contracts should usually price below otherwise similar **touch** or broad-window contracts, even when the asset is well above the threshold at analysis time.
- Possible missing or underbuilt driver: none from this run.
- Possible source-quality lesson: explicit venue/pair/time/field checking remains important in crypto threshold markets because casual summaries often compress these distinctions.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **no**
- one-sentence reason: this looks like a straightforward application of existing resolution-discipline lessons rather than evidence of a new recurring canon gap.

## Recommended follow-up

If this case is revisited closer to resolution, the highest-value refresh is simple: check Binance BTC/USDT level and volatility on Apr 19-20 relative to the exact **Apr 20 12:00 ET** resolving minute, rather than expanding source breadth.