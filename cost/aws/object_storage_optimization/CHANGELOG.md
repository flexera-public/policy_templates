# Changelog

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to filter objects by multiple tag key:value pairs
- Added ability to filter objects/buckets by region
- Added option to automatically delete offending S3 objects
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export
- Policy no longer raises new escalations if object tags changed but nothing else has
- Streamlined code for better readability and faster execution

## v3.3

- Changed internal name of escalation code to ensure "Meta Policy" works as expected

## v3.2

- Optimized policy code to speed up execution.
- Tags for objects are not requested if the parameter `Exclude Tag` is empty.
- Added a new parameter `Bucket List`.

## v3.1

- Updated description of `Account Number` parameter

## v3.0

- Added logic required for "Meta Policy" use-cases

## v2.9

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.8

- Added default to aws_account_number parameter to enable existing API users.

## v2.7

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added default_frequency "daily"

## v2.4

- Modified escalation label and description for consistency

## v2.3

- Added AWS Account ID to resource table

## v2.2

- Adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.1

- modified constructing S3 bucket endpoint.

## v1.0

- initial release
