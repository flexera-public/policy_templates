# Google Rightsize VM Instances

## What It Does

This policy template checks all the instances in Google Projects for the average or maximum CPU and/or memory usage over a user-specified number of days. If the usage is less than the user provided Idle Instance CPU and/or memory percentage threshold then the Virtual Machine is recommended for deletion. If the usage is less than the user provided Underutilized Instance CPU and/or Memory percentage threshold, then the Virtual Machine is recommended for downsizing. Both sets of Virtual Machines returned from this policy are emailed to the user.

NOTE: If you prefer to receive recommendations produced by the Google Recommender service rather than Flexera, please use the [Google Rightsize VM Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_vm_recommender) policy template instead of this one.
