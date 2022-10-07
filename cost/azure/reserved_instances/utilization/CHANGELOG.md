# Changelog

## v2.7

- Added field for Instance Family to policy incident export
- Updated "Quantity Purchased" to reflect quantity purchased as of most recent month, rather than at start of term
- Fixed "Average Utilization Percentage" to reflect full 7/30 day period

## v2.6

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.5

- Added parameter for 7/30 day utilization lookback period
- Added details on reservation amounts:
  - the monthly cost of reservation
  - reservation amount paid to date
  - reservation amount remaining to be paid
- Added description to policy incident summary for total wasted spend on reservations
- Updated default_frequency to "weekly"
- Updated README.md to reflect new parameters added

## v2.4

- Updated README.md rightscale documentation links with docs.flexera documentation links

## v2.3

- Added default_frequency "daily"

## v2.2

- Adjusted check condition so RIs with 100 utilization are not incorrectly identified
- Added min(1) and max(100) value validation to param_utilization parameter

## v2.1

- Added Resource Table

## v2.0

- Added credential services

## v1.2

- Updated the metadata

## v1.0

- Initial release
