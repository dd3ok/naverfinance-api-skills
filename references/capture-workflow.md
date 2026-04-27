# Capture Workflow

1. Open the relevant public page without logging in.
2. Check page source or network requests for read-only endpoints.
3. Discard analytics, ads, auth, MY, WTS, order, open-talk, comments, broker, and personalization calls.
4. Copy only method, URL path, public query/body parameters, response format, and visible UI section.
5. Test with a simple stock/index code such as `005930`, `000660`, `KOSPI`, or `KOSDAQ`.
6. Add the endpoint to `references/api-catalog.md` only if it answers stock or market information questions without credentials.
7. Add or update a bundled script only when the endpoint is stable enough to be useful repeatedly.

For PC pages, remember that many finance pages are EUC-KR and many item iframe pages require a normal browser-like `User-Agent` and `Referer`.
