## Downsize Instances Policy Template

### What it does
This Policy Template uses data from the monitoring api to determine is you can decrease the size of your running instance.

### Usage
There are two policy templates required to support this policy, `Downsize Instances Policy Template` and `Downsize Instances Add Tags Policy Template`.
The Downsize Instances Policy Template is used to actually downsize instances. If you chose `Email` from the `Escalation Options`, it will only email you which instances can be downsized.
If you chose `Downsize And Email` from the `Escalation Options`, it will email you a list of servers that were downsized and the size to which were changed. This policy will also resize the instance. This required the instance to be **stopped**.
If a server is marked `N/A`, no action will be taken and only the resize tag will be removed. You will need to manually move that instance to another family type.

### Parameters

#### Downsize Instances Policy Template
1. Average free memory percent to allow for downsize - Value: 0-100, -1 disables this metric
2. Maximum free memory percent to allow for downsize - Value: 0-100, -1 disables this metric
3. Maximum cpu idle percent to allow for downsize - Value: 0-100, -1 disables this metric
4. Average cpu idle percent to allow for downsize - Value: 0-100, -1 disables this metric
5. Instance tags used to filter instances that must validate policy. Example: rs_monitoring:resize=1
6. Email address to send escalation emails to - Example: noreply@example.com
7. Escalation Options - Allowed Values: "Email", "Downsize And Email"
8. Days to cooldown between checks of same machine - Number of days to cooldown between checks of the same instance. This drives the `Downsize Instances Add Tags Policy Template`

#### Downsize Instances Add Tags Policy Template
1. Instance tags used to filter instances that must validate policy. Example: rs_monitoring:resize=1
2. Email address to send escalation emails to - Example: noreply@example.com

### Supported Clouds
The following clouds are supported:
- AWS
- Azure
- Google

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
