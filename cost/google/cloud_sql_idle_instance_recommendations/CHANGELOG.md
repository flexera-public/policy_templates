# Changelog

## v2.9

- Added `Lookback Period In Days` incident field.
- Added `Platform` incident field.

## v2.8

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v2.7

- Fix: Duplicated entries from incident report were removed.

## v2.6

- Modified filters, previously applied in code, now those are applied in request
- Support for empty "param_regions" value
- Adding request per minute to prevent quota error and disable sleep 10 seconds for each recommender call

## v2.5

- Changed provider to "Google" from "GCE" to match other Google policies

## v2.4

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- remove duplicate data fields for subscriptionID and subscriptionName

## v2.2

- added project name/id/number fields and moved account versions to end

## v2.1

- Fixed missing savings field

## v2.0

- Initial Release
