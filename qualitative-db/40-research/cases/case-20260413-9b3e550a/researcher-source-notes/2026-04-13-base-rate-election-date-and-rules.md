---
artifact_type: source_note
schema_version: v1
case_key: case-20260413-9b3e550a
persona: base-rate
source_type: primary-plus-market-rules
title: Election date, electoral system, and market resolution rules for 2026 Bulgarian parliamentary election third-place contract
source_url: https://en.wikipedia.org/wiki/2026_Bulgarian_parliamentary_election
source_date: 2026-04-13
retrieved_at: 2026-04-13
entity: []
driver:
  - elections
related_entities:
  - associated-press
related_drivers:
  - elections
proposed_entities:
  - central-election-commission-of-bulgaria
  - we-continue-the-change-democratic-bulgaria
  - revival-bulgaria
  - movement-for-rights-and-freedoms
reliability: medium
---

# Summary
- Election date is stated as 19 April 2026, matching the market description and AP-cited appointment of a caretaker government on 18 February 2026.
- Bulgaria uses proportional representation with a 4% threshold, so third place in seats will usually come from the cluster of parties polling around low-double-digits rather than from a marginal micro-party.
- The market resolves by seats first, then valid votes, with a fallback to official Central Election Commission of Bulgaria (CIK) results if consensus reporting is ambiguous.

# Key extracted facts
- Wikipedia raw page states: "Parliamentary elections are scheduled to be held in Bulgaria on 19 April 2026" and cites Politico/Al Jazeera plus AP for the appointment of caretaker PM Andrey Gyurov and election date.
- Electoral system section says all 240 seats are elected by proportional representation in 31 constituencies with a 4% threshold.
- Market description supplied in assignment says resolution is based on the party or coalition with the third-greatest number of seats; tie-breakers are valid votes then alphabetical abbreviation, and if reporting is ambiguous resolution falls back to official CIK results.

# Why this matters
- Confirms the relevant date and that the contract is a seat-ranking market, not a vote-share market.
- Confirms source-of-truth hierarchy: consensus of credible reporting first, official CIK as fallback when ambiguous.
- The threshold and seat-allocation structure imply third place should usually be one of PP–DB, Revival, or DPS rather than a tail outcome.

# Caveats
- Direct fetch of CIK was blocked by Cloudflare in this environment, so I could not independently inspect the official site here.
- Wikipedia is not itself authoritative, but it compiles current polling and cites AP/Politico for the election-date facts.

# Verbatim anchors
- "Parliamentary elections are scheduled to be held in Bulgaria on 19 April 2026"
- "The electoral threshold was 4% for all parties or electoral coalitions"
- Market rule: resolves by "the third-greatest number of seats" with CIK fallback if ambiguity remains.
