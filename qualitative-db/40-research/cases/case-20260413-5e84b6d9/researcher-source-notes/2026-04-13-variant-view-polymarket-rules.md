---
type: source_note
case_key: case-20260413-5e84b6d9
dispatch_id: dispatch-case-20260413-5e84b6d9-20260413T210605Z
analysis_date: 2026-04-13
persona: variant-view
domain: politics
subdomain: bulgaria
topic: next-prime-minister-of-bulgaria
question: Will Rumen Radev be the next prime minister of Bulgaria after the 2026 parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market rules page
source_type: market_contract
source_url: https://polymarket.com/event/next-prime-minister-of-bulgaria
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: []
tags: [market-rules, resolution, source-of-truth]
---

# Summary
The market contract is unusually important here because the resolution depends on a formal swearing-in after the April 19, 2026 parliamentary election, excludes caretaker or interim prime ministers, and defaults to “Other” if no qualifying PM is appointed by March 31, 2027 11:59 PM ET.

## Key facts extracted
- Parliamentary elections are scheduled for April 19, 2026.
- The market resolves to the next individual officially sworn in as Prime Minister of Bulgaria following that election.
- Interim or caretaker prime ministers do not count.
- If no such PM is appointed by March 31, 2027 11:59 PM ET, the market resolves to “Other”.
- Primary source of truth is official information from the Government of Bulgaria, though consensus credible reporting may be used.

## Evidence directly stated by source
The source directly states the operative resolution logic, timing boundary, and exclusion rule.

## What is uncertain
The contract does not itself identify who is likely to be sworn in, nor does it define how to handle prolonged coalition deadlock short of the “Other” fallback.

## Why this source may matter
This is the governing contract surface. It means political prominence alone is insufficient; the winning answer must be the first qualifying post-election sworn-in PM, not merely the most-discussed leader.

## Possible impact on the question
This wording materially lowers confidence in any candidate when coalition formation is uncertain, especially in a fragmented parliamentary system where caretaker governments are common.

## Reliability notes
Highly reliable for market interpretation because it is the market’s own operative wording. It is not evidence about the real-world likelihood of any candidate absent outside reporting.
