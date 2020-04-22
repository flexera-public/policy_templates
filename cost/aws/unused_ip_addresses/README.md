# AWS Unused IP Addresses

## What it does

This Policy finds AWS unused IP addresses and deletes them after approval.

## Functional Details

This policy gets a list of EIP(Elastic IPs) which can be on the following platforms:

1. EC2-Classic- In this platform instances run in a single, flat network that is shared with other customers.
2. EC2- VPC- In EC2-VPC, instances run in a virtual private cloud (VPC) that is logically isolated to only one AWS account.

Please note that all new AWS accounts are automatically on the EC2-VPC platform.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify 
- *Exclusion Tags Key:Value* - list of tags that an EIP(Elastic IP) can have to exclude it from the list.

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