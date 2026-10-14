"""Invoice totals for the billing service. All money is integer cents."""
from dataclasses import dataclass, field


@dataclass
class Line:
    description: str
    quantity: int
    unit_price_cents: int

    def subtotal_cents(self) -> int:
        return self.quantity * self.unit_price_cents


@dataclass
class Invoice:
    lines: list = field(default_factory=list)
    tax_rate_pct: int = 0

    def subtotal_cents(self) -> int:
        return sum(line.subtotal_cents() for line in self.lines)

    def tax_cents(self) -> int:
        # Round to the nearest cent, halves up (finance rule); never truncate.
        return (self.subtotal_cents() * self.tax_rate_pct + 50) // 100

    def total_cents(self) -> int:
        return self.subtotal_cents() + self.tax_cents()
