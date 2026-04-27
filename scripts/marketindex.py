#!/usr/bin/env python3
"""Fetch public NaverFinance market-index menu data."""

from __future__ import annotations

import argparse
import re

from indices import fetch_market_index
from naverfinance_api import (
    add_limit_argument,
    add_output_argument,
    clean_cell,
    emit_output,
    extract_tables,
    pc_text,
    render_json,
    strip_tags,
    table_to_records,
)


def fetch_marketindex(kind: str, *, code: str | None, page: int, limit: int) -> dict:
    if kind == "overview":
        html = pc_text("/marketindex/")
        return {
            "source": "finance.naver.com public marketindex page",
            "kind": kind,
            "marketIndexes": _extract_links(html, "/marketindex/")[:limit] if limit else _extract_links(html, "/marketindex/"),
            "news": _extract_links(html, "/news/news_read.naver")[:limit] if limit else _extract_links(html, "/news/news_read.naver"),
            "research": _extract_links(html, "/research/")[:limit] if limit else _extract_links(html, "/research/"),
        }
    if kind == "exchange-list":
        return _fetch_tables("/marketindex/exchangeList.naver", {}, kind=kind, page=page, limit=limit)
    if not code:
        raise SystemExit("--code is required for --kind detail")
    return fetch_market_index(code, limit=limit)


def _fetch_tables(path: str, params: dict, *, kind: str, page: int, limit: int) -> dict:
    html = pc_text(path, params)
    tables = []
    for table in extract_tables(html):
        records = _clean_records(table_to_records(table["rows"]))
        if records:
            tables.append(
                {
                    "summary": table["attrs"].get("summary", ""),
                    "class": table["attrs"].get("class", ""),
                    "rows": records[:limit] if limit else records,
                }
            )
    return {"source": "finance.naver.com public marketindex HTML table", "kind": kind, "page": page, "tables": tables[:limit] if limit else tables}


def _clean_records(records: list[dict[str, str]]) -> list[dict[str, str]]:
    return [record for record in records if any(re.search(r"\d", value) for value in record.values())]


def _extract_links(html: str, contains: str) -> list[dict[str, str]]:
    links = []
    seen = set()
    for href, body in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, flags=re.S):
        if contains not in href:
            continue
        label = clean_cell(strip_tags(body))
        if not label or (label, href) in seen:
            continue
        seen.add((label, href))
        links.append({"label": label, "url": href})
    return links


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["overview", "exchange-list", "detail"], default="overview")
    parser.add_argument("--code", help="Market index code, e.g. FX_USDKRW, FX_USDJPY, OIL_CL, CMDT_GC, IRR_CD91")
    parser.add_argument("--page", type=int, default=1)
    add_limit_argument(parser, default=10)
    add_output_argument(parser)
    args = parser.parse_args()
    emit_output(render_json(fetch_marketindex(args.kind, code=args.code, page=args.page, limit=args.limit)), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
