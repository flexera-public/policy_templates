# Flexera CMP Policy Templates

This repository contains a library of open source Flexera CMP Policy Templates to provide governance via automation across Cost, Security, Operational, and Compliance categories.  All contributions are shared under the MIT license.

Please contact sales@flexera.com to learn more.

## Released Policy Templates

<!-- Begin Policy Template Table of Contents -->
### Categories

- [Optimization](#policy-templates-for-optimization)
- [Compliance](#policy-templates-for-compliance)
- [Cost](#policy-templates-for-cost)
- [Operational](#policy-templates-for-operational)
- [SaaS Management](#policy-templates-for-saas-management)
- [Security](#policy-templates-for-security)

### Policy Templates for Optimization

These templates can generate savings estimates for your environment.

#### AWS

- [AWS Old Snapshots](./cost/aws/old_snapshots)
- [AWS Rightsize Compute Instances](./cost/aws/rightsize_compute_instances)
- [AWS GP3 Upgradeable Volumes](./cost/aws/gp3_volume_upgrade)
- [AWS Unused Volumes](./cost/aws/unused_volumes)
- [AWS Unused IP Addresses](./cost/aws/unused_ip_addresses)
- [AWS Idle Compute Instances](./cost/aws/idle_compute_instances)
- [AWS Unused RDS Instance](./cost/aws/unused_rds)
- [AWS Rightsize EBS Volumes](./cost/aws/rightsize_ebs_volumes)

#### Azure

- [Azure Old Snapshots](./cost/azure/old_snapshots)
- [Azure Rightsize Compute Instances](./cost/azure/rightsize_compute_instances)
- [Azure Unused SQL Databases](./cost/azure/unused_sql_databases)
- [Azure Unused IP Addresses](./cost/azure/unused_ip_addresses)
- [Azure Unused Volumes](./cost/azure/unattached_volumes)
- [Azure Idle Compute Instances](./cost/azure/idle_compute_instances)
- [Azure Savings Plan Recommendations](./cost/azure/savings_plan/recommendations)

#### Google

- [Google Cloud SQL Idle Instance Recommender](./cost/google/cloud_sql_idle_instance_recommendations)
- [Google Idle VM Recommender](./cost/google/idle_vm_recommendations)
- [Google Idle IP Address Recommender](./cost/google/idle_ip_address_recommendations)
- [Google Idle Persistent Disk Recommender](./cost/google/idle_persistent_disk_recommendations)
- [Google Committed Use Discount Recommender](./cost/google/cud_recommendations)

### Policy Templates for Compliance

#### AWS

- [AWS Untagged Resources](./compliance/aws/untagged_resources)

- EC2

  - [AWS Disallowed Regions](./compliance/aws/disallowed_regions)
  - [AWS Long-stopped Instances](./compliance/aws/long_stopped_instances)
  - [AWS EC2 Instances not running FlexNet Inventory Agent](./compliance/aws/instances_without_fnm_agent)

- ECS

  - [AWS Unused ECS Clusters](./compliance/aws/ecs_unused)

- IAM

  - [AWS IAM Role Audit](./compliance/aws/iam_role_audit)

- Org

  - [AWS Service Control Policy Audit](./compliance/aws/scp_audit)

#### Azure

- [Azure Regulatory Compliance](./compliance/azure/compliance_score)
- [Azure Untagged Resources](./compliance/azure/azure_untagged_resources)
- [Azure Tag Resources with Resource Group Name](./compliance/tags/azure_rg_tags)

- Compute

  - [Azure AHUB Utilization with Manual Entry](./compliance/azure/ahub_manual)
  - [Azure Disallowed Regions](./compliance/azure/azure_disallowed_regions)
  - [Azure Instances not running FlexNet Inventory Agent](./compliance/azure/instances_without_fnm_agent)
  - [Azure Long Stopped Instances](./compliance/azure/azure_long_stopped_instances)

- Identity

  - [Azure Subscription Access](./compliance/azure/subscription_access)

- Policy

- [Azure Guest Users Audit](./security/azure/guest_users/)

##### Database

- [Azure Publicly Accessible Managed SQL Instance](./security/azure/sql_publicly_accessible_managed_instance/)

###### CIS Policies

- [Azure Ensure Correct PostgreSQL Servers Log Settings](./security/azure/pg_log_settings/)
- [Azure Ensure MySQL Flexible Servers Use Secure TLS](./security/azure/mysql_tls_version/)
- [Azure Ensure MySQL Servers Enforce SSL Connections](./security/azure/mysql_ssl/)
- [Azure Ensure PostgreSQL Servers Connection Throttling Enabled](./security/azure/pg_conn_throttling/)
- [Azure Ensure PostgreSQL Servers Infrastructure Encryption](./security/azure/pg_infra_encryption/)
- [Azure Ensure PostgreSQL Servers Sufficient Log Retention](./security/azure/pg_log_retention/)
- [Azure Ensure SQL Database Encryption](./security/azure/sql_db_encryption/)
- [Azure Ensure SQL Server AD Admin Configured](./security/azure/sql_ad_admin/)
- [Azure Ensure SQL Server ATP (Advanced Threat Protection) Enabled](./security/azure/sql_server_atp/)
- [Azure Ensure SQL Server Auditing Enabled](./security/azure/sql_server_auditing/)
- [Azure Ensure SQL Server Minimum Auditing Retention Of 90 Days](./security/azure/sql_auditing_retention/)
- [Azure Ensure SQL Server VA Email Notifications](./security/azure/sql_server_va_emails/)
- [Azure Ensure SQL Server VA Notify Admins/Subscription Owners](./security/azure/sql_server_va_admins/)
- [Azure Ensure SQL Server VA Periodic Scans Enabled](./security/azure/sql_server_va_scans/)
- [Azure Ensure SQL Server Vulnerability Assessment (VA) Enabled](./security/azure/sql_server_va/)

##### Web Apps

- [Azure Web App Minimum TLS Version](./security/azure/webapp_tls_version_support/)

##### Storage

- [Azure Storage Accounts Without HTTPs Enforced](./security/storage/azure/storage_account_https_enabled/)

###### CIS Policies

- [Azure Ensure Storage Account Default Network Access Set To Deny](./security/azure/storage_network_deny/)
- [Azure Ensure Blob Containers Set To Private](./security/azure/private_blob_containers/)
- [Azure Ensure Storage Logging Enabled For Blob Service](./security/azure/blob_storage_logging/)
- [Azure Ensure Storage Logging Enabled For Queue Service](./security/azure/queue_storage_logging/)
- [Azure Ensure Storage Logging Enabled For Table Service](./security/azure/table_storage_logging/)
- [Azure Ensure Secure Transfer Required](./security/azure/secure_transfer_required/)
- [Azure Ensure Soft Delete Enabled For Azure Storage](./security/azure/storage_soft_delete/)
- [Azure Ensure Storage Accounts Require Secure TLS Version](./security/azure/storage_tls_version/)
- [Azure Ensure Trusted Microsoft Services Enabled](./security/azure/storage_trusted_services/)

##### Security

###### CIS Policies

- [Azure Ensure Owners Receive Security Alerts](./security/azure/security_alert_owners/)
- [Azure Ensure High Severity Alerts](./security/azure/high_severity_alerts/)
- [Azure Ensure Security Contact Email](./security/azure/security_contact_email/)
- [Azure Network Security Groups With Inbound RDP Open](./security/azure/restrict_rdp_internet/)
- [Azure Network Security Groups With Inbound SSH Open](./security/azure/restrict_ssh_internet/)

#### Google

- [Google Open Buckets](./security/storage/google/public_buckets/)

### Compliance

#### Flexera

- IAM

  - [Flexera IAM Explicit User Roles](./compliance/flexera/iam_explicit_user_roles)

#### Flexera Cloud Management

- [Policy Update Notification](./compliance/policy_update_notification)

#### Flexera FNMS

- [ITAM Overused Licenses](./compliance/fnms/overused_licenses)

#### Flexera ITAM

- [ITAM Expiring Licenses](./compliance/fnms/fnms_licenses_expiring)
- [ITAM Missing Active Machines](./compliance/fnms/missing_active_machines)
- [ITAM VMs Missing Host ID](./compliance/fnms/vms_missing_hostid)
- [ITAM Ignored Recent Inventory Dates](./compliance/fnms/ignored_recent_inventory_dates)

#### Flexera Optima

- [Billing Center Access Report](./compliance/billing_center_access_report)

#### GCE

- Compute

  - [Google Long-stopped instances](./compliance/google/long_stopped_instances)

#### GitHub

- [GitHub.com Available Seats Report](./compliance/github/available_seats)
- [GitHub.com Repository Branches without Protection](./compliance/github/repository_branch_protection)
- [GitHub.com Unpermitted Top-Level Teams](./compliance/github/toplevel_teams)
- [GitHub.com Unpermitted Sized Repositories](./compliance/github/repository_size)
- [GitHub.com Unpermitted Outside Collaborators](./compliance/github/outside_collaborators)
- [GitHub.com Unpermitted Repository Names](./compliance/github/repository_naming)
- [GitHub.com Repositories without Admin Team](./compliance/github/repository_admin_team)

#### Google

- [Google Unlabeled Resources](./compliance/google/unlabeled_resources)

### Policy Templates for Cost

####

- [Currency Conversion](./cost/currency_conversion)

#### AWS

- [AWS Savings Plan Recommendations](./cost/aws/savings_plan/recommendations)
- [AWS Savings Plan Utilization](./cost/aws/savings_plan/utilization)

- Compute

  - [AWS Rightsize Compute Instances](./cost/aws/rightsize_compute_instances)

- EBS

  - [AWS GP3 Upgradeable Volumes](./cost/aws/gp3_volume_upgrade)
  - [AWS Unused Volumes](./cost/aws/unused_volumes)

- EC2

  - [AWS Schedule Instance](./cost/aws/schedule_instance)
  - [AWS Unused IP Addresses](./cost/aws/unused_ip_addresses)
  - [AWS Burstable Instance CloudWatch Utilization](./cost/aws/burstable_instance_cloudwatch_credit_utilization)
  - [AWS Reserved Instances Recommendations](./cost/aws/reserved_instances/recommendations)
  - [Reserved Instances Coverage](./cost/aws/reserved_instances/coverage)
  - [AWS Idle Compute Instances](./cost/aws/idle_compute_instances)
  - [AWS Inefficient Instance Utilization using CloudWatch](./cost/aws/instance_cloudwatch_utilization)
  - [AWS Rightsize EBS Volumes](./cost/aws/rightsize_ebs_volumes)

- ELB

  - [AWS Delete Unused Classic Load Balancers](./cost/aws/elb/clb_unused)

- RDS

  - [AWS RDS Instances](./cost/aws/rds_instance_license_info)
  - [AWS Rightsize RDS Instances](./cost/aws/rds_instance_cloudwatch_utilization)
  - [AWS Unused RDS Instance](./cost/aws/unused_rds)

- S3

  - [AWS S3 Bucket Intelligent Tiering Check](./cost/aws/s3_storage_policy)
  - [AWS Bucket Size Check](./cost/aws/s3_bucket_size)
  - [AWS Object Storage Optimization](./cost/aws/object_storage_optimization)

- Storage

  - [AWS Old Snapshots](./cost/aws/old_snapshots)

#### Azure

- [Azure Hybrid Use Benefit for Windows Server](./cost/azure/hybrid_use_benefit)
- [Azure Reserved Instances Recommendations](./cost/azure/reserved_instances/recommendations)
- [Azure Savings Plan Utilization](./cost/azure/savings_plan/utilization)

- Blob Store

  - [Azure Blob Storage Optimization](./cost/azure/object_storage_optimization)

- Compute

  - [Azure Rightsize Compute Instances](./cost/azure/rightsize_compute_instances)
  - [Azure Inefficient Instance Utilization using Log Analytics](./cost/azure/instances_log_analytics_utilization)
  - [Azure Schedule Instance](./cost/azure/schedule_instance)
  - [Azure Unused IP Addresses](./cost/azure/unused_ip_addresses)
  - [Azure Reserved Instances Recommendations](./cost/azure/reserved_instances/mca_recommendations)
  - [Azure Reserved Instances Utilization](./cost/azure/reserved_instances/utilization)
  - [Azure Idle Compute Instances](./cost/azure/idle_compute_instances)
  - [Azure Savings Plan Recommendations](./cost/azure/savings_plan/recommendations)

- SQL

  - [Azure Rightsize SQL Databases](./cost/azure/rightsize_sql_instances)
  - [Azure Unused SQL Databases](./cost/azure/unused_sql_databases)
  - [Azure SQL Databases without Elastic Pools](./operational/azure/azure_sql_using_elastic_pool)

- Storage

  - [Azure Old Snapshots](./cost/azure/old_snapshots)
  - [Azure Unused Volumes](./cost/azure/unattached_volumes)

- Storage Accounts

  - [Azure Storage Accounts without Lifecycle Management Policies](./cost/azure/storage_account_lifecycle_management)

- compute

  - [Azure Hybrid Use Benefit for Linux Server](./cost/azure/hybrid_use_benefit_linux)
  - [Azure Hybrid Use Benefit for SQL](./cost/azure/hybrid_use_benefit_sql)

#### Azure China

- N/A

  - [Azure China Common Bill Ingestion](./cost/azure/azure_china_cbi)

#### Flexera

- All

  - [Azure Savings Realized from Reservations](./cost/azure/savings_realized)
  - [AWS Savings Realized from Reservations](./cost/aws/savings_realized)

#### Flexera Cloud Management

- [Inefficient Instance Utilization using RightLink Add Tags](./cost/rightlink_rightsize)

#### Flexera Optima

- [Low Account Usage](./cost/low_account_usage)
- [Azure Expiring Reserved Instances](./cost/azure/reserved_instances/expiration)
- [Monthly Actual v. Budgeted Spend Report](./cost/budget_v_actual)
- [Budget Alerts](./cost/budget_report_alerts)
- [New Service Usage](./cost/new_service_usage)
- [Cloud Cost Anomaly Alerts](./cost/cloud_cost_anomaly_alerts)
- [Superseded Instances](./cost/superseded_instance)
- [Budget Alerts by Cloud Account](./cost/budget_alerts_by_account)
- [Reserved Instance Report by Billing Center](./cost/aws/reserved_instances/report_by_bc)
- [AWS Reserved Instances Utilization](./cost/aws/reserved_instances/utilization)
- [AWS Reserved Instances Recommendations with Purchase](./cost/aws/reserved_instances/compute_purchase_recommendation)
- [AWS Expiring Reserved Instances](./cost/aws/reserved_instances/expiration)
- [AWS Expiring Savings Plans](./cost/aws/savings_plan/expiration)
- [Vendor Commitment Forecast](./cost/forecasting/commitment_forecast)
- [Cloud Spend Forecast - Straight-Line (Simple Model)](./cost/forecasting/straight_line_forecast/simple)
- [Cloud Spend Forecast - Straight-Line (Linear Regression Model)](./cost/forecasting/straight_line_forecast/linear_regression)
- [Cloud Spend Forecast - Moving Average](./cost/forecasting/moving_average)
- [Cheaper Regions](./cost/cheaper_regions)
- [Low Service Usage](./cost/low_service_usage)
- [Scheduled Report](./cost/scheduled_reports)
- [Budget Alerts (Legacy)](./cost/budget_alerts)
- [Master Org Cost Policy with Currency Conversion](./msp/cost/master_org_cost_policy_currency)
- [Master Org Cost Policy](./msp/cost/master_org_cost_policy)

#### GCE

- [Google Unutilized IP Addresses](./cost/google/unutilized_ip_addresses)

- Compute

  - [Google Expiring Committed Use Discount (CUD)](./cost/google/cud_expiration)
  - [Google Schedule Instance](./cost/google/schedule_instance)
  - [Google Inefficient Instance Utilization using StackDriver](./cost/google/instances_stackdriver_utilization)
  - [Google Idle Compute Instances](./cost/google/idle_compute_instances)
  - [Google Committed Use Discount (CUD)](./cost/google/cud_report)

- SQL

  - [Google Rightsize CloudSQL Instances](./cost/google/cloudsql_rightsizing)
  - [Google Unused CloudSQL Instances](./cost/google/unused_cloudsql_instances)

- Storage

  - [Google Object Storage Optimization](./cost/google/object_storage_optimization)

#### Google

- Compute

  - [Google Idle VM Recommender](./cost/google/idle_vm_recommendations)
  - [Google Idle IP Address Recommender](./cost/google/idle_ip_address_recommendations)
  - [Google Committed Use Discount Recommender](./cost/google/cud_recommendations)

- SQL

  - [Google Cloud SQL Idle Instance Recommender](./cost/google/cloud_sql_idle_instance_recommendations)

- Storage

  - [Google Old Snapshots](./cost/google/old_snapshots)
  - [Google Unused Volumes](./cost/google/unattached_volumes)
  - [Google Recommender Policy](./cost/google/recommender)
  - [Google Idle Persistent Disk Recommender](./cost/google/idle_persistent_disk_recommendations)

#### Oracle

- Common Bill Ingestion

  - [Oracle Cloud Common Bill Ingestion](./cost/oracle/oracle_cbi)

### Policy Templates for Operational

#### AWS

- EC2

  - [AWS Long Running Instances](./operational/aws/long_running_instances)
  - [AWS Instance Scheduled Events](./operational/aws/instance_scheduled_events)

- Lambda

  - [AWS Lambda Functions with high error rate](./operational/aws/lambda_functions_with_high_error_rate)

- RDS

  - [AWS RDS Backup Settings](./operational/dbaas/aws/rds_backup)

- Tags

  - [AWS Tag Cardinality Report](./operational/aws/tag_cardinality)

#### Azure

- [Azure Sync Tags with Optima](./operational/azure/sync_tags_with_optima)

- AKS

  - [AKS Node Pools Without Autoscaling](./operational/azure/aks_nodepools_without_autoscaling)
  - [AKS Node Pools Without Zero Autoscaling](./operational/azure/aks_nodepools_without_zero_autoscaling)

- Compute

  - [Azure Long Running Instances](./operational/azure/azure_long_running_instances)
  - [Azure Migrate Integration](./operational/azure/azure_migrate)
  - [Azure VMs Not Using Managed Disks](./operational/azure/vms_without_managed_disks)
  - [Expiring Azure Certificates](./operational/azure/azure_certificates)

- Tags

  - [Azure Tag Cardinality Report](./operational/azure/tag_cardinality)

#### Flexera

- FNMS

  - [Schedule FlexNet Manager Report](./operational/fnms/schedule_fnms_reports)

#### Flexera Cloud Management

- [Bill Processing Error Notification](./operational/bill_processing_errors_notification)
- [Applied Policy Error Notification](./operational/applied_policy_error_notification)

#### Flexera Optima

- [AWS Usage Forecast - Number of Instance Hours Used](./operational/aws/total_instance_hours_forecast)
- [AWS Usage Report - Number of Instance Hours Used](./operational/aws/total_instance_hours)
- [AWS Usage Forecast - Number of Instance vCPUs Used](./operational/aws/total_instance_vcpus_forecast)
- [AWS Usage Report - Number of Instance vCPUs Used](./operational/aws/total_instance_vcpus)

#### Flexera RISC

- [NetFlow Top Talkers](./operational/azure/network_flow)
- [Application Migration Recommendations](./operational/compute_instance_migration)

### Policy Templates for SaaS Management

#### Flexera

- All

  - [SaaS Manager - Inactive Users for Integrated Applications](./saas/fsm/inactive_users_for_integrated_apps)

#### Flexera SaaS Manager

- [SaaS Manager - Inactive Users by Department](./saas/fsm/inactive_users_by_dept)
- [SaaS Manager - Redundant Apps](./saas/fsm/redundant_apps)
- [SaaS Manager - Unsanctioned Applications with Existing Contract](./saas/fsm/unsanctioned_apps_with_contract)
- [SaaS Manager - Duplicate User Accounts](./saas/fsm/duplicate_users)
- [SaaS Manager - Renewal Reminder](./saas/fsm/renewal_reminder)
- [SaaS Manager - Suspicious Users](./saas/fsm/suspicious_users)
- [SaaS Manager - SaaS App User Report by Category](./saas/fsm/users_by_category)
- [SaaS Manager - Unsanctioned Spend](./saas/fsm/unsanctioned_spend)
- [SaaS Manager - User Status Change](./saas/fsm/user_status_change)

#### Microsoft

- Office 365

  - [Office 365 Security Alerts](./saas/office365/security_alerts)

#### Okta

- [Okta Inactive Users](./saas/okta/inactive_users)

#### ServiceNow

- [ServiceNow Inactive Approvers](./saas/servicenow/inactive_approvers)

### Policy Templates for Security

#### AWS

- CloudTrail

  - [AWS Ensure CloudTrail S3 Buckets Non-Public](./security/aws/log_ensure_cloudtrail_bucket_not_public)
  - [AWS Ensure CloudTrail Logs Encrypted At Rest](./security/aws/log_ensure_cloudtrail_encrypted)
  - [AWS Ensure Object-level Events Logging Enabled For CloudTrails](./security/aws/log_ensure_cloudtrail_bucket_object_logging)
  - [AWS Ensure Log File Validation Enabled For All CloudTrails](./security/aws/log_file_validation_enabled)
  - [AWS Ensure CloudTrail Enabled In All Regions](./security/aws/log_ensure_cloudtrail_multiregion)
  - [AWS Ensure CloudTrail S3 Buckets Have Access Logging](./security/aws/log_ensure_cloudtrail_bucket_access_logging)
  - [AWS Ensure CloudTrail Integrated With Cloudwatch](./security/aws/log_cloudtrail_cloudwatch_integrated)

- Config

  - [AWS Ensure AWS Config Enabled In All Regions](./security/aws/aws_config_enabled)

- DBS

  - [AWS EBS Ensure Encryption By Default](./security/aws/ebs_ensure_encryption_default)

- EBS

  - [AWS Unencrypted Volumes](./security/aws/ebs_unencrypted_volumes)

- ELB

  - [AWS Internet-facing ELBs & ALBs](./security/aws/loadbalancer_internet_facing)
  - [AWS Unencrypted ELB Listeners (CLB)](./security/aws/clb_unencrypted)
  - [AWS Unencrypted ELB Listeners (ALB/NLB)](./security/aws/elb_unencrypted)

- IAM

  - [AWS IAM Report Root Account Access Keys](./security/aws/iam_no_root_access_keys)
  - [AWS IAM Ensure Credentials Unused For >45 days Are Disabled](./security/aws/iam_disable_45_day_creds)
  - [AWS IAM Ensure One Active Key Per IAM User](./security/aws/iam_one_active_key_per_user)
  - [AWS IAM Support Role Created](./security/aws/iam_support_role_created)
  - [AWS IAM Report Regions Without Access Analyzer](./security/aws/iam_access_analyzer_enabled)
  - [AWS IAM Report Root Accounts Without Hardware MFA](./security/aws/iam_hwmfa_enabled_for_root)
  - [AWS IAM Report Root Accounts Without MFA](./security/aws/iam_mfa_enabled_for_root)
  - [AWS IAM Ensure One Active Key Per IAM User](./security/aws/iam_users_perms_via_groups_only)
  - [AWS IAM Report Root User Doing Everyday Tasks](./security/aws/iam_no_root_for_tasks)
  - [AWS IAM Report Insufficient Password Policy](./security/aws/iam_min_password_length)
  - [AWS IAM Report Attached Admin IAM Policies](./security/aws/iam_no_admin_iam_policies_attached)
  - [AWS IAM Ensure MFA Enabled For IAM Users](./security/aws/iam_mfa_enabled_for_iam_users)
  - [AWS IAM Ensure Access Keys Are Rotated](./security/aws/iam_rotate_access_keys)
  - [AWS IAM Report Password Policy No Restrict Password Reuse](./security/aws/iam_prevent_password_reuse)
  - [AWS IAM Report Expired SSL/TLS Certificates](./security/aws/iam_expired_ssl_certs)

- KMS

  - [AWS Ensure Rotation For Customer Master Keys (CMKs) Is Enabled](./security/aws/kms_rotation)

- RDS

  - [AWS Unencrypted RDS Instances](./security/aws/rds_unencrypted)
  - [AWS Publicly Accessible RDS Instances](./security/aws/rds_publicly_accessible)

- S3

  - [AWS S3 Buckets without Server Access Logging](./security/storage/aws/s3_buckets_without_server_access_logging)
  - [AWS Open Buckets](./security/storage/aws/public_buckets)
  - [AWS Unencrypted S3 Buckets](./security/aws/unencrypted_s3_buckets)
  - [AWS S3 Ensure 'Block Public Access' Configured For All Buckets](./security/aws/s3_ensure_buckets_block_public_access)
  - [AWS S3 Ensure MFA Delete Enabled For All Buckets](./security/aws/s3_ensure_mfa_delete_enabled)
  - [AWS S3 Ensure Bucket Policies Deny HTTP Requests](./security/aws/s3_buckets_deny_http)

- VPC

  - [AWS VPC's without FlowLogs Enabled](./security/aws/vpcs_without_flow_logs_enabled)

#### Azure

- App Service

  - [Azure Web App Minimum TLS Version](./security/azure/webapp_tls_version_support)

- IAM

  - [Azure Ensure Log Analytics Auto-Provisioning](./security/azure/log_analytics_autoprovision)
  - [Azure Guest Users Audit](./security/azure/guest_users)

- MySQL

  - [Azure Ensure MySQL Servers Enforce SSL Connections](./security/azure/mysql_ssl)
  - [Azure Ensure MySQL Flexible Servers Use Secure TLS](./security/azure/mysql_tls_version)

- Network Security Group

  - [Azure Network Security Groups With Inbound SSH Open](./security/azure/restrict_ssh_internet)
  - [Azure Network Security Groups With Inbound RDP Open](./security/azure/restrict_rdp_internet)

- PostgreSQL

  - [Azure Ensure Correct PostgreSQL Servers Log Settings](./security/azure/pg_log_settings)
  - [Azure Ensure PostgreSQL Servers Connection Throttling Enabled](./security/azure/pg_conn_throttling)
  - [Azure Ensure PostgreSQL Servers Infrastructure Encryption](./security/azure/pg_infra_encryption)

- SQL

  - [Azure Ensure SQL Server VA Periodic Scans Enabled](./security/azure/sql_server_va_scans)
  - [Azure Ensure SQL Server VA Notify Admins/Subscription Owners](./security/azure/sql_server_va_admins)
  - [Azure Ensure SQL Server Auditing Enabled](./security/azure/sql_server_auditing)
  - [Azure Ensure SQL Server VA Email Notifications](./security/azure/sql_server_va_emails)
  - [Azure Ensure SQL Server AD Admin Configured](./security/azure/sql_ad_admin)
  - [Azure Publicly Accessible Managed SQL Instance](./security/azure/sql_publicly_accessible_managed_instance)
  - [Azure Ensure SQL Server Vulnerability Assessment (VA) Enabled](./security/azure/sql_server_va)

- Security

  - [Azure Ensure Security Contact Email](./security/azure/security_contact_email)
  - [Azure Ensure Owners Receive Security Alerts](./security/azure/security_alert_owners)
  - [Azure Ensure High Severity Alerts](./security/azure/high_severity_alerts)

- Storage

  - [Azure Ensure Secure Transfer Required](./security/azure/secure_transfer_required)
  - [Azure Ensure Storage Logging Enabled For Table Service](./security/azure/table_storage_logging)
  - [Azure Ensure Storage Accounts Require Secure TLS Version](./security/azure/storage_tls_version)
  - [Azure Ensure Soft Delete Enabled For Azure Storage](./security/azure/storage_soft_delete)
  - [Azure Ensure Storage Logging Enabled For Blob Service](./security/azure/blob_storage_logging)
  - [Azure Ensure Storage Account Default Network Access Set To Deny](./security/azure/storage_network_deny)
  - [Azure Ensure Blob Containers Set To Private](./security/azure/private_blob_containers)
  - [Azure Ensure Trusted Microsoft Services Enabled](./security/azure/storage_trusted_services)
  - [Azure Ensure Storage Logging Enabled For Queue Service](./security/azure/queue_storage_logging)

- Storage Accounts

  - [Azure Storage Accounts Without HTTPs Enforced](./security/storage/azure/storage_account_https_enabled)

- compute

  - [Azure Resources with public IP address](./security/azure/resources_with_public_ip_address)

#### GCE

- Storage

  - [Google Open Buckets](./security/storage/google/public_buckets)

<!-- Begin Policy Template Stats -->
<!--
---
:total_count: 225
:optimization_count: 20
:categories:
  Security: 70
  Cost: 87
  Compliance: 33
  Operational: 22
  SaaS Management: 13
:providers:
  Azure: 68
  GCE: 11
  AWS: 71
  Flexera Optima: 28
  Azure China: 1
  Flexera: 5
  Google: 9
  '': 1
  Oracle: 1
  Flexera Cloud Management: 4
  Flexera ITAM: 4
  Flexera FNMS: 1
  GitHub: 7
  Flexera RISC: 2
  Microsoft: 1
  Flexera SaaS Manager: 9
  Okta: 1
  ServiceNow: 1
:services:
  MySQL: 2
  Storage: 18
  SQL: 13
  App Service: 1
  Network Security Group: 2
  IAM: 19
  PostgreSQL: 3
  compute: 3
  Security: 3
  Storage Accounts: 2
  S3: 9
  RDS: 6
  CloudTrail: 7
  VPC: 1
  ELB: 4
  DBS: 1
  Config: 1
  KMS: 1
  EBS: 3
  '': 70
  Compute: 26
  N/A: 1
  All: 3
  Blob Store: 1
  Common Bill Ingestion: 1
  EC2: 13
  Identity: 1
  Policy: 1
  Org: 1
  ECS: 1
  FNMS: 1
  AKS: 2
  Tags: 2
  Lambda: 1
  Office 365: 1
:policy_sets:
  CIS: 57
  '': 89
  Public Database Access: 2
  Storage Security: 1
  Open Buckets: 2
  AWS Config: 1
  Old Snapshots: 3
  Rightsize Compute Instances: 2
  RightSize Database Services: 2
  Inefficient Instance Usage: 3
  Schedule Instance: 3
  Unused Database Services: 3
  Unused IP Addresses: 4
  Unused Volumes: 4
  Common Bill Ingest: 1
  Reserved Instance: 3
  Idle Compute Instances: 4
  N/A: 3
  Savings Plan: 2
  Object Store Optimization: 3
  Lifecycle Management: 1
  Unused Database Service: 1
  Native Recommendations: 1
  Rightsize Database Services: 1
  Committed Use Discount: 1
  Common Bill Ingestion: 1
  GP3 Volumes: 1
  Inefficient Disk Usage: 1
  Forecasting: 4
  ITAM: 4
  Disallowed Regions: 2
  Untagged Resources: 1
  Instances not running FlexNet Inventory Agent: 2
  Long Stopped Instances: 3
  Unlabeled Resources: 1
  Untagged resources: 1
  Schedule Report: 1
  Long Running Instances: 3
  Database Services: 1
  Tag Cardinality: 2
-->
<!-- End Policy Template Stats -->

<!-- End Policy Template Table of Contents -->

## Tools

 - [Flexera Automation CloudFormation Template](./tools/cloudformation-template)
 - [`fpt` Command Line Tool](https://github.com/flexera-public/policy_sdk/tree/master/cmd/fpt)

## Policy Data Sets

Some policies require external data sets to function.  These data sets are stored in the [data](./data) directory.  The following data sets are available:

- [AWS Regions](./data/aws/regions.json)
- [AWS Instance Types](./data/aws/instance_types.json)
- [Azure Instance Types](./data/azure/instance_types.json)
- [Google Instance Types](./data/google/instance_types.json)
- [Currency Reference](./cost/scheduled_reports/currency_reference.json)
- [Azure SQL Service Tier Types](./data/azure/sql_service_tier_types.json)
- [TZ database Timezone List](./data/tz_database/timezones_list.json)

## Instructions to upload policy templates to Flexera CMP Policies

- The policy templates in the repo are the files that have a .pt extension.
- Select the desired policy template, click on the “Raw” button, and then right-click and choose “Save As” to save the file to your computer.
- To upload the template to your account, navigate over to the Templates page in the left nav bar in [Governance](https://governance.rightscale.com). Ensure you have the role to access policy management in RightScale. Learn More about [Policy Access Control](https://docs.flexera.com/flexera/EN/Automation/AutomationGS.htm#how-policies-work-access-control).
- Click the “Upload Policy Template” button in the account you wish to test the policy and follow the instructions to upload the template you just downloaded.

## Policy Template Documentation

- [Getting Started](https://docs.flexera.com/flexera/EN/Automation/AutomationGS.htm)
- [Reference Documentation](https://docs.flexera.com/flexera/EN/Automation/AutomationRefInfo.htm#automationrefinfo_1419216867_1009635)
- [Policy Template Language](https://docs.flexera.com/flexera/EN/Automation/PTL.htm#automationrefinfo_1419216867_1122815)
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

- You can test against a pull request via: `bundle exec danger pr https://github.com/flexera-public/policy_templates/pull/73 --pry`
- [Danger Troubleshooting](http://danger.systems/guides/troubleshooting.html)
