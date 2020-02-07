
# Google Object Storage Optimization

## What it does

This Policy checks Google buckets for older objects and can move old object to 'nearline' or 'coldline' after a given period of time. The user can choose to delete old object by enabling 'delete action' option as mentioned in Enable delete action section below.

## Functional Details

- This policy identifies all Google storage objects last updated outside of the specified timeframe
- For all objects identified as old, the user can choose to move the object to 'nearline' or 'coldline' after the specified timeframe.
- The user can choose to delete old object by enabling 'delete action' option as mentioned in Enable delete action section below.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Move to Nearline after days last modified* - leave blank to skip moving
- *Move to coldline after days last modified* - leave blank to skip moving
- *Exclude Tag* - exclude object with the included tags

## Enable delete action

Perform below steps to enable delete action.

- Edit the file [Google Object Storage Optimization](https://github.com/flexera/policy_templates/tree/master/cost/google/object_storage_optimization/google_object_storage_optimization.pt)
- uncomment the line which conatins 'escalate $esc_delete_bucket_objects_approval'
- comment the line which contains 'escalate $esc_modify_bucket_object_storage_class_approval' and save the changes. and save the changes.
- upload the modified file and apply the policy.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The storage.buckets.list permission
- The storage.buckets.getIamPolicy2 permission
- The storage.objects.list permission
- The storage.objects.getIamPolicy2 permission
- The storage.objects.create (for the destination bucket) permission
- The storage.objects.delete (for the destination bucket)4 permission
- The storage.objects.get (for the source bucket) permission
- The storage.objects.delete permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
