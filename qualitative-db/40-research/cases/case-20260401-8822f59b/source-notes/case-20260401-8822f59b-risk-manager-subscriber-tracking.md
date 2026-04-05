---
type: source_note
domain: culture
subdomain: social-media
entity: MrBeast
topic: MrBeast subscriber threshold tracking around March 31, 2026
question: Will MrBeast hit 474 Million subscribers by March 31, 2026 11:59 PM ET?
driver: media-narratives
date_created: 2026-04-01
source_name: Combined source note — YouTube channel page, SocialCounts, vidIQ
source_type: mixed measurement pages
source_url: https://www.youtube.com/@MrBeast
source_date: 2026-04-01
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: risk-manager
related_entities: [MrBeast, YouTube]
related_drivers: [media-narratives, sentiment]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260401-8822f59b/analyses/2026-04-01/dispatch-case-20260401-8822f59b-20260401T135420Z/assumptions/risk-manager.md
  - qualitative-db/40-research/cases/case-20260401-8822f59b/analyses/2026-04-01/dispatch-case-20260401-8822f59b-20260401T135420Z/personas/risk-manager.md
tags: [source-note, market/mrbeast-474m, platform/youtube, creator-economy]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/source-notes/by-market/case-20260401-8822f59b-risk-manager-subscriber-tracking.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260401-8822f59b
---

# Summary

Three useful measurement signals line up in the same direction:
1. the live YouTube channel page currently displays `474M subscribers` for `@MrBeast`;
2. SocialCounts currently reports an exact count of `474,168,979` subscribers;
3. vidIQ's embedded `dailyStats` history shows `474,000,000` subscribers at timestamp `1774915200` (= 2026-03-31 00:00 UTC, which is 2026-03-30 20:00 ET), with `473,000,000` at `1774828800` (= 2026-03-30 00:00 UTC).

Taken together, the evidence strongly suggests the visible 474M threshold had already been reached by the evening of March 30 ET, comfortably before the March 31 11:59 PM ET resolution deadline.

## Key facts extracted

- Official YouTube channel HTML for `https://www.youtube.com/@MrBeast` includes page-header metadata showing `474m subscribers` / accessibility label `474 million subscribers`.
- SocialCounts page for MrBeast reports `474,168,979 subscribers` as of fetch time on 2026-04-01.
- vidIQ channel stats page HTML includes structured data/embedded stats indicating:
  - 2026-03-31 00:00 UTC: `subscribers = 474000000`, `subscribers_change = 1000000`
  - 2026-03-30 00:00 UTC: `subscribers = 473000000`
  - 2026-03-29 through 2026-03-26 UTC also show `473000000`
- Because 2026-03-31 00:00 UTC equals 2026-03-30 20:00 ET, vidIQ's daily bucket implies the 474M mark was already reflected before the market's deadline day fully began in ET terms.

## Evidence directly stated by source

- YouTube page header metadata: `474m subscribers`.
- SocialCounts: `Explore MrBeast's YouTube presence with 474,168,979 subscribers ...`
- vidIQ page description and embedded daily stats: channel statistics featuring `474,000,000 subscribers`; `dailyStats` row for `1774915200` with `subscribers: 474000000`.

## What is uncertain

- The exact intraday moment of the threshold crossing is not pinned down from the official YouTube page alone.
- Third-party trackers (SocialCounts, vidIQ) may round or bucket subscriber counts differently from the exact internal YouTube counter.
- The market's practical resolution convention may depend on the visible public count on the channel page rather than the exact internal count, though the market description points primarily to the channel itself or credible reporting.

## Why this source may matter

This is the core timing evidence for whether the threshold was reached before the deadline, not just after it. The live YouTube page confirms current threshold attainment; the third-party tracker history helps bridge the key timing question.

## Possible impact on the question

These sources move the case strongly toward `Yes`. The main remaining risk is measurement/resolution mismatch, not directional uncertainty about whether MrBeast was around the 474M threshold.

## Reliability notes

- YouTube is the highest-credibility source for current visible subscriber status, but it is not enough by itself to reconstruct intraday timing.
- SocialCounts and vidIQ are lower-credibility than YouTube for settlement, but useful as corroborating measurement/trend tools.
- The strongest risk is not direction but timing granularity and rounding conventions across sources.
