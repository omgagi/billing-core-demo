"""Invoice totals.

OUTPUT CONTRACT: Invoice.total_cents() and Invoice.tax_cents()
  total_cents = subtotal_cents + tax_cents
  tax_cents   = subtotal_cents * tax_rate_pct / 100, rounded to the NEAREST cent,
                halves up (finance rule: a customer is charged 199.5 cents as 200)

INPUT PARTITIONS:
  tax that lands on a whole cent       -> no rounding involved
  tax with a fractional part below .5  -> rounds down
  tax with a fractional part of .5+    -> rounds up
  zero tax rate                        -> total equals subtotal
"""
import unittest

from invoicing import Invoice, Line


class InvoiceTotals(unittest.TestCase):
    def test_subtotal_sums_lines(self):
        inv = Invoice([Line("widget", 2, 1500), Line("gadget", 1, 999)])
        self.assertEqual(inv.subtotal_cents(), 3999)

    def test_whole_cent_tax(self):
        inv = Invoice([Line("widget", 1, 10000)], tax_rate_pct=10)
        self.assertEqual(inv.total_cents(), 11000)

    def test_zero_tax_rate(self):
        inv = Invoice([Line("widget", 1, 1234)])
        self.assertEqual(inv.total_cents(), 1234)

    def test_tax_below_half_a_cent_rounds_down(self):
        # 10% of 1994 = 199.4 -> 199
        inv = Invoice([Line("widget", 1, 1994)], tax_rate_pct=10)
        self.assertEqual(inv.tax_cents(), 199)

    def test_tax_of_half_a_cent_or_more_rounds_up(self):
        # 10% of 1995 = 199.5 -> 200 (finance rounds halves up, never truncates)
        inv = Invoice([Line("widget", 1, 1995)], tax_rate_pct=10)
        self.assertEqual(inv.tax_cents(), 200)


if __name__ == "__main__":
    unittest.main()
