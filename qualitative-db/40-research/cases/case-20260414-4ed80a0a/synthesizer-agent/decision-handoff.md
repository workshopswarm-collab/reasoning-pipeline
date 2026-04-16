---
type: synthesis_decision_handoff
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
question: "Will Ethereum reach $2,400 April 13-19?"
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/syndicated-finding.md
market_implied_probability: 0.916
syndicated_probability_low: 0.97
syndicated_probability_high: 0.995
syndicated_probability_midpoint: 0.9825
relation_to_market: above_market
edge_quality: moderate
edge_independent_verification_quality: high
compressed_toward_market_due_to_verification: no
contract_ambiguity_level: minor
contract_ambiguity_reason: "Exact qualifying Binance 1m candle was not archived from the final settlement surface despite direct API verification."
independently_verified_points: ["Polymarket rules name Binance ETH/USDT 1m candle High as the resolution source", "The contract window is Apr 13 12:00 AM ET through Apr 19 11:59 PM ET", "Direct Binance data in the checked window showed a high of 2415.5 above the 2400 threshold", "Risk-manager artifacts captured a max observed 1m high of 2415.5 at 2026-04-14 10:32 ET"]
verification_gap_summary: "The remaining gap is archival proof from the exact final Binance 1m settlement surface rather than API-derived verification alone."
best_countercase_summary: "The only serious surviving countercase is a settlement-path mismatch between Binance API verification and the exact data surface Polymarket/UMA would honor."
main_reason_for_disagreement: "Remaining disagreement is mostly about how much source-of-truth and settlement-path risk to haircut after a >2400 Binance print was found."
resolution_mechanics_summary: "Yes resolves if any Binance ETH/USDT 1m candle High reaches 2400 or more during Apr 13-19 ET."
freshness_sensitive: yes
freshness_driver: "Short-dated threshold market with resolution tied to Binance 1m highs and any late dispute or correction in market state."
decision_blockers: ["No major factual blocker remains if Binance API data is accepted as operative evidence", "Residual auditability gap from not archiving the exact qualifying Binance 1m candle from the final settlement surface", "Small tail risk of settlement-path or data-surface inconsistency"]
blockers_require_new_research: no
disagreement_type: interpretation
follow_up_needed: no
---

# Decision summary

Ethereum very likely already satisfied the contract’s $2,400 trigger on the governing venue during the Apr 13-19 ET window, so this should be treated as an almost-settled Yes driven by Binance-specific resolution mechanics rather than a live directional ETH bet.

## Why this may matter now

Market implied probability was 0.916. My final syndicated range is 0.97 to 0.995. The edge versus market looks actionable but modest rather than huge, because the main thesis is that the trigger was already hit on the named venue. The likely mispricing is that the assignment snapshot lagged a near-settled state while Binance-specific threshold evidence already existed.

## Shift versus swarm baseline

This is below the swarm median/center near 0.99 only slightly, not materially. I keep a bounded 0.97 to 0.995 range rather than collapsing to near-100 because large claimed edges should be independently verified, and the final archival chain still lacks a belt-and-suspenders capture of the exact qualifying Binance minute candle on the ultimate settlement surface. That said, the risk-manager lane’s direct 1m verification is strong enough that I did not compress meaningfully toward the 0.916 market.

## Edge verification status

Independent verification was strong. I independently rely on two distinct functions: Polymarket rule text for what counts, and Binance direct market data for whether it happened. Most importantly, the risk-manager source note records paginated Binance 1m klines over the relevant window and a max observed high of 2415.5 at 2026-04-14 10:32 ET. That is stronger than the looser 24h ticker and 1h-kline checks used in some other lanes. What remains unverified is not the threshold crossing itself so much as archival capture from the exact final settlement-facing display path. That is why verification quality is high, not absolute.

## Compression toward market

No meaningful compression toward market was needed. The provisional swarm edge versus 0.916 was about 7.4 points, which ordinarily would warrant skepticism. But the synthesis-stage review found enough independent support: explicit Polymarket rules plus direct Binance 1m evidence above threshold inside the window. The only surviving uncertainty is procedural tail risk, not a missing core fact.

## Timing and catalyst posture

The key catalyst already appears to have occurred: a qualifying Binance print above 2400 on Apr 14. From here the edge should decay toward certainty rather than widen, unless a dispute or data-path anomaly appears. Waiting probably does not improve the decision much except for confirming no settlement reversal.

## Key blockers

There is no major blocker to a high-confidence Yes interpretation. The only caution flags are minor: no archived screenshot/export from the exact final settlement surface, small risk of Binance API versus UI discrepancy, and small risk of an unusual Polymarket/UMA dispute.

## Best countercase

Best surviving countercase came from variant-view: the market may be somewhat overconfident if the exact settlement source or data surface differs from the Binance evidence captured in the run. After checking the raw findings, I think that countercase is preserved but weakened substantially by the risk-manager lane’s direct 1m Binance verification.

## What would change the view

A direct audit showing no Binance ETH/USDT 1m candle high at or above 2400 during the qualifying ET window would change the view materially. So would an official Polymarket/UMA clarification excluding the observed print, a documented API-versus-settlement-surface mismatch, or an actual dispute/reversal of the apparent resolution state.

## Recommended next action

No follow-up needed for current decision use beyond passive monitoring for any settlement dispute or reversal. If a retrospective audit package is wanted, collect the exact qualifying Binance 1m candle artifact.

## Verification impact

Yes, additional verification beyond mere cross-persona summary materially changed the synthesis. Cross-lane comparison exposed that variant-view was cautious mainly because it lacked recovered rules text, while base-rate and market-implied had slightly weaker verification chains than their confidence implied. The risk-manager lane provided the strongest synthesis-stage anchor by documenting direct Binance 1m verification, which materially strengthened the final Yes view and reduced the need to compress toward market.
