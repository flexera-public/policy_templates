require "json"

# List of child policy template files to compile meta parent policy templates for by default
# The child policy template must already have the necessary Meta Parent changes made to it
# and those changes in the version that's published to the Flexera Policy Catalog.
# More info at https://github.com/flexera-public/policy_templates/blob/master/README_META_POLICIES.md
default_child_policy_template_files = [
  # AWS Policy Templates
  "../../cost/aws/idle_compute_instances/idle_compute_instances.pt",
  "../../cost/aws/object_storage_optimization/aws_object_storage_optimization.pt",
  "../../cost/aws/old_snapshots/aws_delete_old_snapshots.pt",
  "../../cost/aws/rightsize_compute_instances/aws_compute_rightsizing.pt",
  "../../cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing.pt",
  "../../cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt",
  "../../cost/aws/unused_rds/unused_rds.pt",
  "../../cost/aws/unused_volumes/aws_delete_unused_volumes.pt",
  # Azure Policy Templates
  "../../cost/azure/idle_compute_instances/azure_idle_compute_instances.pt",
  "../../cost/azure/old_snapshots/azure_delete_old_snapshots.pt",
  "../../cost/azure/rightsize_compute_instances/azure_compute_rightsizing.pt",
  "../../cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances.pt",
  "../../cost/azure/unused_ip_addresses/azure_unused_ip_addresses.pt",
  "../../cost/azure/unused_sql_databases/azure_unused_sql_databases.pt",
  "../../cost/azure/unused_volumes/azure_unused_volumes.pt",
  "../../cost/azure/hybrid_use_benefit/azure_hybrid_use_benefit.pt",
  "../../cost/azure/hybrid_use_benefit_linux/ahub_linux.pt",
  "../../cost/azure/hybrid_use_benefit_sql/ahub_sql.pt",
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
  # print("Name: #{name}\n")
  # print("Description: #{description}\n")
  # print("\n###########################\n")

  # Get the parameters
  parameters = pt.scan(/parameter ".*?" do.*?^end/m)

  # print("Parameters:\n")
  # print(parameters.join("\n---------\n"))
  # print("\n###########################\n")

  # Get the credentials
  credentials = pt.scan(/credentials ".*?" do.*?^end/m)



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
    check eq(size(data), 0)
    export do
      resource_level true
      __PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_FIELDS__
    end
  end
  EOL
  consolidated_incidents_checks = []
  consolidated_indidents_datasources = []
  # Get the checks
  # Use regex to extract the validate and validate_each checks from the policy template string s
  # The regex is not perfect, but it works for now
  checks = pt.scan(/validate.*?do.*?^  end/m)
  checks.each do |validate_block|
    # Print Raw Validate Block as a String
    # print("Raw Validate Block:\n")
    # print(validate_block)
    # print("\n---\n")
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
      # Lazy way to remove the export do // resource_level true blocks that are not needed.
      # A better solution would be a better regex above to capture only the field statements
      field.gsub!(/ *?export.*?do\n *resource_level true\n *field/, "field")
      # Add 6 spaces to the beginning of each field to make it align with the policy.validate.export.<field> in the meta parent
      field = "      " + field
      # print("Field: \n")
      # print(export_block)
      # print("\n---\n")
    end

    # From each validate block, capture the summary_template and detail_template
    summary_template = validate_block.scan(/summary_template\s+\"(.*?)\"/m)
    summary_template = validate_block.scan(/summary_template\s+<<-EOS\s+(.*?)EOS/m) if summary_template.empty?
    # From the summary template, capture the longest string that contains only letters and spaces
    summary_template_search_string = summary_template[0][0].scan(/[a-zA-Z\s]+/).max_by(&:length).strip
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
    # Replace the placeholder with the Child Policy Consolidated Incident Fields
    output_ds = output_ds.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_FIELDS__", fields.join("\n"))
    # Replace the placeholder with the Child Policy Consolidated Incident Datasource Block
    output_ds = output_ds.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE__", datasource_name)
    output_incident = output_incident.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE__", datasource_name)
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
    # Check if the param string container either param_email, param_aws_account_number, or param_subscription_allowed_list
    param.include?("param_email") || param.include?("param_aws_account_number") || param.include?("param_subscriptions_list") || param.include?("param_subscriptions_allow_or_deny") ? nil : output_pt_params.push(param)
  end
  # Replace placeholder with the identified output parameter blocks
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_PARAMETERS_BLOCKS__", output_pt_params.join("\n\n"))
  # Replace placeholder with credentials blocks from child policy
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CREDENTIALS_BLOCKS__", credentials.join("\n\n"))

  # For each check, build the consolidated incident check and datasource
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CONSOLIDATED_INCIDENT_CHECKS__", consolidated_incidents_checks.join("\n"))
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CONSOLIDATED_INCIDENT_DATASOURCES__", consolidated_indidents_datasources.join("\n"))

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
