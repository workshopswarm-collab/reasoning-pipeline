---
type: source_note
case_key: case-20260413-9b3e550a
dispatch_id: dispatch-case-20260413-9b3e550a-20260413T191836Z
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: elections
entity:
topic: Bulgarian 2026 election context and likely party ordering
question: Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Wikipedia 2026 Bulgarian parliamentary election page plus POLITICO Poll of Polls page capture
source_type: contextual election summary / polling aggregator
source_url: https://en.wikipedia.org/wiki/2026_Bulgarian_parliamentary_election ; https://www.politico.eu/europe-poll-of-polls/bulgaria/
source_date: 2026-04-13
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9b3e550a/researcher-analyses/2026-04-13/dispatch-case-20260413-9b3e550a-20260413T191836Z/personas/risk-manager.md]
tags: [source-note, bulgaria, polling, contextual, pp-db]
---

# Summary

This source pair provides the election date and current competitive context. The Wikipedia page confirms the 19 April 2026 snap election and lists current parliamentary seat standings from the prior assembly. The POLITICO Bulgaria Poll of Polls page indicates PP–DB is among the top cluster of parties and not obviously locked into third; the captured page shows Revival around 14.0% and confirms PP–DB, GERB, DPS-New Beginning, and Revival are the key parties displayed in the live competitive set.

## Key facts extracted

- Election scheduled for 19 April 2026.
- Bulgaria remains in a fragmented snap-election cycle following the collapse of the prior government.
- Current-seat context from the outgoing assembly is GERB-SDS 66, PP–DB 36, Revival 33, DPS 29, BSP–OL 19, APS 17, ITN 17, MECh 11, Velichie 10, PB 0.
- This outgoing-seat ordering suggests PP–DB enters with a narrow structural edge over Revival and DPS in the prior parliament, but not an overwhelming one.
- POLITICO’s Bulgaria Poll of Polls page is current and explicitly election-specific; page capture confirms the election date prompt and that Revival is shown at 14.0% in the tracked set, with PP–DB, GERB, and DPS-New Beginning also represented in the main party list.

## Evidence directly stated by source

Directly stated: the election date, the snap-election context, and the outgoing seat order from Wikipedia. Directly observed from the POLITICO page capture: Bulgaria election framing for 19 April and Revival at 14.0%, with PP–DB and other top competitors present in the aggregator list.

## What is uncertain

- My scraping of the POLITICO page did not cleanly extract the full current ranked percentages for all top parties, so this source is stronger on competitive-set confirmation than on exact vote-gap measurement.
- Wikipedia is not itself authoritative and may lag or compress nuances.
- The CIK official election page was protected by anti-bot measures in this environment, so official timing/source-of-truth confirmation is indirect through contract text plus contextual page reporting rather than direct CIK page text capture.

## Why this source may matter

It establishes that PP–DB is operating in a fragmented field where third place is plausible but not safely dominant. The market at 0.78 implies fairly high confidence in an exact-rank outcome; the contextual evidence supports PP–DB as a contender but leaves meaningful room for seat-order variance.

## Possible impact on the question

This pushes toward a yes-lean, but with a lower confidence level than the market price suggests, because fragmentation and a relatively tight competitor set make exact third-place ranking fragile.

## Reliability notes

Useful contextual pair, but not a perfect independent forecast stack. Wikipedia is secondary/compilatory; POLITICO is a stronger contextual polling aggregator but my extract is partial. Good enough to meet a medium-difficulty evidence floor when paired with the contract source, but not strong enough to justify extreme confidence.