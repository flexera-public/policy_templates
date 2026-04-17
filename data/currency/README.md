# Currency Reference

This directory contains manually-maintained reference data for world currencies.

## Manually Maintained Files

### currency_reference.json

**Description:** A reference list of world currencies and their metadata, including symbols, number formatting conventions, and ISO 4217 codes. Used by policy templates and tooling that display or convert monetary values in user-facing output.

**Structure:** Object keyed by ISO 4217 currency code → currency metadata object.

| Field | Type | Description |
| --- | --- | --- |
| `symbol` | string | Currency symbol for display purposes, e.g. `"US$"` |
| `name` | string | Full English name of the currency, e.g. `"US Dollar"` |
| `symbol_native` | string | Native symbol used in the currency's home locale, e.g. `"$"` |
| `decimal_digits` | number | Number of decimal places used for this currency |
| `rounding` | number | Rounding increment; `0` for standard decimal rounding |
| `code` | string | ISO 4217 currency code (same as the top-level key), e.g. `"USD"` |
| `name_plural` | string | Plural form of the currency name, e.g. `"US dollars"` |
| `t_separator` | string | Thousands separator character used in this locale, e.g. `","` |

**Example:**

```json
{
  "USD": {
    "symbol": "US$",
    "name": "US Dollar",
    "symbol_native": "$",
    "decimal_digits": 2,
    "rounding": 0,
    "code": "USD",
    "name_plural": "US dollars",
    "t_separator": ","
  },
  "EUR": {
    "symbol": "€",
    "name": "Euro",
    "symbol_native": "€",
    "decimal_digits": 2,
    "rounding": 0,
    "code": "EUR",
    "name_plural": "euros",
    "t_separator": "."
  }
}
```
