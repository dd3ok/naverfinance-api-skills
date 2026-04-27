# 안전 규칙

## 허용 범위

- 로그인 없이 볼 수 있는 공개 read-only 종목, 지수, 차트, 뉴스, 공시, 랭킹, 시장지표, IPO, 기업분석 데이터.
- 공개 market widget 또는 종목/지수 상세 데이터를 반환하는 `m.stock.naver.com/front-api/...` endpoint.
- 인증 없이 볼 수 있는 `finance.naver.com` PC HTML table.
- 공개 quote polling용 `polling.finance.naver.com/api/realtime`.
- Naver 종목분석 iframe에서 연결되는 `navercomp.wisereport.co.kr` 페이지.

## 제외 범위

- Login, account, order, MY, holdings, portfolio, payment, certificate, WTS, broker landing, partner execution route.
- `/auth/userInfo`, `/setting/wtsList`, 사용자별 MY 페이지, 주문/deep-link broker 페이지.
- OpenTalk, comments, discussion boards, 글쓰기, 닉네임, 프로필 이미지, message stream.
- Raw HAR file, cookie, authorization header, token, storage state, session ID, account identifier, personal data, personalized response payload.
- 고빈도 polling, concurrent fan-out, 대량 scraping, 자동 재시도 loop, rate-limit bypass, anti-bot bypass, paywall bypass, login-wall bypass, access-control bypass.

## Capture 처리

- 가능하면 browser DevTools에서 header 없이 request URL만 복사합니다.
- HAR가 불가피하면 로컬에서만 확인하고 sensitive header와 cookie를 즉시 폐기합니다.
- 카탈로그에는 URL pattern, method, 공개 parameter, response shape, purpose만 남깁니다.
- credential이 필요하거나 user-specific data를 반환하는 endpoint는 중단합니다.
- HTTP 403, HTTP 429, challenge page, login redirect, 비정상 응답이 나오면 중단합니다. 다시 시도하기 전에 현재 공개 browser/page traffic에서 같은 데이터가 보이는지 확인합니다.
- 출력에는 이 데이터가 Naver가 지원하는 public developer API가 아니라 비공식 공개 web data임을 분명히 합니다.
