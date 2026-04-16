---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260413-64e915de | variant-view
question: Will Ethereum reach $2,400 April 13-19?
driver: liquidity
date_created: 2026-04-13
source_name: Assignment contract metadata and primary market page URL
source_type: market metadata / contract context
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [liquidity, macro]
upstream_inputs: []
downstream_uses: []
tags: [contract, resolution, market-metadata, ethereum]
---

# Summary

The assignment metadata establishes the exact contract under study, current market price of 0.905, and the primary Polymarket event URL. This is the governing source for what question is being answered, though not by itself enough to verify detailed settlement mechanics because the live page was not fetched successfully in-run.

## Key facts extracted

- Market question: Will Ethereum reach $2,400 April 13-19?
- Current market price supplied in assignment metadata: 0.905, implying about 90.5% probability.
- Resolution window closes at 2026-04-20T00:00:00-04:00.
- Primary market URL given: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19

## Evidence directly stated by source

- Exact title, probability proxy, timing window, and market URL from assignment metadata.

## What is uncertain

- Detailed settlement language and exchange/source-of-truth rules on the live page were not independently fetched because the endpoint returned 403 during this run.
- The assignment says the primary market URL is the governing market surface, but it does not itself restate the full settlement rule text.

## Why this source may matter

It defines the actual contract and baseline market probability that the finding must assess. Without this metadata, price-action evidence would lack contract context.

## Possible impact on the question

This source anchors the consensus view at an extreme probability and therefore raises the verification bar. It also highlights a source-of-truth ambiguity that should keep confidence from becoming absolute.

## Reliability notes

Assignment metadata is authoritative for this run’s scope and baseline inputs. It is highly relevant for contract framing but only medium-complete for detailed settlement mechanics because the underlying page contents were not directly inspected in-run.