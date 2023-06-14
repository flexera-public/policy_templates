# Changelog

## v4.0

- Policy name changed to reference EC2 service directly
- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to configure how many days to consider CPU/memory statistics for
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to take automated actions to resize or delete resources
- Added ability to make recommendations based on maximum CPU/memory usage
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export
- Policy no longer raises new escalations if statistics or savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v3.1

- Fixed issue where savings would always be 0 if policy were executed at the end of the month.

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.0

- Initial release
