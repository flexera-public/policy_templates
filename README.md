# Flexera CMP Policy Templates

This repository contains a library of open source Flexera CMP Policy Templates to provide governance via automation across Cost, Security, Operational, and Compliance categories.  All contributions are shared under the MIT license.

Please contact sales@flexera.com to learn more.

## Released Policy Templates

### Cost

#### Multi-cloud

- [Billing Center Cost Anomaly](./cost/billing_center_cost_anomaly/)
- [Budget Alerts](./cost/budget_alerts/)
- [Budget Alerts by Cloud Account](./cost/budget_alerts_by_account/)
- [Cheaper Regions](./cost/cheaper_regions/)
- [Downsize Instances](./cost/downsize_instance/)
- [Inefficient Instance Utilization using RightLink](./cost/rightlink_rightsize)
- [Old Snapshots](./cost/volumes/old_snapshots/)
- [Running Instance Count Anomaly](./cost/instance_anomaly/)
- [Unattached IP Addresses](./cost/unattached_addresses/)
- [Unattached Volumes](./cost/volumes/unattached_volumes/)
- [Schedule Instances](./cost/schedule_instances/)
- [Scheduled Report](./cost/scheduled_reports/)
- [Scheduled Report with Estimates](./cost/scheduled_reports_with_estimates/)
- [Scheduled Report with Markups & Markdowns](./cost/scheduled_report_markUpsDowns/)
- [Superseded Instances](./cost/superseded_instance/)
- [Superseded Instance Remediation](./cost/superseded_instance_remediation/)
- [Terminate Instances with End Date](./cost/terminate_policy/)

#### AWS

##### Compute

- [AWS Burstable Instance CloudWatch Utilization](./cost/aws/burstable_instance_cloudwatch_credit_utilization/)
- [AWS Expiring Reserved Instances](./cost/aws/reserved_instances/expiration/)
- [AWS Idle Compute Instances](./cost/aws/idle_compute_instances/)
- [AWS Inefficient Instance Utilization using CloudWatch](./cost/aws/instance_cloudwatch_utilization/)
- [AWS Reserved Instances Utilization](./cost/aws/reserved_instances/utilization/)
- [AWS Reserved Instance Reservation Coverage](./cost/aws/reserved_instances/coverage/)
- [AWS Reserved Instances Report by Billing Center](./cost/aws/reserved_instances/report_by_bc)
- [AWS Reserved Instance Recommendations](./cost/aws/reserved_instances/recommendations)
- [AWS Savings Plan Recommendations](./cost/aws/savings_plan/recommendations)
- [AWS Unused IP Addresses](./cost/aws/unused_ip_addresses)

##### Database

- [AWS Unused RDS Instances](./cost/aws/unused_rds/)
- [AWS RDS Instances RightSizing](./cost/aws/rds_instance_cloudwatch_utilization)
- [AWS RDS Instances License Information](./cost/aws/rds_instance_license_info)

##### Load Balancers

- [AWS Delete Unused Elastic Load Balancers (CLB)](./cost/aws/elb/clb_unused/)

##### Storage

- [AWS Bucket Size Check](./cost/aws/s3_bucket_size/)
- [AWS Unused Volumes](./cost/aws/unused_volumes)
- [AWS S3 Buckets without Server Access Logging](./security/storage/aws/s3_buckets_without_server_access_logging/)
- [AWS Object Storage Optimization](./cost/aws/object_storage_optimization/)
- [AWS Old Snapshots](./cost/aws/old_snapshots/)

#### Azure

##### Compute

- [Azure Hybrid Use Benefit](./cost/azure/hybrid_use_benefit/)
- [Azure Idle Compute Instances](./cost/azure/idle_compute_instances/)
- [Azure Inefficient Instance Utilization using Log Analytics](./cost/azure/instances_log_analitics_utilization/)
- [Azure Expiring Reserved Instances](./cost/azure/reserved_instances/expiration)
- [Azure Reserved Instance Utilization](./cost/azure/reserved_instances/utilization/)
- [Azure Reserved Instance Recommendations](./cost/azure/reserved_instances/recommendations)

##### Database

- [Azure Rightsize SQL Instances](./cost/azure/rightsize_sql_instances/)
- [Azure Unused SQL Databases](./cost/azure/unused_sql_databases/)

##### Storage

- [Azure Blob Storage Optimization](./cost/azure/object_storage_optimization/)
- [Azure Old Snapshots](./cost/azure/old_snapshots/)
- [Azure Unused Volumes](./cost/azure/unattached_volumes)

#### Google

##### Compute

- [Google Inefficient Instance Utilization using StackDriver](./cost/google/instances_stackdriver_utilization/)
- [Google Committed Use Discount (CUD)](./cost/google/cud_report/)
- [Google Idle Compute Instances](./cost/google/idle_compute_instances/)
- [Google Expiring Committed Use Discount (CUD)](./cost/google/cud_expiration/)

##### Database

- [Google Unused CloudSQL Instances](./cost/google/unused_cloudsql_instances)
- [Google Rightsize CloudSQL Instances](./cost/google/cloudsql_rightsizing/)

##### Storage

- [Google Object Storage Optimization](./cost/google/object_storage_optimization/)
- [Google Old Snapshots](./cost/google/old_snapshots/)
- [Google Unused Volumes](./cost/google/unattached_volumes/)

##### Other

- [Google Unutilized IP Addresses](./cost/google/unutilized_ip_addresses/)

### Security

#### Multi-cloud

- [Security Group: ICMP Enabled](./security/security_groups/icmp_enabled/)
- [Security Group: Rules Without Description](./security/security_groups/rules_without_descriptions/)
- [Security Group: High Open Ports](./security/security_groups/high_open_ports/)
- [Security Groups With Ports Open To The World](./security/security_groups/world_open_ports)

#### AWS

##### Database

- [AWS Unencrypted RDS Instances](./security/aws/rds_unencrypted/)
- [AWS Publicly Accessible RDS Instances](./security/aws/rds_publicly_accessible/)

##### Storage

- [AWS Open Buckets](./security/storage/aws/public_buckets/)
- [AWS Unencrypted S3 Buckets](./security/aws/unencrypted_s3_buckets/)
- [AWS Unencrypted Volumes](./security/aws/ebs_unencrypted_volumes/)

##### Load Balancers

- [AWS Internet-facing ELBs & ALBs](./security/aws/loadbalancer_internet_facing/)
- [AWS Unencrypted ELB Listeners (CLB)](./security/aws/clb_unencrypted/)
- [AWS Unencrypted ELB Listeners (ALB/NLB)](./security/aws/elb_unencrypted/)

#### Azure

- [Azure Publicly Accessible Managed SQL Instance](./security/azure/sql_publicly_accessible_managed_instance)

#### Google

- [Google Open Buckets](./security/storage/google/public_buckets/)

### Compliance

#### Multi-cloud

- [Billing Center Access](./compliance/billing_center_access_report/)
- [Untagged Resources](./compliance/tags/tag_checker)
- [Unapproved Instance Types](./compliance/unapproved_instance_types/)
- [Disallowed Cloud Images](./compliance/disallowed_images/)

#### AWS

- [AWS Disallowed Regions](./compliance/aws/disallowed_regions/)
- [AWS Unused ECS Clusters](./compliance/aws/ecs_unused/)
- [AWS EC2 Instances not running FlexNet Inventory Agent - Cloud](./compliance/aws/instances_without_fnm_agent/)
- [AWS EC2 Instances not running FlexNet Inventory Agent - On Premise](./compliance/aws/instances_without_fnm_agent_on_premise/)
- [AWS Long-stopped Instances](./compliance/aws/long_stopped_instances/)
- [AWS Service Control Policy Audit](./compliance/aws/scp_audit/)

#### Azure

- [Azure AHUB Utilization with Manual Entry](./compliance/azure/ahub_manual/)
- [Azure Disallowed Regions](./compliance/azure/azure_disallowed_regions)
- [Azure Instances not running FlexNet Inventory Agent - Cloud](./compliance/azure/instances_without_fnm_agent/)
- [Azure Instances not running FlexNet Inventory Agent - On Premise](./compliance/azure/instances_without_fnm_agent_on_premise/)
- [Azure Long Stopped Instances](./compliance/azure/azure_long_stopped_instances)
- [Azure Regulatory Compliance](./compliance/azure/compliance_score/)
- [Azure Subscription Access](./compliance/azure/subscription_access/)
- [Azure Tag Resources with Resource Group Name](./compliance/tags/azure_rg_tags)

#### Google

- [Google Long-Stopped Instances](./compliance/google/long_stopped_instances)

#### Other

- [FlexNet Manager Licenses At Risk - Cloud](./compliance/fnms/fnms_licenses_at_risk/)
- [FlexNet Manager Licenses At Risk - On Premise](./compliance/fnms/fnms_licenses_at_risk_on_premise/)
- [FlexNet Manager Low Available Licenses](./compliance/fnms/fnms_low_licenses_available)
- [GitHub.com Available Seats](./compliance/github/available_seats/)
- [GitHub.com Unpermitted Outside Collaborators](./compliance/github/outside_collaborators/)
- [GitHub.com Unpermitted Repository Names](./compliance/github/repository_naming/)
- [GitHub.com Unpermitted Top-Level Teams](./compliance/github/toplevel_teams/)
- [GitHub.com Unpermitted Sized Repositories](./compliance/github/repository_size/)
- [GitHub.com Repository Branches without Protection](./compliance/github/repository_branch_protection/)
- [GitHub.com Repositories without Admin Team](./compliance/github/repository_admin_team/)

### Operational

#### Multi-cloud

- [Application Migration Recommendations](./operational/compute_instance_migration/)
- [No Recent Snapshots](./operational/snapshots/)
- [Stranded Servers](./operational/stranded_servers/)
- [NetFlow Top Talkers](./operational/azure/network_flow)

#### AWS

- [AWS Cloud Credentials Rotation](./operational/cloud_credentials/aws)
- [AWS RDS Backup Settings](./operational/dbaas/aws/rds_backup)
- [AWS Subnet Name Tag Sync](./operational/aws/subnet_name_sync)
- [AWS VPC Name Tag Sync](./operational/aws/vpc_name_sync)
- [AWS Long Running Instances](./operational/aws/long_running_instances/)
- [AWS Instance Scheduled Events](./operational/aws/instance_scheduled_events)

#### Azure

- [Azure VMs Not Using Managed Disks](./operational/azure/vms_without_managed_disks/)
- [Azure Migrate Integration](./operational/azure/azure_migrate)
- [AzureAD Group Sync](./operational/azure/azuread_group_sync/)
- [Azure Sync Tags with Optima](./operational/azure/sync_tags_with_optima/)

#### VMWare

- [VMWare Instance Tag Sync](./operational/vmware/instance_tag_sync)

#### Other

- [Schedule FlexNet Manager Report - Cloud](./operational/fnms/schedule_fnms_reports/)
- [Schedule FlexNet Manager Report - On Premise](./operational/fnms/schedule_fnms_reports_on_premise/)

### SaaS Management

- [Okta Inactive Users](./saas/okta/inactive_users)
- [ServiceNow Inactive Approvers](./saas/servicenow/inactive_approvers)
- [Office 365 Security Alerts](./saas/office365/security_alerts)
- [SaaS Manager - Renewal Reminder](./saas/fsm/renewal_reminder)
- [SaaS Manager - User Status Change](./saas/fsm/user_status_change)
- [SaaS Manager - Suspicious Users](./saas/fsm/suspicious_users)
- [SaaS Manager - Unsanctioned Spend](./saas/fsm/unsanctioned_spend)
- [SaaS Manager - Redundant Apps](./saas/fsm/redundant_apps)
- [SaaS Manager - Inactive Users](./saas/fsm/inactive_users_by_dept)
- [SaaS Manager - Duplicate User Accounts](./saas/fsm/duplicate_users)
- [SaaS Manager - Unsanctioned Applications with Existing Contract](./saas/fsm/unsanctioned_apps_with_contract)
- [SaaS Manager - SaaS App User Report by Category](./saas/fsm/users_by_category)

### Policy Data Sets

- [AWS Regions](./data/aws/regions.json)
- [AWS Instance Types](./data/aws/instance_types.json)
- [Azure Instance Types](./data/azure/instance_types.json)
- [Google Instance Types](./data/google/instance_types.json)
- [Currency Reference](./cost/scheduled_reports/currency_reference.json)
- [Azure SQL Service Tier Types](./data/azure/sql_service_tier_types.json)

## Instructions to upload policy templates to Flexera CMP Policies

- The policy templates in the repo are the files that have a .pt extension.
- Select the desired policy template, click on the “Raw” button, and then right-click and choose “Save As” to save the file to your computer.
- To upload the template to your account, navigate over to the Templates page in the left nav bar in [Governance](https://governance.rightscale.com). Ensure you have the role to access policy management in RightScale. Learn More about [Policy Access Control](http://docs.rightscale.com/policies/#how-policies-work-access-control).
- Click the “Upload Policy Template” button in the account you wish to test the policy and follow the instructions to upload the template you just downloaded.

## Policy Template Documentation

- [Getting Started](http://docs.rightscale.com/policies/getting_started/)
- [Reference Documentation](http://docs.rightscale.com/policies/reference/)
- [Policy Template Language](http://docs.rightscale.com/policies/reference/policy_template_language.html)
- [Markdown Editor](https://jbt.github.io/markdown-editor/) - Use this to test Markdown Syntax
- [Libraries](./libraries/README.md)
- [README GUIDELINE](./README_GUIDELINE.md)

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
