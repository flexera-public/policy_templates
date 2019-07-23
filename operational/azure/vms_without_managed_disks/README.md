## Azure VMs not using managed disks

### What it does
This policy checks all Azure VMs and reports on any that are not using Managed Disks, which are the latest offering from Azure and are much easier to manage.

### Functional Details
When a VM that is using unmanaged disks is detected, all details of the VM are reported to the specified users.

#### Input Parameters
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Exclusion Tag Key* - an Azure-native instance tag to ignore instances that match the disallowed instance type. Only supply the tag key

### Required RightScale Roles
- credential_viewer or admin

### Supported Clouds
- Azure Resource Manager

### Cost
This Policy Template does not incur any cloud costs.