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
# Methods
###############################################################################

### Markdown lint test
# Return false if linter finds no problems
def bad_markdown?(file)
  # Adjust testing based on which file we're doing
  case file
  when "README.md"
    mdl = `mdl -r "~MD024","~MD013" #{file}`
  when "tools/cloudformation-template/README.md"
    mdl = `mdl -r "~MD013","~MD033","~MD034" #{file}`
  when ".github/PULL_REQUEST_TEMPLATE.md"
    mdl = `mdl -r "~MD002","~MD013" #{file}`
  else
    mdl = `mdl #{file}`
  end

  # Return the problems found if the md1 file is not empty. Otherwise, return false
  return md1 if !mdl.empty?
  return false
end

### Bad URL test
# Return false if no invalid URLs are found.
def bad_urls?(file)
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

  if diff && diff.patch =~ regex
    diff.patch.each_line do |line|
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
            return "The URL is not valid: #{url_string} in #{file} Status: #{response.code}"
          end
        end
      end
    end
  end

  return false
end

### Policy syntax error test
# Return false if no syntax errors are found using fpt.
def fpt_syntax_error?(file)
  fpt = `[ -x ./fpt ] && ./fpt check #{file} | grep -v Checking`

  # Return errors if any are found. Otherwise, return false
  return "Checking #{file}\n#{fpt}" if !fpt.empty?
  return false
end

### Metadata test
# Return false if policy metadata has missing or problematic field
def bad_metadata?(file, field_name)
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

  if field_name == "name"
    return "Please add a name field. #{file}" if !name
    return "Please add a value other than an empty string to the name field. #{file}" if name && name == ""
  end

  if field_name == "short_description"
    return "Please add a short_description field. #{file}" if !short_description
    return "Please add a value other than an empty string to the short_description field. #{file}" if short_description && short_description == ""
  end

  if field_name == "long_description"
    return "Please add a long_description field with an empty string as its value. #{file}" if !long_description
    return "Please make the long_description field an empty string. #{file}" if long_description && long_description != ""
  end

  if field_name == "category"
    return "Please add a category field. #{file}" if !category
    return "The Category is not valid: #{category}. Valid Categories include #{categories.join(", ")}" if category && !categories.include?(category.downcase)
    return "The First letter of Category is not capitalized: #{category}." if category !~ /^[A-Z]/
  end

  if field_name == "default_frequency"
    return "Please add a default_frequency field. #{file}" if !default_frequency
    return "The default_frequency is not valid: #{default_frequency}. Valid frequencies include #{frequencies.join(", ")}" if default_frequency && !frequencies.include?(default_frequency)
  end

  if field_name == "severity"
    return "Please add a severity field. #{file}" if !severity
    return "The severity is not valid: #{severity}. Valid severities include #{severities.join(", ")}" if severity && !severities.include?(severity)
  end

  if field_name == "info"
    return "Please add the info field. #{file}" if info.nil?
  end

  return false
end

### Info block test
# Return false if policy info block has missing or problematic fields
def missing_info_field?(file, field_name)
  pp = PolicyParser.new
  pp.parse(file)

  info = pp.parsed_info
  return "Please add the info field. #{file}" if info.nil?

  if field_name == "version"
    return "Please add version to the info field. #{file}" if info[:version].nil?
  end

  if field_name == "provider"
    return "Please add provider to the info field. #{file}" if info[:provider].nil?
  end

  if field_name == "service"
    return "Should this include service in the info field? #{file}" if info[:service].nil?
  end

  if field_name == "policy_set"
    return "Should this include policy_set in the info field? #{file}" if info[:policy_set].nil?
  end

  return false
end

### Section order test
# Return false if policy sections are in the correct order.
def sections_out_of_order?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Message to return of test fails
  fail_message = "Policy Template file `#{file}` does not have code blocks in the correct order. Code blocks should be in the following order: Metadata, Parameters, Credentials, Pagination, Datasources & Scripts, Policy, Escalations, Cloud Workflow, Meta Policy"

  # Report back 'true' if policy sections are not properly ordered based on blocks
  found_metadata = false
  found_parameters = false
  found_credentials = false
  found_pagination = false
  found_datasources = false
  found_policy = false
  found_escalations = false
  found_cwf = false

  # Failsafe for meta policy code which won't be in the correct order by design
  found_meta = false

  policy_code.each_line do |line|
    found_meta = true if line.strip.start_with?('# Meta Policy [alpha]')

    if !found_meta
      found_metadata = true if line.strip.start_with?('name ')
      found_parameters = true if line.strip.start_with?('parameter ')
      found_credentials = true if line.strip.start_with?('credentials ')
      found_pagination = true if line.strip.start_with?('pagination ')
      found_datasources = true if line.strip.start_with?('datasource ')
      found_policy = true if line.strip.start_with?('policy ')
      found_escalations = true if line.strip.start_with?('escalation ')
      found_cwf = true if line.strip.start_with?('define ')

      return fail_message if !found_metadata && (found_parameters || found_credentials || found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
      return fail_message if !found_parameters && (found_credentials || found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
      return fail_message if !found_credentials && (found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
      return fail_message if !found_datasources && (found_policy || found_escalations || found_cwf)
      return fail_message if !found_policy && (found_escalations || found_cwf)
      return fail_message if !found_escalations && (found_cwf)
    end
  end

  # Return false if no problems were found
  return false
end

### Block grouping test
# Return false if code blocks are all grouped together by type.
def blocks_ungrouped?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

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

    policy_code.each_line do |line|
      found_meta = true if line.strip.start_with?('# Meta Policy [alpha]')

      if !found_meta
        # Once we've found the block we're testing, start looking for other blocks
        if found_block
          block_names.each do |other_block|
            if other_block != block
              found_other_blocks = true if line.strip.start_with?(other_block)
            end
          end
        end

        # If we've found the block we're testing, and then other blocks, and then
        # found the block we're testing again, return error
        if line.strip.start_with?(block) && found_other_blocks
          return "Policy Template file `#{file}` has unsorted #{block.strip} code blocks. Code blocks should be grouped together in sections by type e.g. all parameter blocks should be next to each other, all credentials blocks should be next to each other, etc. with the exception of Meta Policy code"
        end

        found_block = true if line.strip.start_with?(block)
      end
    end
  end

  # Return false if no problems were found
  return false
end

### Section comment test
# Return false if all required policy section comments are present.
def missing_section_comments?(file, section_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

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
  hash_string = "###############################################################################"
  fail_message = "Policy Template file `#{file}` does **not** have a comment indicating where the #{pretty_name} section begins. Please add a comment like the below before the parameters blocks:\n\n#{hash_string}<br>\# #{pretty_name}<br>#{hash_string}"

  # Return fail message if the block exists but the comment for it does not
  return fail_message if block_regex.match?(policy_code) && !comment_regex.match?(policy_code)
  return false
end

### Bad block name test
# Return false if no invalidly named code blocks are found.
def bad_block_name?(file, block_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

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

  # Message to return if test fails
  fail_message = "Policy Template file `#{file}` has invalidly named #{block_name} blocks. Please ensure all #{block_name} blocks have names that begin with #{proper_name}"

  # Return fail message if an invalidly named block exists
  return fail_message if block_regex.match?(policy_code)
  return false
end

### Deprecated block test
# Return false if no deprecated blocks are found.
def deprecated_code_blocks?(file, block_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Message to return of test fails
  fail_message = "Policy Template file `#{file}` has deprecated `#{block_name}` code blocks. It is recommended that the policy be refactored to no longer use these code blocks."

  permission_regex = /^permission\s+"[^"]*"\s+do$/
  resources_regex = /^resources\s+"[^"]*",\s+type:\s+"[^"]*"\s+do$/

  return fail_message if permission_regex.match?(policy_code) && block_name == "permission"
  return fail_message if resources_regex.match?(policy_code) && block_name == "resources"
  return false
end

### Missing block field test
# Return false if specified field is not missing from any of the specified blocks.
def block_missing_field?(file, block_name, field_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Message to return of test fails
  fail_message = "Policy Template file `#{file}` has #{block_name} block that is missing the #{field_name} field. Please add this field to all #{block_name} blocks"

  in_block = false
  present = false

  policy_code.each_line do |line|
    # Check if we're entering the block
    if line.strip.start_with?(block_name + ' ') && line.strip.end_with?('do')
      in_block = true
      present = false
    end

    # Check for the field if we're in a block
    present = true if in_block && line.strip.start_with?(field_name + ' ')

    # When we reach the end of a block, check if field was present
    if line.strip == 'end' && in_block
      return fail_message unless present
      in_block = false
    end
  end

  # Return false if no problems were found
  return false
end

### Master permissions test
# Return false if master permissions have been recorded for the policy
def missing_master_permissions?(file, permissions_verified_pt_file_yaml)
  # Get the diff to see only the new changes
  diff = git.diff_for_file(file)

  # Use regex to look for blocks that have a "datasource", "request", and "auth" sections of the datasource
  # Example String:
  #   "diff --git a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\nindex 14b3236f..bf6a161d 100644\n--- a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n+++ b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n@@ -193,6 +193,16 @@ datasource \"ds_applied_policy\" do\n   end\n end\n \n+datasource \"ds_applied_policy_test_will_be_removed_later\" do\n+  request do\n+    auth $auth_flexera\n+    host rs_governance_host\n+    path join([\"/api/governance/projects/\", rs_project_id, \"/applied_policies/\", policy_id])\n+    header \"Api-Version\", \"1.0\"\n+    header \"Test\", \"True\"\n+  end\n+end\n+\n # Get region-specific Flexera API endpoints\n datasource \"ds_flexera_api_hosts\" do\n   run_script $js_flexera_api_hosts, rs_optima_host"
  regex = /datasource.*do(\s)+.*request.*do(\s)+.*auth.*([\s\S])+end([\s\+])+end/

  # First check if the PT file has been manually validated and enabled for permission generation
  pt_file_enabled = permissions_verified_pt_file_yaml["validated_policy_templates"].select { |pt| pt.include?(file) }

  if pt_file_enabled.empty?
    # If the PT file has not been manually validated, then print an error message which will block the PR from being merged
    # This will help improve coverage as we touch more PT files
    return "Policy Template file `#{file}` has **not** yet been enabled for automated permission generation. Please help us improve coverage by [following the steps documented in `tools/policy_master_permission_generation/`](https://github.com/flexera-public/policy_templates/tree/master/tools/policy_master_permission_generation) to resolve this"
  end

  return false
end

### New datasource test
# Return false if no new datasources are found.
def new_datasource?(file, permissions_verified_pt_file_yaml)
  # Get the diff to see only the new changes
  diff = git.diff_for_file(file)

  # Use regex to look for blocks that have a "datasource", "request", and "auth" sections of the datasource
  # Example String:
  #   "diff --git a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\nindex 14b3236f..bf6a161d 100644\n--- a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n+++ b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n@@ -193,6 +193,16 @@ datasource \"ds_applied_policy\" do\n   end\n end\n \n+datasource \"ds_applied_policy_test_will_be_removed_later\" do\n+  request do\n+    auth $auth_flexera\n+    host rs_governance_host\n+    path join([\"/api/governance/projects/\", rs_project_id, \"/applied_policies/\", policy_id])\n+    header \"Api-Version\", \"1.0\"\n+    header \"Test\", \"True\"\n+  end\n+end\n+\n # Get region-specific Flexera API endpoints\n datasource \"ds_flexera_api_hosts\" do\n   run_script $js_flexera_api_hosts, rs_optima_host"
  regex = /datasource.*do(\s)+.*request.*do(\s)+.*auth.*([\s\S])+end([\s\+])+end/

  # First check if the PT file has been manually validated and enabled for permission generation
  pt_file_enabled = permissions_verified_pt_file_yaml["validated_policy_templates"].select { |pt| pt.include?(file) }

  if diff && diff.patch =~ regex && !pt_file_enabled.empty?
    # If the PT file has been manually validated, but there are new datasources, then print a warning message
    return "Detected new request datasource in Policy Template file `#{file}`. Please verify the README.md has any new permissions that may be required."
  end

  return false
end

###############################################################################
# Github Pull Request Testing
###############################################################################

fail 'Please provide a summary of your Pull Request.' if github.pr_body.length < 10
fail 'Please add labels to this Pull Request' if github.pr_labels.empty?

###############################################################################
# File Structure Testing
###############################################################################

# Raise error if a policy has been modified but its corresponding CHANGELOG file has not.
no_changelog_entry = (changed_files.grep(/[\w]+CHANGELOG.md/i) + changed_files.grep(/CHANGELOG.md/i)).empty?
fail "Please add a CHANGELOG.md file" if changed_pt_files.length != 0 && no_changelog_entry

# Raise warning if a policy has been modified but its corresponding README file has not.
# This is just a warning because bug fixes and other minor changes may not require this.
missing_doc_changes = (changed_files.grep(/[\w]+README.md/i) + changed_files.grep(/README.md/i)).empty?
warn "Should this include README.md changes?" if changed_pt_files.length != 0 && missing_doc_changes

# Raise error if a new policy is missing a README.md file
fail "A README.md is required for new templates" if new_pt_files.length != 0 && missing_doc_changes

# check for lowercase files and directories
changed_pt_files.each do |file|
  fail "Policy Template path should be lowercase. #{file}" if file.scan(/^[a-z0-9.\/_-]+$/).empty?
end

###############################################################################
# All Files Testing
###############################################################################

# Perform a basic text lint on all changed files
changed_files.each do |file|
  `node_modules/.bin/textlint #{file} 1>textlint.log`

  if $?.exitstatus != 0
    message `cat textlint.log`
    fail "Textlint failed on #{file}"
  end
end

###############################################################################
# README Contents Testing
###############################################################################

# Check README.md contents for issues for each file
changed_readme_files.each do |file|
  # Raise error if the file contains any bad urls
  test = bad_urls?(file); fail test if test

  # Raise error if improper markdown is found via linter
  test = bad_markdown?(file); fail test if test
end

###############################################################################
# CHANGELOG Contents Testing
###############################################################################

# Check CHANGELOG.md contents for issues for each file
changed_changelog_files.each do |file|
  # Raise error if the file contains any bad urls
  test = bad_urls?(file); fail test if test

  # Raise error if improper markdown is found via linter
  test = bad_markdown?(file); fail test if test
end

###############################################################################
# Misc. Markdown Contents Testing
###############################################################################

# Check Markdown contents for issues for each file
changed_misc_md_files.each do |file|
  # Raise error if the file contains any bad urls
  test = bad_urls?(file); fail test if test

  # Raise error if improper markdown is found via linter
  test = bad_markdown?(file); fail test if test
end

###############################################################################
# Policy Code Testing
###############################################################################

# Load external YAML file for testing
permissions_verified_pt_file_yaml = YAML.load_file('tools/policy_master_permission_generation/validated_policy_templates.yaml')

# Check policy code itself for issues for each file
changed_pt_files.each do |file|
  # Run policy through various methods that test for problems.
  # These methods will return false if no problems are found.
  # Otherwise, they return the warning or error message that should be raised.

  # Raise error if the file contains any bad urls
  test = bad_urls?(file); fail test if test

  # Run policy through fpt testing. Only raise error if there is a syntax error.
  test = fpt_syntax_error?(file); fail test if test

  # Raise errors or warnings if bad metadata is found
  test = bad_metadata?(file, "name"); fail test if test
  test = bad_metadata?(file, "short_description"); fail test if test
  test = bad_metadata?(file, "long_description"); fail test if test
  test = bad_metadata?(file, "category"); fail test if test
  test = bad_metadata?(file, "default_frequency"); fail test if test
  test = bad_metadata?(file, "severity"); fail test if test
  test = bad_metadata?(file, "info"); fail test if test

  # Raise errors or warnings if bad info block metadata is found
  if !test
    info_test = missing_info_field?(file, "version"); fail info_test if info_test
    info_test = missing_info_field?(file, "provider"); fail info_test if info_test
    info_test = missing_info_field?(file, "service"); warn info_test if info_test
    info_test = missing_info_field?(file, "policy_set"); warn info_test if info_test
  end

  # Raise error if policy sections are out of order
  test = sections_out_of_order?(file); fail test if test

  # Raise error if policy blocks are not grouped together by type
  test = blocks_ungrouped?(file); fail test if test

  # Report on missing policy section comments
  test = missing_section_comments?(file, "parameter"); fail test if test
  test = missing_section_comments?(file, "credentials"); fail test if test
  test = missing_section_comments?(file, "pagination"); fail test if test
  test = missing_section_comments?(file, "datasource"); fail test if test
  test = missing_section_comments?(file, "policy"); fail test if test
  test = missing_section_comments?(file, "escalation"); fail test if test
  test = missing_section_comments?(file, "cwf"); fail test if test

  # Report on invalidly named code blocks
  test = bad_block_name?(file, "parameter"); fail test if test
  test = bad_block_name?(file, "credentials"); fail test if test
  test = bad_block_name?(file, "pagination"); fail test if test
  test = bad_block_name?(file, "datasource"); fail test if test
  test = bad_block_name?(file, "script"); fail test if test
  test = bad_block_name?(file, "policy"); fail test if test
  test = bad_block_name?(file, "escalation"); fail test if test

  # Report on invalid/deprecated code blocks
  test = deprecated_code_blocks?(file, "permission"); warn test if test
  test = deprecated_code_blocks?(file, "resources"); warn test if test

  # Report on missing fields in code blocks
  fields_to_check = [
    { block: "parameter", fields: ["type", "category", "label", "description"] },
    { block: "credentials", fields: ["schemes", "tags", "label", "description"] },
    { block: "escalation", fields: ["automatic", "label", "description"] }
  ]

  fields_to_check.each do |item|
    item[:fields].each do |field|
      test = block_missing_field?(file, item[:block], field); fail test if test
    end
  end

  # Raise warning, not error, if parameter block is missing a default field.
  # This is because there are occasionally legitimate reasons to not have a default
  if block_missing_field?(file, "parameter", "default")
    warn "Policy Template file `#{file}` has parameter block that is missing the default field. It is recommended that every parameter have a default value unless user input for that parameter is required and too specific for any default value to make sense"
  end

  # Raise error if policy is not in the master permissions file.
  # Raise warning if policy is in this file, but datasources have been added.
  test = missing_master_permissions?(file, permissions_verified_pt_file_yaml); fail test if test
  ds_test = new_datasource?(file, permissions_verified_pt_file_yaml); warn ds_test if ds_test && !test
end

###############################################################################
# Meta Policy Code Testing
###############################################################################

# Check meta policy code itself for issues for each file
changed_meta_pt_files.each do |file|
  # TBD
end
