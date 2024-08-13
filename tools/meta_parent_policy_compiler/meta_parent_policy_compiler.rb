require "json"

# List of child policy template files to compile meta parent policy templates for by default
# The child policy template must already have the necessary Meta Parent changes made to it
# and those changes in the version that's published to the Flexera Policy Catalog.
# More info at https://github.com/flexera-public/policy_templates/blob/master/README_META_POLICIES.md
default_child_policy_template_files = [
  # AWS Policy Templates
  "../../automation/aws/aws_missing_regions/aws_missing_regions.pt",
  "../../compliance/aws/disallowed_regions/aws_disallowed_regions.pt",
  "../../compliance/aws/ecs_unused/aws_unused_ecs_clusters.pt",
  "../../compliance/aws/iam_role_audit/aws_iam_role_audit.pt",
  "../../compliance/aws/instances_without_fnm_agent/aws_instances_not_running_flexnet_inventory_agent.pt",
  "../../compliance/aws/long_stopped_instances/aws_long_stopped_instances.pt",
  "../../compliance/aws/rds_backup/aws_rds_backup.pt",
  "../../compliance/aws/untagged_resources/aws_untagged_resources.pt",
  "../../cost/aws/burstable_ec2_instances/aws_burstable_ec2_instances.pt",
  "../../cost/aws/ec2_compute_optimizer/aws_ec2_compute_optimizer.pt",
  "../../cost/aws/eks_without_spot/aws_eks_without_spot.pt",
  "../../cost/aws/gp3_volume_upgrade/aws_upgrade_to_gp3_volume.pt",
  "../../cost/aws/idle_compute_instances/idle_compute_instances.pt",
  "../../cost/aws/idle_nat_gateways/aws_idle_nat_gateways.pt",
  "../../cost/aws/object_storage_optimization/aws_object_storage_optimization.pt",
  "../../cost/aws/old_snapshots/aws_delete_old_snapshots.pt",
  "../../cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances.pt",
  "../../cost/aws/rds_instance_license_info/rds_instance_license_info.pt",
  "../../cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt",
  "../../cost/aws/s3_bucket_size/aws_bucket_size.pt",
  "../../cost/aws/s3_storage_policy/aws_s3_bucket_policy_check.pt",
  "../../cost/aws/schedule_instance/aws_schedule_instance.pt",
  "../../cost/aws/superseded_instances/aws_superseded_instances.pt",
  "../../cost/aws/unused_clbs/aws_unused_clbs.pt",
  "../../cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt",
  "../../cost/aws/unused_rds/unused_rds.pt",
  "../../cost/aws/unused_volumes/aws_delete_unused_volumes.pt",
  "../../operational/aws/ec2_stopped_report/aws_ec2_stopped_report.pt",
  "../../operational/aws/lambda_functions_with_high_error_rate/lambda_functions_with_high_error_rate.pt",
  "../../operational/aws/long_running_instances/long_running_instances.pt",
  "../../operational/aws/scheduled_ec2_events/aws_scheduled_ec2_events.pt",
  "../../operational/aws/tag_cardinality/aws_tag_cardinality.pt",
  "../../security/aws/aws_config_enabled/aws_config_enabled.pt",
  "../../security/aws/ebs_ensure_encryption_default/ebs_ensure_encryption_default.pt",
  "../../security/aws/ebs_unencrypted_volumes/aws_unencrypted_volumes.pt",
  "../../security/aws/elb_unencrypted/aws_elb_encryption.pt",
  "../../security/aws/rds_publicly_accessible/aws_publicly_accessible_rds_instances.pt",
  "../../security/aws/rds_unencrypted/aws_unencrypted_rds_instances.pt",
  "../../security/aws/loadbalancer_internet_facing/aws_internet_facing_elbs.pt",
  "../../security/aws/public_buckets/aws_public_buckets.pt",
  "../../security/aws/rds_publicly_accessible/aws_publicly_accessible_rds_instances.pt",
  "../../security/aws/s3_buckets_deny_http/s3_buckets_deny_http.pt",
  "../../security/aws/s3_buckets_without_server_access_logging/aws_s3_buckets_without_server_access_logging.pt",
  "../../security/aws/s3_ensure_buckets_block_public_access/s3_ensure_buckets_block_public_access.pt",
  "../../security/aws/s3_ensure_mfa_delete_enabled/s3_ensure_mfa_delete_enabled.pt",
  "../../security/aws/unencrypted_s3_buckets/aws_unencrypted_s3_buckets.pt",
  "../../security/aws/vpcs_without_flow_logs_enabled/aws_vpcs_without_flow_logs_enabled.pt",
  "../../cost/aws/superseded_ebs_volumes/aws_superseded_ebs_volumes.pt",
  "../../cost/aws/rightsize_ebs_volumes/aws_rightsize_ebs_volumes.pt",
  # Azure Policy Templates
  "../../compliance/azure/azure_disallowed_regions/azure_disallowed_regions.pt",
  "../../compliance/azure/azure_policy_audit/azure_policy_audit.pt",
  "../../compliance/azure/azure_untagged_vms/untagged_vms.pt",
  "../../compliance/azure/azure_untagged_resources/untagged_resources.pt",
  "../../compliance/azure/ahub_manual/azure_ahub_utilization_with_manual_entry.pt",
  "../../compliance/azure/azure_long_stopped_instances/long_stopped_instances_azure.pt",
  "../../compliance/azure/compliance_score/azure_regulatory_compliance_report.pt",
  "../../compliance/azure/instances_without_fnm_agent/azure_instances_not_running_flexnet_inventory_agent.pt",
  "../../cost/azure/advisor_compute/azure_advisor_compute.pt",
  "../../cost/azure/reserved_instances/recommendations/azure_reserved_instance_recommendations.pt",
  "../../cost/azure/idle_compute_instances/azure_idle_compute_instances.pt",
  "../../cost/azure/blob_storage_optimization/azure_blob_storage_optimization.pt",
  "../../cost/azure/old_snapshots/azure_delete_old_snapshots.pt",
  "../../cost/azure/rightsize_compute_instances/azure_compute_rightsizing.pt",
  "../../cost/azure/rightsize_managed_disks/azure_rightsize_managed_disks.pt",
  "../../cost/azure/rightsize_managed_sql/azure_rightsize_managed_sql.pt",
  "../../cost/azure/rightsize_netapp_files/azure_rightsize_netapp_files.pt",
  "../../cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances.pt",
  "../../cost/azure/rightsize_sql_storage/azure_rightsize_sql_storage.pt",
  #"../../cost/azure/rightsize_synapse_sql_pools/azure_rightsize_synapse_sql_pools.pt",
  "../../cost/azure/unoptimized_web_app_scaling/azure_unoptimized_web_app_scaling.pt",
  "../../cost/azure/sql_servers_without_elastic_pool/azure_sql_servers_without_elastic_pool.pt",
  "../../cost/azure/unused_firewalls/azure_unused_firewalls.pt",
  "../../cost/azure/unused_ip_addresses/azure_unused_ip_addresses.pt",
  "../../cost/azure/unused_sql_databases/azure_unused_sql_databases.pt",
  "../../cost/azure/unused_volumes/azure_unused_volumes.pt",
  "../../cost/azure/hybrid_use_benefit/azure_hybrid_use_benefit.pt",
  "../../cost/azure/hybrid_use_benefit_linux/ahub_linux.pt",
  "../../cost/azure/hybrid_use_benefit_sql/ahub_sql.pt",
  "../../cost/azure/savings_plan/recommendations/azure_savings_plan_recommendations.pt",
  "../../cost/azure/schedule_instance/azure_schedule_instance.pt",
  "../../cost/azure/superseded_instances/azure_superseded_instances.pt",
  "../../cost/azure/storage_account_lifecycle_management/storage_account_lifecycle_management.pt",
  "../../cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute.pt",
  "../../operational/azure/aks_nodepools_without_autoscaling/aks_nodepools_without_autoscaling.pt",
  "../../operational/azure/aks_nodepools_without_zero_autoscaling/aks_nodepools_without_zero_autoscaling.pt",
  "../../operational/azure/azure_certificates/azure_certificates.pt",
  "../../operational/azure/azure_long_running_instances/azure_long_running_instances.pt",
  "../../operational/azure/compute_poweredoff_report/azure_compute_poweredoff_report.pt",
  "../../operational/azure/tag_cardinality/azure_tag_cardinality.pt",
  "../../operational/azure/vms_without_managed_disks/azure_vms_without_managed_disks.pt",
  "../../security/azure/blob_storage_logging/blob_storage_logging.pt",
  "../../security/azure/mysql_ssl/mysql_ssl.pt",
  "../../security/azure/mysql_tls_version/mysql_tls_version.pt",
  "../../security/azure/pg_conn_throttling/pg_conn_throttling.pt",
  "../../security/azure/pg_infra_encryption/pg_infra_encryption.pt",
  "../../security/azure/pg_log_retention/pg_log_retention.pt",
  "../../security/azure/pg_log_settings/pg_log_settings.pt",
  "../../security/azure/private_blob_containers/private_blob_containers.pt",
  "../../security/azure/queue_storage_logging/queue_storage_logging.pt",
  "../../security/azure/restrict_rdp_internet/azure_restrict_rdp_inet.pt",
  "../../security/azure/restrict_ssh_internet/azure_restrict_ssh_inet.pt",
  "../../security/azure/secure_transfer_required/secure_transfer_required.pt",
  "../../security/azure/security_alert_owners/security_alert_owners.pt",
  "../../security/azure/security_contact_email/security_contact_email.pt",
  "../../security/azure/sql_ad_admin/sql_ad_admin.pt",
  "../../security/azure/sql_auditing_retention/sql_auditing_retention.pt",
  "../../security/azure/sql_db_encryption/sql_db_encryption.pt",
  "../../security/azure/sql_publicly_accessible_managed_instance/sql_publicly_accessible_managed_instance.pt",
  "../../security/azure/sql_server_atp/sql_server_atp.pt",
  "../../security/azure/sql_server_auditing/sql_server_auditing.pt",
  "../../security/azure/sql_server_va/sql_server_va.pt",
  "../../security/azure/sql_server_va_admins/sql_server_va_admins.pt",
  "../../security/azure/sql_server_va_emails/sql_server_va_emails.pt",
  "../../security/azure/sql_server_va_scans/sql_server_va_scans.pt",
  "../../security/azure/storage_network_deny/storage_network_deny.pt",
  "../../security/azure/storage_soft_delete/storage_soft_delete.pt",
  "../../security/azure/storage_tls_version/storage_tls_version.pt",
  "../../security/azure/storage_trusted_services/storage_trusted_services.pt",
  "../../security/azure/table_storage_logging/table_storage_logging.pt",
  "../../security/azure/webapp_tls_version_support/azure_webapp_min_tls_version.pt",
  # Google Policy Templates
  "../../compliance/google/long_stopped_instances/google_long_stopped_instances.pt",
  "../../compliance/google/unlabeled_resources/unlabeled_resources.pt",
  "../../cost/google/cloud_sql_idle_instance_recommendations/google_sql_idle_instance_recommendations.pt",
  "../../cost/google/idle_ip_address_recommendations/google_idle_ip_address_recommendations.pt",
  "../../cost/google/idle_persistent_disk_recommendations/google_idle_persistent_disk_recommendations.pt",
  "../../cost/google/object_storage_optimization/google_object_storage_optimization.pt",
  "../../cost/google/recommender/recommender.pt",
  "../../cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations.pt",
  "../../cost/google/schedule_instance/google_schedule_instance.pt",
  "../../cost/google/cud_expiration/google_cud_expiration_report.pt",
  "../../cost/google/cud_recommendations/google_committed_use_discount_recommendations.pt",
  "../../cost/google/cud_report/google_committed_use_discount_report.pt",
  "../../cost/google/old_snapshots/google_delete_old_snapshots.pt",
  "../../security/google/public_buckets/google_public_buckets.pt"
]

# Compile Meta Parent Policy Definition
# This function takes a child policy template file path
# as input and outputs a meta parent policy definition
def compile_meta_parent_policy(file_path)
  print("Reading child  policy template: "+file_path+"\n") # Intentional extra space after child so the Read/Write output lines up
  file = File.open(file_path, "rb")

  pt = file.read
  ###############################################################################
  # Parse the Policy Template as a string using regex to get the parameters and credential blocks

  ## Grab the first result, then the first/only capture group of that result
  ## This is a safe assumption because we expect only one match and one capture group within that match
  name = pt.scan(/^(?:name ")(.*?)(?:")/)[0][0]
  description = pt.scan(/^(?:short_description ")(.*?)(?:")/)[0][0]
  # Get the version string
  version = pt.scan(/version: "(.*?)"/)[0][0]
  # get the publish string if it exists, defaulting to true if not present
  publish_scan = pt.scan(/publish: "(.*?)"/)
  publish = "true"
  publish = publish_scan[0][0] if !publish_scan.empty?
  # get the deprecated string if it exists, defaulting to false if not present
  deprecated_scan = pt.scan(/publish: "(.*?)"/)
  deprecated = "false"
  deprecated = deprecated_scan[0][0] if !deprecated_scan.empty?
  # print("Name: #{name}\n")
  # print("Description: #{description}\n")
  # print("\n###########################\n")

  # Get the parameters
  parameters = pt.scan(/^parameter ".*?" do.*?^end/m)

  # print("Parameters:\n")
  # print(parameters.join("\n---------\n"))
  # print("\n###########################\n")

  # Get the credentials
  credentials = pt.scan(/^credentials ".*?" do.*?^end/m)

  # Get resource level
  resource_level = pt.scan(/^\s*resource_level (true|false)$/)

  # Get escalations blocks
  escalation_blocks_child = pt.scan(/escalation ".*?" do.*?^end/m)
  escalation_blocks_parent = []
  escalation_blocks_child.each do |escalation|
    consolidated_incident_escalation_template = <<-EOL
# Escalation for __PLACEHOLDER_FOR_CHILD_POLICY_ESC_LABEL__
escalation "__PLACEHOLDER_FOR_CHILD_POLICY_ESC_ID__" do
  automatic false # Do not automatically action from meta parent. the child will handle automatic escalations if param is set
  label "__PLACEHOLDER_FOR_CHILD_POLICY_ESC_LABEL__"
  description "__PLACEHOLDER_FOR_CHILD_POLICY_ESC_DESCRIPTION__"
__PLACEHOLDER_FOR_CHILD_POLICY_ESC_PARAMETERS__
  # Run declaration should go at end, after any parameters that may exist
  run "__PLACEHOLDER_FOR_CHILD_POLICY_ESC_ID__", data, rs_governance_host, rs_project_id__PLACEHOLDER_FOR_CHILD_POLICY_ESC_PARAMETER_VALUES__
end
define __PLACEHOLDER_FOR_CHILD_POLICY_ESC_ID__($data, $governance_host, $rs_project_id__PLACEHOLDER_FOR_CHILD_POLICY_ESC_PARAMETER_VALUES__) do
  __PLACEHOLDER_FOR_CHILD_POLICY_ESC_PARAMETER_ACTION_OPTIONS__
  call child_run_action($data, $governance_host, $rs_project_id, "__PLACEHOLDER_FOR_CHILD_POLICY_ESC_LABEL__", $action_options)
end
    EOL
    # Drop any escalations related to email action
    next if escalation.include?("email")
    # Get Escalation ID
    esc_id = escalation.scan(/escalation "(.*?)" do/)[0][0]
    # Get Escalation Label
    esc_label = escalation.scan(/label "(.*?)"/)[0][0]
    # Get Escalation Description
    esc_description = escalation.scan(/description "(.*?)"/)[0][0]
    # Get Escalation Parameters
    esc_parameters = escalation.scan(/^\s+parameter ".*?" do.*?end/m)
    esc_parameters = esc_parameters.join("\n")
    # Get Escalation Parameter Names
    esc_parameter_names = esc_parameters.scan(/parameter "(.*?)" do/)
    # Flatten the array of arrays to a single array
    esc_parameter_names = esc_parameter_names.flatten
    esc_parameter_values_string = ""
    esc_parameter_values_options_list = []
    if esc_parameter_names.length > 0
      esc_parameter_names.each do |param_name|
        esc_parameter_values_string += ", $" + param_name
        esc_parameter_values_options_list.push("{ \"name\": \""+param_name+"\", \"value\": $"+param_name+" }")
      end
    end
    # Replace the placeholders with the values from the child policy template
    esc = consolidated_incident_escalation_template.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_ESC_ID__", esc_id)
    esc = esc.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_ESC_LABEL__", esc_label)
    esc = esc.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_ESC_DESCRIPTION__", esc_description)
    esc = esc.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_ESC_PARAMETERS__", esc_parameters)
    esc = esc.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_ESC_PARAMETER_VALUES__", esc_parameter_values_string)
    if esc_parameter_values_options_list.length > 0
      esc = esc.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_ESC_PARAMETER_ACTION_OPTIONS__", "$actions_options = [" + esc_parameter_values_options_list.join(", ")+"]")
    else
      esc = esc.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_ESC_PARAMETER_ACTION_OPTIONS__", "$actions_options = []")
    end
    escalation_blocks_parent.push(esc)
    # Print the compiled escalation and parameters strings if exist
    # Helpful for debugging
    # if !esc_parameters.empty?
    #   print("\n###########################\n")
    #   print("Escalation Parameters:\n")
    #   print(esc_parameters)
    #   print("\n###########################\n")
    #   print ("Escalation Names:\n")
    #   print(esc_parameter_names)
    #   print("\n###########################\n")
    #   print("Compiled Escalation:\n")
    #   print(esc)
    #   sleep(10)
    # end
  end


  consolidated_incident_datasource_template = <<~EOL
  datasource "__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE___combined_incidents" do
    run_script $js___PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE___combined_incidents, $ds_child_incident_details
  end

  script "js___PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE___combined_incidents", type: "javascript" do
    parameters "ds_child_incident_details"
    result "result"
    code <<-EOS
    result = []
    _.each(ds_child_incident_details, function(incident) {
      s = incident["summary"];
      // If the incident summary contains "__PLACEHOLDER_FOR_CHILD_POLICY_RESOURCE_TYPE_NAME__" then include it in the filter result
      if (s.indexOf("__PLACEHOLDER_FOR_CHILD_POLICY_RESOURCE_TYPE_NAME__") > -1) {
        _.each(incident["violation_data"], function(violation) {
          violation["incident_id"] = incident["id"];
          result.push(violation);
        });
      }
    });
  EOS
  end
  EOL
  consolidated_incident_template = <<-EOL
  # Consolidated incident for __PLACEHOLDER_FOR_CHILD_POLICY_RESOURCE_TYPE_NAME__
  validate $__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE___combined_incidents do
    summary_template "Consolidated Incident: {{ len data }} __PLACEHOLDER_FOR_CHILD_POLICY_RESOURCE_TYPE_NAME__"
    escalate $esc_email
    __PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_ESCALATIONS__
    check eq(size(data), 0)
    export do
      resource_level __PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_RESOURCE_LEVEL__
      __PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_FIELDS__
    end
  end
  EOL
  consolidated_incidents_checks = []
  consolidated_indidents_datasources = []
  # Get the checks
  # Use regex to extract the validate and validate_each checks from the policy template string s
  # The regex is not perfect, but it works for now
  checks = pt.scan(/^\s+validate.*?do.*?^  end/m)
  checks.each do |validate_block|
    # Print Raw Validate Block as a String
    # print("Raw Validate Block:\n")
    # print(validate_block)
    # print("\n---\n")
    # From validate block, capture the escalate lines
    escalations_child = validate_block.scan(/escalate \$.*\n^/)
    escalations_parent = []
    escalations_child.each do |escalation|
      # Drop any escalations related to email action
      next if escalation.include?("email")
      escalations_parent.push(escalation)
    end

    # From validate block, capture the export block
    export_block = validate_block.scan(/export.*?do.*?^  end/m)
    # print("Export Block: \n")
    # print(export_block)
    # print("\n---\n")
    # From the export block, capture the field blocks
    fields = export_block[0].scan(/(^.*field\s+\".*?\".*?end)/m).flatten
    fields.each do |field|
      # Remove path from the field output in the meta parent
      field.gsub!(/\n.*?path.*?\n/, "\n")
      # Lazy way to remove the export do // resource_level true and false blocks that are not needed.
      # A better solution would be a better regex above to capture only the field statements
      field.gsub!(/ *?export.*?do\n *resource_level true\n *field/, "field")
      field.gsub!(/ *?export.*?do\n *resource_level false\n *field/, "field")
      # Add 6 spaces to the beginning of each field to make it align with the policy.validate.export.<field> in the meta parent
      field = "      " + field
      # print("Field: \n")
      # print(export_block)
      # print("\n---\n")
    end
    # Append the incident_id field to the fields array
    # This holds the child policy incident ID, and can be used for actions from the meta parent
    incident_id = "field \"incident_id\" do\n        label \"Child Incident ID\"\n      end".strip
    fields.push(incident_id)

    # From each validate block, capture the summary_template and detail_template
    summary_template = validate_block.scan(/summary_template\s+\"(.*?)\"/m)
    summary_template = validate_block.scan(/summary_template\s+<<-EOS\s+(.*?)EOS/m) if summary_template.empty?
    # print("Summary Template:\n")
    # print(summary_template)
    # From the summary template, capture the longest string that contains only letters and spaces
    summary_template_from_pt = summary_template[0][0]
    # Remove any strings matching {{.*}} from summary template
    # These can cause mismatch in identifying the real summary template string
    summary_template_from_pt.gsub!(/{{.*?}}/, "")
    summary_template_search_string = summary_template_from_pt.scan(/[a-zA-Z0-9 \s]+/).max_by(&:length).strip
    # print("Summary Template Search String:\n")
    # print(summary_template_search_string)
    # print("\n------------------\n")

    # Get the datasource name from the validate block
    datasource_name = validate_block.scan(/(?:validate|validate_each)\s(.*?)\s+do/m)[0][0]
    # Strip leading $ from the datasource name
    datasource_name.gsub!(/^\$/, "")

    # For each validate block, create a consolidated incident datasource and consolidated incident check blocks
    output_ds = consolidated_incident_datasource_template
    output_check = consolidated_incident_template
    # Replace the placeholder with the Child Policy Resource Type Name
    output_ds = output_ds.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_RESOURCE_TYPE_NAME__", summary_template_search_string)
    output_incident = output_check.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_RESOURCE_TYPE_NAME__", summary_template_search_string)
    # Replace the placeholder with the Child Policy Escalations
    output_incident = output_incident.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_ESCALATIONS__", escalations_parent.join("    ").rstrip)
    # Replace the placeholder with the Child Policy Consolidated Incident Fields
    output_ds = output_ds.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_FIELDS__", fields.join("\n"))
    # Replace the placeholder with the Child Policy Consolidated Incident Datasource Block
    output_ds = output_ds.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE__", datasource_name)
    output_incident = output_incident.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE__", datasource_name)
    # Replace the placeholder with the Child Policy Consolidated Incident Resource Level
    output_incident = output_incident.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_RESOURCE_LEVEL__", resource_level[0][0])
    # Replace the placeholder with the Child Policy Consolidated Incident Fields Blocks
    output_incident = output_incident.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_FIELDS__", fields.join("\n      "))
    # Add the consolidated incident datasource and check blocks to the consolidated incident arrays
    # These are joined and added to the meta parent policy template later
    consolidated_indidents_datasources.push(output_ds)
    consolidated_incidents_checks.push(output_incident)
  end
  # print("Credentials:\n")
  # print(credentials.join("\n---------\n"))

  # Replace Placeholders from Meta Parent Policy Template with values from Child Policy Template
  parent_pt_path = "aws_meta_parent.pt.template"
  if file_path.include?("aws")
    parent_pt_path = "aws_meta_parent.pt.template"
  elsif file_path.include?("azure")
    parent_pt_path = "azure_meta_parent.pt.template"
  elsif file_path.include?("google")
    parent_pt_path = "google_meta_parent.pt.template"
  else
    print("Could not determine parent policy template to use for #{file_path}\n")
    exit(1)
  end
  parent_pt = File.open(parent_pt_path, "rb").read
  # Copy the parent_pt to output_pt so we can manipulate it safely
  output_pt = parent_pt
  output_pt_path = File.basename(file_path).split(".")[0] + "_meta_parent.pt"
  # Replace __PLACEHOLDER_FOR_CHILD_POLICY_NAME__ with the name of the child policy
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_NAME__", name)
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_VERSION__", version)
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_PUBLISH__", publish)
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_DEPRECATED__", deprecated)
  # Attempt to identify the URL to the child policy template file on github using the file_path provided
  # This would only work if the pt file is located under the `policy_templates` repo directory
  # If it is not, then the URL will be incorrect
  pt_path_expanded = File.expand_path(file_path) # Get full path to the pt file provided
  pt_path_repo_file = pt_path_expanded.gsub(/^.*policy_templates\//, "") # Get the path to the pt file relative to the policy_templates directory
  pt_path_repo_dir = pt_path_repo_file.split("/")[0..-2].join("/") # Get the path to the directory containing the child pt file
  github_url = "https://github.com/flexera-public/policy_templates/tree/master/#{pt_path_repo_dir}" # Build the github URL
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_GITHUB_URL__", github_url) # Replace the placeholder with the github URL
  # Build a list of parameter block strings for the output pt
  # We need to do this because we need to exclude the param_email and param_aws_account_number params from meta parent pt
  output_pt_params = []
  parameters.each do |param|
    # Filter out parameters that we don't want the user to manage because they are used by our meta policy automation
    param.include?("param_email") || param.include?("param_aws_account_number") || param.include?("param_subscription_allowed_list") || param.include?("param_subscriptions_list") || param.include?("param_subscriptions_allow_or_deny") || param.include?("param_project") || param.include?("param_projects_list") || param.include?("param_projects_allow_or_deny") || param.include?("param_schedule") ? nil : output_pt_params.push(param)
  end
  # Replace placeholder with the identified output parameter blocks
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_PARAMETERS_BLOCKS__", output_pt_params.join("\n\n"))
  # Replace placeholder with credentials blocks from child policy
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CREDENTIALS_BLOCKS__", credentials.join("\n\n"))

  # For each check, build the consolidated incident check and datasource
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CONSOLIDATED_INCIDENT_CHECKS__", consolidated_incidents_checks.join("\n"))
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CONSOLIDATED_INCIDENT_DATASOURCES__", consolidated_indidents_datasources.join("\n"))

  # For each escalation, build the consolidated incident escalation
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CONSOLIDATED_INCIDENT_ESCALATIONS__", escalation_blocks_parent.join("\n"))

  # Write the output parent policy template to disk
  # The output file will be written to the same directory as the child policy template
  outfile_path = File.dirname(file_path) + "/" + output_pt_path
  print("Writing parent policy template: "+outfile_path+"\n")
  outfile = File.open(outfile_path, "w")
  outfile.puts(output_pt)
  outfile.close
end
# End Compile Meta Parent Policy Template Definition

# Start Compile Meta Parent Policy Template Execution
# If argument is provided, then use those files as the file path to the child policy template
# Else, use the default list of child policy template files we statically defined at the top
if ARGV.length == 0
  child_policy_template_files = default_child_policy_template_files
else
  child_policy_template_files = ARGV
end

# Loop through all Policy Templates specified
child_policy_template_files.each do |child_policy_template|
  compile_meta_parent_policy(child_policy_template)
end
