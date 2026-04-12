---
type: source_note
case_key: case-20260409-92464f9a
dispatch_id: dispatch-case-20260409-92464f9a-20260409T201552Z
analysis_date: 2026-04-09
persona: variant-view
domain: climate
subdomain: global-temperature-index
entity: nasa
topic: march-2026-global-temperature-market-resolution
question: Will global temperature increase by more than 1.29ºC in March 2026?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket event page / market rules
source_type: market-rule-page
source_url: https://polymarket.com/event/march-2026-temperature-increase-c
source_date: 2026-04-09
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [nasa]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.sidecar.json]
tags: [market-rules, resolution-source, timing, fallback]
---

# Summary

This source captures the contract wording and visible resolution state from the Polymarket event page for the March 2026 temperature market.

## Key facts extracted

- The market resolves according to the value reported by the Global Land-Ocean Temperature Index for March 2026 when released.
- The primary source is the NASA GISTEMP table `GLB.Ts+dSST.txt`, specifically the row `2026` and column `Mar`.
- The rules say the March anomaly within the named bracket is necessary and sufficient once the data is available, even if the figure is later revised.
- If NASA’s “Global Temperature Index” is permanently unavailable, other NASA information may be used.
- If no information for February 2026 is provided by NASA by May 1, 2026 11:59 PM ET, the market resolves to the lowest range bracket.
- The event page also displayed `Outcome proposed: No`, `Final outcome: No`, and page metadata indicated the event had resolved with winning outcome `No` at `2026-04-09T18:58:53.000Z`.

## Evidence directly stated by source

Directly stated contract mechanics are the most decision-relevant part here: exact source-of-truth table, the immediate-resolution-on-availability clause, the later-revision-ignored clause, the NASA fallback clause, and the explicit lowest-bracket fallback if the relevant NASA information is not provided by the deadline.

## What is uncertain

- The page text says the fallback triggers if no information for `February 2026` is provided by May 1, 2026, even though the market is about March 2026. That appears to be a likely drafting error or inherited template issue, but it still matters because it is present in the visible rules text.
- The event page did not by itself expose the exact final NASA March 2026 value in the extracted text.
- The page is a market interface, not the underlying NASA source itself.

## Why this source may matter

This source governs what counts, what does not count, and how the market should settle. For this case, rule interpretation is at least as important as climatological intuition.

## Possible impact on the question

This source shifts attention away from a generic climate-trend question and toward a rule-sensitive question: did NASA publish the March 2026 row in the specified table or, failing that, did fallback mechanics force a lowest-bracket resolution. That supports a variant view that operational/source-availability risk could matter more than naive climate expectations.

## Reliability notes

Reliable for contract wording and visible market-state metadata. Not sufficient alone for the exact March 2026 anomaly value because the primary authoritative source is NASA, not Polymarket.