# Changelog

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
