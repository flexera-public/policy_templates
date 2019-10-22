# RightScale Policy Templates

This repo contains a library of open source RightScale Policy Templates to provide governance via automation across Cost, Security, Operational, and Compliance categories.  All contributions are shared under the MIT license.

Please contact sales@rightscale.com to learn more.

## Released Policy Templates

### Cost

- [AWS Expiring Reserved Instances](./cost/aws/reserved_instances/expiration/)
- [AWS Reserved Instances Utilization](./cost/aws/reserved_instances/utilization/)
- [AWS Reserved Instance Reservation Coverage](./cost/aws/reserved_instances/coverage/)
- [AWS Reserved Instances Report by Billing Center](./cost/aws/reserved_instances/report_by_bc)
- [AWS Reserved Instance Recommendations](./cost/aws/reserved_instances/recommendations)
- [Azure Superseded Instance Types](./cost/azure/superseded_instance_types/)
- [Budget Alerts](./cost/budget_alerts/)
- [Downsize Instances](./cost/downsize_instance/)
- [Unattached Volumes Policy](./cost/volumes/unattached_volumes/)
- [Old Snapshots](./cost/volumes/old_snapshots/)
- [Schedule Instances](./cost/schedule_instances/)
- [Unattached IP Addresses](./cost/unattached_addresses/)
- [Scheduled Report](./cost/scheduled_reports/)
- [Azure Hybrid Use Benefit](./cost/azure/hybrid_use_benefit/)
- [Azure Reserved Instance Utilization](./cost/azure/reserved_instances/utilization/)
- [Azure Reserved Instance Recommendations](./cost/azure/reserved_instances/recommendations)
- [Billing Center Cost Anomaly](./cost/billing_center_cost_anomaly/)
- [Google Committed Use Discount (CUD)](./cost/google/cud_report/)
- [AWS Delete Unused Elastic Load Balancers (CLB)](./cost/aws/elb/clb_unused/)
- [Cheaper Regions](./cost/cheaper_regions/)
- [Low Account Usage](./cost/low_account_usage/)
- [Low Service Usage](./cost/low_service_usage/)
- [Google Unutilized IP Addresses](./cost/google/unutilized_ip_addresses/)
- [AWS Instance CloudWatch Utilization](./cost/aws/instance_cloudwatch_utilization/)
- [Google StackDriver Utilization](./cost/google/instances_stackdriver_utilization/)
- [Terminate Instances with End Date](./cost/terminate_policy/)
- [Azure Instances Utilization from Log Analytics](./cost/azure/instances_log_analitics_utilization/)
- [Superseded Instances](./cost/superseded_instance/)
- [Superseded Instance Remediation](./cost/superseded_instance_remediation/)
- [AWS S3 Buckets without Server Access Logging](./security/storage/aws/s3_buckets_without_server_access_logging/)
- [AWS Burstable Instance CloudWatch Utilization](./cost/aws/burstable_instance_cloudwatch_credit_utilization/)
- [AWS Bucket Size Check](./cost/aws/s3_bucket_size/)
- [AWS Idle Compute Instances](./cost/aws/idle_compute_instances/)
- [Google Idle Compute Instances](./cost/google/idle_compute_instances/)
- [Running Instance Count Anomaly](./cost/instance_anomaly/)
- [AWS Object Storage Optimization](./cost/aws/object_storage_optimization/)
- [AWS Unused RDS Instances](./cost/aws/unused_rds/)
- [AWS RDS Instances RightSizing](./cost/aws/rds_instance_cloudwatch_utilization)
- [Azure Blob Storage Optimization](./cost/azure/object_storage_optimization/)
- [Google Object Storage Optimization](./cost/google/object_storage_optimization/)
- [Azure Rightsize SQL Instances](./cost/azure/rightsize_sql_instances/)
- [Google Expiring Committed Use Discount (CUD)](./cost/google/cud_expiration/)
- [Azure Expiring Reserved Instances](./cost/azure/reserved_instances/expiration)
- [Azure Idle Compute Instances](./cost/azure/idle_compute_instances/)
- [Google Rightsize CloudSQL Instances](./cost/google/cloudsql_rightsizing/)
- [Google Unused CloudSQL Instances](./cost/google/unused_cloudsql_instances)
- [Monthly Actual v. Budgeted Spend Report](./cost/budget_v_actual/monthly_budget_v_actual.pt/)

### Security

- [Security Group: ICMP Enabled](./security/security_groups/icmp_enabled/)
- [Security Group: Rules Without Description](./security/security_groups/rules_without_descriptions/)
- [Security Group: High Open Ports](./security/security_groups/high_open_ports/)
- [Security Groups With Ports Open To The World](./security/security_groups/world_open_ports)
- [AWS Open Buckets Policy](./security/storage/aws/public_buckets/)
- [Google Open Buckets Policy](./security/storage/google/public_buckets/)
- [AWS Unencrypted Volumes Policy](./security/aws/ebs_unencrypted_volumes/)
- [AWS Internet-facing ELBs & ALBs](./security/aws/loadbalancer_internet_facing/)
- [AWS Unencrypted RDS Instances](./security/aws/rds_unencrypted/)
- [AWS Publicly Accessible RDS Instances](./security/aws/rds_publicly_accessible/)
- [AWS Unencrypted S3 Buckets](./security/aws/unencrypted_s3_buckets/)
- [Check for publicly accessible Azure SQL Managed Instance](./security/azure/sql_publicly_accessible_managed_instance)
- [AWS Unencrypted ELB Listeners (CLB)](./security/aws/clb_unencrypted/)
- [AWS Unencrypted ELB Listeners (ALB/NLB)](./security/aws/elb_unencrypted/)

### Compliance

- [Untagged Resources](./compliance/tags/tag_checker)
- [Azure Disallowed Regions](./compliance/azure/azure_disallowed_regions)
- [Azure: Tag Resources with Resource Group Name](./compliance/tags/azure_rg_tags)
- [Azure: Long Stopped Instances](./compliance/azure/azure_long_stopped_instances)
- [Billing Center Access Report](./compliance/billing_center_access_report/)
- [GitHub.com Available Seats](./compliance/github/available_seats/)
- [GitHub.com Unpermitted Outside Collaborators](./compliance/github/outside_collaborators/)
- [GitHub.com Unpermitted Repository Names](./compliance/github/repository_naming/)
- [GitHub.com Unpermitted Top-Level Teams](./compliance/github/toplevel_teams/)
- [GitHub.com Unpermitted Sized Repositories](./compliance/github/repository_size/)
- [GitHub.com Repository Branches without Protection](./compliance/github/repository_branch_protection/)
- [GitHub.com Repositories without Admin Team](./compliance/github/repository_admin_team/)
- [AWS Unused ECS Clusters](./compliance/aws/ecs_unused/)
- [Unapproved Instance Types](./compliance/unapproved_instance_types/)
- [Azure Subscription Access](./compliance/azure/subscription_access/)
- [Azure AHUB Utilization with Manual Entry](./compliance/azure/ahub_manual/)
- [Azure Instances not running FlexNet Inventory Agent](./compliance/azure/instances_without_fnm_agent/)
- [FlexNet Manager Licenses At Risk](./compliance/fnms/fnms_licenses_at_risk/)

### Operational

- [AWS Cloud Credentials Rotation Policy](./operational/cloud_credentials/aws)
- [No Recent Snapshots](./operational/snapshots/)
- [AWS RDS Backup Settings](./operational/dbaas/aws/rds_backup)
- [AWS VPC Name Tag Sync](./operational/aws/vpc_name_sync)
- [AWS Subnet Name Tag Sync](./operational/aws/subnet_name_sync)
- [Stranded Servers](./operational/stranded_servers/)
- [VMWare Instance Tag Sync](./operational/vmware/instance_tag_sync)
- [Azure VMs Not Using Managed Disks](./operational/azure/vms_without_managed_disks/)
- [Schedule FlexNet Manager report](./operational/fnms/schedule_fnms_reports)

### SaaS Management

- [Okta Inactive Users](./fsm/okta/inactive_users)

### Policy Data Sets

- [AWS Regions](./data/aws/regions.json)
- [AWS Instance Types](./data/aws/instance_types.json)
- [Azure Instance Types](./data/azure/instance_types.json)
- [Google Instance Types](./data/google/instance_types.json)
- [Currency Reference](./cost/scheduled_reports/currency_reference.json)

## Instructions to upload policy templates to RightScale

- The policy templates in the repo are the files that have a .pt extension.
- Select the desired policy template, click on the “Raw” button, and then right-click and choose “Save As” to save the file to your computer.
- To upload the template to your account, navigate over to the Templates page in the left nav bar in [Governance](https://governance.rightscale.com). Ensure you have the role to access policy management in RightScale. Learn More about [Policy Access Control](http://docs.rightscale.com/policies/#how-policies-work-access-control).
- Click the “Upload Policy Template” button in the account you wish to test the policy and follow the instructions to upload the template you just downloaded.

## RightScale Policy Template Documentation

- [Getting Started](http://docs.rightscale.com/policies/getting_started/)
- [Reference Documentation](http://docs.rightscale.com/policies/reference/)
- [Policy Template Language](http://docs.rightscale.com/policies/reference/policy_template_language.html)
- [Markdown Editor](https://jbt.github.io/markdown-editor/) - Use this to test Markdown Syntax
- [Libraries](./libraries/README.md)

## Getting Help

Support for these policy templates will be provided though GitHub Issues and the Flexera Community.
Visit [Flexera Community](https://community.flexera.com) to join!

### Opening an Issue

Github issues contain a template for three types of requests(Bugs, New Features to an existing Policy Template, New Policy Template Request)

- Bugs: Any issue you are having with an existing policy template not functioning correctly, this does not include missing features, or actions.
- New Feature Request: Any feature(Field, Action, Link, Output, etc) that are to be added to an existing policy template.
- New Policy Template Request: Request for a new policy template.

### Troubleshooting Danger Locally

- You can test against a pull request via: `bundle exec danger pr https://github.com/flexera/policy_templates/pull/73 --pry`
- [Danger Troubleshooting](http://danger.systems/guides/troubleshooting.html)
