# Response Notes

- Make clear that data comes from public NaverFinance/Npay Stock web pages and undocumented web endpoints, not an official API.
- For prices, include `localTradedAt`, market status, or response timestamp when present.
- Preserve Naver's strings for status values such as `PREOPEN`, `TRADING`, and `UNCHANGED`; add a short Korean/English explanation only if useful.
- For mobile integration payloads, avoid dumping everything. Summarize `totalInfos`, `dealTrendInfos`, `researches`, `industryCompareInfo`, `consensusInfo`, and `irScheduleInfo` separately.
- For PC table pages, skip spacer rows and rows without meaningful cells.
- For Wisereport, keep labels as displayed because accounting table structures vary by company and reporting basis.
- Never present Naver AI briefing or news snippets as verified facts; identify them as Naver-provided content.
