## Policy Template Synchronization Tool

### What it does

This Policy Template can be used to synchronize (upload, overwrite, or alert) RS built-in policy templates in your account. It uses a json file stored in the github directory to determine a set of RightScale's current policy templates and then compares them with your current account policies (using the version) to take appropriate action.

<img src="https://github.com/rightscale/policy_templates/tree/master/operational/policy_sync/policy_sync.png" width="600">

### Usage

- The Policy Template Synchronization Policy Template will need to be uploaded to your account and set active. 
- There are currently two actions: `Email` and `Email and Upload`. 
- When you choose `Email` you will get an alert on the the policy templates that can be updated, and no further action will be taken. 
- When you choose `Email and Upload`, you will get an alert on the policy templates that can be updated and we will upload those policies to your account. 

#### Scenarios

1. No RightScale's built-in Policy Templates in the account
   1. `Email` or `Email and Upload`
1. RightScale's built-in Policy Templates exist in the account
   1. Versions are the same: `No Action`
   2. Versions are different: `Email` or `Email and Upload`
   3. Versions are the same, Force Upgrade = 1: `Email` or `Email and Upload`

### Parameters

#### Policy Template Synchronization Policy Template

1. Email addresses of the recipients you wish to notify - Ex: noreply@example.com
2. Actions: `Email` and `Email and Upload`
3. Force Upgrade - Allowed Values: 0:False, 1:True - Setting this to 1 will force upgrade all policy templates in your account. 
4. Governance Host - "Governance Host, Hostname will match your shard: us-3.rightscale.com = governance-3.rightscale.com". Simply navigate to Cloud Management or open browser developer console to see the hostname of the API calls. 

### Required Roles
1. For `Email` Escalation option, either: `policy_manager` or `policy_designer`
2. For `Email and Upload` Escalation option: `policy_designer`

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
