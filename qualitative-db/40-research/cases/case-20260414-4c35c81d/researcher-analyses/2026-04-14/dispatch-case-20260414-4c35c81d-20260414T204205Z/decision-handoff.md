---
type: synthesis_decision_handoff
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
question: "Will Al Qadisiyah Saudi Club win on 2026-04-23?"
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260414-4c35c81d/researcher-analyses/2026-04-14/dispatch-case-20260414-4c35c81d-20260414T204205Z/syndicated-finding.md
market_implied_probability: 0.83
syndicated_probability_low: 0.03
syndicated_probability_high: 0.12
syndicated_probability_midpoint: 0.075
relation_to_market: below_market
edge_quality: strong
edge_independent_verification_quality: high
compressed_toward_market_due_to_verification: no
contract_ambiguity_level: moderate
contract_ambiguity_reason: "assignment date conflicts with independently verified fixture/result timing for the named matchup"
independently_verified_points: ["ESPN scoreboard shows Al Qadsiah vs Al Shabab finished 2-2 on 2026-04-14", "ESPN Saudi Pro League scoreboard for 2026-04-23 does not show an Al Qadsiah vs Al Shabab fixture", "market is a 90-minute win-only contract where a draw resolves no", "risk-manager raw finding faithfully captures the central date-misalignment concern"]
verification_gap_summary: "The main remaining gap is the explicit named official settlement source tying the contract to either the 2026-04-14 result or a different fixture."
best_countercase_summary: "The contract could still refer to a separate future fixture despite the matchup-level evidence pointing to the 2026-04-14 draw."
main_reason_for_disagreement: "Most personas assumed a normal future pre-match pricing problem, while the risk-manager identified a likely event-timestamp mismatch."
resolution_mechanics_summary: "This is a 90-minute win-only market, so if the governing fixture is the verified 2026-04-14 2-2 match the contract should resolve no."
freshness_sensitive: yes
freshness_driver: "Any explicit market-settlement clarification or official league source tying the contract to a different fixture would sharply change the view."
decision_blockers: ["Explicit official settlement-source confirmation is still missing", "Residual chance remains that the contract references a different future fixture than the verified 2026-04-14 match"]
blockers_require_new_research: yes
disagreement_type: mixed
follow_up_needed: yes
---

# Decision summary

The synthesis view is that Al Qadisiyah win should be treated as very unlikely to resolve yes on this contract as currently framed, because the strongest independently verified evidence indicates the relevant Al Qadsiah–Al Shabab league match already finished 2-2 on 2026-04-14, while 2026-04-23 appears to be a date-misalignment problem rather than the true fixture date for this matchup.

## Why this may matter now

Market implies 0.83, but post-synthesis range is 0.03 to 0.12. This looks actionable if the contract is still trading near a normal pre-match favorite price, because the main likely mispricing is event/date misalignment rather than team strength. The edge is large and comes from independently verified fixture timing, not from a modest sports-handicap disagreement.

## Shift versus swarm baseline

This differs materially from the swarm-implied center near the low-0.7s because the synthesis gives much more weight to the risk-manager's contract/timing evidence after independent checking. A bounded truth-finding pass verified that ESPN shows the named matchup as finished 2-2 on 2026-04-14 and that ESPN's 2026-04-23 Saudi Pro League slate does not include this matchup. That made the routine pre-match lanes look incomplete rather than merely conservative.

## Edge verification status

Independent verification was meaningful and material. Beyond the persona bundle, a synthesis-stage ESPN API check confirmed (1) Al Qadsiah vs Al Shabab finished 2-2 on 2026-04-14 and (2) no Al Qadsiah vs Al Shabab fixture appears on the 2026-04-23 Saudi Pro League scoreboard. This does not fully eliminate settlement-source ambiguity, but it does independently verify the central factual premise behind the bearish case. Verification quality is high relative to the key edge because the main dispute is fixture identity/timing, not fine-grained team strength.

## Compression toward market

No. The synthesis did not compress toward market because the additional truth-finding supported the minority bearish view rather than weakening it. The remaining uncertainty is captured as a nonzero yes range only because the exact settlement source still could map to a different event.

## Timing and catalyst posture

The next catalyst is explicit settlement-source clarification, either from Polymarket's named official source or an official league fixture/result page. Until then, the edge is more likely to persist if the market has not recognized the mismatch. Waiting may worsen decision quality if the market corrects once the mismatch becomes obvious.

## Key blockers

Main blockers are explicit source-of-truth confirmation and residual ambiguity over whether the contract references a different fixture than the verified 2026-04-14 draw. Those blockers matter, but they do not erase the currently dominant bearish interpretation.

## Best countercase

Best countercase: the assignment date could be the real governing object, with the 2026-04-14 draw belonging to a different fixture/context and the market therefore still representing a normal future-match favorite. Risk-manager represented the opposite side best; the other four personas collectively represented this surviving countercase by treating the market as a future event.

## What would change the view

A direct official league source or explicit market-settlement source showing Al Qadisiyah vs Al Shabab is actually scheduled and unresolved on 2026-04-23 would sharply raise the probability back toward a normal favorite range. Any evidence that the 2026-04-14 2-2 result belongs to a different competition or different contract object would also change the view materially.

## Recommended next action

Request decision-maker review now if the market is live and still near pre-match favorite pricing, but pair that with one immediate verification step: collect the explicit official settlement source for the exact contract object. If that confirmation is obtained, no broad rerun is needed; only if it contradicts the 2026-04-14 mapping should the sports-handicap lanes be rerun.

## Verification impact

Yes, additional synthesis-stage verification was used, and it materially changed the final view. Cross-lane comparison exposed that four personas were arguing over price calibration on a premise the risk-manager had already challenged at the object level. Independent checking strengthened the risk-manager thesis and made the non-risk lanes look incomplete on the most important question. No extra research was needed on lineups or odds because that would have been lower-yield than verifying fixture identity.
