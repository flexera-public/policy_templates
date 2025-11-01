# AWS RDS Instances With Support Ending Soon

## What It Does

This policy template identifies AWS RDS instances running MySQL or PostgreSQL that are approaching the end of standard support. It checks whether these instances match the list of currently supported versions and calculates an estimated cost for extended support, based on the notification period you specify.

**Note:** Limitations

- This policy template does not currently support serverless deployments.
- If you have a deployment not listed in a region in our list we will default to USD$0.10 per vCPU per running hour.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized for RDS resources if the resource is approaching end of standard support within the predefined time frame.

- The `Estimated Monthly Savings` is calculated by multiplying the number of vCPUs assigned to the RDS instance by the extended support cost rate for MySQL or PostgreSQL in the instance’s region (refer to Notes for pricing links), and then multiplying that result by 720 hours, which represents AWS’s estimated monthly runtime.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

**Note:** The *End of Support dates* list is manually maintained and updated based on the AWS Release calendars and the calculations for extended support costs are provided by AWS. Refer to the links below for further information.

- [AWS PostgreSQL] (https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-release-calendar.html)
- [AWS MySQL] (https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.VersionMgmt.html#MySQL.Concepts.VersionMgmt.ReleaseCalendar)
- [AWS Aurora PostgreSQL] (https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.html#aurorapostgresql.minor.versions.supported)
- [AWS Aurora MySQL] (https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.release-calendars.html#AuroraMySQL.release-calendars.minor)
- [AWS Postgresql extended support pricing] (https://aws.amazon.com/rds/postgresql/pricing/#Amazon_RDS_Extended_Support_costs)
- [AWS MySQL extended support pricing] (https://aws.amazon.com/rds/mysql/pricing/#Amazon_RDS_Extended_Support_costs)
- [AWS Aurora extended support pricing] (https://aws.amazon.com/rds/aurora/pricing/#Amazon_RDS_Extended_Support_costs)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *End of support notification timeframe* - The number of days to check and notify on before the end of standard support date.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `rds:DescribeDBInstances`
  - `rds:ListTagsForResource`
  - `sts:GetCallerIdentity`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                "sts:GetCallerIdentity",
                "ec2:DescribeRegions",
                "rds:DescribeDBInstances",
                "rds:ListTagsForResource"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
