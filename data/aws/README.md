# AWS Cloud Data

Various AWS-specific data assets, such as pricing data. Some assets are manually maintained and some are generated through automation; see the [Cloud Data Scripts README](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/README.md) for more information on how these assets are generated.

## aws_ec2_instance_types.json / instance_types.json

`aws_ec2_instance_types.json` is a newer asset generated and updated through automation. It's data comes directly from the AWS API. This asset should be used in policy templates that need detailed information about AWS EC2 instance types.

`instance_types.json` is similar but is older and manually maintained. It should not be used in policy templates going forward. This asset will remain in the repository long term to ensure that older policy templates continue to function as intended.

Some data fields in `aws_ec2_instance_types.json` are currently imported from `instance_types.json` until we build proper automation to gather/calculate this information:

- burst_info
- superseded
- ec2_classic

## aws_rds_db_size_mapping.json / aws_rds_db_instance_mapping.json / aws_rds_extended_support_cost_mapping.json

`aws_rds_db_size_mapping.json` is a newer asset manually generated to map vCPU sizing to instances.  This data is brought in through AWS API and should be automated in the future.

`aws_rds_db_instance_mapping.json` is used to map Postgres and mySQL versions to end of support dates.  This is all manually updated as AWS does not provide an API to do this. This should be reviewed quarterly as they update versions and give more specific end of support dates as many are estimates from AWS.

`aws_rds_extended_support_cost_mapping.jso` is a set of regional mappings of extended support costs in USD for year one costs. This is manually updated as there was no API for this information at the time.  This should be revisited quarterly to confirm accuracy or changes in costs.
