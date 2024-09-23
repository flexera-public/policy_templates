# Changelog

## v4.1.0

- Updated Azure API versions to provide more up to date and accurate results

## v4.0.0

- Recommendations can now be generated at the "Resource Group" scope

## v3.4.1

- Incident fields for `Subscription ID` and `Subscription Name` no longer show a specific Azure Subscription when providing Shared recommendations.

## v3.4

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.3

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.2

- Fixed issue where policy execution would fail due to 429 error from Azure API
- Added logic required for "Meta Policy" use-cases

## v3.1

- Fixed bug where policy would not filter recommendations by term

## v3.0

- Policy now automatically converts savings to local currency when appropriate
- Added exchange rate context to incident to allow user to revert currency conversion when needed
- Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
- Added ability to filter recommendations by region
- Several parameters altered to be more descriptive and intuitive to use
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential
- Policy now requires `Microsoft.Billing/billingAccounts/read` permission for Azure credential

## v2.17

- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v2.16

- Changed policy set from `Reserved Instance` to `Reserved Instances` to match other similar policies.
- Added `Scope` incident field.
- Added `Lookback Period` incident field.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v2.15

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard
- Modified incident output to facilitate scraping of incidents for Recommendations dashboard

## v2.14

- Fixed subscriptionName empty in the Incident

## v2.13

- Replaced the term **whitelist** with **allowed list**.

## v2.12

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.11

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.10

- changed subscriptionID and subscriptionName value to accountID and accountName

## v2.9

- Added the following attributes to policy output: instanceFlexibilityGroup, instanceFlexibilityRatio, normalizedSize, recommendedQuantityNormalized
- Fixed indentation to make consistent

## v2.8

- Added subscription name field

## v2.7

- Updated README.md rightscale documentation links with docs.flexera documentation links

## v2.6

- Updated policy to only pull from first subscription to avoid duplicate data. this will fix the shared repeating data

## v2.5

- Added subscription filter option and ability to specify Azure API endpoint

## v2.4

- Ignored: {"code":"400","message":"Cost management data is unavailable for subscription XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX. The offer MS-AZR-0243P is not supported."}
- Ignored: {"code":"404","message":"Cost Management supports only Enterprise Agreement, Web direct and Microsoft Customer Agreement offer types. Subscription XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX is not associated with a valid offer type."}

## v2.3

- Add option to include all Reservation types in one incident
- Add option to filter for Reservation term; 1 year or 3 year

## v2.2

- Support for all Reservation types: ['VirtualMachines', 'SQLDatabases', 'PostgreSQL', 'ManagedDisk', 'MySQL', 'RedHat', 'MariaDB', 'RedisCache', 'CosmosDB', 'SqlDataWarehouse', 'SUSELinux', 'AppService', 'BlockBlob', 'AzureDataExplorer', 'VMwareCloudSimple']
- Added support for Shared subscription reservations
- Prevent incident updates when data doesn't change
- This policy replaces the [older policy](../recommendations) that uses the Azure EA key which was deprecated

## v2.1

- Added default_frequency "daily"

## v2.0

- initial release
