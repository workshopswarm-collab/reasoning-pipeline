---
type: source_note
case_key: case-20260413-9b3e550a
dispatch_id: dispatch-case-20260413-9b3e550a-20260413T191836Z
analysis_date: 2026-04-13
persona: market-implied
domain: politics
subdomain: elections
entity:
topic: bulgarian-parliamentary-election-third-place
question: Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market context page
source_type: market contract / resolution text
source_url: https://polymarket.com/event/bulgarian-parliamentary-election-3rd-place
source_date: 2026-04-13
credibility: medium
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [polymarket, resolution, contract, bulgaria]
---

# Summary

This source provides the contract wording and explicit source-of-truth logic for the market. It states the election date, ranking logic, dissolution contingency for named coalitions, and fallback from consensus credible reporting to the Bulgarian Central Election Commission (CIK) if ambiguity exists.

## Key facts extracted

- Parliamentary elections are scheduled for **19 April 2026**.
- The market resolves to the party or coalition with the **third-greatest number of seats** in the next Bulgarian National Assembly election.
- Ties are broken first by **total valid votes**, then by **alphabetical order of listed party abbreviations**.
- If a named coalition dissolves, the market resolves based on the **constituent party within that coalition that held the largest number of seats before the election**.
- Resolution uses a **consensus of credible reporting**, with fallback to the **official results reported by Bulgaria's Central Election Commission (CIK)** if ambiguity exists.
- If results are not known definitively by **October 31, 2026, 11:59 PM ET**, the market resolves to **Other**.

## Evidence directly stated by source

- Direct contract language governs what counts for ranking and source-of-truth.
- The election date and reporting hierarchy are explicit.
- The coalition-dissolution clause is explicit and materially relevant because PP–DB is a coalition.

## What is uncertain

- The page does not itself provide evidence that PP–DB is currently likely to finish third.
- The page does not clarify how quickly credible reporting versus official certification may converge in practice.
- The page does not provide current market microstructure beyond the quoted current price from assignment context.

## Why this source may matter

This is the governing contract source for resolution mechanics. For a date-sensitive election ranking market, explicit interpretation of seat ranking, tie-breaks, and coalition treatment is necessary before comparing market price to public evidence.

## Possible impact on the question

This source does not answer whether PP–DB is likely to finish third, but it sharply defines what outcome must occur for the market to resolve Yes and confirms that official CIK results are the ultimate fallback authority if consensus reporting is ambiguous.

## Reliability notes

- Strong for contract interpretation because it is the market's own resolution text.
- Not independent evidence about Bulgarian electoral strength.
- Should be paired with at least one contextual election-strength source and, ideally, one source addressing the official election schedule / reporting framework.