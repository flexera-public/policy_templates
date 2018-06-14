## Security Group High Open Ports Policy Template

### What it does
This Policy Template leverages the multi cloud RightScale API. It will notify only if a security group has a port higher than  `High Port` field open. 

### Parameters 
1. Email address to send escalation emails to - Example: noreply@example.com
2. Beginning High Port - Any port greater than or equal to this will trigger a report

### Supported Clouds
The following clouds are supported: 
- AWS
- Azure
- Google 

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
