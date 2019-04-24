## AWS Native Utilization Policy

### What it does

This Policy Template checks aws regions configured in RightScale and gets cloudwatch data for instances

### Prerequesites
- The `credential_viewer`,`observer`,`actor` roles
- The `policy_designer`, `policy_manager` & `policy_publisher` roles
- The `CloudWatchReadOnlyAccess` AWS IAM Policy

### Functional Details

- This policy uses RightScale to get a list of instances, it then polls aws cloudwatch for metrics for instance performance and delivers a report. If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics. 

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.