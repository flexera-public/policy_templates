# Changelog

## v3.8.0

- Added `Excluded Cost Anomalies` parameter to allow user to add filters to exclude certain costs from anomaly reporting.

## v3.7.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.7.1

- Fixed bug when sending request to get the anomalies report that caused the policy to fail due to a bad request (400) error.

## v3.7.0

- Added `Minimum Period Spend Variance` parameter to optionally limit results based on amount of variance
- Added `Anomalies To Report` parameter to optionally limit results based on whether the anomaly is upward or downward
- Added `Variance From Average` field to incident table containing the difference (absolute value) between the total cost and the moving average

## v3.6

- Fixed bug where incident link was redirecting to wrong url

## v3.5

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v3.4

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.3

- Updated description to account for new file path in Github repository

## v3.2

- Fixed bug where incident showed dimensions from column `Grouping Dimensions` in random order

## v3.1

- Fixed bug where incident link would render incorrectly if spaces were present in filter value

## v3.0

- Link to Flexera One Cloud Cost Anomalies page now includes filters
- Incident for invalid dimensions now includes list of valid dimensions
- Improved text formatting and presentation of incidents
- Incident now includes currency
- Streamlined code for better readability and faster execution

## v2.5

- now users can use `Billing Centers` or `billing_center_id` value for parameter `Cost Anomaly Dimensions`

## v2.4

- added a filter for dimensions where the user wishes to filter by key pair values, such as Service=AmazonEC2
- added an input list for a mix of dimensions
- if at least one invalid dimension is entered by the user, the policy will fail, resulting in an email to you about the invalid dimension

## v2.3

- changed URL link to Cost Anomalies report, now it's constructed dynamically based on detected shard

## v2.2

- changed cost metric map key from api call value to more readable value

## v2.1

- changed parameter value for dimensions from "Cloud Vendor Account Name" to "Cloud Vendor Account"
- removed parameter dimension "Operating System" and removed mapping for api call
- changed name from Cloud Cost Anomalies to Cloud Cost Anomaly Alerts

## v2.0

- initial release
