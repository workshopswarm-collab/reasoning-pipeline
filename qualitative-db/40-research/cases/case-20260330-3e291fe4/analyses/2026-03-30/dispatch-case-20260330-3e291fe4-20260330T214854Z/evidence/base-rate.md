---
type: evidence_map
domain: economics
subdomain: consumer-prices
entity: u-s-department-of-energy
topic: base-rate evidence map for national gasoline hitting $4 by March 31
question: Will gas hit (High) $4.00 by March 31?
driver: energy
date_created: 2026-03-30
agent: base-rate
status: draft
confidence: medium-high
conflict_status: limited conflict / final-day uncertainty
action_relevance: high
related_entities: [u-s-department-of-energy]
related_drivers: [energy, conflicts]
upstream_inputs:
  - qualitative-db/40-research/cases/case-20260330-3e291fe4/source-notes/case-20260330-3e291fe4-base-rate-aaa-current-level.md
  - qualitative-db/40-research/cases/case-20260330-3e291fe4/source-notes/case-20260330-3e291fe4-base-rate-eia-trend-context.md
  - qualitative-db/40-research/cases/case-20260330-3e291fe4/source-notes/case-20260330-3e291fe4-base-rate-market-news-context.md
  - qualitative-db/40-research/cases/case-20260330-3e291fe4/analyses/2026-03-30/dispatch-case-20260330-3e291fe4-20260330T214854Z/assumptions/base-rate.md
downstream_uses:
  - qualitative-db/40-research/cases/case-20260330-3e291fe4/analyses/2026-03-30/dispatch-case-20260330-3e291fe4-20260330T214854Z/personas/base-rate.md
tags: [market/will-gas-hit-high-4pt00-by-march-31, evidence-map, domain/economics]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/evidence-maps/case-20260330-3e291fe4-base-rate-evidence-map.md
legacy_original_note_kind: evidence
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260330-3e291fe4
dispatch_id: dispatch-case-20260330-3e291fe4-20260330T214854Z
analysis_date: 2026-03-30
persona: base-rate
---

# Summary

The outside view is unusually favorable to "Yes" because the resolution source is already at **$3.990** on March 30. At this point, the event no longer requires a major gasoline shock; it requires only a final one-cent continuation of an already powerful late-March uptrend.

## Question being evaluated

Will the AAA national average for regular gasoline print at **$4.000 or above** on any day by March 31, 2026?

## Current lean

Lean **Yes**.

## Prior / starting view

A generic prior for a specific nominal gasoline threshold would usually be cautious because national averages move gradually and daily threshold events can fail by a hair. But that generic prior becomes much less relevant once the live resolution source is already within one cent of the target and still rising.

## Evidence supporting the claim

1. **Resolution source is already at $3.990 on March 30**
   - Source: `case-20260330-3e291fe4-base-rate-aaa-current-level.md`
   - Why it matters: the remaining distance is only one cent.
   - Direct/indirect: direct, decisive.
   - Weight: very high.

2. **AAA daily series rose one cent from yesterday and 10 cents from a week ago**
   - Source: same note.
   - Why it matters: shows current momentum remains upward into the final day.
   - Direct/indirect: direct.
   - Weight: high.

3. **AAA publicly said on March 26 that the national average could reach $4 in the coming days**
   - Source: same note.
   - Why it matters: contemporaneous industry commentary aligned with the observed approach to the threshold.
   - Direct/indirect: direct.
   - Weight: medium-high.

4. **EIA weekly trend is steep and broad-based**
   - Source: `case-20260330-3e291fe4-base-rate-eia-trend-context.md`
   - Why it matters: the national move is not an isolated glitch; the broader trend had been strong into late March.
   - Direct/indirect: direct structural support.
   - Weight: high.

5. **Oil/conflict backdrop still appears supportive rather than reversing**
   - Source: `case-20260330-3e291fe4-base-rate-market-news-context.md`
   - Why it matters: reduces the chance that the final step to $4 is being asked against a collapsing driver regime.
   - Direct/indirect: indirect contextual support.
   - Weight: medium.

## Evidence against the claim

1. **Threshold events can fail by rounding-adjacent amounts**
   - Source: market rules + AAA source.
   - Why it matters: 3.990 is close, but not yet $4.000 under a literal reading.
   - Direct/indirect: direct rules-based friction.
   - Weight: high.

2. **Daily national averages can flatten even when weekly trends are strong**
   - Source: general measurement logic + assumption note.
   - Why it matters: one more cent is small, but it is still not guaranteed.
   - Direct/indirect: indirect/base-rate caution.
   - Weight: medium.

3. **EIA weekly data are not the resolver**
   - Source: EIA note.
   - Why it matters: supportive macro trend is not identical to AAA's final daily print.
   - Direct/indirect: direct methodological caveat.
   - Weight: medium.

## Ambiguous or mixed evidence

- Conflict-driven oil pressure is bullish for retail gasoline, but pass-through timing can be uneven.
- AAA's commentary that prices could reach $4 is supportive but not a guarantee.
- Being one cent away can be either almost done or just short, depending on publication timing and daily averaging.

## Conflict between inputs

There is only a small **timing-based** conflict:
- trend evidence says the threshold is very likely near
- literal resolution mechanics say near is not the same as crossed

What would resolve it:
- the 2026-03-31 AAA national average print

## Key assumptions

The key assumption is that the uptrend has not already stalled at $3.99. See the linked assumption note.

## Key uncertainties

- exact 3/31 AAA print
- whether the final daily increment is positive, flat, or slightly negative
- whether the market is already fully pricing the one-cent-left setup

## Disconfirming signals to watch

- AAA 3/31 remains at $3.99x
- broad state-level stabilization before the final update
- sudden oil/gasoline retracement that visibly breaks daily retail momentum

## What would increase confidence

- state-by-state AAA updates showing continued national broadening upward on 3/30 into 3/31
- direct confirmation that AAA's 3/31 national read is printing at or above $4.000

## Net update logic

The evidence moves me sharply above any generic threshold prior because the question is no longer "can gasoline rally to $4 eventually?" It is "can a series already at $3.99 and rising add one more cent by tomorrow?" That is a much easier event class. The only serious bearish case is a final-day stall exactly below the line.

## Suggested downstream use

Use this as the base-rate lane's main scaffold. The key message is: once the resolver is one cent short and still climbing, the outside view should lean strongly yes, though not all the way to certainty because literal threshold misses do happen.