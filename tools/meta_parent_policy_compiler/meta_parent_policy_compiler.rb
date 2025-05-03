require "json"
require "yaml"

# Report usage info and exit with error if parameters are malformed
def invalid_parameters()
  print("Parameters not provided or malformed.\n\n")
  print("- Specify --from-list as the first parameter and the file path of a YAML file as the second parameter to automatically generate meta parents from a list of file paths.\n")
  print("  Example: ruby meta_parent_policy_compiler.rb --from-list default_template_files.yaml\n\n")
  print("- Specify --target-policy as the first parameter, a policy template file path as the second parameter and a cloud provider (aws azure google) for the third parameter to generate a meta parent policy template from one of the provided meta parent templates for major cloud providers.\n")
  print("  Example: ruby meta_parent_policy_compiler.rb --target-policy local/aws/aws_vms.pt aws\n\n")
  print("- Specify --target-policy as the first parameter, a policy template file path as the second parameter, 'custom' for the third parameter, and a meta parent template file path for the fourth parameter to generate a meta parent policy template using a custom meta parent template file.\n")
  print("  Example: ruby meta_parent_policy_compiler.rb --target-policy local/oci/oci_vms.pt custom local/oci/oci_vms_meta_parent.pt.template\n\n")
  exit(1)
end

def bad_file_path(file_path)
  print("Provided file path is invalid. File does not exist or is unreadable:\n#{file_path}\n\n")
  exit(1)
end

# Check parameters and set things accordingly
invalid_parameters() if ARGV[0] == nil
invalid_parameters() if ARGV[0] == "--from-list" && ARGV[1] == nil
invalid_parameters() if ARGV[0] == "--target-policy" && ARGV[1] == nil
invalid_parameters() if ARGV[0] == "--target-policy" && ARGV[2] != "aws" && ARGV[2] != "azure" && ARGV[2] != "google" && ARGV[2] != "custom"
invalid_parameters() if ARGV[0] == "--target-policy" && ARGV[2] == "custom" && ARGV[3] == nil

bad_file_path(ARGV[1]) if ARGV[0] == "--from-list" && !File.exist?(ARGV[1])
bad_file_path(ARGV[1]) if ARGV[0] == "--target-policy" && !File.exist?(ARGV[1])
bad_file_path(ARGV[3]) if ARGV[0] == "--target-policy" && ARGV[2] == "custom" && !File.exist?(ARGV[3])

specified_parent_pt_path = nil

if ARGV[0] == "--from-list"
  child_policy_template_files_yaml = YAML.load_file(ARGV[1])
  child_policy_template_files = child_policy_template_files_yaml["policy_templates"]
elsif ARGV[0] == "--target-policy"
  child_policy_template_files = [ ARGV[1] ]

  if ARGV[2] == "aws"
    specified_parent_pt_path = "aws_meta_parent.pt.template"
  elsif ARGV[2] == "azure"
    specified_parent_pt_path = "azure_meta_parent.pt.template"
  elsif ARGV[2] == "google"
    specified_parent_pt_path = "google_meta_parent.pt.template"
  elsif ARGV[2] == "custom"
    specified_parent_pt_path = ARGV[3]
  end
end

# Compile Meta Parent Policy Definition
# This function takes a child policy template file path
# as input and outputs a meta parent policy definition
def compile_meta_parent_policy(file_path, specified_parent_pt_path)
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
  deprecated_scan = pt.scan(/deprecated: "(.*?)"/)
  deprecated = "false"
  deprecated = deprecated_scan[0][0] if !deprecated_scan.empty?
  # get the hide_skip_approvals string if it exists, defaulting to false if not present
  hide_skip_approvals_scan = pt.scan(/hide_skip_approvals: "(.*?)"/)
  hide_skip_approvals = ""
  hide_skip_approvals = hide_skip_approvals_scan[0][0] if !hide_skip_approvals_scan.empty?
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
  checks = pt.scan(/^\s+validate.*?do.*?^  end/m).select { |check| check.include?("export ") }

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
    fields = [] # Provide a default value, which is no fields declared
    # Check if export_block is length > 0
    if export_block.length > 0
      fields = export_block[0].scan(/(^.*field\s+\".*?\".*?end)/m).flatten
    end
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

  # Use user-specified cloud provider path if provided
  # Otherwise, derive it from file name
  if specified_parent_pt_path != nil
    parent_pt_path = specified_parent_pt_path
  elsif file_path.include?("aws")
    parent_pt_path = "aws_meta_parent.pt.template"
  elsif file_path.include?("azure")
    parent_pt_path = "azure_meta_parent.pt.template"
  elsif file_path.include?("google")
    parent_pt_path = "google_meta_parent.pt.template"
  else
    print("Could not determine parent policy template to use for #{file_path}\n")
    exit(1)
  end

  # Exit with error if the template does not exist
  bad_file_path(parent_pt_path) if !File.exist?(parent_pt_path)

  parent_pt = File.open(parent_pt_path, "rb").read
  # Copy the parent_pt to output_pt so we can manipulate it safely
  output_pt = parent_pt
  output_pt_path = File.basename(file_path).split(".")[0] + "_meta_parent.pt"
  # Replace __PLACEHOLDER_FOR_CHILD_POLICY_NAME__ with the name of the child policy
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_NAME__", name)
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_VERSION__", version)
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_PUBLISH__", publish)
  output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_DEPRECATED__", deprecated)
  if !hide_skip_approvals.empty?
    output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_HIDE_SKIP_APPROVALS__", hide_skip_approvals)
  else
    # Remove the entire line containing hide_skip_approvals
    output_pt = output_pt.gsub(/^\s*,?\s*hide_skip_approvals: "__PLACEHOLDER_FOR_CHILD_POLICY_HIDE_SKIP_APPROVALS__",?\s*\n/, "")
    output_pt = output_pt.gsub(/,\s*\)/, "\n)")
  end
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

# Loop through all Policy Templates specified
child_policy_template_files.each do |child_policy_template|
  compile_meta_parent_policy(child_policy_template, specified_parent_pt_path)
end
