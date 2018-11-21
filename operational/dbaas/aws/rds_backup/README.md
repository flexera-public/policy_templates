## AWS RDS Backup Policy Template

### What it does

This Policy Template will check your account for Amazon RDS Instances with non-compliant backup settings. It takes the following parameters:
- `Email addresses of the recipients you wish to notify` - Email to alert when it finds S3 buckets that meet the criteria.
- `Backup Retention Period` - Example value: `7`
- `Preferred Backup Window` - Example value: `08:00-08:30`

### Supported Clouds

- AWS

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
