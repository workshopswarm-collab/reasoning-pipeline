---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-context
entity: ethereum
topic: case-20260416-969f7c01 | variant-view
question: Will the price of Ethereum be above $2,200 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Secondary ETH price context checks
source_type: contextual market references
source_url: https://www.coindesk.com/price/ethereum ; https://coinmarketcap.com/currencies/ethereum/
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [variant-view finding, evidence map]
tags: [coindesk, coinmarketcap, context, cross-check]
---

# Summary

Secondary price references broadly matched the view that ETH was trading materially above 2200 during the research window. Search/fetch results showed Binance around 2317.93 and CoinDesk around 2317.18 at nearby capture times, providing a contextual cross-check that the Binance primary reading was not an obvious outlier.

## Key facts extracted

- Web search result for Binance ETH/USDT showed about 2317.93.
- Web search result for CoinDesk ETH price showed about 2317.18 at Apr. 15, 2026 4:13 am EDT.
- These values are directionally consistent with the direct Binance API spot check later in the run at 2352.52.

## Evidence directly stated by source

- CoinDesk snippet indicated ETH around 2317.18 as of Apr. 15, 2026, 4:13 am EDT.
- Search result for Binance ETH/USDT indicated around 2317.93.

## What is uncertain

- These are secondary or snippet-based contextual reads rather than full authoritative chart exports.
- Capture times differ, so small price differences are expected and not informative by themselves.

## Why this source may matter

These checks provide an additional verification pass appropriate for an extreme-probability market. They help confirm the primary exchange read was directionally consistent with broader market references.

## Possible impact on the question

The cross-checks modestly increase confidence in the Yes direction, but they do not eliminate exact-minute settlement risk or next-day volatility risk.

## Reliability notes

Useful as independent contextual confirmation, but lower authority than Binance for settlement because the contract is exchange-specific and minute-specific.