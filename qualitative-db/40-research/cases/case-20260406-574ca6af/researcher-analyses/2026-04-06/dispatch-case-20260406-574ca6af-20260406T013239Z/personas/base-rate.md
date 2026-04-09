---
type: agent_finding
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: aac3fefe-c0dd-4f02-a63d-013876480c2a
analysis_date: 2026-04-06
persona: base-rate
topic: case-20260406-574ca6af | base-rate
question: Will Ethereum reach $2,200 March 30-April 5?
date_created: 2026-04-06
agent: Orchestrator
stance: no
certainty: medium-high
importance: high
novelty: medium
time_horizon: resolved-window
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [ethereum, polymarket, binance, base-rate, resolution-source]
---

# Claim

My view is that this market should resolve **NO**. The governing source-of-truth is narrow and explicit: Binance ETH/USDT 1-minute candle highs during the March 30-April 5 ET window. A direct pull of that series shows a maximum high of **2167.85**, below the required **2200** threshold.

**Evidence-floor / compliance label:** Met medium-difficulty evidence floor with (1) direct rule-language verification from the market page and (2) direct authoritative source-of-truth verification from the referenced Binance ETH/USDT 1m kline data, plus (3) one contextual cross-check showing broader ETH/USD reference prices also stayed below 2200 in reviewed summaries.

## Market-implied baseline

Current market price is **0.74**, implying roughly **74% YES / 26% NO** before final settlement.

## Own probability estimate

**8% YES / 92% NO.**

The remaining nonzero YES probability is not about underlying price action; it is mostly residual operational uncertainty around my independent verification versus any late-discovered source discrepancy, historical data revision, or non-obvious settlement override.

## Agreement or disagreement with market

I **disagree** with the market. The outside-view prior for short-window threshold-touch markets is less important here than the direct rule check because this is close to a resolved fact question. Once the source-of-truth is explicit, the main job is verifying the exact qualifying print. The market at 74% YES looks too high relative to the direct evidence.

## Implication for the question

If the market is governed exactly as written, this should be interpreted as a likely **NO** resolution despite some traders apparently pricing meaningful residual YES odds late. The key implication is that generalized ETH price chatter or other-exchange touches should not move the answer unless they also appeared on Binance ETH/USDT 1-minute highs.

## Key sources used

- **Primary / authoritative settlement source:** Polymarket market page for the exact contract mechanics and governing resolution language: `https://polymarket.com/event/what-price-will-ethereum-hit-march-30-april-5`
- **Primary / direct verification source:** Binance ETH/USDT 1-minute kline history for the exact ET window specified in the rules, queried via Binance API.
- **Case source note:** `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-source-notes/2026-04-06-base-rate-binance-polymarket-rules.md`
- **Secondary / contextual source:** CoinGecko ETH/USD range data for the same broad window, used only as a contextual check rather than settlement authority.

Direct vs contextual distinction matters here:
- Direct: Polymarket rules + Binance ETHUSDT 1m highs.
- Contextual only: CoinGecko or third-party commentary.

## Supporting evidence

- Polymarket explicitly states the market resolves YES only if any **Binance ETH/USDT 1-minute candle** in the stated date window has a final **High >= 2200**.
- Polymarket explicitly states that **other exchanges, different trading pairs, or spot markets will not be considered**.
- A full-window verification pass over Binance ETH/USDT 1-minute klines returned **8,640 candles** and a maximum observed high of **2167.85**, at **2026-04-01 13:03 ET**.
- Since **2167.85 < 2200**, the direct source-of-truth check points to **NO**.
- Contextual cross-check: reviewed CoinGecko ETH/USD range data in the same broad window also did not show a contextual move to 2200, so there is no obvious cross-source sign that Binance somehow missed a qualifying print.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **not** a bullish ETH narrative; it is the possibility of a **source or interpretation mismatch**:
- the market was still pricing 74% YES, suggesting either traders believed a qualifying Binance print existed, or they distrusted visible rules/data alignment,
- crypto price surfaces can differ across interfaces, timestamp windows, and pair conventions,
- if Polymarket uses a chart surface or data normalization that differs from the API pull, the conclusion could change.

I did not find affirmative evidence of such an override, but it is the strongest reason not to assign 99%+ confidence.

## Resolution or source-of-truth interpretation

**Governing source of truth:** Binance **ETH/USDT** 1-minute candle **High** prices for the title window, not DEX prices, not index prices, not ETH/USD on another venue, and not generalized spot summaries.

Case-specific checks:
- **Verify CEX spot price vs DEX price:** Verified that the contract is governed by a **CEX** source (Binance ETH/USDT). DEX prices are irrelevant unless Polymarket states otherwise, and here it states otherwise explicitly.
- **Check for specific market maker attribution rules:** I found no rule language assigning resolution to a specific market maker, LP, or third-party verifier beyond Polymarket’s stated use of Binance data.
- **Confirm settlement source hierarchy (CEX vs DEX vs index):** The hierarchy appears explicit and narrow: Binance ETH/USDT 1m candle highs control; other exchanges, pairs, or spot references do not count.

## Key assumptions

- Polymarket will settle the contract exactly according to the displayed market page rules.
- Binance API kline history reflects the same underlying 1-minute high series that Polymarket intends to reference.

See assumption note: `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/assumptions/base-rate.md`

## Why this is decision-relevant

This is decision-relevant because the visible market price appears materially above what the direct source-of-truth evidence supports. If a synthesis or decision-maker is using market price as a proxy for truth, this case is a reminder that late-stage prediction-market pricing can still lag or misread narrow contract mechanics.

## What would falsify this interpretation / change your mind

I would change my mind if any of the following appeared:
- a verified Binance ETH/USDT 1-minute candle high of **2200+** within the exact ET window,
- an official Polymarket clarification showing a different controlling source or hierarchy,
- evidence that the chart surface Polymarket references differs materially from the Binance API series I checked.

## Source-quality assessment

- **Primary source used:** Polymarket market page rule language plus Binance ETH/USDT 1-minute kline data.
- **Most important secondary/contextual source used:** CoinGecko ETH/USD range data for broad contextual sanity check.
- **Evidence independence:** **Medium-low.** The decisive evidence is intentionally concentrated around the specified settlement source rather than multiple independent datasets.
- **Source-of-truth ambiguity:** **Low after verification.** It looked ambiguous from the assignment framing, but the market page text itself was explicit.

## Verification impact

- **Additional verification pass performed:** Yes.
- **Did it materially change the view?** Yes.
- The extra pass made the case much cleaner: once Binance ETH/USDT 1m highs were checked directly, the view moved from tentative rule-sensitivity to a strong NO lean.

## Reusable lesson signals

- Possible durable lesson: crypto threshold markets can look ambiguous from title alone but become straightforward once the exact exchange/pair/candle-field rule is read.
- Possible missing or underbuilt driver: none identified from this single case.
- Possible source-quality lesson: for crypto hit-price contracts, direct exchange-specific resolution checks should outrank all generalized price summaries.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **no**
- one-sentence reason: This is a useful recurring methodology lesson for rule-sensitive crypto markets, but not obviously a stable driver or canon-gap issue.

## Recommended follow-up

- If another researcher or controller has contrary evidence, ask them to cite the exact Binance ETH/USDT 1-minute candle and timestamp they believe crossed 2200.
- Otherwise, treat this as a likely **NO** and focus synthesis on whether any settlement-override evidence exists rather than on generic ETH price narratives.