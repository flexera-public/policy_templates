# DangerFile
# https://danger.systems/reference.html
# Tests located in .dangerfile directory

###############################################################################
# Required Libraries
###############################################################################

require 'uri'
require 'yaml'

###############################################################################
# Required External Files
###############################################################################

require_relative '.dangerfile/policy_parser'
require_relative '.dangerfile/github_tests'
require_relative '.dangerfile/general_tests'
require_relative '.dangerfile/code_tests'
require_relative '.dangerfile/readme_tests'
require_relative '.dangerfile/changelog_tests'
require_relative '.dangerfile/policy_tests'

###############################################################################
# File Sorting
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Sorting files for testing..."

# Create lists of files based on specific attributes for testing
# Renamed Files.
renamed_files = git.renamed_files.collect{ |r| r[:before] }
# Changed Files. Ignores renamed files to prevent errors on files that don't exist
changed_files = git.added_files + git.modified_files - renamed_files
# Changed Dangerfile
changed_dangerfiles = changed_files.select{ |file| file == "Dangerfile" || file.start_with?(".dangerfile/") }
# Changed Dot Files
changed_dot_files = changed_files.select{ |file| file.start_with?(".") && !file.start_with?(".dangerfile/") }
# Changed Config Files
config_files = ["Gemfile", "Gemfile.lock", "Rakefile", "package.json", "package-lock.json"]
changed_config_files = changed_files.select{ |file| config_files.include?(file) }
# Changed Ruby files.
changed_rb_files = changed_files.select{ |file| file.end_with?(".rb") || file == "Dangerfile" || file == "Rakefile" }
# Changed Python files.
changed_py_files = changed_files.select{ |file| file.end_with?(".py") }
# Changed Policy Template files. Ignore meta policy files.
changed_pt_files = changed_files.select{ |file| file.end_with?(".pt") && !file.end_with?("meta_parent.pt") }
# Changed Meta Policy Template files.
changed_meta_pt_files = changed_files.select{ |file| file.end_with?("meta_parent.pt") }
# Changed README files.
changed_readme_files = changed_files.select{ |file| file.end_with?("/README.md") && (file.start_with?("automation/") || file.start_with?("compliance/") || file.start_with?("cost/") || file.start_with?("operational/") || file.start_with?("saas/") || file.start_with?("security/")) }
# Changed Changelog files.
changed_changelog_files = changed_files.select{ |file| file.end_with?("/CHANGELOG.md") }
# Changed MD files other than the above.
changed_misc_md_files = changed_files.select{ |file| file.end_with?(".md") && !file.end_with?("/CHANGELOG.md") && !file.start_with?("HISTORY.md") && !(file.end_with?("/README.md") && (file.start_with?("automation/") || file.start_with?("compliance/") || file.start_with?("cost/") || file.start_with?("operational/") || file.start_with?("saas/") || file.start_with?("security/"))) }
# Changed JSON files.
changed_json_files = changed_files.select{ |file| file.end_with?(".json") }
# Changed YAML files.
changed_yaml_files = changed_files.select{ |file| file.end_with?(".yaml") || file.end_with?(".yml") }
# New Policy Template files. Ignore meta policy files.
new_pt_files = git.added_files.select{ |file| file.end_with?(".pt") && !file.end_with?("meta_parent.pt") }

# Temporary for testing
changed_readme_files = []

changed_pt_files = [
  "cost/kubecost/cluster/kubecost_cluster_rightsizing_recommendations.pt",
  "cost/kubecost/sizing/kubecost_resizing_recommendation.pt",
  "cost/oracle/oracle_cbi/oracle_cbi.pt",
  "cost/turbonomics/rightsize_virtual_volumes_recommendations/azure/turbonomics_rightsize_virtual_volumes_recommendations.pt",
  "cost/turbonomics/rightsize_virtual_volumes_recommendations/google/turbonomics_rightsize_virtual_volumes_recommendations.pt",
  "cost/turbonomics/rightsize_virtual_volumes_recommendations/aws/turbonomics_rightsize_virtual_volumes_recommendations.pt",
  "cost/turbonomics/delete_unattached_volumes/azure/turbonomics_delete_virtual_volumes.pt",
  "cost/turbonomics/delete_unattached_volumes/google/turbonomics_delete_virtual_volumes.pt",
  "cost/turbonomics/delete_unattached_volumes/aws/turbonomics_delete_virtual_volumes.pt",
  "cost/turbonomics/scale_virtual_machines_recommendations/azure/turbonomics_scale_virtual_machines.pt",
  "cost/turbonomics/scale_virtual_machines_recommendations/google/turbonomics_scale_virtual_machines.pt",
  "cost/turbonomics/scale_virtual_machines_recommendations/aws/turbonomics_scale_virtual_machines.pt",
  "cost/turbonomics/credential_refresh/turbonomic_cred_refresh.pt",
  "cost/turbonomics/allocate_virtual_machines_recommendations/azure/turbonomics_allocate_virtual_machines.pt",
  "cost/turbonomics/allocate_virtual_machines_recommendations/google/turbonomics_allocate_virtual_machines.pt",
  "cost/turbonomics/allocate_virtual_machines_recommendations/aws/turbonomics_allocate_virtual_machines.pt",
  "cost/turbonomics/rightsize_databases_recommendations/azure/turbonomics_rightsize_databases_recommendations.pt",
  "cost/turbonomics/rightsize_databases_recommendations/google/turbonomics_rightsize_databases_recommendations.pt",
  "cost/turbonomics/rightsize_databases_recommendations/aws/turbonomics_rightsize_databases_recommendations.pt",
  "cost/turbonomics/buy_reserved_instances_recommendations/azure/turbonomics_buy_reserved_instances.pt",
  "cost/turbonomics/buy_reserved_instances_recommendations/aws/turbonomics_buy_reserved_instances.pt",
  # "cost/azure/unused_volumes/azure_unused_volumes.pt",
  # "cost/azure/superseded_instances/azure_superseded_instances.pt",
  # "cost/azure/rightsize_managed_disks/azure_rightsize_managed_disks.pt",
  # "cost/azure/rightsize_netapp/azure_rightsize_netapp.pt",
  # "cost/azure/unused_sql_databases/azure_unused_sql_databases.pt",
  # "cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute.pt",
  # "cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute_meta_parent_cluster.pt",
  # "cost/azure/schedule_instance/azure_schedule_instance.pt",
  # "cost/azure/rightsize_sql_storage/azure_rightsize_sql_storage.pt",
  # "cost/azure/unused_app_service_plans/azure_unused_app_service_plans.pt",
  # "cost/azure/rightsize_compute_instances/azure_compute_rightsizing.pt",
  # "cost/azure/unused_vngs/azure_unused_vngs.pt",
  # "cost/azure/unoptimized_web_app_scaling/azure_unoptimized_web_app_scaling.pt",
  # "cost/azure/unused_load_balancers/azure_unused_load_balancers.pt",
  # "cost/azure/cheaper_regions/azure_cheaper_regions.pt",
  # "cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances.pt",
  # "cost/azure/rightsize_mysql_flexible/azure_rightsize_mysql_flexible.pt",
  # "cost/azure/savings_realized/azure_savings_realized.pt",
  # "cost/azure/savings_plan/recommendations/azure_savings_plan_recommendations.pt",
  # "cost/azure/savings_plan/utilization/azure_savings_plan_utilization.pt",
  # "cost/azure/savings_plan/expiration/azure_savings_plan_expiration.pt",
  # "cost/azure/rightsize_managed_sql/azure_rightsize_managed_sql.pt",
  # "cost/azure/hybrid_use_benefit/azure_hybrid_use_benefit.pt",
  # "cost/azure/reserved_instances/recommendations/azure_reserved_instance_recommendations.pt",
  # "cost/azure/reserved_instances/utilization/azure_reserved_instance_utilization.pt",
  # "cost/azure/reserved_instances/expiration/azure_reserved_instance_expiration.pt",
  # "cost/azure/reserved_instances/utilization_mca/azure_reserved_instance_utilization_mca.pt",
  # "cost/azure/hybrid_use_benefit_sql/ahub_sql.pt",
  # "cost/azure/rightsize_synapse_sql_pools/azure_rightsize_synapse_sql_pools.pt",
  # "cost/azure/unused_ip_addresses/azure_unused_ip_addresses.pt",
  # "cost/azure/unused_firewalls/azure_unused_firewalls.pt",
  # "cost/azure/idle_compute_instances/azure_idle_compute_instances.pt",
  # "cost/azure/rightsize_managed_sql_storage/azure_rightsize_managed_sql_storage.pt",
  # "cost/azure/blob_storage_optimization/azure_blob_storage_optimization.pt",
  # "cost/azure/sql_servers_without_elastic_pool/azure_sql_servers_without_elastic_pool.pt",
  # "cost/azure/azure_china_cbi/azure_china_cbi.pt",
  # "cost/azure/hybrid_use_benefit_linux/ahub_linux.pt",
  # "cost/azure/rightsize_mysql_single/azure_rightsize_mysql_single.pt",
  # "cost/azure/old_snapshots/azure_delete_old_snapshots.pt",
  # "cost/azure/advisor_compute/azure_advisor_compute.pt",
  # "cost/azure/storage_account_lifecycle_management/storage_account_lifecycle_management.pt",
  # "cost/azure/instances_log_analytics_utilization/azure_instance_log_analytics_utilization.pt",
  # "cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations.pt",
  # "cost/google/schedule_instance/google_schedule_instance.pt",
  # "cost/google/idle_persistent_disk_recommendations/google_idle_persistent_disk_recommendations.pt",
  # "cost/google/object_storage_optimization/google_object_storage_optimization.pt",
  # "cost/google/unused_cloudsql_instances/google_unused_cloudsql_instances.pt",
  # "cost/google/idle_ip_address_recommendations/google_idle_ip_address_recommendations.pt",
  # "cost/google/recommender/recommender.pt",
  # "cost/google/unutilized_ip_addresses/google_unutilized_ip_addresses.pt",
  # "cost/google/cheaper_regions/google_cheaper_regions.pt",
  # "cost/google/cloud_sql_idle_instance_recommendations/google_sql_idle_instance_recommendations.pt",
  # "cost/google/cloud_run_anomaly_detection/google_cloud_run_anomaly_detection.pt",
  # "cost/google/cud_expiration/google_cud_expiration_report.pt",
  # "cost/google/idle_compute_instances/google_idle_compute_instances.pt",
  # "cost/google/idle_vm_recommendations/google_vm_recommendations.pt",
  # "cost/google/cloudsql_rightsizing/google_cloudsql_rightsizing.pt",
  # "cost/google/instances_stackdriver_utilization/google_instances_stackdriver_utilization.pt",
  # "cost/google/cud_recommendations/google_committed_use_discount_recommendations.pt",
  # "cost/google/unattached_volumes/google_delete_unattached_volumes.pt",
  # "cost/google/cud_report/google_committed_use_discount_report.pt",
  # "cost/google/rightsize_cloudsql_recommendations/google_rightsize_cloudsql_recommendations.pt",
  # "cost/google/old_snapshots/google_delete_old_snapshots.pt",
  # "cost/aws/rightsize_ebs_volumes/aws_rightsize_ebs_volumes.pt",
  # "cost/aws/unused_volumes/aws_delete_unused_volumes.pt",
  # "cost/aws/extended_support/aws_extended_support.pt",
  # "cost/aws/ec2_compute_optimizer/aws_ec2_compute_optimizer.pt",
  # "cost/aws/superseded_instances/aws_superseded_instances.pt",
  # "cost/aws/unused_rds/unused_rds.pt",
  # "cost/aws/schedule_instance/aws_schedule_instance.pt",
  # "cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt",
  # "cost/aws/object_storage_optimization/aws_object_storage_optimization.pt",
  # "cost/aws/unused_albs/aws_unused_albs.pt",
  # "cost/aws/burstable_ec2_instances/aws_burstable_ec2_instances.pt",
  # "cost/aws/eks_without_spot/aws_eks_without_spot.pt",
  # "cost/aws/instance_cost_per_hour/aws_instance_cost_per_hour.pt",
  # "cost/aws/cheaper_regions/aws_cheaper_regions.pt",
  # "cost/aws/instance_cloudwatch_utilization/aws_instance_cloudwatch_utilization.pt",
  # "cost/aws/rds_instance_license_info/rds_instance_license_info.pt",
  # "cost/aws/savings_realized/aws_savings_realized.pt",
  # "cost/aws/superseded_ebs_volumes/aws_superseded_ebs_volumes.pt",
  # "cost/aws/savings_plan/recommendations/aws_savings_plan_recommendations.pt",
  # "cost/aws/savings_plan/utilization/aws_savings_plan_utilization.pt",
  # "cost/aws/savings_plan/expiration/aws_savings_plan_expiration.pt",
  # "cost/aws/unused_nlbs/aws_unused_nlbs.pt",
  # "cost/aws/reserved_instances/recommendations/aws_reserved_instance_recommendations.pt",
  # "cost/aws/reserved_instances/coverage/reserved_instance_coverage.pt",
  # "cost/aws/reserved_instances/utilization/utilization_ris.pt",
  # "cost/aws/reserved_instances/expiration/aws_reserved_instance_expiration.pt",
  # "cost/aws/reserved_instances/report_by_bc/ri_report_by_bc.pt",
  # "cost/aws/reserved_instances/compute_purchase_recommendation/aws_reserved_instance_recommendations_with_purchase.pt",
  # "cost/aws/gp3_volume_upgrade/aws_upgrade_to_gp3_volume.pt",
  # "cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt",
  # "cost/aws/cloudtrail_read_logging/aws_cloudtrail_read_logging.pt",
  # "cost/aws/idle_compute_instances/idle_compute_instances.pt",
  # "cost/aws/s3_bucket_size/aws_bucket_size.pt",
  # "cost/aws/unused_clbs/aws_unused_clbs.pt",
  # "cost/aws/s3_storage_policy/aws_s3_bucket_policy_check.pt",
  # "cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances.pt",
  # "cost/aws/rightsize_redshift/aws_rightsize_redshift.pt",
  # "cost/aws/old_snapshots/aws_delete_old_snapshots.pt",
  # "cost/aws/idle_nat_gateways/aws_idle_nat_gateways.pt",
  # "cost/flexera/cmp/downsize_instance/downsize_instance.pt",
  # "cost/flexera/cmp/schedule_instances/schedule_instances.pt",
  # "cost/flexera/cmp/instance_anomaly/instance_anomaly.pt",
  # "cost/flexera/cmp/rightlink_rightsize/rightlink_rightsize.pt",
  # "cost/flexera/cmp/rightlink_rightsize/rightlink_rightsize_add_tags.pt",
  # "cost/flexera/cmp/unattached_addresses/unattached_addresses.pt",
  # "cost/flexera/cmp/superseded_instance_remediation/superseded_instance_remediation.pt",
  # "cost/flexera/cmp/unattached_volumes/uav_policy.pt",
  # "cost/flexera/cmp/terminate_policy/instance_terminate.pt",
  # "cost/flexera/cmp/old_snapshots/old_snapshot.pt",
  # "cost/flexera/cco/currency_conversion/currency_conversion.pt",
  # "cost/flexera/cco/new_usage/new_usage.pt",
  # "cost/flexera/cco/email_recommendations/email_recommendations.pt",
  # "cost/flexera/cco/scheduled_reports_with_estimates/costs_forecasting.pt",
  # "cost/flexera/cco/budget_alerts/budget_alert.pt",
  # "cost/flexera/cco/scheduled_report_unallocated/scheduled_report_unallocated.pt",
  # "cost/flexera/cco/moving_average/moving_average.pt",
  # "cost/flexera/cco/scheduled_report_markupsdowns/scheduled_report_markpsdowns.pt",
  # "cost/flexera/cco/budget_v_actual_spend_report/budget_v_actual_spend_report.pt",
  # "cost/flexera/cco/budget_v_actual/monthly_budget_v_actual.pt",
  # "cost/flexera/cco/cheaper_regions/cheaper_regions.pt",
  # "cost/flexera/cco/superseded_instance/superseded_instance.pt",
  # "cost/flexera/cco/cloud_cost_anomaly_alerts/cloud_cost_anomaly_alerts.pt",
  # "cost/flexera/cco/budget_alerts_by_account/budget_alerts_by_account.pt",
  # "cost/flexera/cco/forecasting/commitment_forecast/commitment_forecast.pt",
  # "cost/flexera/cco/forecasting/straight_line_forecast_simple/straight_line_forecast_simple.pt",
  # "cost/flexera/cco/forecasting/straight_line_forecast/straight_line_forecast.pt",
  # "cost/flexera/cco/focus_report/focus_report.pt",
  # "cost/flexera/cco/billing_center_cost_anomaly/billing_center_cost_anomaly.pt",
  # "cost/flexera/cco/scheduled_reports/scheduled_report.pt",
  # "cost/flexera/cco/low_usage/low_usage.pt",
  # "cost/flexera/cco/fixed_cost_cbi/fixed_cost_cbi.pt",
  # "cost/flexera/cco/budget_report_alerts/budget_report_alerts.pt",
  # "cost/flexera/cco/low_service_usage/low_service_usage.pt",
  # "cost/flexera/msp/master_org_cost_policy_currency/master_org_cost_policy_currency.pt",
  # "cost/flexera/msp/master_org_cost_policy/master_org_cost_policy.pt",
  # "security/azure/security_alert_owners/security_alert_owners.pt",
  # "security/azure/pg_conn_throttling/pg_conn_throttling.pt",
  # "security/azure/storage_trusted_services/storage_trusted_services.pt",
  # "security/azure/blob_storage_logging/blob_storage_logging.pt",
  # "security/azure/pg_infra_encryption/pg_infra_encryption.pt",
  # "security/azure/storage_network_deny/storage_network_deny.pt",
  # "security/azure/log_analytics_autoprovision/log_analytics_autoprovision.pt",
  # "security/azure/mysql_tls_version/mysql_tls_version.pt",
  # "security/azure/guest_users/guest_users.pt",
  # "security/azure/sql_server_va_scans/sql_server_va_scans.pt",
  # "security/azure/queue_storage_logging/queue_storage_logging.pt",
  # "security/azure/storage_soft_delete/storage_soft_delete.pt",
  # "security/azure/storage_account_https_enabled/azure_storage_account_https_enabled.pt",
  # "security/azure/sql_ad_admin/sql_ad_admin.pt",
  # "security/azure/sql_server_auditing/sql_server_auditing.pt",
  # "security/azure/webapp_tls_version_support/azure_webapp_min_tls_version.pt",
  # "security/azure/pg_log_retention/pg_log_retention.pt",
  # "security/azure/sql_server_va/sql_server_va.pt",
  # "security/azure/secure_transfer_required/secure_transfer_required.pt",
  # "security/azure/sql_server_atp/sql_server_atp.pt",
  # "security/azure/pg_log_settings/pg_log_settings.pt",
  # "security/azure/restrict_rdp_internet/azure_restrict_rdp_inet.pt",
  # "security/azure/storage_tls_version/storage_tls_version.pt",
  # "security/azure/mysql_ssl/mysql_ssl.pt",
  # "security/azure/sql_server_va_emails/sql_server_va_emails.pt",
  # "security/azure/sql_publicly_accessible_managed_instance/sql_publicly_accessible_managed_instance.pt",
  # "security/azure/security_contact_email/security_contact_email.pt",
  # "security/azure/private_blob_containers/private_blob_containers.pt",
  # "security/azure/sql_server_va_admins/sql_server_va_admins.pt",
  # "security/azure/sql_auditing_retention/sql_auditing_retention.pt",
  # "security/azure/restrict_ssh_internet/azure_restrict_ssh_inet.pt",
  # "security/azure/high_severity_alerts/high_severity_alerts.pt",
  # "security/azure/table_storage_logging/table_storage_logging.pt",
  # "security/azure/sql_db_encryption/sql_db_encryption.pt",
  # "security/azure/resources_with_public_ip_address/azure_open_ip_address_policy.pt",
  # "security/google/public_buckets/google_public_buckets.pt",
  # "security/aws/ebs_ensure_encryption_default/ebs_ensure_encryption_default.pt",
  # "security/aws/iam_no_admin_iam_policies_attached/iam_no_admin_iam_policies_attached.pt",
  # "security/aws/elb_unencrypted/aws_elb_encryption.pt",
  # "security/aws/log_ensure_cloudtrail_multiregion/log_ensure_cloudtrail_multiregion.pt",
  # "security/aws/public_buckets/aws_public_buckets.pt",
  # "security/aws/s3_ensure_mfa_delete_enabled/s3_ensure_mfa_delete_enabled.pt",
  # "security/aws/unencrypted_s3_buckets/aws_unencrypted_s3_buckets.pt",
  # "security/aws/iam_one_active_key_per_user/iam_one_active_key_per_user.pt",
  # "security/aws/iam_no_root_for_tasks/iam_no_root_for_tasks.pt",
  # "security/aws/s3_buckets_deny_http/s3_buckets_deny_http.pt",
  # "security/aws/loadbalancer_internet_facing/aws_internet_facing_elbs.pt",
  # "security/aws/iam_unused_creds/iam_unused_creds.pt",
  # "security/aws/iam_min_password_length/iam_min_password_length.pt",
  # "security/aws/log_ensure_cloudtrail_bucket_access_logging/log_ensure_cloudtrail_bucket_access_logging.pt",
  # "security/aws/iam_mfa_enabled_for_iam_users/iam_mfa_enabled_for_iam_users.pt",
  # "security/aws/iam_users_perms_via_groups_only/iam_users_perms_via_groups_only.pt",
  # "security/aws/rds_publicly_accessible/aws_publicly_accessible_rds_instances.pt",
  # "security/aws/iam_expired_ssl_certs/iam_expired_ssl_certs.pt",
  # "security/aws/iam_mfa_enabled_for_root/iam_mfa_enabled.pt",
  # "security/aws/s3_ensure_buckets_block_public_access/s3_ensure_buckets_block_public_access.pt",
  # "security/aws/log_cloudtrail_cloudwatch_integrated/log_cloudtrail_cloudwatch_integrated.pt",
  # "security/aws/kms_rotation/kms_rotation.pt",
  # "security/aws/s3_buckets_without_server_access_logging/aws_s3_buckets_without_server_access_logging.pt",
  # "security/aws/rds_unencrypted/aws_unencrypted_rds_instances.pt",
  # "security/aws/log_file_validation_enabled/log_file_validation_enabled.pt",
  # "security/aws/iam_hwmfa_enabled_for_root/aws_iam_hwmfa_enabled.pt",
  # "security/aws/clb_unencrypted/aws_clb_encryption.pt",
  # "security/aws/log_ensure_cloudtrail_bucket_not_public/log_ensure_cloudtrail_bucket_not_public.pt",
  # "security/aws/vpcs_without_flow_logs_enabled/aws_vpcs_without_flow_logs_enabled.pt",
  # "security/aws/iam_rotate_access_keys/iam_rotate_access_keys.pt",
  # "security/aws/log_ensure_cloudtrail_encrypted/log_ensure_cloudtrail_encrypted.pt",
  # "security/aws/iam_prevent_password_reuse/iam_prevent_password_reuse.pt",
  # "security/aws/iam_access_analyzer_enabled/iam_access_analyzer_enabled.pt",
  # "security/aws/ebs_unencrypted_volumes/aws_unencrypted_volumes.pt",
  # "security/aws/log_ensure_cloudtrail_bucket_object_logging/log_ensure_cloudtrail_bucket_object_logging.pt",
  # "security/aws/iam_no_root_access_keys/aws_iam_no_root_access_keys.pt",
  # "security/aws/aws_config_enabled/aws_config_enabled.pt",
  # "security/aws/iam_support_role_created/iam_support_role_created.pt",
  # "security/flexera/cmp/high_open_ports/open_ports.pt",
  # "security/flexera/cmp/icmp_enabled/icmp_enabled.pt",
  # "security/flexera/cmp/rules_without_descriptions/security_group_rules_without_descriptions.pt",
  # "security/flexera/cmp/world_open_ports/security_group_rules_with_world_open_ports.pt"
]

# End Temporary for Testing


###############################################################################
# File Loading
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Loading file-based assets..."

permissions_yaml = YAML.load_file('tools/policy_master_permission_generation/validated_policy_templates.yaml')

###############################################################################
# Github Pull Request Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing Github pull request..."

test = github_pr_bad_title?(github); warn test if test
test = github_pr_missing_summary?(github); fail test if test
test = github_pr_missing_labels?(github); fail test if test
test = github_pr_missing_ready_label?(github); message test if test

###############################################################################
# Modified Important Files Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing if important files were modified..."

modified_important_files = changed_dangerfiles + changed_dot_files + changed_config_files
modified_important_files = modified_important_files.join("\n")

# Consolidate changed files into a single warning to save space
warn "### **Important Files Modified**\n\nPlease make sure these modifications were intentional and have been tested. These files are necessary for configuring the Github repository and managing automation.\n\n" + modified_important_files.strip if !modified_important_files.empty?

###############################################################################
# All Files Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed files..."

changed_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  warnings = []
  failures = []

  # Perform a basic text lint on all changed files
  test = general_textlint?(file); warnings << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Ruby File Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed Ruby files..."

# Perform a lint check on changed Ruby files
changed_rb_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Raise error if code errors found
  test = code_ruby_errors?(file); failures << test if test

  # Rubocop linting currently disabled. It is *very* verbose.
  #test = code_rubocop_problems?(file); warn test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Python File Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed Python files..."

# Perform a lint check on changed Python files
changed_py_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Raise error if code errors found
  test = code_python_errors?(file); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# JSON/YAML File Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed JSON files..."

changed_json_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Look for out of place JSON files
  test = code_json_bad_location?(file); failures << test if test

  # Lint test JSON files
  test = code_json_errors?(file); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed YAML files..."

changed_yaml_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Look for out of place YAML files
  test = code_yaml_bad_location?(file); failures << test if test

  # Lint test YAML files
  test = code_yaml_errors?(file); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# README Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed README.md files..."

# Check README.md for issues for each file
changed_readme_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Don't run tests against deprecated READMEs
  unless readme_deprecated?(file, file_lines)
    # Run aspell spell check on file
    test = general_spellcheck?(file); warnings << test if test

    # Raise warning if outdated terminology found
    test = general_outdated_terminology?(file, file_lines); warnings << test if test

    # Raise error if the file contains any bad urls
    test = general_bad_urls?(file, file_diff); failures << test if test

    # Raise error if improper markdown is found via linter
    test = general_bad_markdown?(file); failures << test if test

    # Raise error if README is missing required sections
    test = readme_missing_sections?(file, file_lines); failures << test if test

    # Raise error if README sections are out of order
    test = readme_sections_out_of_order?(file, file_lines); failures << test if test

    # Raise error if README credentials are formatted incorrectly
    test = readme_invalid_credentials?(file, file_lines); failures << test if test
  end

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# CHANGELOG Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed CHANGELOG.md files..."

# Check CHANGELOG.md for issues for each file
changed_changelog_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Don't run tests against deprecated CHANGELOGs
  unless changelog_deprecated?(file, file_lines)
    # Raise error if the file contains any bad urls
    test = general_bad_urls?(file, file_diff); failures << test if test

    # Raise error if improper markdown is found via linter
    test = general_bad_markdown?(file); failures << test if test

    # Raise error if CHANGELOG is incorrectly formatted
    test = changelog_bad_formatting?(file, file_lines); failures << test if test
  end

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Misc. Markdown Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed misc MD files..."

# Check Markdown files for issues for each file
changed_misc_md_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Run aspell spell check on file
  test = general_spellcheck?(file); warnings << test if test

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Raise error if the file contains any bad urls
  test = general_bad_urls?(file, file_diff); failures << test if test

  # Raise error if improper markdown is found via linter
  test = general_bad_markdown?(file); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Policy Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed Policy Template files..."

# Check policies for issues for each file
changed_pt_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  # Run policy through various methods that test for problems.
  # These methods will return false if no problems are found.
  # Otherwise, they return the warning or error message that should be raised.
  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_parsed = PolicyParser.new
  file_parsed.parse(file)
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise error if policy is deprecated but missing deprecated field in info() block
  test = policy_missing_deprecated_field?(file, file_parsed); failures << test if test

  # Raise error if policy changed but changelog has not been
  #test = policy_unmodified_changelog?(file, changed_changelog_files); failures << test if test

  # Raise error if policy and changelog do not have matching version numbers
  test = policy_changelog_mismatch?(file, file_parsed); failures << test if test

  # Run policy through fpt testing. Only raise error if there is a syntax error.
  test = policy_fpt_syntax_error?(file); failures << test if test

  # Don't run remaining tests against deprecated policies
  unless policy_deprecated?(file, file_parsed)
    # Raise error if policy is not in a valid directory within the repo directory structure
    test = policy_bad_directory?(file); failures << test if test

    # Raise warning if policy changed but readme has not been
    rd_test = policy_unmodified_readme?(file, changed_readme_files); warnings << rd_test if rd_test

    # Raise error if policy template name does not match name in README file
    test = policy_readme_correct_name?(file, file_parsed); failures << test if test

    # Raise error if policy is not in the master permissions file.
    # Raise warning if policy is in this file, but datasources have been added.
    # Only raise the above warning if the more general warning about updating the README doesn't exist.
    test = policy_missing_master_permissions?(file, permissions_yaml); failures << test if test
    #ds_test = policy_new_datasource?(file, file_diff, permissions_yaml); warnings << ds_test if ds_test && !test && !rd_test

    # Raise error if policy filename/path contains any uppercase letters
    test = policy_bad_filename_casing?(file); failures << test if test

    # Raise error if policy short_description is missing valid README link
    test = policy_bad_readme_link?(file, file_parsed); failures << test if test

    # Raise warning if policy won't be published
    test = policy_unpublished?(file, file_parsed); warnings << test if test

    # Raise warning if policy's name has changed
    #test = policy_name_changed?(file, file_diff); warnings << test if test

    # Raise warning if outdated terminology found
    test = general_outdated_terminology?(file, file_lines); warnings << test if test

    # Raise error if the file contains any bad urls
    #test = general_bad_urls?(file, file_diff); failures << test if test

    # Raise warning if policy contains invalid indentation
    test = policy_bad_indentation?(file, file_lines); warnings << test if test

    # Raise error if policy contains multiple blank lines
    test = policy_consecutive_empty_lines?(file, file_lines); failures << test if test

    # Raise errors or warnings if bad metadata is found
    test = policy_bad_metadata?(file, file_parsed, "name"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "short_description"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "long_description"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "category"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "default_frequency"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "severity"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "info"); failures << test if test

    # Raise errors or warnings if bad info block metadata is found
    if !test
      info_test = policy_missing_info_field?(file, file_parsed, "version"); failures << info_test if info_test
      info_test = policy_missing_info_field?(file, file_parsed, "provider"); failures << info_test if info_test
      info_test = policy_missing_info_field?(file, file_parsed, "service"); warnings << info_test if info_test
      info_test = policy_missing_info_field?(file, file_parsed, "policy_set"); warnings << info_test if info_test
    end

    # Raise error if policy version number does not use semantic versioning
    test = policy_nonsemantic_version?(file, file_parsed); failures << test if test

    # Raise error if there is a mismatch between the policy's credentials and the README
    test = policy_readme_missing_credentials?(file, file_lines); failures << test if test

    # Raise error if policy sections are out of order
    test = policy_sections_out_of_order?(file, file_lines); failures << test if test

    # Raise error of code blocks exist in policy that aren't used anywhere
    test = policy_orphaned_blocks?(file, file_lines, "parameter"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "credentials"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "pagination"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "datasource"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "script"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "escalation"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "define"); failures << test if test

    # Raise error if policy blocks are not grouped together by type
    test = policy_blocks_ungrouped?(file, file_lines); failures << test if test

    # Report on missing policy section comments
    test = policy_missing_section_comments?(file, file_text, "parameter"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "credentials"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "pagination"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "datasource"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "policy"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "escalation"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "cwf"); failures << test if test

    # Report on invalidly named code blocks
    test = policy_bad_block_name?(file, file_lines, "parameter"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "credentials"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "pagination"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "datasource"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "script"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "policy"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "escalation"); failures << test if test

    # Report on invalid/deprecated code blocks
    test = policy_deprecated_code_blocks?(file, file_lines, "permission"); warnings << test if test
    test = policy_deprecated_code_blocks?(file, file_lines, "resources"); warnings << test if test

    # Report on missing fields in code blocks
    fields_to_check = [
      { block: "parameter", fields: ["type", "category", "label", "description"] },
      { block: "credentials", fields: ["schemes", "tags", "label", "description"] },
      { block: "escalation", fields: ["automatic", "label", "description"] }
    ]

    fields_to_check.each do |item|
      item[:fields].each do |field|
        test = policy_block_missing_field?(file, file_lines, item[:block], field); failures << test if test
      end
    end

    # Raise warning, not error, if parameter block is missing a default field.
    # This is because there are occasionally legitimate reasons to not have a default
    test = policy_block_missing_field?(file, file_lines, "parameter", "default")

    if test
      warnings << test + "\n\nWhile not required, it is recommended that every parameter have a default value unless user input for that parameter is required and too specific for any default value to make sense"
    end

    # Raise warning, not error, if a datasource and the script it calls have mismatched names.
    # Warning because there are occasionally legitimate reasons to do this.
    test = policy_ds_js_name_mismatch?(file, file_lines); warnings << test if test

    # Raise error if run_script statements with incorrect parameter ordering are found
    test = policy_run_script_incorrect_order?(file, file_lines); failures << test if test

    # Raise error if code blocks have fields in improper order
    test = policy_block_fields_incorrect_order?(file, file_lines, "parameter"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "credentials"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "pagination"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "datasource"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "script"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "policy"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "escalation"); failures << test if test

    # Raise error if recommendation policy is missing required export fields
    test = policy_missing_recommendation_fields?(file, file_lines, file_parsed, "required"); failures << test if test

    # Raise warning if recommendation policy is missing recommended export fields
    test = policy_missing_recommendation_fields?(file, file_lines, file_parsed, "recommended"); warnings << test if test

    # Raise error if policy has outdated links
    test = policy_outdated_links?(file, file_lines); failures << test if test

    # Raise warning if policy has any datasources using http instead of https
    test = policy_http_connections?(file, file_lines); warnings << test if test

    # Raise warning if improper spacing between comma-separated items found
    test = policy_bad_comma_spacing?(file, file_lines); warnings << test if test

    # Raise error if policy has console.log() statements
    test = policy_console_log?(file, file_lines); failures << test if test
  end

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Meta Policy Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * Testing all changed Meta Parent Policy Template files..."

# Check meta policies for issues for each file
changed_meta_pt_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** Testing " + file + "..."

  # Run meta policy through various methods that test for problems.
  # These methods will return false if no problems are found.
  # Otherwise, they return the warning or error message that should be raised.
  warnings = []
  failures = []

  # Run policy through fpt testing. Only raise error if there is a syntax error.
  test = policy_fpt_syntax_error?(file, "meta"); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end
