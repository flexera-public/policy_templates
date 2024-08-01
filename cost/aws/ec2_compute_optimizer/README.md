# AWS EC2 Compute Optimizer Recommendations

## What It Does

This policy template reports EC2 rightsizing recommendations produced by the [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/faqs/#EC2_instance_recommendations). Optionally, this report can be emailed and the offending instances can be resized.

## How It Works

The policy utilizes the [AWS Compute Optimizer API](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEC2InstanceRecommendations.html) to get a list of recommendations for EC2 instances. The specific recommendations produced by the AWS Compute Optimizer will depend on how it is configured within the AWS environment. Please consult the [relevant AWS documentation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendation-preferences.html) for more information on how to do this.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is resized to the recommended size. The `Estimated Monthly Savings` and `Estimated Monthly Savings After Discounts` are obtained directly from the [AWS Compute Optimizer API](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEC2InstanceRecommendations.html). If the Flexera organization is configured to use a currency other than the one returned by the [AWS Compute Optimizer API](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEC2InstanceRecommendations.html), the savings values will be converted using the exchange rate at the time that the policy executes.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. This is based on the value of the `Estimated Monthly Savings` field.
- *Include ARM Recommendations* - Whether or not to include recommendations that would involve migrating from x86-64 instances to ARM instances.
- *Show Multiple Recommendations* - Whether or not to show multiple recommendations for a single instance or to only show the one with the most savings potential. Note that including multiple recommendations per instance may skew metrics around potential savings in the Flexera One platform and is not recommended in most cases.
- *Allow/Deny Regions* - Whether to treat regions parameter as allow or deny list.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Resize Resources" action while applying the policy, all the resources that didn't satisfy the policy condition will be resized.

## Policy Actions

- Send an email report
- Resize EC2 instances after approval

## Prerequisites

Since this policy template relies on the AWS Compute Optimizer, it must be enabled in the various accounts and regions that one wishes to obtain recommendations for. Please consult the [relevant AWS documentation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html) for more information on how to do this.

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `compute-optimizer:GetEC2InstanceRecommendations`
  - `ec2:DescribeRegions`
  - `ec2:DescribeInstances`
  - `ec2:ModifyInstanceAttribute`*
  - `ec2:StartInstances`*
  - `ec2:StopInstances`*

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
                  "compute-optimizer:GetEC2InstanceRecommendations",
                  "ec2:DescribeRegions",
                  "ec2:DescribeInstances",
                  "ec2:ModifyInstanceAttribute",
                  "ec2:StartInstances",
                  "ec2:StopInstances"
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

This Policy Template does not launch any instances, and so does not incur any cloud costs.
