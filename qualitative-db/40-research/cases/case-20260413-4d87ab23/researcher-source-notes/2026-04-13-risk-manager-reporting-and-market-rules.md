---
type: source_note
case_key: case-20260413-4d87ab23
dispatch_id: dispatch-case-20260413-4d87ab23-20260413T174302Z
analysis_date: 2026-04-13
persona: risk-manager
domain: tech-ai
subdomain: model-releases
entity:
topic: deepseek-v4-reporting-and-resolution-rules
question: What counts for this market, and what does current secondary reporting imply?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market page + aggregated search/reporting snippets
source_type: mixed
source_url: https://polymarket.com/event/deepseek-v4-released-by-march-31
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, market-rules, secondary-reporting]
---

# Summary

This note captures the contract wording from the market page and the current state of secondary/contextual reporting visible through search results. The key takeaway is that the contract is narrower than casual "V4 is coming" chatter: only a clearly positioned successor to V3 that is publicly accessible to the general public counts.

## Key facts extracted

- Market rules require the next major DeepSeek V model to be publicly accessible to the general public by the deadline; private access or closed beta does not count.
- Rules explicitly exclude intermediate or experimental variants such as V3.5 and preview/exp versions that are not the new flagship V successor.
- The market page currently shows an April 15, 2026 11:59 PM ET deadline, despite this run assignment being framed as "by May 15"; this makes date/source-of-truth auditing essential.
- Search-result level secondary reporting describes V4 as anticipated, rumored, or "ahead of" release, not as clearly confirmed and generally available already.
- Reuters/Google snippet indicates a report that DeepSeek's V4 model will run on Huawei chips, but that is expectation/reportage about a coming model rather than confirmation of qualifying public availability.
- Search snippets also point to SCMP coverage describing new chatbot modes ahead of a much-awaited V4 release, again implying pre-release positioning rather than settled release.

## Evidence directly stated by source

- Polymarket page text defines what counts and what does not count.
- Secondary snippets use language like "ahead of much-awaited V4 release" and expected timing in late April, which is not equivalent to released and publicly accessible.

## What is uncertain

- Search snippets are weaker than full article reads and may compress nuance.
- The assignment metadata says "May 15" while the market page fetch shows "April 15"; the market URL slug also says "march-31". This inconsistency raises nontrivial resolution-risk and suggests the visible market text should dominate over assignment shorthand.
- Consensus of credible reporting may strengthen quickly if DeepSeek announces a release shortly after this run.

## Why this source may matter

The market is heavily rule-sensitive. Misreading what counts could easily produce a false-positive Yes view from rumors, leaks, preview modes, or non-general-public access.

## Possible impact on the question

This source materially lowers confidence in an easy Yes. Even if V4 is imminent, the contract requires all material conditions to hold: correct model identity, clear successor positioning, public accessibility, official announcement, and credible-reporting confirmation.

## Reliability notes

- Strong for contract interpretation because it is the actual market rules page.
- Medium quality for search-snippet reporting because snippets are indirect and not fully independent.
- Still useful as a disconfirming check against market overconfidence and against falsely counting preview/experimental artifacts.