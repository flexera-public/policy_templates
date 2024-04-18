# Changelog

## v3.4

- Fixed issue where filter would not work correctly if `Month` was selected for the `Billing Term` parameter.

## v3.3

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v3.2

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.1

- Updated description to account for new file path in Github repository

## v3.0

- Added ability to specify custom dimensions for the graph in the report
- Added ability to filter costs in report by any user-specified dimension
- Improved incident output for readability and removed references to Optima
- Incident table now shows the raw data used to create the graph in the report
- Streamlined code for better readability and faster execution

## v2.1

- Fixed issue with incorrectly-rendered graph when selecting "Week" for the Billing Term parameter

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.26

- URIEncode all the image-charts options

## v1.25

- Now using OAuth2 credentials instead of the built-in Rightscale authentication.

## v1.24

- Fixed issue with top 10 cost categories when there is no data yet for current month.

## v1.23

- Fixed markdown block.

## v1.22

- Modified escalation label and description for consistency
- Added incident resource table

## v1.21

- Added "Billing Centers" as a reportable dimension

## v1.20

- Fixed date value issue.

## v1.9

- Fix for Bug Dimension Information Missing for DAY and WEEK.
- Added default_frequency "monthly"

## v1.8

- Provided option to display chart with different granularity.

## v1.7

- Added tenancy "single" in metadata

## v1.6

- added "Resource Group", "Cloud Vendor", "Cloud Vendor Account", and "Cloud Vendor Account Name" as a dimensions
- added support to report on child Billing Centers
- forced chart legend to bottom of chart
- fixed the billing data api call that was leaving off a days worth of costs
- Added currency symbol support
- Added thousands separator support based on currency

## v1.5

- added the ability to select any "common" dimension for the chart image
- changed the chart image to only show the "top 10" values for the current month, and group the rest of the data into "Other"

## v1.4

- added chart with previous 6 months utilization, based on [category](https://docs.rightscale.com/optima/reference/rightscale_dimensions.html#category)

## v1.3

- allow user to select all billing centers
- allow user to enter billing center names

## v1.2

- update date calculation logic in current week datasource and current month datasource
- update summary_template and detail_template with org details

## v1.1

- update short and long long_description

## v1.0

- initial release
