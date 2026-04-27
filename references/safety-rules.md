# Safety Rules

## Allowed

- Public read-only stock, index, chart, news, disclosure, ranking, market-indicator, IPO, and company-analysis data visible without login.
- `m.stock.naver.com/front-api/...` endpoints that return public market widgets or stock/index detail data.
- `finance.naver.com` PC HTML tables that are visible without authentication.
- `polling.finance.naver.com/api/realtime` for public quote polling.
- `navercomp.wisereport.co.kr` pages linked from Naver stock-analysis iframes.

## Excluded

- Login, account, order, MY, holdings, portfolio, payment, certificate, WTS, broker landing, or partner execution routes.
- `/auth/userInfo`, `/setting/wtsList`, user-specific MY pages, and all order/deep-link broker pages.
- OpenTalk, comments, discussion boards, post writing, nicknames, profile images, and message streams.
- Raw HAR files, cookies, tokens, storage state, session IDs, and personalized response payloads.

## Handling Captures

- Prefer browser DevTools request URLs copied without headers.
- If a HAR is unavoidable, inspect it locally and immediately discard sensitive headers and cookies.
- Catalog only URL pattern, method, public parameters, response shape, and purpose.
- Stop if the endpoint needs credentials or returns user-specific data.
