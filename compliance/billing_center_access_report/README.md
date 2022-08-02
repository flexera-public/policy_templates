# Billing Center Access Report

This Policy Template can target either all Billing Centers in an Organization or target a specific Billing Center.  Child Billing Centers are supported as well.  The resulting incident is a report of all users that have access to the target Billing Center(s).  If RightScale Groups have been granted access to a Billing Center, the report will indicate which Group has delegated access to a particular user.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer` or `billing_center_admin`
  - `enterprise_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *All Billing Centers?* - report on all Billing centers, true or false.
- *Billing Center Name* - If not reporting on all Billing Centers, provide the name of a specific Billing Center
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
