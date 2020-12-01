# AWS Untagged Resources

## What it does

This Policy finds all AWS resources missing any of the user provided tags with the option to update the resources with the missing tags.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses* - A list of email addresses to notify
- *Tags Key=Value* - List of tags against which the resources will be compared.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Tag the resource with the provided user input.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
 {
   "Version": "2012-10-17",
   "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "tag:GetResources",
                "tag:TagResources",
                "ec2:DescribeRegions"
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
