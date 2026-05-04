# Changelog

## v0.1.1

- Fixed an issue where instances would never receive underutilized recommendations when the `cloudwatch:ListMetrics` permission is denied (e.g., by an AWS SCP). Memory metrics are now queried for all instances using platform-appropriate CWAgent dimensions as a fallback, matching the behavior of the original template. Instances without CWAgent installed will still have no memory data returned and will continue to be skipped for rightsizing.

## v0.1.0

- Initial release
