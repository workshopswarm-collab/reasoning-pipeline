---
type: agent_finding
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: 26c93914-c5c6-45b7-bbb4-2001b4d5f8b5
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: ethereum-above-2100-on-april-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: operational-risk
date_created: 2026-04-09
agent: risk-manager
stance: lean-yes-below-market-confidence
certainty: medium
importance: medium
novelty: low
time_horizon: "through 2026-04-10 12:00 ET resolution minute"
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["crypto", "ethereum", "polymarket", "binance", "risk-manager", "resolution-mechanics"]
---

# Claim

My directional view is **Yes**, but with less confidence than the market: ETH is currently comfortably above $2,100 and the simplest read is that it stays above that threshold into the relevant minute, yet the contract is fragile because it resolves on a **single Binance 1-minute candle close at noon ET**, not on a broad daily close or exchange-average price.

Compliance note: this run met the evidence floor with **one authoritative/direct source-of-truth family (Binance API + Binance-linked resolution mechanics)** plus **one contextual verification source (Polymarket market page/rules)**, and included an explicit additional verification pass on UTC offset vs Binance server time and on 1-minute candle close definition.

## Market-implied baseline

The assignment `current_price` is **0.94**, implying a **94% Yes** baseline. The contemporaneous Polymarket event page also displayed the 2,100 contract around **97.4 cents Yes**, so the market is embedding very high confidence rather than merely a modest directional lean.

## Own probability estimate

**88% Yes.**

## Agreement or disagreement with market

I **roughly agree on direction** but **disagree on confidence**. The market is probably right that ETH is more likely than not to settle above $2,100, especially because direct Binance spot checks during this run showed ETHUSDT trading around **2211-2213**, leaving roughly a $110 buffer above the threshold. But a 94-97% market price looks somewhat too compressed for a contract that resolves on a **single one-minute close on one venue**. My discount versus market is mostly an **uncertainty discount**, not a bearish directional call.

## Implication for the question

The case still leans Yes, but a risk-aware synthesis should not treat this as near-locked. The underpriced risk is not some broad ETH thesis reversal; it is that **narrow timing mechanics** and **minute-level volatility** can matter more than the market is admitting.

## Key sources used

- **Primary / authoritative settlement family:** Binance public API
  - `GET /api/v3/time`
  - `GET /api/v3/exchangeInfo?symbol=ETHUSDT`
  - `GET /api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5`
  - captured in source note: `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-source-notes/2026-04-09-risk-manager-binance-resolution-check.md`
- **Contextual / rules source:** Polymarket event page and market rules for `ethereum-above-on-april-10`

Governing source of truth: **Binance ETH/USDT 1-minute candle close**, as specified by the market rules. Polymarket is useful for contract wording and current market-implied probability, but Binance is the operative settlement surface.

## Supporting evidence

- Direct Binance kline samples during this run showed ETH trading around **2211-2213**, materially above $2,100.
- The Polymarket strike ladder was internally coherent: $2,000 was near certain, $2,100 was very high probability, $2,200 was around 60%, and $2,300 was low. That pattern is consistent with spot ETH currently sitting above $2,100 but not with an enormous cushion above higher strikes.
- The case is mechanically simple in one sense: if the correct candle is identified, settlement reduces to a clean numerical comparison of the candle’s **final close** versus **2100**.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that this market is **not** asking whether ETH is generally above $2,100 tomorrow; it asks whether the **single Binance 1-minute candle for noon ET** closes above that level. That creates path risk and timing fragility. If ETH drifts back near the threshold by late morning tomorrow, one brief downswing ending with a close below $2,100 could still resolve No even if the broader daily market remains constructive.

## Resolution or source-of-truth interpretation

This is the key risk-management section.

- Polymarket rules say the market resolves to Yes if the Binance **ETH/USDT 1 minute candle for 12:00 in the ET timezone (noon)** has a final close above $2,100.
- Additional verification was performed on Binance surfaces:
  - Binance `exchangeInfo` explicitly reports `timezone: UTC`.
  - Binance `serverTime` mapped cleanly to ET with the expected **UTC-4** offset for April 2026 daylight time.
  - Binance kline arrays show a 1-minute candle structure with **open time**, **OHLC**, and **close time**, where close time is open time + 59.999 seconds.
- My operational interpretation is that **12:00 ET on April 10 corresponds to 16:00:00 UTC**, and the relevant candle is the candle that **opens at 16:00:00 UTC** and receives its final close price at the end of that minute.
- Case-specific checklist items addressed explicitly:
  - **verify UTC offset vs Binance server:** done; Binance API uses UTC timestamps and ET noon maps to 16:00 UTC on April 10.
  - **check candle close definition:** done; Binance kline structure makes clear that a 1-minute candle has a distinct final close field set at minute end.

Residual ambiguity remains because the rule points users to the Binance **UI** with `1m` candles selected, while my verification used Binance’s public API rather than a captured UI screenshot. I think API/UI mismatch risk is low, but it is the main residual contract-mechanics fragility.

## Key assumptions

- The Binance UI candle labeling convention aligns with the public API interpretation of the relevant minute.
- ETH does not experience a sharp enough move before noon ET on April 10 to erase the current cushion and produce a final 1-minute close below $2,100.
- No exchange-specific anomaly, chart glitch, or clarification changes which candle counts.

## Why this is decision-relevant

At a 94% implied probability, the market is signaling near-certainty. The risk-manager contribution is that this certainty deserves trimming because **single-minute, single-venue contracts are more fragile than they look**. Even when the directional call is probably right, overconfidence can still be expensive.

## What would falsify this interpretation / change your mind

What would most quickly invalidate the current working view:

- ETH trading back toward **2120 or below** ahead of the resolution window, making a sub-2100 one-minute close materially plausible.
- Direct evidence from Binance UI documentation or a live screenshot showing that the operative candle mapping differs from the API-based 16:00 UTC interpretation.
- A volatility spike or venue-specific dislocation on Binance that makes the noon minute unusually noisy.

If fresh checks near resolution still show ETH comfortably above $2,100 and the minute mapping remains clean, I would move closer to the market. If ETH compresses toward the strike or timing ambiguity widens, I would move further away.

## Source-quality assessment

- **Primary source used:** Binance public API surfaces for exchange time, timezone, and 1-minute klines.
- **Most important secondary/contextual source used:** Polymarket event page/rules for contract wording and market-implied probability.
- **Evidence independence:** **low to medium**. Market pricing is independent in one sense, but the actual settlement mechanics are heavily single-source because Binance governs the operative price surface.
- **Source-of-truth ambiguity:** **low to medium**. The numeric source is clear, but there is still mild operational ambiguity around exact UI/API candle labeling conventions in a close call.

## Verification impact

Yes, an explicit additional verification pass was performed because the market price was extreme (>85%) and the checklist required case-specific timing checks.

It **did not materially change the directional view**, but it **did matter for confidence framing**:
- it confirmed Binance uses UTC timestamps,
- it confirmed how 1-minute candles expose final close values,
- it reduced but did not fully eliminate concern about minute-selection ambiguity.

## Reusable lesson signals

- Possible durable lesson: **intraday crypto strike markets can look simpler than they are; the main risk can be timing mechanics rather than asset fundamentals.**
- Possible missing or underbuilt driver: none clearly required from this run; existing `operational-risk` and `reliability` drivers are adequate.
- Possible source-quality lesson: when Polymarket references a venue UI, it is still worth verifying the venue API timestamp and candle schema before accepting apparent simplicity.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: the case suggests a reusable lesson around minute-bar settlement fragility, and there may be a linkage gap because the operative exchange is effectively Binance global while the available canonical entity note in-path is `binance-us`.

## Recommended follow-up

- Recheck Binance ETH/USDT closer to the actual resolution minute if the broader system supports reruns.
- If this class of market recurs often, consider a small standard operating note for **venue-timezone mapping + candle-label verification** before high-confidence conclusions are accepted.