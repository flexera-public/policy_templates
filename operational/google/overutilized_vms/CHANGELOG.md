# Changelog

## v0.2.5

- Fixed issue with incident table that cause policy execution to fail


## v0.2.4

- Updated instance type data source from `data/google/instance_types.json` to `data/google/google_compute_instance_types.json`. Upsize recommendations now use a computed lookup based on vCPU count and memory-to-vCPU ratio, matching the approach used by the Google Rightsize VM Instances policy template.

## v0.2.3

- Updated documentation link in policy description. Functionality unchanged.

## v0.2.2

- Updated API call for listing Google Projects to speed up policy execution and reduce the number of paginated requests.
- Incident table no longer includes Project Number. This is not supported by the above API and only has limited utility.

## v0.2.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.2.0

- Added support for attaching CSV files to incident emails.

## v0.1.5

- Fixed issue where CPU stats would sometimes not be correctly calculated

## v0.1.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.3

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.1.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.0

- Initial release
