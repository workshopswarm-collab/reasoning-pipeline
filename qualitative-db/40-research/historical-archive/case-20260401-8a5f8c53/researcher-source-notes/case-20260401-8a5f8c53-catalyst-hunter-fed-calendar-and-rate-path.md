---
type: source_note
domain: economics
subdomain: us-macro
entity: Federal Reserve
topic: case-20260401-8a5f8c53 | catalyst timing
question: Which scheduled policy catalysts are most likely to move SPX before end-March 2026?
driver: macro
date_created: 2026-04-01
source_name: Federal Reserve / CME FedWatch
source_type: official calendar + market-implied rate tool
source_url: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
source_date: 2026-03-18
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [Federal Reserve, S&P 500]
related_drivers: [macro, liquidity, sentiment]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260401-8a5f8c53/researcher-analyses/2026-04-01/dispatch-case-20260401-8a5f8c53-20260401T170939Z/personas/catalyst-hunter.md]
tags: [case/case-20260401-8a5f8c53, persona/catalyst-hunter, driver/macro, driver/liquidity]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/researcher-source-notes/by-market/case-20260401-8a5f8c53-catalyst-hunter-fed-calendar-and-rate-path.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260401-8a5f8c53
---

# Summary
The main scheduled policy catalyst inside the contract month is the March 17-18, 2026 FOMC meeting, with minutes due three weeks later and CME FedWatch serving as the market-implied path monitor for rate expectations.

## Key facts extracted
- The Fed lists a March 17-18, 2026 FOMC meeting.
- The Fed notes that minutes for regular meetings are released three weeks after the policy decision.
- CME FedWatch is explicitly framed as the market-implied probabilities of Fed rate changes from Fed funds futures.

## Evidence directly stated by source
- Federal Reserve official calendar shows 2026 meetings on Jan 27-28, Mar 17-18, Apr 28-29, Jun 16-17, Jul 28-29, Sep 15-16, Oct 27-28, Dec 8-9.
- March is a starred meeting, i.e. one with Summary of Economic Projections / press conference cadence in the standard Fed schedule convention.
- CME describes FedWatch as tracking probabilities of upcoming FOMC moves implied by 30-Day Fed Funds futures prices.

## What is uncertain
- The fetched CME page did not expose point-in-time probabilities in readable text.
- The actual policy path between now and March 2026 can change materially with inflation, labor, or geopolitical shocks.
- It is unknown whether the March 2026 meeting will be bullish because of cuts, bearish because of no cuts, or volatile because of repricing around dot-plot messaging.

## Why this source may matter
This is the cleanest official calendar anchor for the highest-information macro catalyst inside the contract month. For a level-triggered SPX threshold market, a single dovish or hawkish repricing day around the March meeting could matter more than slow-moving valuation debate.

## Possible impact on the question
A favorable inflation/growth backdrop going into March 17-18 could create a late-window melt-up catalyst via lower-rate expectations, easier financial conditions, or dovish guidance. Conversely, sticky inflation or hawkish dots near that meeting could cap upside precisely when the market would need a final push toward 6300.

## Reliability notes
- Fed calendar is official and high confidence on dates.
- CME FedWatch is a standard market-based expectations reference, but the fetched text was descriptive rather than numerical, so this note should be used for timing structure more than exact probabilities.