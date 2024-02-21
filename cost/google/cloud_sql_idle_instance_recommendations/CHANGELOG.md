# Changelog

## v4.0

- Added support for regex when filtering resources by label

## v3.0

- Policy now requires a Flexera credential
- Policy now converts savings to local currency when appropriate
- Several parameters altered to be more descriptive and human-readable
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter resources by project and by region via an allow list or a deny list
- Added ability to filter resources by multiple label key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if savings data changed but nothing else has
- Added ability to stop or delete Cloud SQL instances from policy/incident
- Streamlined code for better readability and faster execution
- Added logic required for "Meta Policy" use-cases

## v2.11

- Fixed the method used to match recommendations with the SQL instances introduced at v2.6

## v2.10

- Updated policy README file with a deeper explanation of how the GCP recommender works and the roles required to use it.

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
