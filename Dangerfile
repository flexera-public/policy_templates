# DangerFile
# https://danger.systems/reference.html

###############################################################################
# Required Libraries
###############################################################################

require 'uri'
require 'yaml'
require_relative 'tools/lib/policy_parser'

###############################################################################
# File Sorting
###############################################################################

# Create lists of files based on specific attributes for testing
# Renamed Files.
renamed_files = git.renamed_files.collect{ |r| r[:before] }
# Changed Files. Ignores renamed files to prevent errors on files that don't exist
changed_files = git.added_files + git.modified_files - renamed_files
# Changed Dangerfile
changed_dangerfile = changed_files.select{ |file| file == "Dangerfile" }
# Changed Dot Files
changed_dot_files = changed_files.select{ |file| file.start_with?(".") }
# Changed Config Files
config_files = ["Gemfile", "Gemfile.lock", "Rakefile", "package.json", "package-lock.json"]
changed_config_files = changed_files.select{ |file| config_files.include?(file) }
# Changed Policy Template files. Ignore meta policy files.
changed_pt_files = changed_files.select{ |file| file.end_with?(".pt") && !file.end_with?("meta_parent.pt") }
# Changed Meta Policy Template files.
changed_meta_pt_files = changed_files.select{ |file| file.end_with?("meta_parent.pt") }
# Changed README files.
changed_readme_files = changed_files.select{ |file| file.end_with?("/README.md") }
# Changed Changelog files.
changed_changelog_files = changed_files.select{ |file| file.end_with?("/CHANGELOG.md") }
# Changed MD files other than the above.
changed_misc_md_files = changed_files.select{ |file| file.end_with?(".md") && !file.end_with?("/README.md") && !file.end_with?("/CHANGELOG.md") }
# New Policy Template files. Ignore meta policy files.
new_pt_files = git.added_files.select{ |file| file.end_with?(".pt") && !file.end_with?("meta_parent.pt") }

###############################################################################
# Methods: General
###############################################################################

### Spell check test
# Run the Danger spell checker on a file
def general_spellcheck?(file)
  # Import the ignore list from a file but ignore entries starting with #
  # This is so we can have comments in this file
  prose.ignored_words = File.readlines('.spellignore').map(&:chomp).select{ |entry| !entry.start_with?("#") }

  # Disable functionality to prevent a lot of pointless results
  prose.ignore_numbers = true
  prose.ignore_acronyms = true

  # Set language
  prose.language = "en-us"

  # Check spelling
  prose.check_spelling(file)
end

### Markdown lint test
# Return false if linter finds no problems
def general_bad_markdown?(file)
  # Adjust testing based on which file we're doing
  case file
  when "README.md"
    mdl = `mdl -r "~MD007","~MD013","~MD024" #{file}`
  when "tools/cloudformation-template/README.md"
    mdl = `mdl -r "~MD007","~MD013","~MD033","~MD034" #{file}`
  when ".github/PULL_REQUEST_TEMPLATE.md"
    mdl = `mdl -r "~MD002","~MD007","~MD013" #{file}`
  else
    mdl = `mdl -r "~MD007","~MD013" #{file}`
  end

  # Return the problems found if the mdl file is not empty. Otherwise, return false
  return "**#{file}**\nMarkdown syntax errors found:\n\n#{mdl}" if !mdl.empty?
  return false
end

### Bad URL test
# Return false if no invalid URLs are found.
def general_bad_urls?(file)
  # List of hosts to ignore in the analysis
  exclude_hosts = [
    'api.loganalytics.io',          'management.azure.com',
    'management.core.windows.net',  'login.microsoftonline.com',
    'oauth2.googleapis.com',        'www.googleapis.com',
    'image-charts.com',             'graph.microsoft.com',
    'www.w3.org',                   'tempuri.org',
    'us-3.rightscale.com',          'us-4.rightscale.com'
  ]

  diff = git.diff_for_file(file)
  regex = /(^\+)/
  fail_message = ""

  if diff && diff.patch =~ regex
    diff.patch.each_line.with_index do |line, index|
      line_number = index + 1

      if line =~ regex
        URI.extract(line,['http', 'https']).each do |url|
          # Skip excluded hosts
          next if exclude_hosts.include?(url.scan(URI.regexp)[0][3])

          # Clean up URL string and convert it into a proper URI object
          url_string = url.to_s.gsub(/[!@#$%^&*(),.?":{}|<>]/,'')
          url = URI(url_string)

          # Check for a valid host. Skip URLs that are dynamicly constructed and may not have a valid hostname.
          # Example: http://ec2. + $region + .awsamazon.com/... does not have a valid hostname to query.
          next if url.host !~ /(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)/

          # Make HTTP request to URL
          response = Net::HTTP.get_response(url)

          # Test again when the file isn't found and path includes tree/master
          # This is in case it is the README link or a new file included in the repo
          if response.code == '404' && url_string =~ /tree\/master/
            # Modify URL string and convert it back into a proper URI object
            url_string = url.to_s.gsub('tree/master',"tree/#{github.branch_for_head}").gsub(')','')
            url = URI(url_string)

            # Make HTTP request to URL again
            response = Net::HTTP.get_response(url) #make request
          end

          # Return error details if a proper response code was not received
          if response.code !~ /200|302/
            fail_message += "Line: #{line_number.to_s}\nURL: #{url_string}\nResponse Code: #{response.code}\n\n"
          end
        end
      end
    end
  end

  fail_message = "**#{file}**\nBad URLs found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

###############################################################################
# Methods: README
###############################################################################

### Missing README Sections
# Verify that README file has all required sections
def readme_missing_sections?(file)
  fail_message = ""

  # Store contents of file for direct analysis
  readme_text = File.read(file)

  # Flags for whether sections are found
  name_found = false
  what_it_does_found = false
  input_parameters_found = false
  policy_actions_found = false
  prerequisites_found = false
  supported_clouds_found = false
  cost_found = false

  readme_text.each_line.with_index do |line, index|
    name_found = true if index == 0 && line.start_with?("# ")
    what_it_does_found = true if line.start_with?("## What It Does")
    input_parameters_found = true if line.start_with?("## Input Parameters")
    policy_actions_found = true if line.start_with?("## Policy Actions")
    prerequisites_found = true if line.start_with?("## Prerequisites")
    supported_clouds_found = true if line.start_with?("## Supported Clouds")
    cost_found = true if line.start_with?("## Cost")
  end

  fail_message += "```# Policy Name```\n" if !name_found
  fail_message += "```## What It Does```\n" if !what_it_does_found
  fail_message += "```## Input Parameters```\n" if !input_parameters_found
  fail_message += "```## Policy Actions```\n" if !policy_actions_found
  fail_message += "```## Prerequisites```\n" if !prerequisites_found
  fail_message += "```## Supported Clouds```\n" if !supported_clouds_found
  fail_message += "```## Cost```\n" if !cost_found

  fail_message = "**#{file}**\nREADME.md is missing required sections. Please make sure the following sections exist and are indicated with the below markdown. Spelling, spacing, and capitalization should conform to the below:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Out of order README Sections
# Verify that README file has the various sections in the correct order
def readme_sections_out_of_order?(file)
  fail_message = ""

  # Store contents of file for direct analysis
  readme_text = File.read(file)

  # Flags for whether sections are found
  name_found = false
  what_it_does_found = false
  how_it_works_found = false
  policy_savings_found = false
  input_parameters_found = false
  policy_actions_found = false
  prerequisites_found = false
  supported_clouds_found = false
  cost_found = false

  what_it_does_raised = false
  how_it_works_raised = false
  policy_savings_raised = false
  input_parameters_raised = false
  policy_actions_raised = false
  prerequisites_raised = false
  supported_clouds_raised = false
  cost_raised = false

  readme_text.each_line.with_index do |line, index|
    line_number = index + 1

    name_found = true if index == 0 && line.start_with?("# ")
    what_it_does_found = true if line.start_with?("## What It Does")
    how_it_works_found = true if line.start_with?("## How It Works")
    policy_savings_found = true if line.start_with?("### Policy Savings Details")
    input_parameters_found = true if line.start_with?("## Input Parameters")
    policy_actions_found = true if line.start_with?("## Policy Actions")
    prerequisites_found = true if line.start_with?("## Prerequisites")
    supported_clouds_found = true if line.start_with?("## Supported Clouds")
    cost_found = true if line.start_with?("## Cost")

    if !what_it_does_raised && what_it_does_found && !name_found
      fail_message += "Line #{line_number.to_s}: What It Does out of order.\n"
      what_it_does_raised = true
    end

    if !how_it_works_raised && how_it_works_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number.to_s}: How It Works out of order.\n"
      how_it_works_raised = true
    end

    if !policy_savings_raised && policy_savings_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number.to_s}: Policy Savings Details out of order.\n"
      policy_savings_raised = true
    end

    if !input_parameters_raised && input_parameters_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number.to_s}: Input Parameters out of order.\n"
      input_parameters_raised = true
    end

    if !policy_actions_raised && policy_actions_found && (!name_found || !what_it_does_found || !input_parameters_found)
      fail_message += "Line #{line_number.to_s}: Policy Actions out of order.\n"
      policy_actions_raised = true
    end

    if !prerequisites_raised && prerequisites_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found)
      fail_message += "Line #{line_number.to_s}: Prerequisites out of order.\n"
      prerequisites_raised = true
    end

    if !supported_clouds_raised && supported_clouds_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found || !prerequisites_found)
      fail_message += "Line #{line_number.to_s}: Supported Clouds out of order.\n"
      supported_clouds_raised = true
    end

    if !cost_raised && cost_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found || !prerequisites_found)
      fail_message += "Line #{line_number.to_s}: Cost out of order.\n"
      cost_raised = true
    end
  end

  fail_message = "**#{file}**\nREADME.md sections are out of order. Sections should be in the following order: Policy Name, What It Does, How It Works, Policy Savings Details, Input Parameters, Policy Actions, Prerequisites, Supported Clouds, Cost\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### README Credentials formatting
# Verify that README file has credentials in the proper formatting
def readme_invalid_credentials?(file)
  fail_message = ""

  # Store contents of file for direct analysis
  readme_text = File.read(file)

  prereq_line_number = -1

  azure_line_number = -1
  google_line_number = -1
  flexera_line_number = -1

  aws_line_number = -1
  aws_perm_endline = -1
  aws_perm_section = false
  aws_perm_asterix = false
  aws_json_line = -1

  aws_perm_tester = /^ *- *`[a-zA-Z]+:[a-zA-Z]+`\*?$/
  aws_json_tester = /^\s{2}```json\n\s{2}\{\n\s{6}"Version": "2012-10-17",\n\s{6}"Statement": \[\n\s{10}\{\n\s{14}"Effect": "Allow",\n\s{14}"Action": \[\n[\s\S]*?\n\s{10}\}\n\s{6}\]\n\s{2}\}\n\s{2}```$/


  readme_text.each_line.with_index do |line, index|
    line_number = index + 1

    # Description check
    prereq_line_number = line_number if line.start_with?("## Prerequisites")

    if line_number == prereq_line_number + 2
      if !line.start_with?("This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).")
        fail_message += "Line #{line_number.to_s}: README has invalid description for credentials section or description is not correctly located two lines below `## Prerequisites`. Credentials section should contain the following description text before the credential list:\n\n"
        fail_message += "```This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).```\n\n"
      end
    end

    # AWS check
    aws_json_line = line_number if aws_line_number != -1 && line.include?("json")

    if line_number == aws_perm_endline + 1 && !aws_perm_asterix
      if !line.start_with?("  Example IAM Permission Policy:")
        fail_message += "Line #{line_number.to_s}: AWS permissions missing example IAM permission policy or proper text indicating this section of the policy. The following line should exist in the README followed by a JSON example:\n\n"
        fail_message += "```  Example IAM Permission Policy:```\n\n"
      end
    end

    if line_number == aws_perm_endline + 1 && aws_perm_asterix
      if !line.start_with?("  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.")
        fail_message += "Line #{line_number.to_s}: AWS permissions contain potentially destructive permissions, signified by an *, but no disclaimer. The following disclaimer should be present below the permissions list:\n\n"
        fail_message += "```  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n\n"
      end

      aws_perm_endline = line_number + 1
      aws_perm_asterix = false
    end

    if aws_perm_section
      if line.strip.empty?
        aws_perm_section = false
        aws_perm_endline = line_number
      else
        aws_perm_asterix = true if line.include?("*")

        if !line.start_with?("  - ")
          fail_message += "Line #{line_number.to_s}: Incorrectly formatted AWS permission. AWS permissions should be formatted in a markdown list with the first 4 characters being [space][space][hyphen][space] like in the below examples:\n\n"
          fail_message += "```  - `sts:GetCallerIdentity` ```\n"
          fail_message += "```  - `s3:DeleteObject`* ```\n"
          fail_message += "```  - `ec2:DescribeSnapshots` ```\n\n"
        elsif !line.match?(aws_perm_tester)
          fail_message += "Line #{line_number.to_s}: Incorrectly formatted AWS permission. AWS permissions should be formatted like the following examples, with an optional * at the end to signify if a permission enables changes to be made to the cloud environment:\n\n"
          fail_message += "```  - `sts:GetCallerIdentity` ```\n"
          fail_message += "```  - `s3:DeleteObject`* ```\n"
          fail_message += "```  - `ec2:DescribeSnapshots` ```\n\n"
        elsif line == line.downcase || line == line.upcase || line.split(':')[0] != line.split(':')[0].downcase || line.split(':')[1][0] != line.split(':')[1][0].upcase
          fail_message += "Line #{line_number.to_s}: Incorrectly cased AWS permission. AWS permissions should have a mix of uppercase and lowercase like the following examples:\n\n"
          fail_message += "```  - `sts:GetCallerIdentity` ```\n"
          fail_message += "```  - `s3:DeleteObject`* ```\n"
          fail_message += "```  - `ec2:DescribeSnapshots` ```\n\n"
        end
      end
    end

    aws_line_number = line_number if aws_line_number == -1 && prereq_line_number != -1 && (line.include?("AWS") || line.include?("aws"))

    if aws_line_number == line_number
      if line.strip != "- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:"
        fail_message += "Line #{line_number.to_s}: README has invalid description for AWS credential. AWS credentials should always have the following description:\n\n"
        fail_message += "```- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:```\n\n"
      end

      aws_perm_section = true
    end
  end

  # AWS JSON Testing
  if aws_line_number != -1 && !readme_text.match?(aws_json_tester)
    fail_message += "Line #{aws_json_line.to_s}: Correctly-formatted JSON example of AWS permissions missing. Please ensure this JSON is present and correctly formatted. See other AWS policy READMEs for examples.\n\n"
  end

  fail_message = "**#{file}**\nREADME.md sections are out of order. Sections should be in the following order: Policy Name, What It Does, How It Works, Policy Savings Details, Input Parameters, Policy Actions, Prerequisites, Supported Clouds, Cost\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

###############################################################################
# Methods: Changelog
###############################################################################

### Bad CHANGELOG Formatting test
# Verify that CHANGELOG is formatted correctly
# This only covers details that won't be picked up by the Markdown linter
def changelog_bad_formatting?(file)
  fail_message = ""

  # Store contents of file for direct analysis
  changelog_text = File.read(file)

  # Regex to test proper formatting of version numbers
  version_tester = /^\d+\.\d+(\.\d+)?$/

  changelog_text.each_line.with_index do |line, index|
    line_number = index + 1

    if line_number == 1
      if line.chomp != "# Changelog"
        fail_message += "Line #{line_number.to_s}: Invalid first line. The first line should always be: # Changelog\n"
      end
    else
      if line.strip.start_with?("#")
        if !line.start_with?("## v")
          fail_message += "Line #{line_number.to_s}: Invalid hash. Hash (#) should always precede a version number formatted like so: `## v1.0`\n"
        elsif !line.split("v")[1].match?(version_tester)
          fail_message += "Line #{line_number.to_s}: Invalid version number. Version numbers should always consist of two or three integers separated by periods. Valid examples: `1.0` `2.3.76` `11.5`\n"
        end
      elsif line.strip.start_with?("-")
        if !line.start_with?("- ")
          fail_message += "Line #{line_number.to_s}: Invalid list formatting. List items under a version number should always begin with `- ` followed by some text explaining the change.\n"
        end
      elsif !line.strip.empty?
        fail_message += "Line #{line_number.to_s}: Invalid content. After the first line, CHANGELOG files should only have version numbers preceded by `##`, changes preceded by `-`, and empty lines.\n"
      end
    end
  end

  fail_message = "**#{file}**\nCHANGELOG.md has formatting problems. Please correct the below:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

###############################################################################
# Methods: Policy
###############################################################################

### Unmodified README test
# Verify that .pt file also has an updated README
def policy_unmodified_readme?(file, changed_readme_files)
  fail_message = ""

  # Get file path for readme file
  file_sections = file.split('/')
  file_sections.pop
  readme_file_path = file_sections.join('/') + "/README.md"

  if !File.exist?(readme_file_path)
    fail_message = "**#{file}**\nPolicy template has no README.md file. Please create this file and document the policy's functionality within."
  elsif !changed_readme_files.include?(readme_file_path)
    fail_message = "**#{file}**\nPolicy template updated but associated README.md file has not been. Please verify that any necessary changes have been made to the README."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Unmodified CHANGELOG test
# Verify that .pt file also has an updated CHANGELOG
def policy_unmodified_changelog?(file, changed_changelog_files)
  fail_message = ""

  # Get file path for changelog file
  file_sections = file.split('/')
  file_sections.pop
  changelog_file_path = file_sections.join('/') + "/CHANGELOG.md"

  if !File.exist?(changelog_file_path)
    fail_message = "**#{file}**\nPolicy template has no CHANGELOG.md file. Please create this file and document the policy's version changes within."
  elsif !changed_changelog_files.include?(changelog_file_path)
    fail_message = "**#{file}**\nPolicy template updated but associated CHANGELOG.md file has not been. Please increment version number and update CHANGELOG.md accordingly."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Policy syntax error test
# Return false if no syntax errors are found using fpt.
def policy_fpt_syntax_error?(file)
  fpt = `[ -x ./fpt ] && ./fpt check #{file} | grep -v Checking`

  # Return errors if any are found. Otherwise, return false
  return "**#{file}**\nfpt has detected errors:\n\n#{fpt}" if !fpt.empty?
  return false
end

### Filename Casing test
# Verify that the filename is in lowercase
def policy_bad_filename_casing?(file)
  fail_message = ""

  if file.match?(/[A-Z]/)
    fail_message = "**#{file}**\nPolicy template name and file path should be in lowercase. Please remove any uppercase [A-Z] characters."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Metadata test
# Return false if policy metadata has missing or problematic field
def policy_bad_metadata?(file, field_name)
  # Valid values
  # https://docs.flexera.com/flexera/EN/Automation/PoliciesList.htm
  categories = [ 'cost', 'compliance', 'operational', 'saas management', 'security' ]
  frequencies = [ '15 minutes', 'hourly', 'daily', 'weekly', 'monthly' ]
  severities = [ 'low', 'medium', 'high', 'critical' ]

  pp = PolicyParser.new
  pp.parse(file)

  name = pp.parsed_name
  short_description = pp.parsed_short_description
  long_description = pp.parsed_long_description
  category = pp.parsed_category
  default_frequency = pp.parsed_default_frequency
  severity = pp.parsed_severity
  info = pp.parsed_info

  fail_message = ""

  if field_name == "name"
    fail_message += "Please add a name field.\n\n" if !name
    fail_message += "Please add a value other than an empty string to the name field.\n\n" if name && name == ""
  end

  if field_name == "short_description"
    fail_message += "Please add a short_description field.\n\n" if !short_description
    fail_message += "Please add a value other than an empty string to the short_description field.\n\n" if short_description && short_description == ""
  end

  if field_name == "long_description"
    fail_message += "Please add a long_description field with an empty string as its value.\n\n" if !long_description
    fail_message += "Please make the long_description field an empty string.\n\n" if long_description && long_description != ""
  end

  if field_name == "category"
    fail_message += "Please add a category field.\n\n" if !category
    fail_message += "The Category is not valid: #{category}. Valid Categories include #{categories.join(', ')}\n\n" if category && !categories.include?(category.downcase)
    fail_message += "The First letter of Category is not capitalized: #{category}.\n\n" if category !~ /^[A-Z]/
  end

  if field_name == "default_frequency"
    fail_message += "Please add a default_frequency field.\n\n" if !default_frequency
    fail_message += "The default_frequency is not valid: #{default_frequency}. Valid frequencies include #{frequencies.join(', ')}\n\n" if default_frequency && !frequencies.include?(default_frequency)
  end

  if field_name == "severity"
    fail_message += "Please add a severity field.\n\n" if !severity
    fail_message += "The severity is not valid: #{severity}. Valid severities include #{severities.join(', ')}\n\n" if severity && !severities.include?(severity)
  end

  if field_name == "info"
    fail_message += "Please add an info field.\n\n" if info.nil?
  end

  fail_message = "**#{file}**\nBad #{field_name} metadata found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Info block test
# Return false if policy info block has missing or problematic fields
def policy_missing_info_field?(file, field_name)
  pp = PolicyParser.new
  pp.parse(file)

  info = pp.parsed_info

  fail_message = ""

  if info.nil?
    fail_message += "Please add the info field.\n\n" if info.nil?
  else
    if field_name == "version"
      fail_message += "Please add version to the info field.\n\n" if info[:version].nil?
    end

    if field_name == "provider"
      fail_message += "Please add provider to the info field.\n\n" if info[:provider].nil?
    end

    if field_name == "service"
      fail_message += "Should this include service in the info field?\n\n" if info[:service].nil?
    end

    if field_name == "policy_set"
      fail_message += "Should this include policy_set in the info field?\n\n" if info[:policy_set].nil?
    end
  end

  fail_message = "**#{file}**\nBad #{field_name} info metadata field found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Section order test
# Return false if policy sections are in the correct order.
def policy_sections_out_of_order?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Message to return of test fails
  fail_message = ""

  # Report back 'true' if policy sections are not properly ordered based on blocks
  found_metadata = false
  found_parameters = false
  found_credentials = false
  found_pagination = false
  found_datasources = false
  found_policy = false
  found_escalations = false
  found_cwf = false

  # Ensure that each type of error is only reported once
  metadata_fail = false
  parameters_fail = false
  credentials_fail = false
  datasources_fail = false
  policy_fail = false
  escalations_fail = false

  # Failsafe for meta policy code which won't be in the correct order by design
  found_meta = false

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    found_meta = true if line.strip.start_with?('# Meta Policy [alpha]')

    if !found_meta
      found_metadata = true if line.start_with?('name ')
      found_parameters = true if line.strip.start_with?('parameter ') && line.strip.end_with?('do')
      found_credentials = true if line.strip.start_with?('credentials ') && line.strip.end_with?('do')
      found_pagination = true if line.strip.start_with?('pagination ') && line.strip.end_with?('do')
      found_datasources = true if line.strip.start_with?('datasource ') && line.strip.end_with?('do')
      found_policy = true if line.strip.start_with?('policy ') && line.strip.end_with?('do')
      found_escalations = true if line.strip.start_with?('escalation ') && line.strip.end_with?('do')
      found_cwf = true if line.strip.start_with?('define ') && line.strip.end_with?('do')

      if !metadata_fail && !found_metadata && (found_parameters || found_credentials || found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before metadata\n\n"
        metadata_fail = true
      end

      if !parameters_fail && !found_parameters && (found_credentials || found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before parameter\n\n"
        parameters_fail = true
      end

      if !credentials_fail && !found_credentials && (found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before credentials\n\n"
        credentials_fail = true
      end

      if !datasources_fail && !found_datasources && (found_policy || found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before datasources\n\n"
        datasources_fail = true
      end

      if !policy_fail && !found_policy && (found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before policy block\n\n"
        policy_fail = true
      end

      if !escalations_fail && !found_escalations && (found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before escalations\n\n"
        escalations_fail = true
      end
    end
  end

  fail_message = "**#{file}**\nPolicy Template does not have code blocks in the correct order.\nCode blocks should be in the following order: Metadata, Parameters, Credentials, Pagination, Datasources & Scripts, Policy, Escalations, Cloud Workflow, Meta Policy\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Block grouping test
# Return false if code blocks are all grouped together by type.
def policy_blocks_ungrouped?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Store failure message
  fail_message = ""

  # Report back 'true' if specific block types are not organized together in the policy
  block_names = [
    'parameter ', 'credentials ', 'pagination ',
    'datasource ', 'policy ', 'escalation ', 'define '
  ]

  block_names.each do |block|
    found_block = false
    found_other_blocks = false

    # Failsafe for meta policy code which won't be in the correct order by design
    found_meta = false

    policy_code.each_line.with_index do |line, index|
      line_number = index + 1

      found_meta = true if line.strip.start_with?('# Meta Policy [alpha]')

      if !found_meta
        # If we've found the block we're testing, and then other blocks,
        # and then found the block we're testing again, return error
        if line.strip.start_with?(block) && line.strip.end_with?('do') && found_other_blocks
          fail_message += "Line #{line_number.to_s}: Unsorted #{block.strip} code block found\n"
          found_block = false
          found_other_blocks = false
        end

        # Once we've found the block we're testing, start looking for other blocks
        if found_block
          block_names.each do |other_block|
            if other_block != block
              found_other_blocks = true if line.strip.start_with?(other_block) && line.strip.end_with?('do')
            end
          end
        end

        found_block = true if line.strip.start_with?(block) && line.strip.end_with?('do')
      end
    end
  end

  fail_message = "**#{file}**\nUngrouped code blocks found. Code blocks should be grouped together in sections by type e.g. all parameter blocks should be next to each other, all credentials blocks should be next to each other, etc. with the exception of Meta Policy code:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Section comment test
# Return false if all required policy section comments are present.
def policy_missing_section_comments?(file, section_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  # Set values based on which section we're checking.
  # block_regex: Test for presence of block
  # comment_regex: Test for presence of section comment for that block
  # pretty_name: Name as it should appear in section comment
  case section_name
  when "parameter"
    block_regex = /^parameter\s+"[^"]*"\s+do$/
    comment_regex = /^\#{79}\n# Parameters\n\#{79}$/
    pretty_name = "Parameters"
  when "credentials"
    block_regex = /^credentials\s+"[^"]*"\s+do$/
    comment_regex = /^\#{79}\n# Authentication\n\#{79}$/
    pretty_name = "Authentication"
  when "pagination"
    block_regex = /^pagination\s+"[^"]*"\s+do$/
    comment_regex = /^\#{79}\n# Pagination\n\#{79}$/
    pretty_name = "Pagination"
  when "datasource"
    block_regex = /^datasource\s+"[^"]*"\s+do$/
    comment_regex = /^\#{79}\n# Datasources & Scripts\n\#{79}$/
    pretty_name = "Datasources & Scripts"
  when "policy"
    block_regex = /^policy\s+"[^"]*"\s+do$/
    comment_regex = /^\#{79}\n# Policy\n\#{79}$/
    pretty_name = "Policy"
  when "escalation"
    block_regex = /^escalation\s+"[^"]*"\s+do$/
    comment_regex = /^\#{79}\n# Escalations\n\#{79}$/
    pretty_name = "Escalations"
  when "cwf"
    block_regex = /^define\s+\w+\(\s*([$]\w+\s*,\s*)*([$]\w+\s*)?\)\s*(return\s+([$]\w+\s*,\s*)*([$]\w+\s*)?)?do$/
    comment_regex = /^\#{79}\n# Cloud Workflow\n\#{79}$/
    pretty_name = "Cloud Workflow"
  else
    block_regex = /.*/
    comment_regex = /.*/
    pretty_name = ""
  end

  # Failure message to return if problem is detected
  if block_regex.match?(policy_code) && !comment_regex.match?(policy_code)
    hash_string = "###############################################################################"
    fail_message += "Policy Template does **not** have a comment indicating where the #{pretty_name} section begins. Please add a comment like the below before the parameters blocks:\n\n#{hash_string}<br>\# #{pretty_name}<br>#{hash_string}\n\n"
  end

  fail_message = "**#{file}**\nMissing policy section comments:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Bad block name test
# Return false if no invalidly named code blocks are found.
def policy_bad_block_name?(file, block_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  # Set values based on which section we're checking.
  # proper_name: Correct prefix that block name ought to have
  # block_regex: Test for presence of block with an invalid name
  case block_name
  when "parameter"
    proper_name = "param_"
    block_regex = /^parameter\s+"(?!param_[^"]+")[^"]*"\s+do$/
  when "credentials"
    proper_name = "auth_"
    block_regex = /^credentials\s+"(?!auth_[^"]+")[^"]*"\s+do$/
  when "pagination"
    proper_name = "pagination_"
    block_regex = /^pagination\s+"(?!pagination_[^"]+")[^"]*"\s+do$/
  when "datasource"
    proper_name = "ds_"
    block_regex = /^datasource\s+"(?!ds_[^"]+")[^"]*"\s+do$/
  when "script"
    proper_name = "js_"
    block_regex = /^script\s+"(?!js_[^"]+)([^"]*)",\s+type:\s+"javascript"\s+do$/
  when "policy"
    proper_name = "pol_"
    block_regex = /^policy\s+"(?!pol_[^"]+")[^"]*"\s+do$/
  when "escalation"
    proper_name = "esc_"
    block_regex = /^escalation\s+"(?!esc_[^"]+")[^"]*"\s+do$/
  else
    proper_name = ""
    block_regex = /.*/
  end

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1
    fail_message += "Line #{line_number.to_s}\n" if block_regex.match?(line)
  end

  fail_message = "**#{file}**\nInvalidly named #{block_name} blocks. Please ensure all #{block_name} blocks have names that begin with `#{proper_name}`:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Deprecated block test
# Return false if no deprecated blocks are found.
def policy_deprecated_code_blocks?(file, block_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  permission_regex = /^permission\s+"[^"]*"\s+do$/
  resources_regex = /^resources\s+"[^"]*",\s+type:\s+"[^"]*"\s+do$/

  fail_message = ""

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1
    fail_message += "Line #{line_number.to_s}: Permission block found\n" if permission_regex.match?(line)
    fail_message += "Line #{line_number.to_s}: Resources block found\n" if resources_regex.match?(line)
  end

  fail_message = "**#{file}**\nDeprecated #{block_name} blocks found. It is recommended that the policy be refactored to no longer use these code blocks:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Missing block field test
# Return false if specified field is not missing from any of the specified blocks.
def policy_block_missing_field?(file, block_name, field_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  present = false
  line_number = nil

  policy_code.each_line.with_index do |line, index|
    # Check if we're entering the block
    if line.strip.start_with?(block_name + ' ') && line.strip.end_with?('do')
      present = false
      line_number = index + 1
    end

    # Check for the field if we're in a block
    present = true if line_number && line.strip.start_with?(field_name + ' ')

    # When we reach the end of a block, check if field was present
    if line.strip == 'end' && line_number
      fail_message += "Line #{line_number.to_s}\n" unless present
      line_number = nil
    end
  end

  fail_message = "**#{file}**\n#{block_name} code blocks with missing `#{field_name}` field found. Please add the `#{field_name}` field to these blocks:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Datasource/script name matching test
# Return message if datasource and script do not have matching names. Otherwise, return false
def policy_ds_js_name_mismatch?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""
  ds_name = nil
  js_name = nil
  line_number = nil

  policy_code.each_line.with_index do |line, index|
    # Stop doing the check once we hit the Meta Policy section
    if line.strip.start_with?('# Meta Policy [alpha]')
      break
    # When we find a datasource, store its name
    elsif line.strip.start_with?("datasource ") && line.strip.end_with?('do')
      name_test = line.match(/"([^"]*)"/)
      ds_name = name_test[1] if name_test
      line_number = index + 1
    # When we find a run_script, store its name and compare to datasource
    elsif line.strip.start_with?("run_script ")
      name_test = line.match(/run_script \$([a-zA-Z0-9_]+)/)
      js_name = name_test[1] if name_test

      if ds_name != nil && js_name != nil
        if ds_name[3..-1] != js_name[3..-1]
          fail_message += "Line #{line_number.to_s}: #{ds_name} / #{js_name}\n"
        end
      end

      # Reset all variables to start the process over for the next datasource we find
      ds_name = nil
      js_name = nil
      line_number = nil
    end
  end

  fail_message = "**#{file}**\nDatasources and scripts with mismatched names found. These names should match; for example, a datasource named ds_currency should be paired with a script named js_currency. This convention should only be ignored when the same script is called by multiple datasources. The following datasource/script pairs have mismatched names:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Script parameter order test
# Return message if script parameters are not in the correct order. Otherwise, return false
def policy_run_script_incorrect_order?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""
  ds_name = nil

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    # Stop doing the check if we've reached the meta policy section
    break if line.strip.start_with?('# Meta Policy [alpha]')

    if line.strip.start_with?("datasource ") && line.strip.end_with?('do')
      name_test = line.match(/"([^"]*)"/)
      ds_name = name_test[1] if name_test
    end

    disordered = false

    if line.strip.start_with?("run_script")
      # Store a list of all of the parameters for the run_script
      parameters = line.strip.sub('run_script ', '').split(',').map(&:strip)

      # Remove the first item because it's just the name of the script itself
      script_name = parameters.shift

      ds_found = false       # Whether we've found a datasource parameter
      param_found = false    # Whether we've found a parameter parameter
      constant_found = false # Whether we've found a constant, like rs_org_id
      value_found = false    # Whether we've found a raw value, like a number or string

      parameters.each do |parameter|
        if parameter.start_with?('$ds')
          ds_found = true
          disordered = true if param_found || constant_found || value_found
          puts parameter
        elsif parameter.start_with?('$param')
          param_found = true
          disordered = true if constant_found || value_found
        elsif /[A-Za-z]/.match(parameter[0]) # If parameter starts with a letter
          constant_found = true
          disordered = true if value_found
        else # Assume a raw value, like a number or string, if none of the above
          value_found = true
        end
      end
    end

    fail_message += "Line #{line_number.to_s}: #{ds_name} / run_script #{script_name}\n" if disordered
  end

  fail_message = "**#{file}**\nrun_script statements found whose parameters are not in the correct order. run_script parameters should be in the following order: script, datasources, parameters, variables, raw values:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Master permissions test
# Return false if master permissions have been recorded for the policy
def policy_missing_master_permissions?(file, permissions_yaml)
  # Get the diff to see only the new changes
  diff = git.diff_for_file(file)

  fail_message = ""

  # Use regex to look for blocks that have a "datasource", "request", and "auth" sections of the datasource
  # Example String:
  #   "diff --git a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\nindex 14b3236f..bf6a161d 100644\n--- a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n+++ b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n@@ -193,6 +193,16 @@ datasource \"ds_applied_policy\" do\n   end\n end\n \n+datasource \"ds_applied_policy_test_will_be_removed_later\" do\n+  request do\n+    auth $auth_flexera\n+    host rs_governance_host\n+    path join([\"/api/governance/projects/\", rs_project_id, \"/applied_policies/\", policy_id])\n+    header \"Api-Version\", \"1.0\"\n+    header \"Test\", \"True\"\n+  end\n+end\n+\n # Get region-specific Flexera API endpoints\n datasource \"ds_flexera_api_hosts\" do\n   run_script $js_flexera_api_hosts, rs_optima_host"
  regex = /datasource.*do(\s)+.*request.*do(\s)+.*auth.*([\s\S])+end([\s\+])+end/

  # First check if the PT file has been manually validated and enabled for permission generation
  pt_file_enabled = permissions_yaml["validated_policy_templates"].select { |pt| pt.include?(file) }

  if pt_file_enabled.empty?
    # If the PT file has not been manually validated, then print an error message which will block the PR from being merged
    # This will help improve coverage as we touch more PT files
    fail_message = "**#{file}**\nPolicy Template file has **not** yet been enabled for automated permission generation. Please help us improve coverage by [following the steps documented in `tools/policy_master_permission_generation/`](https://github.com/flexera-public/policy_templates/tree/master/tools/policy_master_permission_generation) to resolve this."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### New datasource test
# Return false if no new datasources are found.
def policy_new_datasource?(file, permissions_yaml)
  # Get the diff to see only the new changes
  diff = git.diff_for_file(file)

  fail_message = ""

  # Use regex to look for blocks that have a "datasource", "request", and "auth" sections of the datasource
  # Example String:
  #   "diff --git a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\nindex 14b3236f..bf6a161d 100644\n--- a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n+++ b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n@@ -193,6 +193,16 @@ datasource \"ds_applied_policy\" do\n   end\n end\n \n+datasource \"ds_applied_policy_test_will_be_removed_later\" do\n+  request do\n+    auth $auth_flexera\n+    host rs_governance_host\n+    path join([\"/api/governance/projects/\", rs_project_id, \"/applied_policies/\", policy_id])\n+    header \"Api-Version\", \"1.0\"\n+    header \"Test\", \"True\"\n+  end\n+end\n+\n # Get region-specific Flexera API endpoints\n datasource \"ds_flexera_api_hosts\" do\n   run_script $js_flexera_api_hosts, rs_optima_host"
  regex = /datasource.*do(\s)+.*request.*do(\s)+.*auth.*([\s\S])+end([\s\+])+end/

  # First check if the PT file has been manually validated and enabled for permission generation
  pt_file_enabled = permissions_yaml["validated_policy_templates"].select { |pt| pt.include?(file) }

  if diff && diff.patch =~ regex && !pt_file_enabled.empty?
    # If the PT file has been manually validated, but there are new datasources, then print a warning message
    fail_message = "**#{file}**\nDetected new request datasource(s) in Policy Template file. Please verify the README.md has any new permissions that may be required."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

###############################################################################
# Github Pull Request Testing
###############################################################################

fail "**Github Pull Request**\nPull Request is missing summary. Please provide a summary of your Pull Request." if github.pr_body.length < 10
fail "**Github Pull Request**\nPull Request is missing labels. Please add labels to this Pull Request." if github.pr_labels.empty?

###############################################################################
# All Files Testing
###############################################################################

# Perform a basic text lint on all changed files
changed_files.each do |file|
  `node_modules/.bin/textlint #{file} 1>textlint.log`

  if $?.exitstatus != 0
    message `cat textlint.log`
    fail "**#{file}**\nTextlint failed"
  end
end

###############################################################################
# Dangerfile Testing
###############################################################################

# Perform testing on Dangerfile itself if it has been modified
changed_dangerfile.each do |file|
  warn "**#{file}**\nDangerfile has been modified! Please ensure changes were intentional, have been tested, and do not break existing tests."
end

###############################################################################
# Dot File Testing
###############################################################################

# Perform testing on modified dot files
changed_dot_files.each do |file|
  warn "**#{file}**\nDot file `#{file}` has been modified! Please make sure these modifications were intentional and have been tested. Dot files are necessary for configuring the Github repository and managing automation."
end

###############################################################################
# Config File Testing
###############################################################################

# Perform testing on modified config files
changed_config_files.each do |file|
  warn "**#{file}**\nConfig file `#{file}` has been modified! Please make sure these modifications were intentional and have been tested. Config files are necessary for configuring the Github repository and managing automation."
end

###############################################################################
# README Testing
###############################################################################

# Check README.md for issues for each file
changed_readme_files.each do |file|
  # Run Danger spell check on file
  general_spellcheck?(file)

  # Raise error if the file contains any bad urls
  test = general_bad_urls?(file); fail test if test

  # Raise error if improper markdown is found via linter
  test = general_bad_markdown?(file); fail test if test

  # Raise error if README is missing required sections
  test = readme_missing_sections?(file); fail test if test

  # Raise error if README sections are out of order
  test = readme_sections_out_of_order?(file); fail test if test

  # Raise error if README credentials are formatted incorrectly
  test = readme_invalid_credentials?(file); fail test if test
end

###############################################################################
# CHANGELOG Testing
###############################################################################

# Check CHANGELOG.md for issues for each file
changed_changelog_files.each do |file|
  # Raise error if the file contains any bad urls
  test = general_bad_urls?(file); fail test if test

  # Raise error if improper markdown is found via linter
  test = general_bad_markdown?(file); fail test if test

  # Raise error if CHANGELOG is incorrectly formatted
  test = changelog_bad_formatting?(file); fail test if test
end

###############################################################################
# Misc. Markdown Testing
###############################################################################

# Check Markdown files for issues for each file
changed_misc_md_files.each do |file|
  # Run Danger spell check on file
  general_spellcheck?(file)

  # Raise error if the file contains any bad urls
  test = general_bad_urls?(file); fail test if test

  # Raise error if improper markdown is found via linter
  test = general_bad_markdown?(file); fail test if test
end

###############################################################################
# Policy Testing
###############################################################################

# Load external YAML file for testing
permissions_yaml = YAML.load_file('tools/policy_master_permission_generation/validated_policy_templates.yaml')

# Check policies for issues for each file
changed_pt_files.each do |file|
  # Run policy through various methods that test for problems.
  # These methods will return false if no problems are found.
  # Otherwise, they return the warning or error message that should be raised.

  # Raise error if policy changed but changelog has not been
  test = policy_unmodified_changelog?(file, changed_changelog_files); fail test if test

  # Raise warning if policy changed but readme has not been
  test = policy_unmodified_readme?(file, changed_readme_files); warn test if test

  # Raise error if policy filename/path contains any uppercase letters
  test = policy_bad_filename_casing?(file); fail test if test

  # Raise error if the file contains any bad urls
  test = general_bad_urls?(file); fail test if test

  # Run policy through fpt testing. Only raise error if there is a syntax error.
  test = policy_fpt_syntax_error?(file); fail test if test

  # Raise errors or warnings if bad metadata is found
  test = policy_bad_metadata?(file, "name"); fail test if test
  test = policy_bad_metadata?(file, "short_description"); fail test if test
  test = policy_bad_metadata?(file, "long_description"); fail test if test
  test = policy_bad_metadata?(file, "category"); fail test if test
  test = policy_bad_metadata?(file, "default_frequency"); fail test if test
  test = policy_bad_metadata?(file, "severity"); fail test if test
  test = policy_bad_metadata?(file, "info"); fail test if test

  # Raise errors or warnings if bad info block metadata is found
  if !test
    info_test = policy_missing_info_field?(file, "version"); fail info_test if info_test
    info_test = policy_missing_info_field?(file, "provider"); fail info_test if info_test
    info_test = policy_missing_info_field?(file, "service"); warn info_test if info_test
    info_test = policy_missing_info_field?(file, "policy_set"); warn info_test if info_test
  end

  # Raise error if policy sections are out of order
  test = policy_sections_out_of_order?(file); fail test if test

  # Raise error if policy blocks are not grouped together by type
  test = policy_blocks_ungrouped?(file); fail test if test

  # Report on missing policy section comments
  test = policy_missing_section_comments?(file, "parameter"); fail test if test
  test = policy_missing_section_comments?(file, "credentials"); fail test if test
  test = policy_missing_section_comments?(file, "pagination"); fail test if test
  test = policy_missing_section_comments?(file, "datasource"); fail test if test
  test = policy_missing_section_comments?(file, "policy"); fail test if test
  test = policy_missing_section_comments?(file, "escalation"); fail test if test
  test = policy_missing_section_comments?(file, "cwf"); fail test if test

  # Report on invalidly named code blocks
  test = policy_bad_block_name?(file, "parameter"); fail test if test
  test = policy_bad_block_name?(file, "credentials"); fail test if test
  test = policy_bad_block_name?(file, "pagination"); fail test if test
  test = policy_bad_block_name?(file, "datasource"); fail test if test
  test = policy_bad_block_name?(file, "script"); fail test if test
  test = policy_bad_block_name?(file, "policy"); fail test if test
  test = policy_bad_block_name?(file, "escalation"); fail test if test

  # Report on invalid/deprecated code blocks
  test = policy_deprecated_code_blocks?(file, "permission"); warn test if test
  test = policy_deprecated_code_blocks?(file, "resources"); warn test if test

  # Report on missing fields in code blocks
  fields_to_check = [
    { block: "parameter", fields: ["type", "category", "label", "description"] },
    { block: "credentials", fields: ["schemes", "tags", "label", "description"] },
    { block: "escalation", fields: ["automatic", "label", "description"] }
  ]

  fields_to_check.each do |item|
    item[:fields].each do |field|
      test = policy_block_missing_field?(file, item[:block], field); fail test if test
    end
  end

  # Raise warning, not error, if parameter block is missing a default field.
  # This is because there are occasionally legitimate reasons to not have a default
  test = policy_block_missing_field?(file, "parameter", "default")

  if test
    warn test + "\n\nWhile not required, it is recommended that every parameter have a default value unless user input for that parameter is required and too specific for any default value to make sense"
  end

  # Raise warning, not error, if a datasource and the script it calls have mismatched names.
  # Warning because there are occasionally legitimate reasons to do this.
  test = policy_ds_js_name_mismatch?(file); warn test if test

  # Raise error if run_script statements with incorrect parameter ordering are found
  test = policy_run_script_incorrect_order?(file); fail test if test

  # Raise error if policy is not in the master permissions file.
  # Raise warning if policy is in this file, but datasources have been added.
  test = policy_missing_master_permissions?(file, permissions_yaml); fail test if test
  ds_test = policy_new_datasource?(file, permissions_yaml); warn ds_test if ds_test && !test
end

###############################################################################
# Meta Policy Testing
###############################################################################

# Check meta policies for issues for each file
changed_meta_pt_files.each do |file|
  # TBD
end
