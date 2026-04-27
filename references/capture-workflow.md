# Capture Workflow

1. 로그인하지 않은 상태에서 관련 공개 페이지를 엽니다.
2. page source 또는 network request에서 read-only endpoint를 확인합니다.
3. analytics, ads, auth, MY, WTS, order, open-talk, comments, broker, personalization call은 버립니다.
4. method, URL path, 공개 query/body parameter, response format, visible UI section만 복사합니다.
5. `005930`, `000660`, `KOSPI`, `KOSDAQ` 같은 단순한 종목/지수 code로 테스트합니다.
6. credential 없이 주식 또는 시장 정보 질문에 답할 수 있을 때만 endpoint를 `references/api-catalog.md`에 추가합니다.
7. 반복적으로 유용할 만큼 안정적인 endpoint일 때만 bundled script를 추가하거나 갱신합니다.

PC page는 EUC-KR인 경우가 많고, 많은 종목 iframe page는 일반 browser와 비슷한 `User-Agent`와 `Referer`를 요구합니다.
