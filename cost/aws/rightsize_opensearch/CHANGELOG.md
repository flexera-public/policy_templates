# Changelog

## v0.2.1

- Fixed memory-based rightsizing formula to account for the AWS OpenSearch Service 32 GiB JVM heap cap; previously, the formula overestimated required memory for instance types with more than 64 GiB RAM, suppressing valid downsize recommendations
- Fixed EBS disk I/O risk checks to use peak (maximum) IOPS and throughput values instead of averages, so the risk flags correctly fire when peak usage approaches configured EBS volume limits

## v0.2.0

- Added `r7g` and `m7i` instance families to the instance type lookup
- Improved rightsizing savings accuracy: estimated savings now use instance-only billing costs (excluding EBS storage, Extended Support, data transfer, and other non-scalable charges) instead of total domain costs

## v0.1.0

- Initial release
