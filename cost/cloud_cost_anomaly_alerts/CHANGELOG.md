# Changelog

## v.2.5

- added a filter for multiple values on same dimension, such as "Cloud Vendor Account Name=Account1,Account2,Account3"

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
