require "json"
require "time"

# File paths
activepolicy_json_filepath = "../../data/active_policy_list/active_policy_list.json"
permission_json_filepath = "../../data/policy_permissions_list/master_policy_permissions_list.json"
template_filepath = "./aws_cft_generator.template.txt"
output_filepath = "./FlexeraAutomationPolicies.template"

# Get list of deprecated and generally recommended policies
activepolicy_json = JSON.parse(File.read(activepolicy_json_filepath))

deprecated_policies = activepolicy_json["policies"].select { |policy| policy["deprecated"] == true }
deprecated_names = deprecated_policies.map { |policy| policy["name"] }

recommended_policies = activepolicy_json["policies"].select { |policy| policy["generally_recommended"] == true }
recommended_names = recommended_policies.map { |policy| policy["name"] }

# Read AWS permissions data
permission_json = JSON.parse(File.read(permission_json_filepath))

# Remap data for easy parsing
permission_list = []

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
end

# Sort alphabetically and by whether policy is recommended or not
sorted_permission_list = permission_list.sort_by { |policy| policy["name"] }
recommended_list = sorted_permission_list.select { |policy| recommended_names.include?(policy["name"]) }
other_list = sorted_permission_list.select { |policy| !recommended_names.include?(policy["name"]) }
final_permission_list = recommended_list + other_list

# Create strings to insert into template
parameter_groups = ""
parameter_labels = ""
parameter_group_definitions = ""
conditions = ""
mappings = ""
resources = ""

final_permission_list.each do |policy|
  # Entry for __PLACEHOLDER_FOR_PARAMETER_GROUPS__
  parameter_groups += "          ## " + policy["name"] + "\n"
  parameter_groups += "          - paramPerms" + policy["short_name"] + "\n"

  # Entry for __PLACEHOLDER_FOR_PARAMETER_LABELS__
  parameter_labels += "      ## " + policy["name"] + "\n"
  parameter_labels += "      paramPerms" + policy["short_name"] + ":\n"

  if recommended_names.include?(policy["name"])
    parameter_labels += "        default: \"[RECOMMENDED] Permissions for Policy Template: " + policy["name"] + "\"\n"
  else
    parameter_labels += "        default: \"Permissions for Policy Template: " + policy["name"] + "\"\n"
  end

  # Entry for __PLACEHOLDER_FOR_PARAMETER_GROUP_DEFINITIONS__
  parameter_group_definitions += "  ## " + policy["name"] + "\n"

  parameter_group_definitions += "  paramPerms" + policy["short_name"] + ":\n"

  if recommended_names.include?(policy["name"])
    parameter_group_definitions += "    Description: '[RECOMMENDED] What permissions should policies using \"" + policy["name"] + "\" Policy Template be granted on the IAM Role that will be created?'\n"
  else
    parameter_group_definitions += "    Description: 'What permissions should policies using \"" + policy["name"] + "\" Policy Template be granted on the IAM Role that will be created?'\n"
  end

  parameter_group_definitions += "    Type: String\n"

  # Only default to access if policy has read permissions and is a recommended policy
  if policy["read"].empty? || !recommended_names.include?(policy["name"])
    parameter_group_definitions += "    Default: No Access\n"
  else
    parameter_group_definitions += "    Default: Read Only\n"
  end

  parameter_group_definitions += "    AllowedValues:\n"
  parameter_group_definitions += "      - No Access\n"
  parameter_group_definitions += "      - Read Only\n" unless policy["read"].empty?
  parameter_group_definitions += "      - Read and Take Action\n" unless policy["action"].empty?

  # Entry for __PLACEHOLDER_FOR_CONDITIONS__
  conditions += "  ## " + policy["name"] + "\n"

  unless policy["read"].empty?
    conditions += "  CreatePolicy" + policy["short_name"] + "Read: !Not\n"
    conditions += "    - !Equals\n"
    conditions += "      - !Ref paramPerms" + policy["short_name"] + "\n"
    conditions += "      - No Access\n"
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
empty_template = File.read(template_filepath)

final_template = empty_template.gsub("__PLACEHOLDER_FOR_GENERATION_DATETIME__", Time.now.utc.iso8601)
final_template = final_template.gsub("__PLACEHOLDER_FOR_PARAMETER_GROUPS__", parameter_groups)
final_template = final_template.gsub("__PLACEHOLDER_FOR_PARAMETER_LABELS__", parameter_labels)
final_template = final_template.gsub("__PLACEHOLDER_FOR_PARAMETER_GROUP_DEFINITIONS__", parameter_group_definitions)
final_template = final_template.gsub("__PLACEHOLDER_FOR_CONDITIONS__", conditions)
final_template = final_template.gsub("__PLACEHOLDER_FOR_MAPPINGS__", mappings)
final_template = final_template.gsub("__PLACEHOLDER_FOR_RESOURCES__", resources)

# Write new CloudFormation Template to disk
output_file = File.open(output_filepath, "w")
output_file.puts(final_template)
output_file.close
