# Flexera Automation Outdated Applied Policies

## What It Does

This policy template checks all applied policies for the following:

- Whether the policy template is an older version than the current version in the policy catalog.
- Whether the policy template has been deprecated.

The following policy types will always be ignored and not reported on by this policy:

- This policy itself.
- Policies applied from a source other than the Flexera Automation Catalog.
- Organization-specific policies published to that organization's own catalog.
- Flexera policies present in the [policy-templates Github Repository](https://github.com/flexera-public/policy_templates) but not published in the Flexera Automation Catalog, such as meta policies and other misc. utility policies.
- Policy aggregates applied across multiple projects. Aggregates applied only to the project this policy is applied in will still be included in the results and are actionable.

## How It Works

The list of outdated policies is generated as follows:

- The list of applied policies are obtained using the [Flexera Policy API](https://reference.rightscale.com/governance-policies/).
- The list of catalog policies are obtained using the [Active Policy List JSON file](https://github.com/flexera-public/policy_templates/blob/master/data/active_policy_list/active_policy_list.json) in the [policy-templates Github Repository](https://github.com/flexera-public/policy_templates).
- The list of applied policies is filtered for just those applied policies that were applied from a catalog policy and whose version number does not match the version number in the catalog.

The list of deprecated policies is generated as follows:

- The list of applied policies are obtained using the [Flexera Policy API](https://reference.rightscale.com/governance-policies/).
- The list of catalog policies are obtained using the [Active Policy List JSON file](https://github.com/flexera-public/policy_templates/blob/master/data/active_policy_list/active_policy_list.json) in the [policy-templates Github Repository](https://github.com/flexera-public/policy_templates).
- The list of applied policies is filtered for just those applied policies marked as deprecated in the [Active Policy List JSON file](https://github.com/flexera-public/policy_templates/blob/master/data/active_policy_list/active_policy_list.json).

Updating an outdated policy is done as follows:

- The [major version](https://semver.org/) of the applied policy is compared to the catalog policy. If the major version has changed, and the `Allow Automated Major Version Updates` parameter is set to "Do Not Allow", an error is raised indicating that the update should be done manually. This is because a major version change usually involves major changes in functionality and input parameters that would require the user to intelligently determine how to apply the updated policy.
- If the major version has not changed, or the `Allow Automated Major Version Updates` parameter is set to "Allow", the catalog policy is applied with the exact same configuration and settings as the existing applied policy.
- If the above action was successful, the existing applied policy is deleted. If the above action failed, an error is raised and the existing applied policy remains in place so that the user can manually update as needed.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Policy Ignore List* - A list of applied policy names and/or IDs to ignore and not report on. Leave blank to assess all applied policies.
- *Policy Templates To Report* - Whether to report outdated policy templates, deprecated policy templates, or both. Separate incidents will be raised/emailed if both are selected and found.
- *Allow Automated Major Version Updates* - Whether to allow actions to automatically update outdated policy templates when there's been a major version change. This is not recommended in most cases.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

## Policy Actions

- Send an email report
- Update applied policy to the newest version after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for taking action (updating applied policies); the policy will still function in a read-only capacity without these permissions.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs. Cloud costs may be incurred by the applied policies that this policy reports on and updates. Please consult the README of each policy for more information.
