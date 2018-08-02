## Security Group with High Open Ports Policy Template

### What it does

This Policy Template leverages the multi cloud RightScale API. It will notify only if a security group has a port higher than `Beginning High Port` field open. 

### Parameters 

1. Email addresses of the recipients you wish to notify - Example: noreply@example.com
2. Beginning High Port - Any port greater than or equal to this will trigger a report

### Supported Clouds

- AWS
- Azure
- Google 

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
