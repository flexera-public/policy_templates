# Changelog

## v1.0.0

- Changed cost estimation methodology from billing-data lookup to analytical rate-times-size calculation
- Removed `Billing Center List` parameter; extended-support surcharge is now estimated directly from resource size and reference rates rather than from billing data
- Added `shared_core_hourly_rate` to Cloud SQL reference data entries for accurate shared-core (f1-micro, g1-small) tier pricing
- Updated minimum-savings filter to apply to "currently under extended support" resources only; "approaching" resources always appear regardless of estimated surcharge
- Updated incident detail to display "Estimated Monthly Extended-Support Surcharge" label

## v0.1.0

- Initial release
