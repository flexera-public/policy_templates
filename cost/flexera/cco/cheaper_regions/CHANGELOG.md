# Changelog

## v2.4.0

- Updated list of cheaper regions for Azure and AWS vendors.

## v2.3

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v2.2

- Updated description to account for new file path in Github repository

## v2.1

- added vendor type for Azure CSP's

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.14

- Use provided keyword for Optima endpoint

## v1.13

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.12

- added Google and AzureMCA expression blobs for filters

## v1.11

- Added check that AWS account array is not empty before assigning it

## v1.10

- Modified escalation label and description for consistency

## v1.9

- Updating path for ds_cloud_vendor_accounts

## v1.8

- adding incident resource table

## v1.7

- Updated the metadata

## v1.6

- fix link to README

## v1.5

- removed tag_instance_name

## v1.4

- Adding in resource_id so it easy to find resource

## v1.3

- Fixing cheaper region billing center

## v1.2

- Using instance data only to calculate cheaper regions to get closer to matching recommendations.

## v1.1

- Changing Azure to Cheaper Region Recommendations

## v1.0

- initial release
