"""Tests for the tiny checkout calculation."""

import unittest

from checkout import calculate_checkout


class CalculateCheckoutTests(unittest.TestCase):
    def test_checkout_without_discount(self) -> None:
        result = calculate_checkout(2_000)

        self.assertEqual(result.subtotal_cents, 2_000)
        self.assertEqual(result.discount_cents, 0)
        self.assertEqual(result.total_cents, 2_000)

    def test_percentage_discount(self) -> None:
        result = calculate_checkout(10_000, "SAVE10")

        self.assertEqual(result.discount_cents, 1_000)
        self.assertEqual(result.total_cents, 9_000)

    def test_fixed_discount_below_subtotal(self) -> None:
        result = calculate_checkout(2_000, "TAKE5")

        self.assertEqual(result.discount_cents, 500)
        self.assertEqual(result.total_cents, 1_500)

    def test_fixed_discount_capped_at_subtotal(self) -> None:
        result = calculate_checkout(2_000, "VIP50")

        self.assertEqual(result.discount_cents, 2_000)
        self.assertEqual(result.total_cents, 0)
        self.assertEqual(
            result.subtotal_cents,
            result.discount_cents + result.total_cents,
        )

    def test_code_is_normalized(self) -> None:
        result = calculate_checkout(2_000, " save10 ")

        self.assertEqual(result.discount_cents, 200)
        self.assertEqual(result.total_cents, 1_800)

    def test_unknown_code_has_no_effect(self) -> None:
        result = calculate_checkout(2_000, "NOT-A-CODE")

        self.assertEqual(result.discount_cents, 0)
        self.assertEqual(result.total_cents, 2_000)

    def test_negative_subtotal_is_rejected(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "subtotal_cents must be non-negative",
        ):
            calculate_checkout(-1)


if __name__ == "__main__":
    unittest.main()
