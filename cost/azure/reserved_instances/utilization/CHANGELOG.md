# Changelog

## v3.1.1

- Fixed Microsoft VM Size Flexibility URL which prevented the policy from completing without error.

## v3.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.0

- Updated policy to move away from Azure Legacy EA API endpoints and use the Azure Modern API endpoints due to EA Key deprecation in 2024
- Updated credential required for policy - it now requires an Azure Resource Manager credential due to EA Key deprecation in 2024
- Removed "Enrollment ID" parameter as no longer required
- Added "Reservation Expiration Date" field to policy incident

## v2.8

- Added fix for "Reservation ID" to reflect the most recent Reservation ID for each Reservation Order
- Updated escalation name to have correct prefix
- Added logic to handle reservation with null Utilization data such as Azure Databricks
- Updated README.md to correctly reflect 'param_utilization' parameter description

## v2.7

- Added field for Instance Family to policy incident export
- Updated "Quantity Purchased" to reflect quantity purchased as of most recent month, rather than at start of term
- Added fix for "Average Utilization Percentage" to reflect full 7/30 day period

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
