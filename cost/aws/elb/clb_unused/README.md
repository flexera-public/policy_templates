# AWS Unused Classic Load Balancers (CLB)

This policy checks all Classic Load Balancers (CLB) to determine if any are unused (have no healthy instances) and allows them to be deleted by the user after approval.

Note: Elastic Load Balancing (ELB) supports three types of load balancers: Application Load Balancers, Network Load Balancers and Classic Load Balancers.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `elasticloadbalancing:DescribeLoadBalancers`
  - `elasticloadbalancing:DescribeInstanceHealth`
  - `elasticloadbalancing:DescribeTags`
  - `elasticloadbalancing:DeleteLoadBalancer`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "elasticloadbalancing:DescribeLoadBalancers",
                  "elasticloadbalancing:DescribeInstanceHealth",
                  "elasticloadbalancing:DescribeTags",
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

## Functional Details

The policy leverages the AWS elasticloadbalancing API to determine if the CLB is in use.

When an unused CLB is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the CLB after manual approval if needed.

### Policy savings details

The policy includes the estimated savings.  The estimated savings is recognized if the resource is terminated.   Optima is used to receive the estimated savings which is the product of the most recent full day’s cost of the resource * 30.  The savings is displayed in the Estimated Monthly Savings column.  If the resource can not be found in Optima the value is n/a.  The incident detail message includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.

If the user is missing the minimum required role of `billing_center_viewer`or if there is no enough data received from Optima to calculate savings, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as N/A in the incident table.

## Input Parameters

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses* - A list of email addresses to notify
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Ignore tags* - List of one or more Tags that will exclude Classic Load Balancer from actions being taken. Format: Key=Value
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Load Balancers" action while applying the policy, all the identified unused load balancers will get deleted.

## Policy Actions

- Sends an email notification.
- Delete unused CLB after approval.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
