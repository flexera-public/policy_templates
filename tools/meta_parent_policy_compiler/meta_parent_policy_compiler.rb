require "json"
require "logger"

if ARGV.length != 1
  puts "Usage: ruby meta_parent_policy_compiler.rb <path_to_child_policy_template>"
  exit
end
file_path = ARGV[0]
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
parameters = pt.scan(/parameter ".*?" do.*?end/m)

# print("Parameters:\n")
# print(parameters.join("\n---------\n"))
# print("\n###########################\n")

# Get the credentials
credentials = pt.scan(/credentials ".*?" do.*?end/m)



consolidated_incident_datasource_template = <<-EOL
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

consolidated_incident_template = <<-EOS
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
EOS
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
  # From vb string, capture the string between field and do within the export block
  # Between the `export do` and `end` statements, capture the field statements that are between `field` and `do`
  export_block = validate_block.scan(/export.*?do.*?^  end/m)
  # print("Export Block: \n")
  # print(export_block)
  # print("\n---\n")
  # From the export block, capture the field names
  fields = export_block[0].scan(/(^.*field\s+\".*?\".*?end)/m).flatten
  fields.each do |field|
    # Remove path from the field output in the meta parent
    field.gsub!(/\n.*?path.*?\n/, "\n")
    # Lazy way to remove the export do // resource_level true blocks that are not needed.
    # A better solution would be a better regex above to capture only the field statements
    field.gsub!(/ *?export.*?do\n *resource_level true\n *field/, "field")
    # Add 6 spaces to the beginning of each field to make it align with the policy.validate.export.<field> in the meta parent
    field = "      " + field
    # print("Field:\n#{JSON.pretty_generate(field)}")

  end
  # print("\n")
  # print("Incident String: ")
  # print(validate_block)
  # print("\n\n")
  # From each validate block, capture the summary_template and detail_template
  summary_template = validate_block.scan(/summary_template\s+\"(.*?)\"/m)
  summary_template = validate_block.scan(/summary_template\s+<<-EOS\s+(.*?)EOS/m) if summary_template.empty?
  # From the summary template, capture the longest string that contains only letters and spaces
  # print("Summary Template:\n")
  summary_template_search_string = summary_template[0][0].scan(/[a-zA-Z\s]+/).max_by(&:length).strip
  # print("Summary Template Search String:\n")
  # print(summary_template_search_string)
  # print("\n------------------\n")

  # Get the datasource name from the validate block
  # The name of the datsource comes after the datasource keyword and before the do keyword
  # Example:
  # validate $ds_child_incident_details
  datasource_name = validate_block.scan(/(?:validate|validate_each)\s(.*?)\s+do/m)[0][0]
  # Strip leading $ from the datasource name
  datasource_name.gsub!(/^\$/, "")


  # print("Fields: \n")
  # # print(JSON.pretty_generate(field_names))
  # fields.each do |field|
  #   # Prefix each field with 6 spaces
  #   # This will align it under the policy.validate.export.<field> in the meta parent
  #   print("      "+field)
  #   print("\n")
  # end
  # print("\n---\n")
  output_ds = consolidated_incident_datasource_template
  output_check = consolidated_incident_template

  output_ds = output_ds.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_RESOURCE_TYPE_NAME__", summary_template_search_string)
  output_incident = output_check.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_RESOURCE_TYPE_NAME__", summary_template_search_string)

  output_ds = output_ds.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_FIELDS__", fields.join("\n"))

  output_ds = output_ds.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE__", datasource_name)
  output_incident = output_incident.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_DATASOURCE__", datasource_name)

  output_incident = output_incident.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CONSOLIDATED_INCIDENT_FIELDS__", fields.join("\n      "))

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
# Copy the parent_pt to output_pt
output_pt = parent_pt
output_pt_path = File.basename(file_path).split(".")[0] + "_meta_parent.pt"
# Replace __PLACEHOLDER_FOR_CHILD_POLICY_NAME__ with the name of the child policy
output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_NAME__", name)
output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_VERSION__", version)
# Attempt to identify the URL to the child policy template file on github using the file_path provided
# This would only work if the pt file is located under the `policy_templates` repo directory
# If it is not, then the URL will be incorrect
# This is a limitation of this script
# Get full path to the pt file provided
pt_path_expanded = File.expand_path(file_path)
pt_path_repo_file = pt_path_expanded.split("policy_templates/")[1]
pt_path_repo_dir = pt_path_repo_file.split("/")[0..-2].join("/")
github_url = "https://github.com/flexera-public/policy_templates/tree/master/#{pt_path_repo_dir}"
output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_GITHUB_URL__", github_url)
# Build a list of parameter block strings for the output pt
# We need to do this because we need to exclude the param_email and param_aws_account_number params from meta parent pt
output_pt_params = []
parameters.each do |param|
  # Check if the param string container either param_email, param_aws_account_number, or param_subscription_allowed_list
  param.include?("param_email") || param.include?("param_aws_account_number") || param.include?("param_subscription_allowed_list") ? nil : output_pt_params.push(param)
end
# Replace __PLACEHOLDER_FOR_CHILD_POLICY_PARAMETERS_BLOCKS__ with the identified output parameter blocks
output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_PARAMETERS_BLOCKS__", output_pt_params.join("\n\n"))
# Replace __PLACEHOLDER_FOR_CHILD_POLICY_CREDENTIALS_BLOCKS__ with credentials blocks from child policy
output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CHILD_POLICY_CREDENTIALS_BLOCKS__", credentials.join("\n\n"))

# For each check, build the consolidated incident check and datasource
output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CONSOLIDATED_INCIDENT_CHECKS__", consolidated_incidents_checks.join("\n"))
output_pt = output_pt.gsub("__PLACEHOLDER_FOR_CONSOLIDATED_INCIDENT_DATASOURCES__", consolidated_indidents_datasources.join("\n"))


outfile_path = File.dirname(file_path) + "/" + output_pt_path
print("Writing output to: "+outfile_path+"\n")
outfile = File.open(outfile_path, "w")
outfile.puts(output_pt)
outfile.close
