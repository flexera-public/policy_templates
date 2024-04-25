# Changelog

## v3.0.0

- Added support for new recommender: Idle Cloud SQL Instance
- Added support for new recommender: Overprovisioned Cloud SQL Instance
- Added support for new recommender: Idle GKE Cluster
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter results by project and by region via an allow list or a deny list
- Added additional context to incident description
- Added ability to report on several recommenders at once
- Policy now reports savings and converts it to local currency when appropriate
- Several parameters altered to be more descriptive and human-readable
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export for additional context
- Policy no longer raises new escalations if savings data changed but nothing else has
- Streamlined code for better readability and faster execution
- Policy now requires a Flexera credential
- Added logic required for "Meta Policy" use-cases

## v2.5

- Modified the number of GCP recommender API calls that can be done before waiting to prevent a quota limit error: 100 request per minute.

## v2.4

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added cost to incident output and ability to filter by projects

## v2.1

- Updating the short description

## v2.0

- Initial Release
