# Changelog

## v2.13.1

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v2.13

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v2.12

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v2.11

- Updated policy README file with a deeper explanation of how the GCP recommender works and the roles required to use it.

## v2.10

- Modified the number of GCP recommender API calls that can be done before waiting to prevent a quota limit error: 100 request per minute.

## v2.9

- Added `Lookback Period In Days` incident field.

## v2.8

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard
- Updated incident export to facilitate scraping of incidents for Recommendations dashboard

## v2.7

- Fix: Duplicated entries from incident report were removed.

## v2.6

- Fixed the values shown at `cpuMaximum`, `cpuMinimum` and `cpuAverage`:

At version 2.5 we changed the way we calculated the CPU utilization, we retrieved the average of utilization of each day and then we selected the maximum average as the maximum and the minimum average as the minimum, now we show the actual maximum and minimum of the CPU utilization thanks to a change in our GCP MQL query.

## v2.5

- Modified to make this policy run faster by using aggregated GCP API endpoints.

## v2.4

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- remove duplicate data fields for subscriptionID and subscriptionName

## v2.2

- added project name/id/number fields and moved account versions to end

## v2.1

- Fixed missing savings field

## v2.0

- Initial Release
