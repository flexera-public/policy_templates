## Azure Reserved Instances Recommendation Policy Template

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

### What it does


### Prerequesites

- The following RightScale Credentials
  - `AZURE_EA_KEY` - the Azure EA key for the enrollment being checked

### Input Parameters

This policy has the following input parameters required when launching the policy.


### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Supported Clouds

- Azure

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
