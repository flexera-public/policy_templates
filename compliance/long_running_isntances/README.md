## Long Running Instances 


### What it does

This policy template checks all instances running, and checks them against a user provided number of days.  If the instance has been running longer than the specified number of days then the policy reports those instances for termination, and seeks approval before termination.  The policy accepts using tags to not include instances.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Days* - How many days is considered long running.
- *Tags to Ignore* - A comma delimited list of tags that indicate the policy should ignore instances with those tags


### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an escalation requiring approval to terminate the instances


### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
