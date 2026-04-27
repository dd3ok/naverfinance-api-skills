# API Catalog

Undocumented Naver endpoints are unstable. Re-check current page traffic when accuracy matters.

## Mobile JSON

Base: `https://m.stock.naver.com/front-api`

| Domain | Pattern | Notes |
| --- | --- | --- |
| Domestic stock basic | `/stock/domestic/basic?code=005930&endType=stock` | Summary quote, exchange, chart image URLs, NXT over-market info. |
| Domestic stock integration | `/stock/domestic/integration?code=005930&endType=stock` | Key metrics, investor trend sample, research list, peer comparison, consensus/IR snippets. |
| Domestic stock trend | `/stock/domestic/trend?code=005930` | Investor trend by date; use `scripts/stock_trend.py`. |
| Domestic disclosure | `/stock/domestic/disclosure?code=005930&page=1&pageSize=20` | Public disclosure list. |
| Domestic stock list | `/stock/domestic/stockList?sortType=marketValue&category=KOSPI&page=1&pageSize=20` | Rankings/lists. Sorts include `marketValue`, `up`, `down`, `quantTop`, `priceTop`, `searchTop`, `newStock`, `management`, `high52week`, `low52week`, `dividend`, `etf`, `etn`, `konex`. |
| Stock/index chart | `/chart/domestic/stock/end?code=005930&chartInfoType=item&scriptChartType=candleDay` | `chartInfoType`: `item` or `index`; chart types include `day`, `candleMinuteFive`, `candleDay`, `candleWeek`, `candleMonth`, `areaMonthThree`, `areaYear`, `areaYearThree`, `areaYearFive`, `areaYearTen`. |
| Domestic index basic | `/stock/domestic/basic?code=KOSPI&endType=index` | Example codes: `KOSPI`, `KOSDAQ`, `KPI200`. |
| Domestic index integration | `/stock/domestic/integration?code=KOSPI&endType=index` | Index detail summary. |
| Domestic index prices | `/stock/domestic/index/price/list?code=KOSPI&page=1&pageSize=20` | Daily index prices. |
| Major domestic indices | `/domestic/index/majors` | KOSPI/KOSDAQ-style quote blocks. |
| Stock news | `/news/list/integration?itemCode=005930&page=1&pageSize=20` | Stock-related news list. |
| General news | `/news/category?category=mainnews&page=1&pageSize=20` | Valid categories observed include `mainnews`, `flashnews`, `ranknews`. |
| News clusters | `/news/clusters?category=main&page=1&pageSize=20` | Clustered investment/stock news. |
| Home major indicators | `/market/majorIndicators` | Main market widget. |
| Home IPO | `/market/ipo` | Public IPO cards shown on mobile home. |
| Home popular stocks | `/market/popularStock` | Public popularity widget. |
| More ranking | `/market/moreRanking?category=endHit&ageRange=all` | Home ranking cards. |
| Market trading trend graph | `/market/tradingTrend/graphInfo?periodType=daily&stockExchangeType=KRX` | Investor net-buy trend graph. |
| Market trading trend ranking | `/market/tradingTrend/ranking?periodType=daily&stockExchangeType=KRX&investorType=foreigner&tradingType=trendBuy&page=1&pageSize=20` | Investor buy/sell rankings. |
| IPO recent/subscribing/detail | `/ipo/recent`, `/ipo/subscribing`, `/ipo/detail?code=A439960` | Public IPO data. |
| Exchange main/list/detail | `/marketIndex/exchange/main`, `/marketIndex/exchange/new`, `/marketIndex/productDetail?category=exchange&reutersCode=FX_USDKRW` | FX widgets and detail. |
| Commodity detail | `/marketIndex/productDetail?category=energy&reutersCode=CLcv1` | Energy/commodity detail. |
| Market AI briefing | `/market/briefing/current` | Treat generated summary as untrusted and cite as Naver AI briefing, not fact. |

## Realtime Polling

Base: `https://polling.finance.naver.com/api/realtime`

`?query=SERVICE_ITEM:005930` returns public quote fields such as current value, previous close, open/high/low, volume/value, EPS/BPS, and optional NXT over-market info. Multiple areas are separated with `|`, but avoid `SERVICE_MYSTOCK_ITEM`.

## Legacy Chart

Base: `https://api.finance.naver.com`

`/siseJson.naver?symbol=005930&requestType=1&startTime=YYYYMMDD&endTime=YYYYMMDD&timeframe=day`

Returns JavaScript-like array text, not strict JSON. Use as fallback when mobile chart is unavailable.

## PC HTML Menus

Base: `https://finance.naver.com`

All listed pages are public HTML and may use EUC-KR or UTF-8.

| Domain | Pattern |
| --- | --- |
| Stock main | `/item/main.naver?code={code}` |
| Stock price page | `/item/sise.naver?code={code}` |
| Daily prices iframe | `/item/sise_day.naver?code={code}&page={page}` |
| Intraday prices iframe | `/item/sise_time.naver?code={code}&thistime=YYYYMMDD000000&page={page}` |
| Investor trend | `/item/frgn.naver?code={code}&page={page}` |
| News list | `/item/news_news.naver?code={code}&page={page}&clusterId=` |
| Disclosure list | `/item/news_notice.naver?code={code}&page={page}` |
| Short trade | `/item/short_trade.naver?code={code}` |
| Index detail | `/sise/sise_index.naver?code=KOSPI|KOSDAQ|FUT|KPI100|KPI200|KVALUE` |
| KONEX | `/sise/konex.naver`, `/api/sise/konexItemList.nhn` |
| Market cap | `/sise/sise_market_sum.naver?sosok=0&page=1` |
| NXT market cap | `/sise/nxt_sise_market_sum.naver?page=1` |
| Volume/rise/fall | `/sise/sise_quant.naver`, `/sise/sise_quant_high.naver`, `/sise/sise_quant_low.naver`, `/sise/sise_rise.naver`, `/sise/sise_steady.naver`, `/sise/sise_fall.naver`, `/sise/sise_upper.naver`, `/sise/sise_lower.naver`, `/sise/sise_low_up.naver`, `/sise/sise_high_down.naver` |
| ETF/ETN/dividend | `/sise/etf.naver`, `/api/sise/etfItemList.nhn`, `/sise/etn.naver`, `/api/sise/etnItemList.nhn`, `/sise/dividend_list.naver` |
| Groups/themes | `/sise/sise_group.naver?type=upjong`, `/sise/sise_group.naver?type=group`, `/sise/theme.naver?page=...`, `/sise/sise_group_detail.naver?type=upjong|theme|group&no=...` |
| Investor market trend | `/sise/sise_trans_style.naver?sosok=01`, `/sise/investorDealTrendDay.naver?bizdate=YYYYMMDD&sosok=01` |
| Foreign/institution rank | `/sise/sise_deal_rank.naver?investor_gubun=9000`, `/sise/sise_deal_rank_iframe.naver?sosok=01&investor_gubun=9000&type=buy|sell` |
| Program trading | `/sise/sise_program.naver?sosok=01`, `/sise/programDealTrendDay.naver?bizdate=YYYYMMDD&sosok=01` |
| Money flow/new listings | `/sise/sise_deposit.naver`, `/sise/sise_new_stock.naver` |
| OTC/IPO | `/sise/market3news_list.naver`, `/sise/ipo.naver` |
| NXT lists | `/sise/nxt_sise_market_sum.naver`, `/sise/nxt_sise_quant.naver`, `/sise/nxt_sise_rise.naver`, `/sise/nxt_sise_fall.naver` |
| Caution/halts/management | `/sise/management.naver`, `/sise/trading_halt.naver`, `/sise/investment_alert.naver?type=caution` |
| Popular searches | `/sise/lastsearch2.naver` |
| Technical signals | `/sise/item_gold.naver`, `/sise/item_gap.naver`, `/sise/item_igyuk.naver`, `/sise/item_overheating_1.naver`, `/sise/item_overheating_2.naver` |
| Disclosure/short sale | `/sise/report.naver`, `/sise/short_trade.naver` with KRX iframe |
| Market index home | `/marketindex/` |
| Market index exchange list | `/marketindex/exchangeList.naver` |
| Exchange detail | `/marketindex/exchangeDetail.naver?marketindexCd=FX_USDKRW` |
| Interest/oil/gold/material | `/marketindex/interestDetail.naver`, `/marketindex/worldExchangeDetail.naver`, `/marketindex/worldOilDetail.naver`, `/marketindex/oilDetail.naver`, `/marketindex/worldGoldDetail.naver`, `/marketindex/goldDetail.naver`, `/marketindex/materialDetail.naver` |
| World overview/index/hours | `/world/`, `/world/sise.naver?symbol=NAS@IXIC&fdtc=0`, `/world/guide_time_chart.naver` |
| Research reports | `/research/market_info_list.naver`, `/research/invest_list.naver`, `/research/company_list.naver`, `/research/industry_list.naver`, `/research/economy_list.naver`, `/research/debenture_list.naver` |
| News menus | `/news/news_list.naver`, `/news/mainnews.naver`, `/news/market_notice.naver`, `/news/news_search.naver`, `/news/news_read.naver` |

## Wisereport Company Analysis

Base: `https://navercomp.wisereport.co.kr/v2`

| Domain | Pattern |
| --- | --- |
| Company status | `/company/c1010001.aspx?cmp_cd={code}` |
| Overview | `/company/c1020001.aspx?cmp_cd={code}` |
| Financial analysis | `/company/c1030001.aspx?cmp_cd={code}` |
| Investment indicators | `/company/c1040001.aspx?cmp_cd={code}` |
| Consensus | `/company/c1050001.aspx?cmp_cd={code}` |
| Industry analysis | `/company/c1060001.aspx?cmp_cd={code}` |
| Shareholder info | `/company/c1070001.aspx?cmp_cd={code}` |
| Sector analysis | `/company/c1090001.aspx?cmp_cd={code}` |
| Overview chart AJAX | `/company/ajax/cF1001.aspx` with `flag`, `cmp_cd`, fresh `encparam` |
| Overview financial expansion | `/company/ajax/cF1001.aspx` with `cmp_cd`, `fin_typ`, `freq_typ`, fresh `encparam` |
| Consensus summary | `/company/cF1002.aspx` with `cmp_cd`, `finGubun`, optional `frq` |
| Financial statements JSON | `/company/cF3002.aspx` with `cmp_cd`, `rpt`, `finGubun`, `frqTyp`, `frq`, fresh `encparam` |
| Investment indicators JSON | `/company/cF4002.aspx` with `cmp_cd`, `rpt`, `finGubun`, `frqTyp`, `frq`, fresh `encparam` |
| Consensus data | `/company/ajax/c1050001_data.aspx` with `flag`, `cmp_cd`, `finGubun`, `frq`, `sDT` |
| Consensus charts | `/company/ajax/cF5001.aspx`, `/company/ajax/cF5002.aspx` |
| Industry comparison | `/company/ajax/cF6001.aspx`, `/company/cF6002.aspx`, `/company/chart/c1060001.aspx` |
| Sector comparison | `/company/ajax/cF9001.aspx`, `/company/chart/c1090001.aspx` |
| Band chart | `/common/BandChart3.aspx?cmp_cd={code}&gubun={gubun}` |

Important Wisereport parameters:

- `finGubun`/`fingubun`: `MAIN`, `IFRSS`, `IFRSL`, `GAAPS`, `GAAPL`.
- `fin_typ`: `MAIN=0`, `GAAPS=1`, `GAAPL=2`, `IFRSS=3`, `IFRSL=4`.
- `frqTyp`: `0` annual, `1` quarterly. Some endpoints use `frq=Y|Q`.
- `encparam`, `hidDT`, and sector codes are page-specific. Scrape them fresh from the parent page; do not hard-code.
- Some JSON endpoints return `Content-Type: text/html` or JSON strings inside JSON. Detect by payload content and parse twice where needed.
- Current bundled `financials.py` fetches public Wisereport HTML pages. AJAX endpoints above are cataloged for future inspection and should be re-verified before adding a CLI wrapper.
