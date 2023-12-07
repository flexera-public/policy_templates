#encoding: UTF-8
require 'json'
require 'fileutils'

class Readme
	attr_accessor :path, :credentials

	def initialize(path, credentials: [])
		@path = path
		@credentials = credentials
	end
end

class PolicyTemplate
  attr_accessor :name, :path

  def initialize(name, path)
    @name = name
    @path = path
  end
end

# Get a list of all README and Policy Template files
policy_categories = [ "automation", "compliance", "cost", "operational", "saas", "security" ]

pt_files = Dir.glob('./**/*.pt')
readme_files = []
policy_categories.each do |category|
  readme_files += Dir.glob("./#{category}/**/[Rr][Ee][Aa][Dd][Mm][Ee]*")
end

# Initialize arrays to store README array of objects and Policy Template array of objects
policy_templates = []
readmes = []

# Process Policy Template files
pt_files.each do |file|
  pt_content = File.read(file)
  name = pt_content.match(/name "([^"]+)"/)&.captures&.first
  policy_templates << PolicyTemplate.new(name, file) if name
end

# Process README files
def extract_permissions_from_readme(readme_content)
  policy_credentials = []

  # Identify Sections to look for Permissions, Roles, APIs
  sections = [
    "[**AWS Credentials**]",
    "[**AWS Credential**]",
    "[**Azure Resource Manager Credential**]",
    "[**Google Cloud Credential**]",
    "[**Flexera Credential**]"
  ]

  sections.each do |section|
    case section
    when "[**AWS Credentials**]", "[**AWS Credential**]"
      provider = "aws"
    when "[**Azure Resource Manager Credential**]"
      provider = "azure"
    when "[**Google Cloud Credential**]"
      provider = "gcp"
    when "[**Flexera Credential**]"
      provider = "flexera"
    end

    if section_start = readme_content.index(section)

      # Extract the text from this section
      section_text = readme_content[section_start..-1]
    
      credentials_section = ""
      section_text.each_line do |line|
        break if line.strip.start_with?( "##", "###", "- [**") && !line.strip.start_with?(section)

        if line.strip == "- Roles"
          credentials_section = "roles"
        elsif line.strip == "- Permissions"
          credentials_section = "permissions"
        else
          line.scan(/-\s*`([^`]+)`/) do |match|
            if credentials_section == "roles"
              policy_credentials << { role: match.first, provider: provider,  }
            elsif credentials_section == "permissions"
              policy_credentials << { permission: match.first, provider: provider }
            else
              policy_credentials << { permission: match.first, provider: provider }
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
    readme_content.force_encoding('ISO-8859-1')
    readme_content.encode('utf-8', replace: nil)

    # if path == "./cost/google/idle_persistent_disk_recommendations/README.md"
      policy_credentials = extract_permissions_from_readme(readme_content)
    # end
  
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
      "name" => matching_template.name
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
            cred_permissions.push(credential[:permission])
          elsif credential[:role]
            cred_roles.push(credential[:role])
          end
        end

        if cred_permissions.any?
          provider[:permissions] = cred_permissions
        end
        if cred_roles.any?
          provider[:roles] = cred_roles
        end
      end

      policy_template_details[:providers] = cred_providers
    end

    # Push each policy template permission details to the 'values' array
    values.push(policy_template_details)
  end
end

master_policy_permissions_doc[:values] = values

# Create '.data/policy_permissions_list' directory
# permissions_list_dir = "./dist"
permissions_list_dir = "./data/policy_permissions_list"
FileUtils.mkdir_p(permissions_list_dir) unless Dir.exist?(permissions_list_dir)

# Create JSON document in '.data/policy_permissions_list' directory
File.open("#{permissions_list_dir}/master_policy_permissions_list.json", "w") do |f|
  f.write(JSON.pretty_generate(master_policy_permissions_doc))
end
