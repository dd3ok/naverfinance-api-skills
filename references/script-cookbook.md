# Script Cookbook

## Common Lookups

```bash
python3 scripts/stock_summary.py --code 005930
python3 scripts/quote.py --code 005930 --code 000660
python3 scripts/stock_chart.py --code 005930 --period day --start 20260420 --end 20260427
python3 scripts/stock_trend.py --code 005930 --limit 10
python3 scripts/news.py --code 005930 --kind stock --limit 5
python3 scripts/market_ranking.py --kind market-cap --market kospi --page 1 --limit 10
python3 scripts/market_ranking.py --kind konex --page 1 --limit 10
python3 scripts/market_ranking.py --kind upjong --page 1 --limit 10
python3 scripts/market_ranking.py --kind upjong --detail-no 264 --limit 10
python3 scripts/market_ranking.py --kind theme --page 2 --limit 10
python3 scripts/market_ranking.py --kind theme --detail-no 318 --limit 10
python3 scripts/market_ranking.py --kind group --page 1 --limit 10
python3 scripts/market_ranking.py --kind etf --page 1 --limit 10
python3 scripts/market_ranking.py --kind etn --page 1 --limit 10
python3 scripts/market_ranking.py --kind low-up --limit 10
python3 scripts/market_ranking.py --kind quant-high --limit 10
python3 scripts/market_ranking.py --kind investor-trend --market kospi --limit 10
python3 scripts/market_ranking.py --kind foreign-buy --market kospi --limit 10
python3 scripts/market_ranking.py --kind program-trend --market kospi --limit 10
python3 scripts/market_ranking.py --kind nxt-market-cap --limit 10
python3 scripts/market_ranking.py --kind popular-search --limit 10
python3 scripts/market_ranking.py --kind golden-cross --limit 10
python3 scripts/market_ranking.py --kind report
python3 scripts/market_ranking.py --kind short-trade
python3 scripts/indices.py --code KOSPI --include-chart --period day --start 20260420 --end 20260427
python3 scripts/indices.py --code KVALUE
python3 scripts/indices.py --code FX_USDKRW --limit 3
python3 scripts/indices.py --code FX_USDJPY --limit 3
python3 scripts/indices.py --code IRR_CD91 --limit 3
python3 scripts/indices.py --code CMDT_GC --limit 3
python3 scripts/indices.py --code GOLD_KRX --limit 3
python3 scripts/world.py --kind overview --limit 5
python3 scripts/world.py --kind index --symbol nasdaq --limit 5
python3 scripts/world.py --kind hours --limit 10
python3 scripts/marketindex.py --kind overview --limit 5
python3 scripts/marketindex.py --kind exchange-list --limit 10
python3 scripts/marketindex.py --kind detail --code FX_USDKRW --limit 3
python3 scripts/research.py --kind company --page 1 --limit 10
python3 scripts/research.py --kind economy --page 1 --limit 10
python3 scripts/news.py --kind flash --page 1 --limit 10
python3 scripts/news.py --kind main --page 1 --limit 10
python3 scripts/news.py --kind notice --page 1 --limit 10
python3 scripts/news.py --kind search --query 삼성전자 --page 1 --limit 10
python3 scripts/financials.py --code 005930 --kind overview
```

## Output

All scripts default to JSON. Use `--output path.json` to write output to a file.

## Market Ranking Kinds

`konex`, `market-cap`, `volume`, `quant-high`, `quant-low`, `rise`, `fall`, `steady`, `upper`, `lower`, `low-up`, `high-down`, `etf`, `etn`, `dividend`, `foreign-hold`, `theme`, `upjong`, `group`, `investor-trend`, `foreign-buy`, `foreign-sell`, `institution-buy`, `institution-sell`, `program-trend`, `deposit`, `new-stock`, `market3`, `ipo`, `nxt-market-cap`, `nxt-volume`, `nxt-rise`, `nxt-fall`, `management`, `trading-halt`, `investment-alert`, `popular-search`, `golden-cross`, `gap-up`, `disparity-overheat`, `sentiment-overheat`, `relative-strength-overheat`, `report`, `short-trade`.

Use `--page N` for list pages. For `theme`, `upjong`, and `group`, list rows include `detailNo` and `detailUrl`; pass `--detail-no <no>` with the same `--kind` to fetch related stocks from `sise_group_detail.naver`.

`report` returns public disclosure tab links. `short-trade` returns the KRX iframe URL embedded by Naver because the detailed short-selling table is served by KRX inside the page.

## World, Market Index, Research, News

- `world.py --kind overview|index|hours`; common symbols include `nasdaq`, `dow`, `sp500`, `nikkei225`, or raw symbols like `NAS@IXIC`.
- `marketindex.py --kind overview|exchange-list|detail`; detail codes include `FX_USDKRW`, `FX_USDJPY`, `OIL_CL`, `OIL_GSL`, `CMDT_GC`, `GOLD_KRX`, `IRR_CD91`, and similar Naver marketindex codes.
- `research.py --kind market-info|invest|company|industry|economy|debenture`.
- `news.py --kind flash|main|market|analysis|world|bond|memo|fx|rank|photo|tv|notice|search`; `stock` and `disclosure` still require `--code`, and `search` requires `--query`.

## Date Formats

- Mobile chart endpoints use `YYYYMMDD0000`.
- Legacy `siseJson` uses `YYYYMMDD`.
- Bundled chart CLIs accept date arguments as `YYYYMMDD`.
- PC pages often display dates as `YYYY.MM.DD`.
