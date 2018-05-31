### Unattached Volumes

**What it does**
This Policy Template scans all volumes in the given account and identifies any unattached volumes that have been unattached for at least the number of user-specified days.
If any are found, an incident report will show the volumes, and related information and an email will be sent to the user-specified email address.

Optionally, the user can specify if the aged volumes should be deleted by the policy.

## Supported Clouds
The following clouds are supported: 
- AWS
- Azure
- AzureRM
- Google
- VMware (RCA-V)

**Cost**

This Policy Template does not incur any cloud costs.