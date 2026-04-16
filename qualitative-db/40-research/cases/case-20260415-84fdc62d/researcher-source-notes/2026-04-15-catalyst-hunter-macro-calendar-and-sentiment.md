---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: macro
subdomain: crypto-macro
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Federal Reserve FOMC calendar, BLS CPI release schedule, Alternative.me Fear & Greed, Investing calendar
source_type: mixed-primary-context
source_url: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [catalyst-hunter.md, catalyst-hunter.sidecar.json, catalyst-hunter.md#key-assumptions]
tags: [macro-calendar, fomc, cpi, sentiment, catalyst-timing]
---

# Summary
The major scheduled U.S. macro catalysts that most often jolt BTC are not packed into the narrow April 15-20 window. BLS shows March CPI was released on April 10, already before this research date. The Federal Reserve calendar shows the next 2026 FOMC meeting is April 28-29, after market resolution. Meanwhile, Alternative.me showed crypto sentiment at `23` (`Extreme Fear`), which is a disconfirming contextual signal because it implies fragile risk appetite despite BTC remaining above $70k.

## Key facts extracted
- BLS CPI schedule lists `March 2026 CPI` release on `Apr. 10, 2026 at 08:30 AM`.
- Federal Reserve calendar lists next FOMC meeting on `Apr. 28-29, 2026`, after this April 20 market resolves.
- Alternative.me Fear and Greed Index on 2026-04-15 showed `23` / `Extreme Fear`.
- Investing.com calendar for 2026-04-15 showed ongoing macro speakers and routine data flow, but no obvious single scheduled event between now and April 20 comparable to CPI or an FOMC decision.

## Evidence directly stated by source
- Fed: `2026 FOMC Meetings ... April 28-29`.
- BLS: `March 2026 ... Apr. 10, 2026 08:30 AM`.
- Alternative.me API: `value 23`, `value_classification Extreme Fear`.

## What is uncertain
- This note does not rule out unscheduled catalysts such as regulatory headlines, geopolitical stress, or exchange-specific disruptions.
- Investing.com is contextual rather than authoritative for every event on the calendar.
- Sentiment readings can stay bearish while price stays elevated or rises.

## Why this source may matter
For a five-day horizon, catalyst timing matters heavily. Absence of a near-term scheduled macro shock supports a base case of drift/hold rather than forced repricing, while the fear reading flags fragility if an unscheduled negative catalyst hits.

## Possible impact on the question
This source mix modestly supports Yes by showing that the biggest routine macro catalysts are mostly behind or after the contract window. But it also identifies the main disconfirming mechanism: unscheduled risk-off shocks could matter more than the routine calendar because sentiment is weak.

## Reliability notes
Fed and BLS are primary for schedule timing and therefore strong on the catalyst-calendar question. Alternative.me is secondary/contextual and should not be overweighted, but it is useful as an independent mood check that sharpens the downside-tail discussion.
