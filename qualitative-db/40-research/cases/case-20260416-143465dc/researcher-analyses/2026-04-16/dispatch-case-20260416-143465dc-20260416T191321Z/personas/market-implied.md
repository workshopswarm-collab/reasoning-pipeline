---
type: agent_finding
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
research_run_id: 2d9132f2-60e4-4b10-ba84-1d2091e0201c
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: price-threshold-markets
entity: sol
topic: will-solana-reach-90-april-13-19
question: "Will Solana reach $90 April 13-19?"
driver:
date_created: 2026-04-16
agent: Orchestrator
stance: lean-yes-below-market
certainty: medium
importance: high
novelty: medium
time_horizon: days
related_entities: ["sol", "solana"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-intraday-wick-risk", "threshold-touch-market-microstructure"]
upstream_inputs: []
downstream_uses: []
tags: ["market-implied", "solana", "polymarket", "binance", "touch-market"]
---

# Claim

The market is pricing a reasonable but somewhat aggressive touch probability. I think Yes is still slightly more likely than No, but not as likely as the current 0.74 price implies.

## Market-implied baseline

Current market-implied probability: **0.74**.

That implies traders think a Binance SOL/USDT 1-minute high at or above 90 before the end of April 19 ET is distinctly likely, not merely plausible.

## Own probability estimate

**0.62**.

## Agreement or disagreement with market

**Disagree modestly with the market.**

I agree with the market's core logic: this is a touch market on Binance 1-minute highs, not a requirement to close above 90 or hold above 90, so the bar is easier to clear than casual spot readers may think. That structure alone makes Yes materially more likely than a naive spot-vs-threshold framing.

Where I disagree is on degree. My direct verification still found sampled Binance highs below 90, with the checked recent window topping at **89.15**, while TradingView context showed spot around **87.55** and identified **88** as an important nearby resistance area. That is close enough to keep Yes favored, but not enough for me to treat 74% as efficient with high confidence.

## Implication for the question

The market does not look crazy or obviously stale. It looks like it is correctly respecting contract microstructure, but may be **slightly overextended** in how confidently it assumes a remaining wick to 90 will occur. My read is: **lean Yes, but below market confidence**.

## Key sources used

**Primary / authoritative / direct**
- Polymarket contract wording and resolution source: `qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-market-implied-polymarket-resolution-source.md`
- Binance SOLUSDT 1m kline verification pass: `qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-market-implied-binance-1m-window-check.md`

**Secondary / contextual**
- TradingView SOLUSD page fetched April 16, 2026: current price 87.55; nearby resistance 85.80, 86.50, 88; note that a close above 88 could target 95 and 102.

**Governing source of truth**
- The market resolves from **Binance SOL/USDT 1-minute candle High values** during **April 13 00:00 ET to April 19 23:59 ET**. Other exchanges, other pairs, and generic spot references **do not count**.

**Compliance / evidence floor**
- Evidence floor met with at least **two meaningful sources**: one primary rule source (Polymarket contract wording) plus one primary outcome-relevant exchange source (Binance 1m klines), with a separate contextual source (TradingView) used to sanity-check proximity and resistance framing.
- Extra verification pass performed because the case is flagged high-resolution-risk and my estimate differs from market by more than 10 percentage points.

## Supporting evidence

- The contract uses **Binance 1-minute highs**, which materially favors Yes versus any close-based interpretation.
- Direct Binance verification showed the asset already trading very near the threshold, with a sampled recent maximum high of **89.15**.
- Contextual market data puts SOL in the upper-80s, so 90 is within short-horizon crypto noise range rather than a remote tail outcome.
- The strongest case that the market is efficient is simple: traders are likely pricing **wick probability**, not just visible spot price. In crypto, those are not the same thing.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming evidence is also direct: **the verified Binance window still remained below 90**. The event is near, but not already effectively done. If SOL keeps failing in the 88-89 area, the 74% price will look too optimistic.

## Resolution or source-of-truth interpretation

This section is decisive for the case.

**What counts:**
- Any **Binance SOL/USDT** 1-minute candle during the stated time window with a final **High >= 90**.

**What does not count:**
- Coinbase or TradingView prints by themselves.
- Other exchanges.
- Other pairs.
- End-of-day closes below 90, even if spot looked strong elsewhere.
- Generic references to "Solana price" that are not the Binance SOL/USDT governing series.

**How the contract wording affects the view:**
- This wording raises Yes probability versus a close-above-90 contract.
- It also makes the market more sensitive to short-lived intraday spikes and exchange-specific microstructure.
- That is the main reason I stay above 50% despite direct evidence still being sub-90 in the checked window.

## Key assumptions

- The market is mainly assuming a remaining **intraday wick** is likely from current levels.
- No broad crypto risk-off move interrupts the setup before April 19 closes.
- Binance remains the relevant venue for the move, not just broader aggregate spot references.

## Why this is decision-relevant

If the synthesis layer treats this like a plain spot-price question, it will underestimate Yes. If it treats 74% as already near-settled, it will overestimate Yes. The useful middle view is that the market is incorporating the right mechanism, but perhaps with too much confidence.

## What would falsify this interpretation / change your mind

I would raise toward the market or above it if:
- a fuller Binance-window audit showed repeated prior touches near 90 during the relevant interval,
- SOL cleanly reclaimed and held above 88.5-89 with continued momentum,
- broader crypto tape turned decisively risk-on and increased odds of a fast wick.

I would cut materially below 0.62 if:
- repeated attempts fail below 89,
- a broader crypto drawdown starts pulling SOL away from the threshold,
- a more complete Binance 1m review showed the market had less latent touch-risk than the current price suggests.

## Source-quality assessment

- **Primary source used:** Polymarket contract wording for settlement mechanics, plus direct Binance SOLUSDT 1m kline data for outcome-relevant verification.
- **Most important secondary/contextual source:** TradingView SOLUSD page for live contextual price and nearby resistance framing.
- **Evidence independence:** **Medium.** The contract source and Binance source are distinct in function, but both ultimately revolve around the same market mechanism. TradingView adds context, not independent settlement proof.
- **Source-of-truth ambiguity:** **Low for rules, medium for real-time verification completeness.** The governing source is explicit, but my Binance pass was sampled recent-window verification rather than a full end-to-end interval audit.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the view?** Yes, modestly.
- The extra pass reinforced the market's touch logic but also constrained my confidence because the checked Binance highs were still below 90. Without that pass I might have stayed closer to the market prior; after it, I remain lean Yes but at **0.62**, not 0.74.

## Reusable lesson signals

- Possible durable lesson: crypto threshold-touch markets can trade much richer than spot-distance intuition when settlement uses exchange-specific 1m highs.
- Possible missing or underbuilt driver: **threshold-touch-market-microstructure** / **binance-intraday-wick-risk** look like reusable causal concepts.
- Possible source-quality lesson: for narrow touch markets, direct proof of governing-source mechanics plus at least one live exchange verification pass is worth preserving explicitly.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **yes**
- reason: this case again suggests the system should have a cleaner canonical way to represent exchange-specific touch-market microstructure and governing-source proof requirements.

## Recommended follow-up

- If time allows before synthesis, run a **full Binance 1m interval check** across the entire April 13-19 window rather than relying on sampled recent-window verification.
- In synthesis, treat the current price as **informative but slightly rich** rather than obviously wrong.