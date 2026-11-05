# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a shipping quote
in dollars. Zones are `local` and `regional`; weights must be positive.

| Service    | Local base | Regional base | Surcharge |
|------------|-----------|---------------|-----------|
| `standard` | $5.00     | $8.00         | –         |
| `express`  | $5.00     | $8.00         | +$7.00    |

All services add $1.50 per kilogram on top of the base and any surcharge. An
unknown zone or service raises `ValueError`.

### CLI

The command-line entry point prints a quote for an order:

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
python -m warehouse.cli 2 local                    # → $8.00  (standard)
python -m warehouse.cli 2 local --service express  # → $15.00 (express)
```
