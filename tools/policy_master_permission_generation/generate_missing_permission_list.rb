#encoding: UTF-8
require 'fileutils'
require 'find'
require 'json'
require 'yaml'

# List of Validated Policy Templates
validated_pt_files_yaml = YAML.load_file("./tools/policy_master_permission_generation/validated_policy_templates.yaml")
validated_pt_files = validated_pt_files_yaml["validated_policy_templates"]

# List of Relevant Policy Templates in Repo
found_pt_files = []

Find.find(".") do |path|
  next unless File.file?(path)          # Skip if not a file
  next unless path =~ /\.pt\z/          # File must end with .pt
  next if path =~ /meta_parent/         # Exclude files containing 'meta_parent' in the filename
  next if path =~ /\/tools\//           # Exclude files in the /tools directory
  next if path =~ /\/data\//            # Exclude files in the /data directory

  # Check if the file contains the string 'deprecated: "true"'
  file_contents = File.read(path)
  next if file_contents =~ /deprecated:\s*\"true\"/i

  # Add file path if all criteria are met
  found_pt_files << path
end

# Find missing files
missing_files = found_pt_files - validated_pt_files

# Record missing files
json_file_path = './data/policy_permissions_list/missing_policy_templates.json'
yaml_file_path = './data/policy_permissions_list/missing_policy_templates.yaml'

data = { "missing_templates" => missing_files }
json_data = JSON.pretty_generate(data, indent: '  ')  # 2-space indentation
yaml_data = data.to_yaml

FileUtils.mkdir_p(File.dirname(json_file_path))
FileUtils.mkdir_p(File.dirname(yaml_file_path))
File.open(json_file_path, 'w') { |file| file.write(json_data) }
File.open(yaml_file_path, 'w') { |file| file.write(yaml_data) }
