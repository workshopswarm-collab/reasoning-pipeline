---
type: agent_finding
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: b29230d1-9199-41b0-bfbe-3521de8f43e7
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity:
topic: eth-above-2100-apr-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: market-implied
stance: yes-lean
certainty: medium-high
importance: medium
novelty: low
time_horizon: "<1d"
related_entities: []
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["ethereum", "binance", "polymarket", "contract-interpretation", "market-implied"]
---

# Claim

The market’s high-Yes pricing looks broadly efficient. With ETHUSDT currently trading around 2211-2213 on Binance and the contract resolving on a single Binance 1-minute close above 2100 at noon ET tomorrow, a Yes result is very likely, but not quite as close to certainty as an ultra-high 97%+ print would imply because one-minute settlement and overnight crypto volatility still leave real tail risk.

## Market-implied baseline

The assignment baseline implies **94% Yes**. A contemporaneous fetch of the Polymarket event page showed the 2100 line closer to **97.4% Yes**, which I treat as likely timing drift rather than a substantive contradiction. Either way, the market is pricing a very high probability of Yes.

## Own probability estimate

**92% Yes.**

## Agreement or disagreement with market

**Roughly agree, with a mild lean that the market is a little rich.** The strongest case for market efficiency is simple: ETHUSDT is already trading more than $100 above the strike on the governing exchange, nearby strike pricing is internally coherent, and the contract is mechanically simple relative to many Polymarket markets. I mark slightly below the market because the question is not “is ETH generally above 2100?” but “is the final close of one exact 1-minute Binance candle above 2100?”, which preserves some meaningful jump/timing risk.

## Implication for the question

This should be interpreted as a **high-probability Yes** market where most of the informational work is already done by current Binance spot level and the proximity of settlement. The remaining uncertainty is mostly minute-level timing risk, not a hidden macro thesis.

## Key sources used

- **Primary / authoritative settlement-source family:** Binance Spot API docs for klines and server time, plus live Binance API checks for `/api/v3/time`, `/api/v3/exchangeInfo?symbol=ETHUSDT`, and recent `/api/v3/klines?symbol=ETHUSDT&interval=1m`. Preserved in source note: `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-source-notes/2026-04-09-market-implied-binance-api-contract-and-timing.md`
- **Secondary / direct market surface:** Polymarket event page and rules text for the assigned market. Preserved in source note: `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-source-notes/2026-04-09-market-implied-polymarket-rules-and-price-surface.md`
- **Supporting audit artifacts:**
  - assumption note: `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/assumptions/market-implied.md`
  - evidence map: `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/evidence/market-implied.md`

**Compliance / evidence floor:** Met and exceeded the case evidence floor with one authoritative source family (Binance docs + live API) plus one contextual/direct market source (Polymarket rules and live price surface), and an explicit additional verification pass.

## Supporting evidence

- Live Binance 1-minute klines showed ETHUSDT trading around **2211-2213** on Apr 9 afternoon ET, leaving roughly a **$111+ cushion** above the 2100 threshold.
- The nearby-strike Polymarket ladder is coherent with that spot level: 2000 near certainty, 2100 very high, 2200 much closer to toss-up territory, 2300 low. That is exactly what an information-efficient market should look like if spot is in the low 2200s.
- The governing settlement source is a single exchange and a single 1-minute candle, reducing multi-source ambiguity.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **single-minute resolution risk**. Crypto can move violently, and the market only needs ETHUSDT to print a final close at or below 2100 on one exact 1-minute candle for No to win. This is the main reason not to round up toward near-certainty.

## Resolution or source-of-truth interpretation

**Governing source of truth:** Binance ETH/USDT 1-minute candle close, as referenced by the Polymarket rules.

Case-specific checks completed:

- **Verify UTC offset vs Binance server:** Noon ET on Apr 10, 2026 converts to **16:00 UTC** because New York is on daylight saving time. Binance server time is exposed in UTC-oriented millisecond timestamps, and Binance docs state `startTime` / `endTime` are interpreted in UTC.
- **Check candle close definition:** Binance docs state klines are uniquely identified by **open time** and return a separate close-time field. For a 1-minute bar, the close time ends at `...9999`. So the strongest interpretation is that the relevant candle is the one **opened at 12:00:00 ET / 16:00:00 UTC**, whose final close price determines resolution.

Residual ambiguity is low but nonzero because Polymarket references the Binance website chart rather than the REST API explicitly; if the UI labels candles differently, there could be edge-case confusion. I do not think that is the base case.

## Key assumptions

- The noon-ET contract refers to the candle opened at 12:00:00 ET rather than some alternate close-time labeling convention.
- ETHUSDT remains in roughly the current price regime through tomorrow noon.
- No exchange anomaly or settlement-surface mismatch appears at the target minute.

## Why this is decision-relevant

The useful takeaway is not just “ETH is above 2100 now.” It is that the market appears to be pricing this contract in a mostly efficient way already, so any anti-market thesis would need stronger evidence than “crypto is volatile.” The residual edge, if any, lies in minute-level contract mechanics or an overnight selloff, not in broad misunderstanding of the threshold.

## What would falsify this interpretation / change your mind

- ETHUSDT falling materially closer to the threshold before the target window, especially into the 2110-2140 range.
- A Polymarket clarification or precedent showing a different candle-label interpretation than the open-time reading.
- Evidence that the Binance web chart used operationally for settlement could diverge from the standard kline mechanics I verified.

## Source-quality assessment

- **Primary source used:** Binance Spot API docs and live Binance API responses.
- **Most important secondary/contextual source used:** Polymarket event page showing the live strike ladder and formal market wording.
- **Evidence independence:** **Medium-low.** The settlement mechanics evidence is concentrated in one authoritative source family, which is appropriate here but not highly independent.
- **Source-of-truth ambiguity:** **Low-medium.** The governing source is explicit, but the exact UI-vs-API candle-label interpretation is a small residual ambiguity worth naming.

## Verification impact

- **Additional verification pass performed:** Yes.
- **What I verified:** Binance server-time behavior, live ETHUSDT 1-minute kline structure, future timestamp mapping for the target noon-ET bar, and the kline open-time/close-time definition in Binance docs.
- **Did it materially change the view?** No material directional change. It increased confidence in the contract-timing interpretation and reduced the chance of an off-by-timezone mistake.

## Reusable lesson signals

- **Possible durable lesson:** For single-exchange, single-candle crypto contracts, most of the real research value is in precise timing/settlement interpretation rather than macro narrative.
- **Possible missing or underbuilt driver:** None strongly identified; current canonical drivers were adequate.
- **Possible source-quality lesson:** When Polymarket references an exchange UI, it is still worth checking the exchange API docs to audit candle identity, timezone handling, and precision.
- **Confidence that any lesson here is reusable:** Medium.

## Orchestrator review suggestions

- **Review later for durable lesson:** no
- **Review later for driver candidate:** no
- **Review later for canon or linkage issue:** yes
- **One-sentence reason:** `binance-global` appears causally central to many crypto settlement questions, but the provided canonical entity path was `binance-us`, which is not a clean fit for this global Binance settlement surface.

## Recommended follow-up

No immediate follow-up suggested for this persona beyond a last-hour spot check if the synthesis process wants to tighten the final estimate near resolution.