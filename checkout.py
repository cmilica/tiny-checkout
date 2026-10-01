"""Checkout total calculation used by the Week 4 training issue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class CheckoutResult:
    """Amounts reported by checkout, represented in integer cents."""

    subtotal_cents: int
    discount_cents: int
    total_cents: int


PERCENT_DISCOUNTS: Final = {
    "SAVE10": 10,
    "SAVE20": 20,
}

FIXED_DISCOUNTS: Final = {
    "TAKE5": 500,
    "VIP50": 5_000,
}


def calculate_checkout(
    subtotal_cents: int,
    discount_code: str | None = None,
) -> CheckoutResult:
    """Calculate the discount and final total for one checkout."""
    if subtotal_cents < 0:
        raise ValueError("subtotal_cents must be non-negative")

    code = (discount_code or "").strip().upper()

    if code in PERCENT_DISCOUNTS:
        discount_cents = subtotal_cents * PERCENT_DISCOUNTS[code] // 100
    else:
        discount_cents = min(FIXED_DISCOUNTS.get(code, 0), subtotal_cents)

    return CheckoutResult(
        subtotal_cents=subtotal_cents,
        discount_cents=discount_cents,
        total_cents=subtotal_cents - discount_cents,
    )
