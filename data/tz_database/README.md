# Timezone List

This directory contains manually-maintained timezone reference data.

## Manually Maintained Files

### timezones_list.json

**Description:** A reference list of all [tz database](https://en.wikipedia.org/wiki/Tz_database) (IANA) timezones, mapping URL-safe slug keys to their standard IANA timezone identifiers. Used by policy templates that present timezone selection parameters to users, converting the URL-safe key back to the standard IANA name for use with time zone APIs and libraries.

**Structure:** Object keyed by URL-safe timezone slug → IANA timezone identifier string. The key is derived from the IANA name by converting to lowercase and replacing `/` and `_` with `-`. The value is the canonical IANA name as used in the tz database.

**Example:**

```json
{
  "africa-abidjan": "Africa/Abidjan",
  "africa-accra": "Africa/Accra",
  "america-new_york": "America/New_York",
  "america-los_angeles": "America/Los_Angeles",
  "europe-london": "Europe/London",
  "asia-tokyo": "Asia/Tokyo"
}
```
