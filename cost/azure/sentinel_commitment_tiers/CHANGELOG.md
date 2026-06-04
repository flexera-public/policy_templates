# Changelog

## v0.3.1

- Fixed incorrect overage billing calculation: usage exceeding a commitment tier's daily GB level is now billed at the tier's effective per-GB rate (`Tier Daily Rate / Tier GB Level`) rather than the Pay-As-You-Go rate, consistent with Microsoft Sentinel pricing.

## v0.3.0

- Added `Allow/Deny Resource Groups` and `Allow/Deny Resource Groups List` filter parameters to allow filtering resources by resource group

## v0.2.0

- Added error incident when no Azure Subscriptions are found, indicating a potential credential or permissions issue.

## v0.1.0

- Initial release
