# ServiceNow Inactive Approvers

## What it does

This policy will identify approver users in ServiceNow that have not approved any requests in the past **n** days.

## Functional Description

This policy integrates with the ServiceNow API to retrieve approval history. Therefore the following are prerequisites for this policy to execute:

- ServiceNow implementation
- ServiceNow user with the appropriate permissions to read approval history (sysapproval_approver table), read roles (sys_user_role table), and read users (sys_user table)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *ServiceNow Instance Name* - Name of the instance in your ServiceNow url (e.g. "contoso" if your ServiceNow instance is contoso.service-now.com)
- *Approval Roles* - ServiceNow Roles that identify Approver Users to target for this policy
- *Number of Days* - Number of days without an approval action executed in ServiceNow
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `servicenow`

## Policy Actions

- Sends an email notification

