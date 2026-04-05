---
type: evidence_map
domain: energy
subdomain: retail-gasoline
entity: aaa-fuel-prices
topic: case-20260405-b842cb71 | risk-manager
question: Will gas hit (High) $4.00 by March 31?
driver: contract-mechanics
date_created: 2026-04-05
agent: risk-manager
status: complete
confidence: high
conflict_status: low
action_relevance: high
related_entities: [aaa-fuel-prices, polymarket, internet-archive]
related_drivers: [contract-mechanics, resolution-source-verification, threshold-crossing-timing]
upstream_inputs: []
downstream_uses: [agent-finding]
tags: [aaa, gas-prices, resolution, evidence-map, risk-manager]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/evidence-maps/case-20260405-b842cb71-risk-manager-evidence-map.md
legacy_original_note_kind: evidence
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260405-b842cb71
dispatch_id: dispatch-case-20260405-b842cb71-20260405T074926Z
analysis_date: 2026-04-05
persona: risk-manager
---

# Summary
The highest-weight evidence says the market should resolve **Yes** because AAA’s own March 31 homepage, preserved by the Internet Archive, shows the `Regular` / `Current Avg.` cell at **$4.018**.

## Question being evaluated
Will gas hit (High) $4.00 by March 31, using AAA’s `Regular` / `Current Avg.` cell and the contract’s first-two-digits rule?

## Current lean
Strong lean **Yes**.

## Prior / starting view
Before checking the source-of-truth surface directly, the market price of 0.775 suggested the market still assigned meaningful failure risk or had stale uncertainty.

## Evidence supporting the claim
1. **AAA March 31 archived homepage shows `$4.018` in `Current Avg.` / `Regular`.**
   - Source: `case-20260405-b842cb71-risk-manager-aaa-2026-03-31-archived-homepage.md`
   - Why it matters: this is direct verification of the named settlement surface on the key date.
   - Direct or indirect: direct.
   - Weight: very high.

2. **Contract’s own example implies truncation, not rounding.**
   - Source: market description in assignment prompt.
   - Why it matters: even under truncation, `$4.018 -> $4.01`, still above $4.00.
   - Direct or indirect: direct contract-mechanics evidence.
   - Weight: high.

3. **AAA April 2 post says the national average exceeded $4/gallon “this week for the first time since August 2022.”**
   - Source: `case-20260405-b842cb71-risk-manager-aaa-2026-04-02-post.md`
   - Why it matters: contextual timing check consistent with a threshold crossing right around March 31 / April 1.
   - Direct or indirect: contextual primary source.
   - Weight: medium.

## Evidence against the claim
1. **Runtime metadata lists `closes_at` / `resolves_at` as 2026-03-30 20:00 ET.**
   - Why it matters: creates a small operational ambiguity versus the plain-language “by March 31” wording.
   - Direct or indirect: indirect/operational.
   - Weight: low-to-medium.

2. **Current market price only implies 77.5%.**
   - Why it matters: either some traders saw unresolved rule/timing ambiguity or the market had not fully incorporated late data.
   - Direct or indirect: indirect sentiment/confidence evidence.
   - Weight: low.

## Ambiguous or mixed evidence
- AAA’s April 2 wording “this week” does not isolate the exact crossing date by itself.
- Internet Archive is independent as a preservation layer, but not independent of AAA as the underlying data source.

## Conflict between inputs
- Main disagreement is between the direct source-of-truth check (strong Yes) and the lower market price / slightly awkward close-time metadata.
- This is mostly a timing/interpretation conflict, not a factual one.
- Best resolving evidence would be an explicit Polymarket clarification that March 31 readings count despite the listed close time.

## Key assumptions
- March 31 is included in the eligible date range.
- Archived AAA page faithfully preserves the named source-of-truth surface.
- The first-two-digits rule means truncation.

## Key uncertainties
- Whether any operational settlement note narrows the eligible window in a way not reflected in the contract text.

## Disconfirming signals to watch
- A Polymarket resolution note excluding March 31 readings.
- Evidence that AAA’s March 31 displayed value at settlement time differed from the archived value used here.

## What would increase confidence
- Direct Polymarket moderator/resolution comment confirming March 31 counted.
- A second independent archival capture of the AAA page on March 31 showing the same `$4.018` reading.

## Net update logic
The decisive update was moving from price-based uncertainty to a direct check of the named AAA settlement surface. Once the March 31 archived AAA table showed `$4.018`, the market moved from probabilistic to near-resolved unless a narrow rule/timing exception overrides the plain contract text.

## Suggested downstream use
Use as a forecast update and Orchestrator synthesis input; little additional investigation is needed unless the close-time-vs-March-31 wording discrepancy becomes operationally important.