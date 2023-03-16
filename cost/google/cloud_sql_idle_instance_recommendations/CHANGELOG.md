# Changelog

## v2.5

- Performance improved with next changes: Get only Google projects with "ACTIVE" lifecycle state, replace API to get SQL instances, replace "ds_sanitize_sql_instances" with filter "NOT settings.userLabels.[key]:[value]" in request to get SQL instances. Support for empty "param_regions" value.

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
