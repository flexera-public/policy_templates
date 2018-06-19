## Policy Template Synchronization Policy Template

### What it does

This Policy Template uses a json file stored in the github directory to determine a set of active policies, and versions. It then compares those
 policies with your current account policy versions, and alerts on difference. 

### Usage
The Policy Template Synchronization Policy Template will need to be uploaded to your account and set active. There are currently two escalation options: `Email`,
and `Email and Upload`. When you choose `Email` you will get an alert on the the policy templates that can be updated, and no further action will be taken. 
When you choose `Email and Upload`, you will get an alert on the policy templates that can be updated and we will upload those policies to your account. 

#### Scenarios
1. Existing Templates
   1. Versions are the same: `No Action Taken`
   2. Versions are different: `Escalate`
   3. Versions are the same, but Force Upgrade = 1: `Escalate`
2. Templates Do Not Existing
   1. `Escalate`

### Parameters

#### Policy Template Synchronization Policy Template
1. Email addresses of the recipients you wish to notify - Ex: noreply@example.compares
2. Escalation Options - Allowed Values: "Email", "Email and Upload"
3. Force Upgrade - Allowed Values: 0:False, 1:True - Setting this to 1 will force upgrade all policy templates in your account. 
4. Governance Host - "Governance Host, Hostname will match your shard: us-3.rightscale.com = governance-3.rightscale.com"

### Required Roles
1. policy_designer

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
