## No Recent Snapshots Policy Template

### What it does
This Policy Template verifies that you have snapshots on all of your important volumes. 

### Usage
**_Warning: This policy will stop your servers to guarantee consistency._**
This policy template has two options: `Email` and `Snapshot And Email`. If you choose `Email` you will get a report of volumes that have missing snapshots within the timeperiod.
If you choose `Snapshot And Email` it will email you a report of volumes that have missing snapshots, and then it will stop the server, wait for completion, take a snapshot and
start up the server. 


### Parameters
1. Email address to send escalation emails to - Example: noreply@example.com
2. Number of days between snapshots - The number of days between snapshots that the policy will check against. 
3. Escalation Options - Allowed Values: "Email", "Snapshot And Email"
4. Include Root Device - This option instructs the policy template whether or not to check root volumes for compliance, anything connected to `/dev/sda1`. 
5. Volume and Server tags to exclude -  Example: snapshot_policy:exclude=1

### Supported Clouds
The following clouds are supported:
- AWS
- Azure
- Google

### Cost
This Policy Template will increase the cost of overall cloud usage by taking snapshots of data. 