## AWS Open Buckets Policy Template

### What it does

This Policy Template will check your account for Amazon S3 buckets with public permission. It takes the following parameter: 
- `Email addresses of the recipients you wish to notify` - Email to alert when it finds S3 buckets that meet the criteria.

#### Slack Channel Notification Support
The policy includes optional support to send a notification to a slack channel when an anomaly is detected.
The policy accepts two optional input parameters to support this capability:
- `Slack Channel Name`: This is the slack channel name, e.g. #policy_alerts
- `RightScale Credential for Slack Channel Webhook`: This is the name of a RightScale credential in the account that contains the Slack webhook URL.

### Supported Clouds

- AWS

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
