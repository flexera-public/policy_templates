## Old Snapshots Policy Template

### What it does

This Policy Template will check your account for old snapshots. It takes several parameters: 
- `Number of days old snapshot to delete` - if a snapshot is older than this parameter it will be added to list
- `Email address to send escalation emails to` - Email to alert when it finds snapshots that meet the criteria
- `Snapshot Tag List` - list of tags that a snapshot can have to exclude it from the list. 

### Supported Clouds

- AWS
- Azure
- Google 

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.