#!/usr/bin/env python3
"""Fetch public NaverFinance world-market menu data."""

from __future__ import annotations

import argparse
import re

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


WORLD_SYMBOLS = {
    "dow": "DJI@DJI",
    "nikkei225": "NII@NI225",
    "ftse100": "LNS@FTSE100",
    "nasdaq": "NAS@IXIC",
    "shanghai": "SHS@000001",
    "cac40": "PAS@CAC40",
    "sp500": "SPI@SPX",
    "hangseng": "HSI@HSI",
    "dax": "XTR@DAX30",
}


def fetch_world(kind: str, *, symbol: str | None, page: int, limit: int) -> dict:
    if kind == "overview":
        html = pc_text("/world/")
        return {
            "source": "finance.naver.com public world page",
            "kind": kind,
            "indices": _extract_links(html, "/world/sise.naver")[:limit] if limit else _extract_links(html, "/world/sise.naver"),
            "news": _extract_links(html, "/news/news_read.naver")[:limit] if limit else _extract_links(html, "/news/news_read.naver"),
        }
    if kind == "hours":
        return _fetch_tables("/world/guide_time_chart.naver", {}, kind=kind, page=page, limit=limit)
    resolved = WORLD_SYMBOLS.get(symbol or "", symbol)
    if not resolved:
        raise SystemExit("--symbol is required for --kind index")
    return _fetch_tables("/world/sise.naver", {"symbol": resolved, "fdtc": 0, "page": page}, kind=kind, page=page, limit=limit)


def _fetch_tables(path: str, params: dict, *, kind: str, page: int, limit: int) -> dict:
    html = pc_text(path, params)
    tables = []
    for table in extract_tables(html):
        records = table_to_records(table["rows"])
        if records:
            tables.append(
                {
                    "summary": table["attrs"].get("summary", ""),
                    "class": table["attrs"].get("class", ""),
                    "rows": records[:limit] if limit else records,
                }
            )
    return {"source": "finance.naver.com public world HTML table", "kind": kind, "page": page, "tables": tables[:limit] if limit else tables}


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
    parser.add_argument("--kind", choices=["overview", "index", "hours"], default="overview")
    parser.add_argument("--symbol", help="World index alias or symbol, e.g. nasdaq or NAS@IXIC")
    parser.add_argument("--page", type=int, default=1)
    add_limit_argument(parser, default=10)
    add_output_argument(parser)
    args = parser.parse_args()
    emit_output(render_json(fetch_world(args.kind, symbol=args.symbol, page=args.page, limit=args.limit)), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
