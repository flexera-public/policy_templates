# AWS Unused IP Addresses

## What it does

This Policy finds AWS unused IP addresses and deletes them after approval.

## Functional Details

An Elastic IP (EIP) is an IP address that can be reserved from AWS for an account. Once Elastic IP is created, it can be assigned to any instance available in an account.
The reserved IP in an account which is not associated with a running EC2 instance or an Elastic Network Interface (ENI) is known as Unused Elastic IP and it incur charges. 
If EIP is not needed, charges can be stopped by releasing the unused EIP.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created 
- *Exclusion Tags Key:Value* - AWS tag to ignore Elastic IPs. Format: Key:Value.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report 
- Delete unused IP addresses after approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.  

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

{
  "Version": "2012-10-17",
  "Statement": [
        {
        "Effect": "Allow", 
        "Action": [
          "ec2:DescribeAddresses",
          "ec2:ReleaseAddress"
        ],
        "Resource": "*"
        }
  ] 
}

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.