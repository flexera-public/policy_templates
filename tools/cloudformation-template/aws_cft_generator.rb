require "json"
require "time"

# Method for generating template
def create_template(perm_list, template_path)
  # Create strings to insert into template
  parameter_groups = ""
  parameter_labels = ""
  parameter_group_definitions = ""
  conditions = ""
  mappings = ""
  resources = ""

  perm_list.each do |policy|
    # Entry for __PLACEHOLDER_FOR_PARAMETER_GROUPS__
    parameter_groups += "          ## " + policy["name"] + "\n"
    parameter_groups += "          - paramPerms" + policy["short_name"] + "\n"

    # Entry for __PLACEHOLDER_FOR_PARAMETER_LABELS__
    parameter_labels += "      ## " + policy["name"] + "\n"
    parameter_labels += "      paramPerms" + policy["short_name"] + ":\n"

    if policy["id"] == "all_policy_templates"
      parameter_labels += "        default: \"Permissions for all AWS Policy Templates\"\n"
    else
      parameter_labels += "        default: \"Permissions for Policy Template: " + policy["name"] + "\"\n"
    end

    # Entry for __PLACEHOLDER_FOR_PARAMETER_GROUP_DEFINITIONS__
    parameter_group_definitions += "  ## " + policy["name"] + "\n"

    parameter_group_definitions += "  paramPerms" + policy["short_name"] + ":\n"

    if policy["id"] == "all_policy_templates"
      parameter_group_definitions += "    Description: 'What permissions for all AWS Policy Templates should be granted on the AWS Role that will be created? Note that the more granular permissions below only need to be enabled if this option is disabled or you want to grant access to take actions only for specific policy templates.'\n"
    else
      parameter_group_definitions += "    Description: 'What permissions for the \"" + policy["name"] + "\" Policy Template should be granted on the AWS Role that will be created?'\n"
    end

    parameter_group_definitions += "    Type: String\n"

    if policy["id"] == "all_policy_templates"
      parameter_group_definitions += "    Default: Read Only\n"
    else
      parameter_group_definitions += "    Default: None\n"
    end

    parameter_group_definitions += "    AllowedValues:\n"
    parameter_group_definitions += "      - None\n"
    parameter_group_definitions += "      - Read Only\n" unless policy["read"].empty?
    parameter_group_definitions += "      - Read and Take Action\n" unless policy["action"].empty?

    # Entry for __PLACEHOLDER_FOR_CONDITIONS__
    conditions += "  ## " + policy["name"] + "\n"

    unless policy["read"].empty?
      conditions += "  CreatePolicy" + policy["short_name"] + "Read: !Not\n"
      conditions += "    - !Equals\n"
      conditions += "      - !Ref paramPerms" + policy["short_name"] + "\n"
      conditions += "      - None\n"
    end

    unless policy["action"].empty?
      conditions += "  CreatePolicy" + policy["short_name"] + "Action: !Equals\n"
      conditions += "    - !Ref paramPerms" + policy["short_name"] + "\n"
      conditions += "    - Read and Take Action\n"
    end

    # Entry for __PLACEHOLDER_FOR_MAPPINGS__
    mappings += "    ## " + policy["name"] + "\n"
    mappings += "    " + policy["short_name"] + ":\n"

    if policy["read"].empty?
      mappings += "      read: []\n"
    else
      mappings += "      read:\n"

      policy["read"].each do |permission|
        mappings += "        - \"" + permission + "\"\n"
      end
    end

    if policy["action"].empty?
      mappings += "      action: []\n"
    else
      mappings += "      action:\n"

      policy["action"].each do |permission|
        mappings += "        - \"" + permission + "\"\n"
      end
    end

    # Entry for __PLACEHOLDER_FOR_RESOURCES__
    resources += "  ## " + policy["name"] + "\n"

    unless policy["read"].empty?
      resources += "  iamPolicy" + policy["short_name"] + "Read:\n"
      resources += "    Type: \"AWS::IAM::Policy\"\n"
      resources += "    Condition: CreatePolicy" + policy["short_name"] + "Read\n"
      resources += "    Properties:\n"
      resources += "      PolicyName: !Join\n"
      resources += "        - \"_\"\n"
      resources += "        - - !Ref paramRoleName\n"
      resources += "          - " + policy["short_name"] + "ReadPermissionPolicy\n"
      resources += "      Roles:\n"
      resources += "        - !Ref iamRole\n"
      resources += "      PolicyDocument:\n"
      resources += "        Version: 2012-10-17\n"
      resources += "        Statement:\n"
      resources += "          - Effect: Allow\n"
      resources += "            Action: !FindInMap\n"
      resources += "              - PermissionMap\n"
      resources += "              - " + policy["short_name"] + "\n"
      resources += "              - read\n"
      resources += "            Resource: \"*\"\n"
    end

    unless policy["action"].empty?
      resources += "  iamPolicy" + policy["short_name"] + "Action:\n"
      resources += "    Type: \"AWS::IAM::Policy\"\n"
      resources += "    Condition: CreatePolicy" + policy["short_name"] + "Action\n"
      resources += "    Properties:\n"
      resources += "      PolicyName: !Join\n"
      resources += "        - \"_\"\n"
      resources += "        - - !Ref paramRoleName\n"
      resources += "          - " + policy["short_name"] + "ActionPermissionPolicy\n"
      resources += "      Roles:\n"
      resources += "        - !Ref iamRole\n"
      resources += "      PolicyDocument:\n"
      resources += "        Version: 2012-10-17\n"
      resources += "        Statement:\n"
      resources += "          - Effect: Allow\n"
      resources += "            Action: !FindInMap\n"
      resources += "              - PermissionMap\n"
      resources += "              - " + policy["short_name"] + "\n"
      resources += "              - action\n"
      resources += "            Resource: \"*\"\n"
    end
  end

  # Generate new CloudFormation Template
  empty_template = File.read(template_path)

  final_template = empty_template.gsub("__PLACEHOLDER_FOR_GENERATION_DATETIME__", Time.now.utc.iso8601)
  final_template = final_template.gsub("__PLACEHOLDER_FOR_PARAMETER_GROUPS__", parameter_groups)
  final_template = final_template.gsub("__PLACEHOLDER_FOR_PARAMETER_LABELS__", parameter_labels)
  final_template = final_template.gsub("__PLACEHOLDER_FOR_PARAMETER_GROUP_DEFINITIONS__", parameter_group_definitions)
  final_template = final_template.gsub("__PLACEHOLDER_FOR_CONDITIONS__", conditions)
  final_template = final_template.gsub("__PLACEHOLDER_FOR_MAPPINGS__", mappings)
  final_template = final_template.gsub("__PLACEHOLDER_FOR_RESOURCES__", resources)

  return final_template
end

# File paths
activepolicy_json_filepath = "../../data/active_policy_list/active_policy_list.json"
permission_json_filepath = "../../data/policy_permissions_list/master_policy_permissions_list.json"
template_filepath = "./aws_cft_generator.template.txt"
output_filepath = "./FlexeraAutomationPolicies.template"
output_readonly_filepath = "./FlexeraAutomationPoliciesReadOnly.template"

# Get list of deprecated policies
activepolicy_json = JSON.parse(File.read(activepolicy_json_filepath))
deprecated_policies = activepolicy_json["policies"].select { |policy| policy["deprecated"] == true }
deprecated_names = deprecated_policies.map { |policy| policy["name"] }

# Read AWS permissions data
permission_json = JSON.parse(File.read(permission_json_filepath))

# Remap data for easy parsing
permission_list = []
readonly_permission_list = []

permission_json['values'].each do |item|
  read = []
  action = []

  if item["providers"]
    item["providers"].each do |provider|
      if provider["name"] == "aws"
        provider["permissions"].each do |permission|
          if permission["read_only"]
            read << permission["name"]
          else
            action << permission["name"]
          end
        end
      end
    end
  end

  # Skip deprecated policies and policies with no permissions needed
  unless (read.empty? && action.empty?) || deprecated_names.include?(item["name"])
    short_name = item["name"].gsub(/[^a-zA-Z0-9]/, '')

    permission_list << {
      "id" => item["id"],
      "name" => item["name"],
      "short_name" => short_name,
      "version" => item["version"],
      "read" => read,
      "action" => action
    }
  end

  unless read.empty? || deprecated_names.include?(item["name"])
    short_name = item["name"].gsub(/[^a-zA-Z0-9]/, '')

    readonly_permission_list << {
      "id" => item["id"],
      "name" => item["name"],
      "short_name" => short_name,
      "version" => item["version"],
      "read" => read,
      "action" => []
    }
  end
end

# Create special entry for all AWS policy templates
special_permission_list = []
readonly_special_permission_list = []

all_read = permission_list.map { |policy| policy["read"] }.flatten.uniq.sort
all_action = permission_list.map { |policy| policy["action"] }.flatten.uniq.sort

special_permission_list << {
  "id" => "all_policy_templates",
  "name" => "All AWS Policy Templates",
  "short_name" => "AllAWSPolicyTemplates",
  "version" => "1.0",
  "read" => all_read,
  "action" => all_action
}

readonly_special_permission_list << {
  "id" => "all_policy_templates",
  "name" => "All AWS Policy Templates",
  "short_name" => "AllAWSPolicyTemplates",
  "version" => "1.0",
  "read" => all_read,
  "action" => []
}

# Sort alphabetically and by whether policy is recommended or not
sorted_permission_list = permission_list.sort_by { |policy| policy["name"] }
final_permission_list = special_permission_list + sorted_permission_list

readonly_sorted_permission_list = readonly_permission_list.sort_by { |policy| policy["name"] }
readonly_final_permission_list = readonly_special_permission_list + readonly_sorted_permission_list

final_template = create_template(final_permission_list, template_filepath)
readonly_final_template = create_template(readonly_final_permission_list, template_filepath)

# Write new CloudFormation Templates to disk
output_file = File.open(output_filepath, "w")
output_file.puts(final_template)
output_file.close

output_file = File.open(output_readonly_filepath, "w")
output_file.puts(readonly_final_template)
output_file.close
