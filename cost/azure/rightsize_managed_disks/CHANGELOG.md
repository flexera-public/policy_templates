# Changelog

## v1.2

- Updated the descriptions and labels of the IOPS and throughput parameters in the README and policy template files.
- Updated the short description of the policy.
- Changed the functionality of `param_min_savings`: Before this version, the `param_min_savings` parameter was used to consider the total savings (the sum of all the savings per resource) and not the savings per resource to decide whether to recommend or not. In this new version, this parameter is used to recommend or not based on the savings of each resource, just as other policies do.

## v1.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v1.0

- Initial release.
