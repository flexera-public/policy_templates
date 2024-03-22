# Changelog

## v4.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v4.0

- Added support for regex when filtering resources by label

## v3.2

- Fixed issue where currency conversion would sometimes not work as expected.

## v3.1

- Added ability to filter by how long a disk has been detached

## v3.0

- Policy now requires a Flexera credential
- Policy now converts savings to local currency when appropriate
- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Removed ability to filter by zone; filtering by region is now supported
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter resources by project and by region via an allow list or a deny list
- Added ability to filter resources by multiple label key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if savings data changed but nothing else has
- Streamlined code for better readability and faster execution
- Added logic required for "Meta Policy" use-cases

## v2.10

- Updated policy README file with a deeper explanation of how the GCP recommender works and the roles required to use it.

## v2.9

- Modified the number of GCP recommender API calls that can be done before waiting to prevent a quota limit error: 100 request per minute.

## v2.8

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v2.7

- Fix: Duplicated entries from incident report were removed.

## v2.6

- Fixed error getting zone name as region
- Adding missing fields for policy logs
- Filtering data before requests to avoid unnecessary requests to `/aggregated/disks` and `/recommenders/google.compute.disk.IdleResourceRecommender/recommendations` APIs

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
