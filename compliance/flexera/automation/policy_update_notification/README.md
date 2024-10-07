# Policy Update Notification

## Deprecated

This policy is no longer being updated. The [Flexera Automation Outdated Applied Policies](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/outdated_applied_policies/) policy has superseded this one and includes significantly more functionality.

## What It Does

This Policy Template scans all applied policies in a Flexera account and finds ones that are using an outdated version of a policy template from the Flexera catalog. An incident is raised, and optionally an email is sent, containing a list of these outdated applied policies.

## How It Works

The policy utilizes the Flexera API to get a list of all applied policies in the Flexera account. The same API is then used to get a list of all policy templates in the catalog. An incident is raised with any applied policies whose version number does not match the version number for that same template in the catalog. Applied policies created from templates not in the policy catalog are not included in the results.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `Automation: View Policies`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Cost

This Policy Template does not incur any cloud costs.
