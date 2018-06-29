## Unattached Volumes

### What it does

This Policy Template scans all volumes in the given account and identifies any unattached volumes that have been unattached for at least the number of user-specified days. If any are found, an incident report will show the volumes, and related information and an email will be sent to the user-specified email address.

Optionally, the user can specify one or more RightScale tags that if found on a volume will exclude the volume from the list.
Additionally, the user can optionally specify if the aged volumes should be deleted by the policy.

### Supported Clouds

- AWS
- Azure
- AzureRM
- Google
- VMware (RCA-V)

### Cost

This Policy Template does not incur any cloud costs.