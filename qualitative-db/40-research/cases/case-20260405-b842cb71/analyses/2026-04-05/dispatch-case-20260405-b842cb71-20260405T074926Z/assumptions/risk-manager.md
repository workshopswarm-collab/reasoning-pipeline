---
legacy_imported: true
legacy_original_path: qualitative-db/40-research/assumption-notes/case-20260405-b842cb71-risk-manager-assumptions.md
legacy_original_note_kind: assumption
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260405-b842cb71
dispatch_id: dispatch-case-20260405-b842cb71-20260405T074926Z
analysis_date: 2026-04-05
persona: risk-manager
---

# Risk-manager assumption note — case-20260405-b842cb71

## Core working assumptions
1. **The governing resolution surface is exactly the AAA homepage table named in the contract**: the cell under `Regular` and the row `Current Avg.` on `https://gasprices.aaa.com/`.
2. **The contract’s “first two digits” example implies truncation, not conventional rounding.** On that reading, `$4.018` maps to the `$4.01` bracket and therefore still clears a `$4.00` threshold.
3. **March 31 counts as an eligible date** despite the supplied runtime metadata listing `closes_at` / `resolves_at` at 2026-03-30 20:00 ET. The plain-language market rule says “between market creation and March 31, 2026” and “by March 31.”
4. **Internet Archive captures of AAA’s page are acceptable after-the-fact verification of the named AAA source surface.**

## Main fragility / failure modes
- If the resolver uses some unpublished AAA backend or a different timestamped daily snapshot than the archived homepage, the March 31 archived reading could in principle diverge from the resolver’s record.
- If Polymarket operationally treated the market as ending before any March 31 reading could count, then the plain-language rule and the metadata would be in tension.
- If “first two digits” were interpreted in some nonstandard way other than truncation of the displayed price, contract mechanics could matter more than expected.

## Why these assumptions currently look acceptable
- The contract is unusually explicit: it names AAA, the exact page, and the exact table cell.
- The example `3.157 -> 3.15` strongly points to truncation rather than rounding.
- The archived AAA March 31 page directly shows `Current Avg.` / `Regular` = `$4.018`, which clears the threshold even under the stricter truncation interpretation.

## What would most change my mind
- Evidence from Polymarket rules/comments/moderation stating that only dates through March 30 counted.
- Evidence that AAA revised or backfilled the March 31 homepage value after the fact and that the resolver used a different contemporaneous reading.
- A direct authoritative Polymarket resolution note rejecting the March 31 reading because of market-close timing.