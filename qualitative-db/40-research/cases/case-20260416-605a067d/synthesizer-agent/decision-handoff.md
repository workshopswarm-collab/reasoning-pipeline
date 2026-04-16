---
type: synthesis_decision_handoff
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
question: "Will the price of Ethereum be above $2,200 on April 17?"
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/syndicated-finding.md
market_implied_probability: 0.871
syndicated_probability_low: 0.82
syndicated_probability_high: 0.86
syndicated_probability_midpoint: 0.84
relation_to_market: below_market
edge_quality: moderate
edge_independent_verification_quality: medium
compressed_toward_market_due_to_verification: no
contract_ambiguity_level: minor
contract_ambiguity_reason: "small residual UI-vs-API candle mapping risk on the governing Binance surface"
independently_verified_points: ["Polymarket-style mechanism is a Binance ETH/USDT 12:00 ET 1-minute final close-above test", "Fresh Binance spot remained above threshold at about 2301 during synthesis", "Fresh Binance 24h low still remained above 2200 at 2285.10", "Recent hourly Binance path shows downside volatility is real but threshold cushion still exists"]
verification_gap_summary: "The only decisive fact still unavailable is the actual Apr 17 12:00 ET Binance final close."
best_countercase_summary: "A routine 4-5% crypto drawdown before the exact settlement minute would flip this to No despite current spot being safely above 2200."
main_reason_for_disagreement: "Remaining disagreement is mostly about how much discount to apply for exact-minute timing risk versus current price cushion."
resolution_mechanics_summary: "Yes resolves only if Binance ETH/USDT's Apr 17 12:00 ET 1-minute candle final close is strictly above 2200."
freshness_sensitive: yes
freshness_driver: "Binance ETH/USDT path into the Apr 17 noon ET settlement minute"
decision_blockers: ["Single-minute settlement risk remains materially unresolved until the final candle exists", "Fresh overnight or U.S.-morning crypto risk-off move could erase the cushion quickly"]
blockers_require_new_research: no
disagreement_type: timing
follow_up_needed: yes
---

# Decision summary

ETH is more likely than not to finish above 2200 on the governing Binance noon-ET minute close on April 17, but the market’s 87.1% Yes price still looks somewhat rich for a single exact future 1-minute close contract. My post-synthesis view is Yes, with a final range of 0.82 to 0.86 after a fresh verification pass that confirmed current cushion above 2200 but did not justify trusting the market’s upper-80s confidence fully.

## Why this may matter now

Market-implied baseline is 0.871. My syndicated range is 0.82-0.86. That implies at most a marginal No-side edge versus market, not a strong one. The likely mispricing is that the market may be slightly underdiscounting exact-minute settlement risk for a contract that depends on one future Binance 1-minute close rather than an intraday touch.

## Shift versus swarm baseline

This is only slightly above the swarm-implied center near 0.83. The small upward nudge comes from fresh synthesis-stage verification that Binance spot was still around 2301 and the 24h low remained above 2200, which modestly supports the Yes case. I did not move to market because the extra verification did not solve the main problem: the contract still depends on one future minute close that has not happened yet.

## Edge verification status

Verification quality is medium. I independently checked fresh Binance ticker, 24h stats, and recent hourly path after reading the persona findings. That independently confirmed the current cushion, confirmed that recent realized lows remained above 2200, and confirmed that downside volatility is real rather than hypothetical. What remains unverified is the only thing that truly decides the contract: the Apr 17 12:00 ET final close. That prevents a high verification grade.

## Compression toward market

No. I did not compress materially toward the market because the fresh verification mostly supported the swarm’s slightly-below-market consensus rather than undermining it. The extra check justified a small upward trim from the swarm floor, but not enough to erase the mechanism discount.

## Timing and catalyst posture

The next real catalyst is not a news item but the Binance ETH/USDT path into the U.S. morning and especially the final hour before noon ET on Apr 17. The edge is more likely to decay than widen if ETH stays stable, because market confidence should remain high or drift higher as time-to-resolution shrinks. Waiting may improve accuracy but may also reduce any tradable edge unless volatility rises.

## Key blockers

There is no major contract ambiguity blocker; the main blocker is irreducible timing risk. The decision is also freshness-sensitive because a sharp overnight or morning move can quickly invalidate today’s cushion. So the blocker is less 'need more theory' and more 'need late-stage price-state awareness.'

## Best countercase

Best countercase: the market may be right or even slightly low because ETH is already above 2300, 24h lows stayed above 2200, and with less than 24 hours left the contract mostly needs to avoid an ordinary but not inevitable selloff. Catalyst-hunter best represented that view.

## What would change the view

A fresh Apr 17 morning Binance check still showing ETH comfortably above 2300 with subdued volatility would push me upward, likely toward market. A drop toward 2240 or below, or evidence of Binance-specific weakness, would push me down materially. Any evidence that the settlement surface differs materially from API-observed candles would also change the view.

## Recommended next action

Wait for the Apr 17 morning checkpoint and rerun only a narrow late-stage verification pass rather than the full swarm unless price action materially changes before then.

## Verification impact

Yes, synthesis-stage external verification was used. Fresh Binance checks modestly strengthened the Yes case and supported a slight move up from the swarm floor, but cross-lane comparison also reinforced that most lanes besides catalyst-hunter were right to keep a timing discount. The synthesis did not uncover major provenance failures; it mainly rejected the most aggressive bullish weighting as a bit overconfident.
