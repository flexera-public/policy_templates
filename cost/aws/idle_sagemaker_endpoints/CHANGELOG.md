# Changelog

## v0.2.0

- Savings estimates now use AWS Price List API data (`data/aws/aws_sagemaker_pricing.json`) instead of Flexera CCO billing data. CCO does not reliably capture SageMaker endpoint resource IDs, making billing-based savings estimates unreliable for this resource type.
- Monthly cost is calculated as: `Σ (hourly_rate × instance_count × 730.5)` across all production variants.

## v0.1.0

- Initial release
