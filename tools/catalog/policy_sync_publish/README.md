# Policy Template Synchronization - Publish

## What It Does

This Policy Template can be used to synchronize (upload, overwrite, or alert) RS built-in policy templates in your account. It uses a json file stored in the github directory to determine a set of RightScale's current policy templates and then compares them with your current account policies (using the version) to take appropriate action.

![Policy Sync]("policy_sync_publish.png")

## Prerequisites

This policy uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `policy_designer`
  - `policy_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Usage

- The Policy Template Synchronization Policy Template will need to be uploaded to your account and set active.
- There are currently two actions: `Email` and `Email and Upload`.
- When you choose `Email` you will get an alert on the the policy templates that can be updated, and no further action will be taken.
- When you choose `Email and Upload`, you will get an alert on the policy templates that can be updated and we will upload those policies to your account.

### Scenarios

1. No RightScale's built-in Policy Templates in the account
    1. `Email` or `Email and Upload`
1. RightScale's built-in Policy Templates exist in the account
    1. Versions are the same: `No Action`
    1. Versions are different: `Email` or `Email and Upload`
    1. Versions are the same, Force Upgrade = 1: `Email` or `Email and Upload`

## Parameters

### Policy Template Synchronization Policy Template

1. Email addresses of the recipients you wish to notify - Ex: noreply@example.com
1. Actions: `Email` and `Email and Upload`
1. Force Upgrade - Allowed Values: 0:False, 1:True - Setting this to 1 will force upgrade all policy templates in your account.
1. Governance Host - "Governance Host, Hostname will match your shard: us-3.rightscale.com = governance-3.rightscale.com". Simply navigate to Cloud Management or open browser developer console to see the hostname of the API calls.

## Required Roles

1. For `Email` Escalation option, either: `policy_manager` or `policy_designer`
1. For `Email and Upload` Escalation option: `policy_designer`

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
