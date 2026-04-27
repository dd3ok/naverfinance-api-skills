#!/usr/bin/env python3
"""Fetch a compact public Naver stock summary."""

from __future__ import annotations

import argparse

from naverfinance_api import (
    add_limit_argument,
    add_output_argument,
    emit_output,
    front_json,
    normalize_stock_code,
    render_json,
)


def fetch_summary(code: str, *, limit: int) -> dict:
    code = normalize_stock_code(code)
    basic = front_json(
        "/stock/domestic/basic",
        {"code": code, "endType": "stock"},
        referer_path=f"/domestic/stock/{code}/total",
    )
    integration = front_json(
        "/stock/domestic/integration",
        {"code": code, "endType": "stock"},
        referer_path=f"/domestic/stock/{code}/total",
    )
    return {
        "source": "m.stock.naver.com public JSON",
        "code": code,
        "basic": {
            key: basic.get(key)
            for key in [
                "stockName",
                "stockExchangeName",
                "closePrice",
                "compareToPreviousClosePrice",
                "compareToPreviousPrice",
                "fluctuationsRatio",
                "marketStatus",
                "localTradedAt",
                "delayTimeName",
                "overMarketPriceInfo",
            ]
            if key in basic
        },
        "totalInfos": integration.get("totalInfos", []),
        "dealTrendInfos": integration.get("dealTrendInfos", [])[:limit],
        "researches": integration.get("researches", [])[:limit],
        "industryCompareInfo": integration.get("industryCompareInfo", [])[:limit],
        "consensusInfo": integration.get("consensusInfo"),
        "irScheduleInfo": integration.get("irScheduleInfo"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--code", required=True, type=normalize_stock_code)
    add_limit_argument(parser, default=5)
    add_output_argument(parser)
    args = parser.parse_args()
    emit_output(render_json(fetch_summary(args.code, limit=args.limit)), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
