# Changelog

## v0.1.1

- Fixed idle threshold comparisons to use `<=` instead of `<` so instances at exactly the configured threshold percentage are correctly flagged as idle
- Fixed missing `ec2:DescribeInstanceStatus` permission in README; this permission is required for all action workflows to poll instance state
- Fixed `hash_exclude` blocks to remove non-exported fields that had no effect
- Added pagination to CloudWatch `ListMetrics` requests to avoid missing instances in large deployments

## v0.1.0

- Initial release
