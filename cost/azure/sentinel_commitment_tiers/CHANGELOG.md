# Changelog

## v0.4.0

- Fixed bug where workspaces using Azure Sentinel Simplified pricing (unified SKU) received no recommendations or incorrect savings estimates. The policy now detects the pricing scheme per workspace via the OperationsManagement Solutions API and applies the correct rate model: Simplified workspaces use the all-inclusive Sentinel unified rate; Classic workspaces continue to use the sum of Log Analytics and Sentinel component rates.
- Added `Pricing Scheme` field to the incident table, indicating whether each recommendation was generated using Classic or Simplified pricing.
- Added downgrade and PAYG switch recommendations: the policy now evaluates all commitment tiers in both directions and checks whether switching to Pay-As-You-Go pricing would be cheaper than a workspace's current commitment tier.

## v0.3.1

- Fixed incorrect overage billing calculation: usage exceeding a commitment tier's daily GB level is now billed at the tier's effective per-GB rate (`Tier Daily Rate / Tier GB Level`) rather than the Pay-As-You-Go rate, consistent with Microsoft Sentinel pricing.

## v0.3.0

- Added `Allow/Deny Resource Groups` and `Allow/Deny Resource Groups List` filter parameters to allow filtering resources by resource group

## v0.2.0

- Added error incident when no Azure Subscriptions are found, indicating a potential credential or permissions issue.

## v0.1.0

- Initial release
