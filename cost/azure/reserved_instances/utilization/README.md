# Azure Reserved Instances Utilization Policy Template

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

## What it does

This Policy Template leverages the [Azure EA API for Reserved Instance Utilization](https://docs.microsoft.com/en-us/rest/api/billing/enterprise/billing-enterprise-api-reserved-instance-usage#request-for--reserved-instance-usage-summary). It will notify only if utilization of a RI falls below the value specified in the `Show RI's with utilization below this value` field. It examines the RI utilization for the prior 7 days (starting from 2 days ago) in making this determination.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Enrollment ID* - the Azure EA enrollment ID
- *Show RI's with utilization below this value*
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no
credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed: 

Provider tag value to match this policy: `azure_ea`

Required permissions in the provider:

- Microsoft.Consumption/reservationSummaries/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
