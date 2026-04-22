# AWS Resources Under or Approaching Extended Support

## What It Does

This policy template uses the AWS APIs (RDS, EKS, and ElastiCache) to identify all resources running versions covered by AWS Extended Support. Extended support start and end dates are determined using the static reference data file at `data/aws/aws_extended_support_dates.json`. Resource-level billing data from the Flexera CCO platform is used to obtain actual extended support costs for resources already incurring those charges. These resources are outdated and AWS charges an extended support fee for continued use. A report is produced containing a list of these resources, and optionally, an email is sent with this report.

## How It Works

- The policy queries the AWS APIs (RDS, EKS, and ElastiCache) across all opted-in regions to enumerate all running resources.
- Each discovered resource's version is matched against the reference data file at `data/aws/aws_extended_support_dates.json` to determine if it is currently under extended support or will enter extended support within the number of days specified by the `Days Until Extended Support` parameter.
- The policy also pulls resource-level billing data from the Flexera CCO platform from 3 days ago, filtered to resources with a `Usage Type` that contains `ExtendedSupport`. This data is used only for obtaining actual costs for resources already incurring extended support charges. Data from 3 days ago is used to ensure that we have available, processed billing data to search through.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is migrated to a newer supported version, avoiding the extended support fee.

The `Estimated Monthly Savings` is calculated differently depending on whether the resource is currently under extended support or approaching it:

- For resources **currently under extended support**: the policy first attempts to match the resource against Flexera CCO billing data. If a match is found, the `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month. This reflects the actual extended support fee currently being charged. If no CCO match is found (e.g., due to billing data lag), the estimated rate below is used as a fallback.
  - Since actual costs for resources currently under extended support are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- For resources **approaching extended support** (when the `Days Until Extended Support` parameter is greater than 0): the `Estimated Monthly Savings` is calculated using the AWS published Year 1 extended support hourly rates and resource-level data collected from the AWS APIs:
  - **RDS**: `$0.12 per vCPU-hour × estimated vCPU count × 24 hours × 30.44 days`. The vCPU count is estimated from the instance class (e.g. `db.m5.xlarge` → 4 vCPUs).
  - **EKS**: `$0.60 per cluster-hour × 24 hours × 30.44 days` (~$438/mo per cluster).
  - **ElastiCache**: `$0.05 per node-hour × number of cache nodes × 24 hours × 30.44 days`.
  - These estimates reflect the Year 1 extended support rate. AWS extended support rates double in Year 2 and double again in Year 3, so actual costs may be higher the longer a resource remains on an unsupported version.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Only applies to resources currently under extended support.
- *Days Until Extended Support* - Report resources that will enter extended support within this many days. Set to 0 to only report resources currently under extended support. Uses static reference data for RDS, EKS, and ElastiCache extended support schedules.
- *Billing Center List* - List of Billing Center names or IDs you want to report on. Leave blank to report on resources in all Billing Centers.
- *Allow/Deny AWS Accounts* - Whether to treat `Allow/Deny AWS Accounts List` parameter as allow or deny list. Has no effect if `Allow/Deny AWS Accounts List` is left empty.
- *Allow/Deny AWS Accounts List* - A list of allowed or denied AWS Account IDs/names. Leave blank to check all AWS Accounts.
- *Allow/Deny Regions* - Whether to treat `Allow/Deny Regions List` parameter as allow or deny list. Has no effect if `Allow/Deny Regions List` is left empty.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Regions can be entered in shorthand format, such as `us-east-2`. Leave blank to check all AWS regions.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; please see the README for more details.
- *Exclusion Tags: Any / All* - Whether to filter resources containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `rds:DescribeDBInstances`
  - `rds:ListTagsForResource`
  - `eks:ListClusters`
  - `eks:DescribeCluster`
  - `elasticache:DescribeCacheClusters`
  - `elasticache:ListTagsForResource`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "rds:DescribeDBInstances",
                  "rds:ListTagsForResource",
                  "eks:ListClusters",
                  "eks:DescribeCluster",
                  "elasticache:DescribeCacheClusters",
                  "elasticache:ListTagsForResource"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
