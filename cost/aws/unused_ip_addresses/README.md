# AWS Unused IP Addresses

## What it does

This Policy Template scans all IP addresses in the given account and identifies any unused IP addresses. If any are found, an incident report will show the IP addresses, and related information, and an email will be sent to the user-specified email address. If the user approves that the IP addresses should be deleted, the policy will delete the IP addresses. Optionally, the user can specify one or more tags that if found on an IP address will exclude the IP address from the list.

## Functional Details

An Elastic IP (EIP) is an IP address that can be reserved from AWS for an account. Once Elastic IP is created, it can be assigned to any instance available in an account.
The reserved IP in an account which is not associated with a running EC2 instance or an Elastic Network Interface (ENI) is known as Unused Elastic IP and it incur charges.
If EIP is not needed, charges can be stopped by releasing the unused EIP.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. The savings is calculated using the per hour cost of unused IPs for a period of 30 days and is displayed in the Estimated Monthly Savings column and the total estimated sum of all the unused IPs is displayed in the incident detail message.
Please note that the estimated savings is calculated and displayed in USD($), excluding any discounts.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tags* - A list of AWS tags to ignore Elastic IPs. Format: Key=Value.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Resources" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete unused IP addresses after approval

## Prerequisites

- This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeAddresses",
        "ec2:ReleaseAddress",
        "ec2:DescribeRegions",
        "pricing:GetProducts"
      ],
      "Resource": "*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
