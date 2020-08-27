# Azure Unused IP Addresses

## What it does  

This Policy Template scans all IP addresses in the given account and identifies any unused IP addresses. If any are found, an incident report will show the IP addresses, and related information along with the estimated monthly savings for each resource, and an email will be sent to the user-specified email address. If the user approves that the IP addresses should be deleted, the policy will delete the IP addresses. Optionally, the user can specify one or more tags that if found on an IP address will exclude the IP address from the list.
The email will also contain Total Estimated Monthly Savings in the incident message details.

## Input Parameters  

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Exclude Tags* - A list of tags used to exclude IP addresses from the incident.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Delete Unused IP Addresses" action while applying the policy, all the unused IP addresses will be deleted.

## Policy Actions  

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report    
- Delete Unused IP addresses after approval

## Prerequisites  

- This policy requires the Azure Credential. When applying the policy select the appropriate credentials from the list for your tenant.  If such credential doesn't exist please contact your cloud admin to create the Credential. The credential must contain the value *Azure RM* in the Provider field. Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)
- billing_center_viewer (note: this role must be applied at the Organization level).

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Network/publicIPAddresses/read
- Microsoft.Network/publicIPAddresses/delete

## Supported Clouds  

- Azure

## Cost  

This Policy Template does not incur any cloud costs.