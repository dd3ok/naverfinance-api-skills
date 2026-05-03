#!/usr/bin/env python3
"""Fetch public realtime quote polling data from NaverFinance."""

from __future__ import annotations

import argparse

from naverfinance_api import (
    POLLING_BASE_URL,
    add_output_argument,
    build_path,
    emit_output,
    normalize_stock_code,
    render_json,
    request_json_url,
)


def fetch_quotes(codes: list[str]) -> dict:
    normalized = [normalize_stock_code(code) for code in codes]
    query = "SERVICE_ITEM:" + ",".join(normalized)
    payload = request_json_url(
        POLLING_BASE_URL + build_path("/api/realtime", {"query": query}),
        referer="https://finance.naver.com/",
    )
    return {
        "source": "polling.finance.naver.com public realtime endpoint",
        "codes": normalized,
        "payload": payload,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--code",
        action="append",
        required=True,
        type=normalize_stock_code,
        help="Six-digit stock code. Repeat --code to fetch multiple quotes.",
    )
    add_output_argument(parser)
    args = parser.parse_args()
    emit_output(render_json(fetch_quotes(args.code)), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
