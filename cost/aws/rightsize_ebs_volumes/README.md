# AWS Rightsize EBS Volumes

## What It Does

This policy checks all GP2 volumes on an AWS Account to see if the GP3 equivalent would be less expensive. An incident is raised with all volumes that would be less expensive if upgraded from GP2 to GP3.

## Functional Details

- The policy leverages the AWS API to retrieve a list of all volumes in an AWS Account
- The policy identifies all GP2 volumes and uses the AWS Pricing API to retrieve the current cost, and the cost of the volume if it were a GP3 volume type.
- If there is a cost savings associated with moving the volume type from GP2 to GP3, this will provide a recommendation.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the volume is upgraded from GP2 to GP3. The AWS Pricing API is used to retrieve and calculate the estimated savings which is the expected GP3 cost subtracted from the estimated current GP2 cost of the volume. The incident message detail includes the sum of each resource *Estimated Monthly Saving* as *Potential Monthly Savings*.

If the Flexera organization is configured to use a currency other than USD, the savings values will be converted from USD using the exchange rate at the time that the policy executes.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the volume is upgraded from GP2 to GP3.

- The `Estimated Monthly Cost` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month. This value is not used for calculating savings but is provided as a reference.
- Since the `Estimated Monthly Cost` of individual resources is obtained from Flexera CCO, it will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- The AWS Pricing API is used to retrieve the list price of the current volume type and the recommended volume type. The `Estimated Monthly Savings` is calculated by subtracting the estimated price of the recommended GP3 volume type from the price of the current GP2 volume type.
- Since `Estimated Monthly Savings` is calculated based on list prices obtained from the AWS Pricing API, they will *not* take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- If the Flexera organization is configured to use a currency other than USD, the savings values will be converted from USD using the exchange rate at the time that the policy executes.

## Input Parameters

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
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *AWS Regional Pricing API* - The regional AWS Pricing API to use when retrieving pricing data. Pricing may vary based on region. More details on these endpoints and how functionality differs between them can be found in the [AWS Price List Query API documentation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/using-price-list-query-api.html#price-list-query-api-endpoints).
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Upgrade Volumes to GP3" action while applying the policy, all the volumes that appear in the raised incident will be upgraded to GP3.

## Policy Actions

- Sends an email notification
- Upgrade GP2 volumes to GP3 after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeVolumes`
  - `ec2:ModifyVolume`*
  - `pricing:GetProducts`

  \* Only required for taking action (upgrading to GP3); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "ec2:DescribeVolumes",
                  "ec2:ModifyVolume",
                  "pricing:GetProducts"
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

This Policy Template does not incur any cloud costs.
