# Changelog

## v0.2.0

- Fixed pricing model to correctly use per-CU rates from the Azure Retail Prices API. Previously, the code attempted to match per-F-SKU price entries using a regex on `skuName`; Fabric pricing is actually per-CU with a generic `skuName` of "Fabric Capacity". Monthly PAYG costs are now calculated as `per_CU_rate × CU_count × active_hours` and reservation costs as `per_CU_annual_cost × CU_count / 12`.
- Fixed extraction of the price type field from the Azure Retail Prices API response. The response field is named `type`, not `priceType`. Without this fix, no pricing entries were classified as PAYG or Reservation and no recommendations were generated.
- Fixed right-sizing recommendation when Azure Monitor returns no Maximum metric data (peak utilization = 0). The policy now falls back to average utilization as the effective peak rather than recommending the smallest F2 SKU for any capacity.
- Added comment in cost estimation logic documenting the assumption that any day with non-zero utilization is treated as fully active (24 hours).
- Updated README to document the per-CU pricing model and formulas, note that the Azure Monitor metric name for `Microsoft.Fabric/capacities` was not publicly documented at the time of initial release, and add a limitation note that the template assumes all capacities are on Pay-As-You-Go pricing.
- Fixed export field order: `resourceGroup` now appears after `region` per catalog conventions.

## v0.1.0

- Initial release
