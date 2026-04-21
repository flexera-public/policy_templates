# AWS Superseded RDS Instances

## What It Does

This policy template checks for AWS RDS instances that are running on superseded instance classes and recommends migrating them to newer, more cost-effective instance types. The policy identifies instances whose current class has a newer-generation equivalent available and calculates estimated monthly savings based on list pricing.

## How It Works

The policy retrieves a list of all RDS instances in the AWS account across all enabled regions and checks each instance class against a table of superseded instance types. If a superseded instance class has a recommended newer replacement, the policy reports the instance as a recommendation.

The recommended instance class is determined by the "Instance Type Category" parameter, which selects from Regular, Next Gen, Burstable, or AMD replacement options. If no replacement exists for the primary category, the "Fallback Instance Type Category" parameter provides an alternate option.

Additionally, the policy validates that the recommended instance class is available for the specific database engine and region combination before generating a recommendation.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the instance class is changed to the recommended class.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the instance for 1 day, as found within Flexera CCO, by 30.44 (the average number of days in a month), and then by the ratio of list prices between the current and recommended instance class.
- The ratio of list prices is derived from the RDS pricing data for the specific database engine, region, and deployment option (Single-AZ or Multi-AZ).
- If list prices are not available for the current or recommended instance type, the savings ratio is estimated using the relative NFU (Normalized Factor Units) values of the instance types.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Cost` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify when new incidents are created.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Instance Type Category* - The instance type category to use when selecting a recommended replacement instance class. Options: Regular, Next Gen, Burstable, AMD.
- *Fallback Instance Type Category* - The instance type category to use if no replacement is available for the primary category. Set to 'None' to disable fallback. Options: Regular, Next Gen, Burstable, AMD, None.
- *Minimum Savings Threshold* - The minimum estimated monthly savings required to generate a recommendation. Instances with savings below this threshold will not be reported.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; please see the README for more details.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions. See the README for more details.
- *Downsize Timeframe* - Whether to change the RDS instance class immediately or wait until the next maintenance window.
- *Automatic Actions* - When set, the policy will automatically take the selected action(s).
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Change Instance Class" action while applying the policy template, all the resources that didn't satisfy the policy condition will have their instance class changed to the recommended class.

## Policy Actions

- Sends an email notification.
- Change the RDS instance class after approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `sts:GetCallerIdentity`
  - `rds:DescribeDBInstances`
  - `rds:ListTagsForResource`
  - `rds:DescribeOrderableDBInstanceOptions`
  - `rds:ModifyDBInstance`*

  \* Only required for taking action (instance class change); the policy will still function in a read-only capacity without this permission.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `sts:GetCallerIdentity`
  - `rds:DescribeDBInstances`
  - `rds:ListTagsForResource`
  - `rds:DescribeOrderableDBInstanceOptions`
  - `rds:ModifyDBInstance`*

  \* Only required for taking action; the policy will still function in a read-only capacity without this permission.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "sts:GetCallerIdentity",
                  "rds:DescribeDBInstances",
                  "rds:ListTagsForResource",
                  "rds:DescribeOrderableDBInstanceOptions",
                  "rds:ModifyDBInstance"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
