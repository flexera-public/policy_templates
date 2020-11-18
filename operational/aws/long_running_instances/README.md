# AWS Long Running Instances

## What It Does

This policy checks for running instances that have been running longer than the `Days Old` parameter. It will then take the appropriate action(Stop/Terminate) on the instance.

## Functional Description

- This policy identifies all instances that have been running longer than the `Days Old` parameter.

## Input Parameters

This policy template has the following Input parameters which require value before
the policy can be applied.

- *Allowed Regions* - A list of allowed regions for an AWS account. Click [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) to check regions in AWS and enter the region code. If this field is left empty, then the policy will throw an error.
- *Email notify list* - Email addresses of the recipients you wish to notify.
- *Days Old* - Number of days to be running before included in list.
- *Exclusion Tag Key:Value* - Cloud native tag key to ignore instances. Format: Key:Value
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Stop Instances" action while applying the policy, all the instances that didn't satisfy the policy condition will be stopped.

## Policy Actions

Policy actions may include automation to alert or remediate violations found in the
 Policy Incident. Actions that destroy or terminate a resource generally require
 approval from the Policy Approver. This policy includes the following actions.

- Sends an email notification
- Stop the instance
- Terminate the instance

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
for connecting to the cloud -- in order to apply this policy you must have a
 credential registered in the system that is compatible with this policy. If
 there are no credentials listed when you apply the policy, please contact your
 cloud admin and ask them to register a credential that is compatible with this
  policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances",
                "ec2:TerminateInstances"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*",
        },
        {
            "Effect": "Allow",
            "Action": ["ec2:DescribeInstances",
                        "ec2:DescribeRegions"]
            "Resource": "*"
        }
    ]
}
```

## Supported Clouds

This policy template supports the following clouds:

- AWS

## Costs

This Policy Template does not incur any cloud costs.
