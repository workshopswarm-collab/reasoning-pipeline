---
type: agent_finding
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 4bdf6b0a-f878-4814-bdb6-1482c609fe49
analysis_date: 2026-04-06
persona: variant-view
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260406-574ca6af | variant-view
question: Will Ethereum reach $2,200 March 30-April 5?
date_created: 2026-04-06
agent: Orchestrator
stance: no
certainty: high
importance: medium
novelty: medium
time_horizon: case-window
related_entities: [ethereum, binance, polymarket, coingecko]
related_drivers: []
upstream_inputs: []
downstream_uses: [orchestrator synthesis, evaluation]
tags: [variant-view, ethereum, binance, threshold-market, settlement-rules]
---

# Claim

The strongest credible variant thesis here was that the market question might be materially narrower than generic “did ETH trade at $2,200 anywhere,” because settlement depends on a specific venue and candle definition. After checking that narrower path directly, the variant view still lands on **No**: Binance ETH/USDT 1-minute highs during the window appear to have topped out around **2167.85**, comfortably below $2,200.

**Compliance label:** Evidence floor met with (1) direct source-of-truth contract text from the market page, (2) direct Binance venue data verification for the designated pair/interval, and (3) one contextual secondary cross-check (CoinGecko). Case-specific checks addressed explicitly below.

## Market-implied baseline

Market-implied probability at assignment: **0.74 / 74%** for Yes.

## Own probability estimate

My estimate is **1% Yes / 99% No**.

## Agreement or disagreement with market

I **disagree strongly** with the market-implied 74% Yes.

The market’s strongest argument was presumably broad ETH strength and the intuitive idea that $2,200 was plausibly reachable sometime during the week. But that narrative is fragile because this contract does **not** ask whether ETH broadly touched $2,200 on any venue or composite feed. It asks whether **Binance ETH/USDT 1m candle High** reached that level during the stated ET window. Once the designated source is checked directly, the Yes case collapses.

## Implication for the question

Under the actual settlement mechanics, this should be interpreted as a near-certain **No** unless there is some Binance-native chart discrepancy versus the public kline data used here. The main variant contribution is not a bullish contrary case; it is that the market may have been overpricing a loose narrative of “ETH almost got there” rather than the actual contract mechanics.

## Key sources used

- **Primary / authoritative settlement source:** Polymarket market page resolution text for this event, establishing Binance ETH/USDT 1m candle High as governing source of truth. See source note: `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-source-notes/2026-04-06-variant-view-polymarket-binance-rules.md`
- **Primary / direct empirical verification:** Binance ETHUSDT 1m kline API pull over the relevant period, showing observed max High 2167.85. See source note: `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-source-notes/2026-04-06-variant-view-binance-klines-crosscheck.md`
- **Secondary / contextual cross-check:** CoinGecko ETH/USD historical range data, used only to sanity-check that broader market prints also remained below $2,200.
- **Supporting audit artifacts:**
  - Assumption note: `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/assumptions/variant-view.md`
  - Evidence map: `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/evidence/variant-view.md`

## Supporting evidence

- The market page states the market resolves Yes only if **any Binance 1-minute candle for ETH/USDT** in the title window has final **High >= $2,200**.
- The same rule text says the resolution source is **Binance**, specifically ETH/USDT on **1m** candles.
- The rule text also says prices from **other exchanges**, **different trading pairs**, or other non-designated prices do not count.
- Direct Binance kline verification over the relevant window produced an observed maximum High of **2167.85**, leaving a **32.15** gap below threshold.
- A CoinGecko contextual cross-check also stayed below $2,200, which reduces the chance that a broader-market spike was simply missed by Binance.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is methodological rather than directional: the rule explicitly names the **Binance chart surface**, while my direct verification used Binance’s public **kline API** as a proxy for the same pair/interval rather than an archived screenshot/export from the chart UI itself. If a reviewer found a Binance-native chart print at or above $2,200 that diverged from the API series, this view would need revision.

## Resolution or source-of-truth interpretation

This section is the crux of the case.

- **Governing source of truth:** Binance ETH/USDT **1-minute candle High** during the window from **12:00 AM ET Mar 30** through **11:59 PM ET Apr 5**.
- **Settlement source hierarchy (cex vs dex vs index):** **CEX-specific Binance pair first and only**. DEX prints, composite indexes, CoinGecko aggregates, or other exchanges are not controlling for settlement.
- **CEX spot price vs DEX price check:** Explicitly addressed. Even if a DEX or another venue printed $2,200, it would not settle this market Yes unless Binance ETH/USDT 1m High also did so. The contextual cross-check found no evidence that broader market pricing exceeded the threshold anyway.
- **Specific market maker attribution rules:** I found **no explicit special market-maker attribution carveout** in the visible market rules beyond the candle-high rule. The market appears to settle mechanically on printed Binance 1m Highs rather than on identifying who caused the trade.

## Key assumptions

- Binance public kline API is a faithful proxy for the Binance 1m chart surface named in the market rules.
- No hidden clarification or special rule overrides the plain candle-high settlement logic.
- The observed max of 2167.85 is far enough below threshold that small data-surface differences are unlikely to erase the gap.

## Why this is decision-relevant

This is decision-relevant because the market price of 74% Yes appears to reflect overconfidence relative to the actual designated settlement surface. In rule-sensitive crypto threshold markets, being right about “ETH was strong” is not enough; you have to be right about the exact venue, pair, interval, and field that govern resolution.

## What would falsify this interpretation / change your mind

- Direct Binance chart evidence showing at least one ETH/USDT 1m High **>= $2,200** during the stated ET window.
- Any Polymarket clarification showing that another source, pair, or hierarchy supersedes the quoted rule text.
- Evidence that the kline API omitted relevant candles or materially diverged from the chart surface named in the contract.

## Source-quality assessment

- **Primary source used:** Polymarket market page rule text plus Binance ETHUSDT 1m kline data.
- **Key secondary/contextual source:** CoinGecko ETH historical range data.
- **Evidence independence:** **Medium.** The rule text is authoritative but not independent; Binance data is direct venue data; CoinGecko is an external contextual sanity check.
- **Source-of-truth ambiguity:** **Low after verification.** It begins as a flagged ambiguity case, but the visible rule text is quite specific once read.

## Verification impact

- **Additional verification pass performed:** Yes.
- **Did it materially change the view?** Yes, in the sense that it collapsed the plausible variant thesis from “maybe source ambiguity matters” to “No unless there is an unlikely Binance chart/API discrepancy.”
- **How it changed the view:** The added verification moved the case from a potentially ambiguous crypto-threshold market to a near-mechanical No.

## Reusable lesson signals

- **Possible durable lesson:** In crypto threshold markets, source-of-truth venue/pair/interval should be audited before taking broad asset-price narratives seriously.
- **Possible missing or underbuilt driver:** None obvious from a single case.
- **Possible source-quality lesson:** Web-visible market rule text plus direct designated-venue data can often resolve ambiguity faster than broad market commentary.
- **Confidence that reusable lesson is reusable:** **Medium.**

## Orchestrator review suggestions

- **Review later for durable lesson:** yes
- **Review later for driver candidate:** no
- **Review later for canon or linkage issue:** no
- **Reason:** This case reinforces a reusable methodological lesson about auditing crypto market settlement mechanics early, but does not obviously require canon or driver restructuring from one instance.

## Recommended follow-up

No major follow-up suggested unless a reviewer wants a stricter archive-quality confirmation from the exact Binance UI chart surface. If such a confirmation is needed, it should be treated as belt-and-suspenders verification rather than evidence of a live directional dispute.