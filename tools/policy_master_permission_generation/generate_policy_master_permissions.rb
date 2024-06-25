#encoding: UTF-8
require 'json'
require 'fileutils'
require 'yaml'

# List of Policy Templates
# Open YAML and parse validated_policy_templates[] array
pt_files_yaml = YAML.load_file("./tools/policy_master_permission_generation/validated_policy_templates.yaml")
pt_files = pt_files_yaml["validated_policy_templates"]

class Readme
	attr_accessor :path, :credentials

	def initialize(path, credentials: [])
		@path = path
		@credentials = credentials
	end
end

class PolicyTemplate
  attr_accessor :name, :path, :version

  def initialize(name, path, version)
    @name = name
    @path = path
    @version = version
  end
end

readme_files = []
pt_files.each do |pt|
  # Get the README file for each Policy Template
  readme_files += Dir.glob("#{File.dirname(pt)}/[Rr][Ee][Aa][Dd][Mm][Ee]*")
end

# Initialize arrays to store README array of objects and Policy Template array of objects
policy_templates = []
readmes = []

# Process Policy Template files
pt_files.each do |file|
  pt_content = File.read(file)
  pt_name = pt_content.match(/name "([^"]+)"/)&.captures&.first

  pt_version_match = pt_content.match(/version:\s*\"([^\"]+)\"/)
  pt_version = pt_version_match[1] if pt_version_match

  policy_templates << PolicyTemplate.new(pt_name, file, pt_version) if pt_name
end

# Process README files
def extract_permissions_from_readme(readme_content)
  policy_credentials = []

  # Identify Sections to look for Permissions, Roles, APIs
  sections = [
    "[**AWS Credentials**]",
    "[**AWS Credential**]",
    "[**Azure Resource Manager Credential**]",
    "[**Azure Storage Credential**]",
    "[**Azure China Enterprise Agreement Credential**]",
    "[**Google Cloud Credential**]",
    "[**Flexera Credential**]",
    "[**Turbonomic Credential**]",
  ]

  sections.each do |section|
    case section
    when "[**AWS Credentials**]", "[**AWS Credential**]"
      provider = "aws"
    when "[**Azure Resource Manager Credential**]"
      provider = "azure_rm"
    when "[**Azure Storage Credential**]"
      provider = "azure_storage"
    when "[**Azure China Enterprise Agreement Credential**]"
      provider = "azure_ea_china"
    when "[**Google Cloud Credential**]"
      provider = "gce"
    when "[**Flexera Credential**]"
      provider = "flexera"
    when "[**Turbonomic Credential**]"
      provider = "turbonomic"
    end

    # If the Credential Section exists...
    if section_start = readme_content.index(section)
      # Extract the text from this section
      section_text = readme_content[section_start..-1]

      # Find the line starting with '/*' or '†' to get any specific notes around permissions from the README
      list_of_notes = []
      # note = ""
      section_text.each_line do |line|
        break if line.strip.start_with?( "##", "###", "- [**") && !line.strip.start_with?(section)

        if line.strip.start_with?("\\*")
          asterisk_note = line.strip.sub(/^\\\*\s*/, '')
          list_of_notes << { symbol: "*", detail: asterisk_note }
        elsif line.strip.start_with?("\u2020")
          dagger_note = line.strip.sub(/^\†\s*/, '')
          list_of_notes << { symbol: "†", detail: dagger_note }
        end
      end

      # For each line within the Section get the list of permissions and roles and push to 'policy_credentials' object
      credentials_section = ""
      section_text.each_line do |line|
        break if line.strip.start_with?( "##", "###", "- [**") && !line.strip.start_with?(section)

        if line.strip == "- Roles" || line.strip == "- Role"
          credentials_section = "roles"
        elsif line.strip == "- Permissions" || line.strip == "Permission"
          credentials_section = "permissions"
        else
          line.scan(/-\s*`([^`]+)`\*?/) do |match|
            permission = match.first

            # Set whether permission is read-only, required, and/or has a description (and depending on the symbol)
            read_only_permission = true
            required = true

            # Checks for a symbol (which would denote that the permission has an accompanying description)
            symbol_if_exists = list_of_notes.find { |note| permission.end_with?(note[:symbol]) == true || line.include?(note[:symbol]) == true }

            if symbol_if_exists != nil && !symbol_if_exists[:detail].strip.empty?
              required = false
              if symbol_if_exists[:detail].include?("Only required for taking action")
                read_only_permission = false
              end

              permission = permission.chomp(symbol_if_exists[:symbol])

              if credentials_section == "roles"
                policy_credentials << { role: permission, provider: provider, read_only: read_only_permission, required: required, description: symbol_if_exists[:detail] }
              elsif credentials_section == "permissions"
                policy_credentials << { permission: permission, provider: provider, read_only: read_only_permission, required: required, description: symbol_if_exists[:detail] }
              else
                policy_credentials << { permission: permission, provider: provider, read_only: read_only_permission, required: required, description: symbol_if_exists[:detail] }
              end
            else
              if credentials_section == "roles"
                policy_credentials << { role: permission, provider: provider, read_only: read_only_permission, required: required }
              elsif credentials_section == "permissions"
                policy_credentials << { permission: permission, provider: provider, read_only: read_only_permission, required: required }
              else
                policy_credentials << { permission: permission, provider: provider, read_only: read_only_permission, required: required }
              end
            end
          end
        end
      end
    end
  end

  policy_credentials
end

readme_files.each do |path|
  begin
    readme_content = File.read(path)
    # ignore non-UTF-8 characters in readmes
    # readme_content.force_encoding('ISO-8859-1')
    readme_content.force_encoding('utf-8')
    readme_content.encode('utf-8', replace: nil)

    policy_credentials = extract_permissions_from_readme(readme_content)

    readmes <<Readme.new(path, credentials: policy_credentials)
  rescue => e
    puts "Error processing file: #{path}"
    puts e.message
  end
end

# Create JSON structure for Master Policy Permissions Document
master_policy_permissions_doc = {}
values = []

readmes.each do |readme|
  # Match READMEs with Policy Templates based on paths
  matching_template = policy_templates.find { |template| readme.path.gsub("/README.md", "") == File.dirname(template.path) }
  if matching_template

    policy_template_details = {
      "id" => matching_template.path,
      "name" => matching_template.name,
      "version" => matching_template.version
    }

    if readme.credentials

      cred_providers = []
      readme.credentials.each do |cred|
        cred_providers.push({ name: cred[:provider] })
      end
      cred_providers = cred_providers.uniq

      cred_providers.each do |provider|
        cred_values = readme.credentials.select { |cred| cred[:provider] == provider[:name] }

        cred_permissions = []
        cred_roles = []
        cred_apis = []

        cred_values.each do |credential|
          if credential[:permission]

            permission_list = {
              "name" => credential[:permission],
              "read_only" => credential[:read_only],
              "required" => credential[:required]
            }
            permission_list["description"] = credential[:description] if credential[:description]

            cred_permissions.push(permission_list)
          elsif credential[:role]

            role_list = {
              "name" => credential[:role],
              "read_only" => credential[:read_only],
              "required" => credential[:required]
            }
            role_list["description"] = credential[:description] if credential[:description]

            cred_roles.push(role_list)
          end
        end

        if cred_permissions.any?
          provider[:permissions] = cred_permissions
        end
        if cred_roles.any?
          provider[:roles] = cred_roles
        end
      end

      policy_template_details[:providers] = cred_providers if cred_providers.any?
    end

    # Push each policy template permission details to the 'values' array
    values.push(policy_template_details)
  end
end

# Sort values by id
# Opted for id over name, because sometimes the name of a PT does change but the filename (id) very rarely changes
values.sort_by! { |value| value["id"] }

master_policy_permissions_doc[:values] = values
puts values

# Create '.data/policy_permissions_list' directory
# permissions_list_dir = "./dist"
permissions_list_dir = "./data/policy_permissions_list"
FileUtils.mkdir_p(permissions_list_dir) unless Dir.exist?(permissions_list_dir)

# Create JSON document in '.data/policy_permissions_list' directory
File.open("#{permissions_list_dir}/master_policy_permissions_list.json", "w") do |f|
  f.write(JSON.pretty_generate(master_policy_permissions_doc))
end

# Create YAML document in '.data/policy_permissions_list' directory
File.open("#{permissions_list_dir}/master_policy_permissions_list.yaml", "w") do |f|
  # Write YAML document
  f.write(master_policy_permissions_doc.to_yaml)
end
