# ServiceNow Inactive Approvers

## What It Does

This policy template reports any approval users in ServiceNow that have not approved any request for a user-specified number of days. Optionally, this report can be emailed.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *ServiceNow Instance Name* - Name of the instance in your ServiceNow domain. For example, *myinstance* if your ServiceNow domain is *myinstance.service-now.com*.
- *ServiceNow Roles* - ServiceNow roles assigned to approval users.
- *Approval Action Threshold (Days)* - Number of days without an approval action executed in ServiceNow to report a user.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**ServiceNow Credential**](https://docs.flexera.com/flexera/EN/Automation/GenericCredentials.htm#automationadmin_3335267112_1121390) (*provider=servicenow*) which has the following permissions:
  - `user_admin`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- ServiceNow

## Cost

This Policy Template does not incur any cloud costs.
