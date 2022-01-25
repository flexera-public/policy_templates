
# Google Object Storage Optimization

## What it does

This Policy checks Google buckets for older objects and can move old object to 'nearline' or 'coldline' after a given period of time. The user can choose to delete old object by enabling 'delete action' option as mentioned in Enable delete action section below.

## Functional Details

- If APIs & Services are not enabled for a project, the policy will skip that particular project. On the next run if APIs & Services are enabled, then the project will be considered for execution.
- This policy identifies all Google storage objects last updated outside of the specified timeframe
- For all objects identified as old, the user can choose to move the object to 'nearline' or 'coldline' after the specified timeframe.
- The user can also choose to delete old object.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Move to Nearline after days last modified* - leave blank to skip moving
- *Move to coldline after days last modified* - leave blank to skip moving
- *Exclude Tag* - exclude object with the included tags
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Update Bucket storage" action while applying the policy, all the identified old resources will be moved to 'nearline' or 'coldline'.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `storage.buckets.list` permission
- The `storage.buckets.getIamPolicy2` permission
- The `storage.objects.list` permission
- The `storage.objects.getIamPolicy2` permission
- The `storage.objects.create` (for the destination bucket) permission
- The `storage.objects.delete` (for the destination bucket)4 permission
- The `storage.objects.get` (for the source bucket) permission
- The `storage.objects.delete` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
