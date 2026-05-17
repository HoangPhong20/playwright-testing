from __future__ import annotations

import re


def parse_price_to_int(text: str) -> int:
    digits = re.sub(r"[^\d]", "", text or "")
    return int(digits) if digits else 0


def is_ascending(values: list[int]) -> bool:
    return values == sorted(values)


def is_descending(values: list[int]) -> bool:
    return values == sorted(values, reverse=True)
