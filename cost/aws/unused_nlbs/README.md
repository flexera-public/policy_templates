# AWS Unused Network Load Balancers

## What It Does

This policy template checks all Network Load Balancers to determine if any are unused (have no listeners or have no healthy target groups) and allows them to be deleted by the user after approval.

Note: Elastic Load Balancing (ELB) supports three types of load balancers: Classic Load Balancers, Network Load Balancers and Application Load Balancers. This policy template only reports on Network Load Balancers; please use the [AWS Unused Application Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_albs) and [AWS Unused Classic Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_clbs) policy templates to report on those.

## How It Works

- The policy leverages the AWS Elastic Load Balancing API to gather a list of Network Load Balancers in the AWS account.
- The same API is then used to gather information about the Network Load Balancer's listeners and target groups.
- If the Network Load Balancer has no listeners, or has no target groups with a `healthy` status, it is considered unused.
  - Note: Target Groups with no targets will not be considered `healthy` for the purposes of this assessment.
- The recommendation provided for unused Network Load Balancers is deletion. These resources can be deleted in an automated manner or after approval.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is deleted.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Load Balancer Age (Hours)* - Age, in hours, that a Network Load Balancer needs to be to include it in the results. This is to avoid reporting on very new Network Load Balancers that are still being configured.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Delete Unused Network Load Balancers" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification.
- Deletes unused Network Load Balancers after approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `ec2:DescribeRegions`
  - `elasticloadbalancing:DescribeLoadBalancers`
  - `elasticloadbalancing:DescribeListeners`
  - `elasticloadbalancing:DescribeTags`
  - `elasticloadbalancing:DescribeTargetGroups`
  - `elasticloadbalancing:DescribeTargetHealth`
  - `elasticloadbalancing:DeleteLoadBalancer`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

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
                  "elasticloadbalancing:DescribeLoadBalancers",
                  "elasticloadbalancing:DescribeListeners",
                  "elasticloadbalancing:DescribeTags",
                  "elasticloadbalancing:DescribeTargetGroups",
                  "elasticloadbalancing:DescribeTargetHealth",
                  "elasticloadbalancing:DeleteLoadBalancer"
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
