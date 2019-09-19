## Google Object Storage Optimization
 
### What it does

This Policy checks Google buckets for older objects and can move old object to 'nearline' or 'coldline' after a given period of time. The user can choose to delete old object by enabling 'delete action' option as mentioned in Enable delete action section below.

### Functional Details
 
- This policy identifies all Google storage objects last updated outside of the specified timeframe
- For all objects identified as old, the user can choose to move the object to 'nearline' or 'coldline' after the specified timeframe.
- The user can choose to delete old object by enabling 'delete action' option as mentioned in Enable delete action section below.
 
### Input Parameters
 
This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Google Cloud Project Id* - Google Cloud Project Id
- *Move to Nearline after days last modified* - leave blank to skip moving
- *Move to coldline after days last modified* - leave blank to skip moving
- *Exclude Tag* - exclude object with the included tags 
 
### Required RightScale Roles
 
- Cloud Management - The `credential_viewer`,`observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles

### Enable delete action

Perform below steps to enable delete action.

- Edit the file [Google Object Storage Optimization](https://github.com/flexera/policy_templates/tree/master/cost/google/object_storage_optimization/google_object_storage_optimization.pt)
- uncomment the line which conatins 'escalate $esc_delete_bucket_objects_approval' 
- comment the line which contains 'escalate $esc_modify_bucket_object_storage_class_approval' and save the changes. and save the changes.
- upload the modified file and apply the policy.

### Google Required Permissions

- This policy requires IAM permissions to storage.buckets.list, storage.buckets.getIamPolicy2, storage.objects.list, storage.objects.getIamPolicy2,6, storage.objects.create (for the destination bucket), storage.objects.delete (for the destination bucket)4, storage.objects.get (for the source bucket) and storage.objects.delete.
- Create a service account (if not exists) with the necessary permissions under Google-cloud platform (IAM & admin -> service accounts). Generate key, a JSON file will get downloaded in which you can find 'client email' and 'private key' which has to be added as credentials in RightScale cloud management Design -> Credentials with name 'GCE_PLUGIN_ACCOUNT' and 'GCE_PLUGIN_PRIVATE_KEY' respectively.

### Supported Clouds
 
- Google
 
### Cost
 
This Policy Template does not incur any cloud costs.
