# MSP Parent to Child Group Sync

## What It Does

This policy template synchronizes groups, roles and users from a parent organization to child MSP organizations based on group description patterns. Groups in the parent org with descriptions matching the pattern `<GroupSync Prefix>_<OrgID>_<Group Name>` will be synchronized to the specified child org.  Using the default Group Sync Prefix, an example configuration string looks like:

OrgID can be a specific Child Org ID to sync the group with one specific child org, or `ALLORGS` to sync the group with all child orgs.

Assuming default Group Sync Prefix is used:
  - A group in the MSP Parent Org containing the string `GroupSync_ALLORGS_Read-Only Access` - Results in a group being created/synced with a name ***Read-Only Access*** in ***ALL*** child orgs

  - A group in the MSP Parent Org containing the string `GroupSync_123_Administrator Access` in the description results in a group being created/synced with a name ***Administrator Access*** in child ***Org 123***

  - A group in the MSP Parent Org containing the string `GroupSync_123_Read-Only Access` - Results in a group being created/synced with a name ***Read-Only Access*** in child ***Org 123***

The policy will:
- Create groups in child orgs if they don't exist
- Synchronize group memberships from parent to child orgs
- Invite users to child orgs if they don't exist
- Grant roles to groups in child orgs matching parent org roles
- Remove roles and memberships in child orgs that no longer exist in parent org

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected actions
  - `Sync Groups` - Automatically synchronize groups when differences are detected
- *Allow/Deny Child Orgs* - Allow or Deny entered Child Orgs to sync groups to
- *Allow/Deny Child Orgs List* - A list of allowed or denied Child Orgs to sync groups to

## Policy Actions

- Creates and updates groups in child orgs
- Adds users if Child Org has Identity Provider, otherwise uses invitation flow to affiliate users to child orgs
- Syncs user membership to groups in child orgs
- Syncs roles to groups in child orgs
- Removes roles and memberships that no longer exist in parent org

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following requirements:
  - Must be deployed in an account that has the `msp` capability enabled
  - Must use a User Refresh Token credential associated with a User that has `org_owner` access in all MSP Child Orgs

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Cost

This Policy Template does not incur any cloud costs.
