# Changelog

## v0.2.0

- Fixed a bug where the policy would fail entirely for any Auto Scaling Group using a `MixedInstancesPolicy` with more than one instance type override. The policy now correctly captures all configured instance types for mixed-instance ASGs instead of assuming there is only one.
- When an Auto Scaling Group has no running instances, the reported "Instance Size" for mixed-instance ASGs now lists all configured instance type overrides (instead of only the first), giving a more complete picture of the resource's actual cost and configuration exposure.
- Replaced non-ASCII punctuation (em dashes, curly quotes, etc.) with standard ASCII equivalents for consistent rendering in the Flexera UI. No functional changes.

## v0.1.3

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.1.2

- Improved the policy's reliability when checking which AWS regions it can access, making it less likely to fail to run due to expected access restrictions in certain regions

## v0.1.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.0

- Initial release
