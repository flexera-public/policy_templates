# Azure Long Running Instances

## What It Does

This policy checks for running instances that have been running longer than the `Minimum Age (Days)` parameter. It will then take the appropriate action (Stop/Terminate) on the instance.

## Functional Description

- This policy identifies all instances that have been running longer than the `Minimum Age (Days)` parameter.

## Input Parameters

This policy template has the following Input parameters which require value before
the policy can be applied.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Minimum Age (Days)* - The minimum age, in days, to consider an instance to be long running.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *Automatic Actions* - The policy will automatically take the selected action.

Please note that the "Automatic Actions" parameter contains a list of actions that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter set to "No Automatic Actions" for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

Policy actions may include automation to alert or remediate violations found in the
Policy Incident. Actions that destroy or terminate a resource generally require
approval from the Policy Approver. This policy includes the following actions.

- Sends an email notification
- Stop virtual machines after approval
- Terminate virtual machines after approval

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm)
for connecting to the cloud -- in order to apply this policy you must have a
credential registered in the system that is compatible with this policy. If
there are no credentials listed when you apply the policy, please contact your
cloud admin and ask them to register a credential that is compatible with this
policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`*

\* Only required for taking action (stopping or terminating instances); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

## Supported Clouds

This policy template supports the following clouds:

- Azure

## Costs

This Policy Template does not incur any cloud costs.
