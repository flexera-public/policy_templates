# AWS Long Running Instances

## What It Does

This policy checks for running instances that have been running longer than the `Days Old` parameter. It will then take the appropriate action(Stop/Terminate) on the instance.

## Functional Description

- This policy identifies all instances that have been running longer than the `Days Old` parameter.

## Input Parameters

This policy template has the following Input parameters which require value before
the policy can be applied.

- *Email notify list* - Email addresses of the recipients you wish to notify.
- *Days Old* - Number of days to be running before included in list.
- *Action to Take* - Either Stop or Terminate the instance
- *Exclusion Tag Key:Value* - Cloud native tag key to ignore instances. Format: Key:Value

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

Provider tag value to match this policy: `aws`

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
            "Action": "ec2:DescribeInstances",
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
