---
type: source_note
case_key: case-20260414-1b10f4b2
dispatch_id: dispatch-case-20260414-1b10f4b2-20260414T201759Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: resolution mechanics and macro calendar
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 ET on 2026-04-20 above 68000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket rules page; Federal Reserve FOMC calendar; BLS CPI schedule
source_type: mixed_primary_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-1b10f4b2/researcher-analyses/2026-04-14/dispatch-case-20260414-1b10f4b2-20260414T201759Z/personas/catalyst-hunter.md]
tags: [source-note, resolution, timezone, catalysts, macro-calendar]
---

# Summary

This note captures the contract mechanics and the most obvious scheduled macro catalysts that could still move BTC before the market resolves.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT **1-minute candle for 12:00 ET on April 20, 2026**, using the candle's final **Close** price.
- The contract is specifically about **Binance BTC/USDT**, not other exchanges or pairs.
- 12:00 ET on 2026-04-20 converts to **16:00 UTC** because New York is on EDT.
- The Federal Reserve's 2026 FOMC calendar shows the next scheduled meeting is **April 28-29, 2026**, which is **after** this market resolves.
- The BLS CPI release schedule shows the **March 2026 CPI** release occurred on **April 10, 2026 at 08:30 AM**; the next CPI release for April data is **May 12, 2026**, also after resolution.

## Evidence directly stated by source

- Polymarket rules: resolve Yes if the Binance 1-minute BTC/USDT candle at 12:00 ET has a final close above 68,000.
- Fed calendar: no scheduled FOMC decision occurs between April 14 and April 20.
- BLS schedule: no CPI release occurs between April 14 and April 20.

## What is uncertain

- Whether unscheduled macro, geopolitical, or crypto-specific news arrives before April 20.
- Whether Binance front-end display exactly matches API-delivered candle data presentation in edge cases, although the contract source-of-truth names Binance directly.

## Why this source may matter

These sources narrow the catalyst window. They imply no major scheduled US macro event of the usual highest BTC-moving class (FOMC decision or CPI release) sits inside the remaining life of the market, so the threshold is mostly exposed to market drift and unscheduled news rather than a known hard catalyst.

## Possible impact on the question

The absence of a major scheduled macro catalyst before resolution makes it easier to treat the market as a short-horizon question about whether BTC can simply stay above 68k for six more days rather than needing a new repricing event to get there.

## Reliability notes

- Polymarket rules are the governing contract description but still rely on Binance as the underlying source of truth.
- Fed and BLS are official primary calendar sources for major US macro events.
- Independence is medium: these sources answer different parts of the question rather than corroborating the same price fact.