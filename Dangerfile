require 'uri'
require 'yaml'

require_relative 'tools/lib/policy_parser'
# DangerFile
# https://danger.systems/reference.html
# get list of old names that were renamed
renamed_files = (git.renamed_files.collect{|r| r[:before]})
# get list of all files changes minus the old files renamed
# remove list of renamed files to prevent errors on files that don't exist
changed_files = (git.added_files + git.modified_files - renamed_files)
has_app_changes = changed_files.select{ |file| file.end_with? "pt" }
has_new_policy_template = git.added_files.select{ |file| (file.end_with? "pt") && (! file.end_with? "meta_parent.pt") } # exclude meta_parent.pt -- these are generated from the child policy templates
md_files = changed_files.select{ |file| file.end_with? "md" }

pp = PolicyParser.new
# Changelog entries are required for changes to library files.
no_changelog_entry = (changed_files.grep(/[\w]+CHANGELOG.md/i)+changed_files.grep(/CHANGELOG.md/i)).empty?
if (has_app_changes.length != 0) && no_changelog_entry
  fail "Please add a CHANGELOG.md file"
end

missing_doc_changes = (changed_files.grep(/[\w]+README.md/i)+changed_files.grep(/README.md/i)).empty?
if (has_app_changes.length != 0) && missing_doc_changes
  warn("Should this include readme changes")
end

if (has_new_policy_template.length != 0) && missing_doc_changes
  fail "A README.md is required for new templates"
end

fpt = nil
has_app_changes.each do |file|
  message "Checking #{file}\n#{fpt}"
  # check if fpt is installed and do the check.  only report if there is a syntax error
  fpt = `[ -x ./fpt ] && ./fpt check #{file} | grep -v Checking`
  if ! fpt.empty?
    fail "Checking #{file}\n#{fpt}"
  end
end

# checks for broken links in the any file
# exclude api and auth hostnames
exclude_hosts = [
  'api.loganalytics.io',
  'management.azure.com',
  'management.core.windows.net',
  'login.microsoftonline.com',
  'oauth2.googleapis.com',
  'www.googleapis.com',
  'image-charts.com',
  'graph.microsoft.com',
  'www.w3.org',
  'tempuri.org',
  'us-3.rightscale.com',
  'us-4.rightscale.com'
]
changed_files.each do |file|
 diff = git.diff_for_file(file)
 regex =/(^\+)/
 if diff && diff.patch =~ regex
   diff.patch.each_line do |line|
     if line =~ regex
       URI.extract(line,['http','https']).each do |url|
         res = nil
         next if exclude_hosts.include?(url.scan(URI.regexp)[0][3])
         url_string = url.to_s.gsub(/[!@#$%^&*(),.?":{}|<>]/,'')  #remove extra chars
         url = URI(url_string) #convert to URL
         # check for a valid host.  skip urls that are dynamicly constructed may not have a valid hostname
         # for example http://ec2. + $region + .awsamazon.com/... does not have a valid hostname to query
         next if url.host !~ /(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)/
         res = Net::HTTP.get_response(url) #make request
         # test again when the file isn't found and path includes tree/master
         # likely the README link or a new file included in the repo
         if res.code == '404' && url_string =~ /tree\/master/
           url_string = url.to_s.gsub('tree/master',"tree/#{github.branch_for_head}").gsub(')','')
           url = URI(url_string) #convert to URL
           res = Net::HTTP.get_response(url) #make request
         end
         if res.code !~ /200|302/ #allow OK and temporary redirects such as login
           fail "The URL is not valid: #{url_string} in #{file} Status: #{res.code}"
         end
       end
     end
   end
 end
end

# check for name field.
#only check .pt files
has_app_changes.each do |file|
  pp.parse(file)
  name = pp.parsed_name
  if ! name
    fail "Please add a name field. #{file}"
  end
  if name && name == ""
    fail "Please add a value other than an empty string to the name field. #{file}"
  end
end

# check for short_description field.
#only check .pt files
has_app_changes.each do |file|
  pp.parse(file)
  short_description = pp.parsed_short_description
  if ! short_description
    fail "Please add a short_description field. #{file}"
  end
  if short_description && short_description == ""
    fail "Please add a value other than an empty string to the short_description field. #{file}"
  end
end

# check for long_description field.
#only check .pt files
has_app_changes.each do |file|
  pp.parse(file)
  long_description = pp.parsed_long_description
  if ! long_description
    fail "Please add a long_description field with an empty string as its value. #{file}"
  end
  if long_description && long_description != ""
    fail "Please make the long_description field an empty string. #{file}"
  end
end

# check for valid category values.
# must be one of the following categories
# when adding a new category update the Rakefile generate_policy_list task and
# https://docs.flexera.com/flexera/EN/Automation/PoliciesList.htm also.
categories = [
  'cost',
  'compliance',
  'operational',
  'saas management',
  'security'
].sort
#only check .pt files
has_app_changes.each do |file|
  pp.parse(file)
  category = pp.parsed_category
  if ! category
    fail "Please add a category field. #{file}"
  end
  # check category meets the expected list
  if category && !categories.include?(category.downcase)
    fail "The Category is not valid: #{category}.  Valid Categories include #{categories.join(", ")}"
  end
  # check first character of category is uppercase
  if category !~ /^[A-Z]/
    fail "The First letter of Category is not capitalised: #{category}."
  end
end

# check for valid default_frequency values.
# must be one of the following default_frequency
frequencies = [
  '15 minutes',
  'hourly',
  'daily',
  'weekly',
  'monthly'
].sort
#only check .pt files
has_app_changes.each do |file|
  pp.parse(file)
  default_frequency = pp.parsed_default_frequency
  if ! default_frequency
    fail "Please add a default_frequency field. #{file}"
  end
  # check default_frequency meets the expected list
  if default_frequency && !frequencies.include?(default_frequency)
    fail "The default_frequency is not valid: #{default_frequency}.  Valid frequencies include #{frequencies.join(", ")}"
  end
end

# check for valid severity values.
# must be one of the following severity
severities = [
  'low',
  'medium',
  'high',
  'critical'
].sort
#only check .pt files
has_app_changes.each do |file|
  pp.parse(file)
  severity = pp.parsed_severity
  if ! severity
    fail "Please add a severity field. #{file}"
  end
  # check default_frequency meets the expected list
  if severity && !severities.include?(severity)
    fail "The severity is not valid: #{severity}.  Valid severities include #{severities.join(", ")}"
  end
end

# check markdown of .md files with markdown lint
# .md files should follow these rules https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md
mdl = nil
md_files.each do |file|
  # Exemptions for top-level README.md
  if file == 'README.md'
    # MD013 Line length
    # MD024 Multiple headers with the same content
    mdl = `mdl -r "~MD024","~MD013" #{file}`
  # Exemptions for tools/cloudformation-template/README.md
  elsif file == 'tools/cloudformation-template/README.md'
      # MD013 Line length
      # MD033 Inline HTML. Required for example snippets.
      # MD034 Bare URL used - Bugged. No bare URLs are actually used in this README.
      mdl = `mdl -r "~MD013","~MD033","~MD034" #{file}`
  # Exemptions for tools/cloudformation-template/README.md
  elsif file == '.github/PULL_REQUEST_TEMPLATE.md'
    # MD002 First header should be a top level header
    # MD013 Line length
    mdl = `mdl -r "~MD002","~MD013" #{file}`
  else
    # use .mdlrc rules
    mdl = `mdl #{file}`
  end
  if !mdl.empty?
    fail mdl
  end
end

# check for lowercase files and directories
has_app_changes.each do |file|
  if file.scan(/^[a-z0-9.\/_-]+$/).empty?
    fail "Policy Template path should be lowercase. #{file}"
  end
end

# check for info field required fields
has_app_changes.each do |file|
  # get info field data
  pp.parse(file)

  fail "Please add the info field. #{file}" if pp.parsed_info.nil?
  if pp.parsed_info
    fail "Please add version to the info field. #{file} " if pp.parsed_info[:version].nil?
    fail "Please add provider to the info field. #{file} " if pp.parsed_info[:provider].nil?
    warn "Should this include service in the info field. #{file}"  if pp.parsed_info[:service].nil?
    warn "Should this include policy_set in the info field. #{file}" if pp.parsed_info[:policy_set].nil?
  end
end

fail 'Please provide a summary of your Pull Request.' if github.pr_body.length < 10

fail 'Please add labels to this Pull Request' if github.pr_labels.empty?

# Lint added and modified files only
# textlint.lint
changed_files.each do |file|
  `node_modules/.bin/textlint #{file} 1>textlint.log`
  if $?.exitstatus != 0
    message `cat textlint.log`
    fail "Textlint failed on #{file}"
  end
end

# check for new datasources
# print warning if new datasource is added to ensure the README permissions have been updated
permissions_verified_pt_file_yaml = YAML.load_file('tools/policy_master_permission_generation/validated_policy_templates.yaml')
has_app_changes.each do |file|
  if file.end_with?(".pt") && !file.end_with?("_meta_parent.pt")
    # Get the diff to see only the new changes
    diff = git.diff_for_file(file)

    # Use regex to look for blocks that have a "datasource", "request", and "auth" sections of the datasource
    # Example String:
    #   "diff --git a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\nindex 14b3236f..bf6a161d 100644\n--- a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n+++ b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n@@ -193,6 +193,16 @@ datasource \"ds_applied_policy\" do\n   end\n end\n \n+datasource \"ds_applied_policy_test_will_be_removed_later\" do\n+  request do\n+    auth $auth_flexera\n+    host rs_governance_host\n+    path join([\"/api/governance/projects/\", rs_project_id, \"/applied_policies/\", policy_id])\n+    header \"Api-Version\", \"1.0\"\n+    header \"Test\", \"True\"\n+  end\n+end\n+\n # Get region-specific Flexera API endpoints\n datasource \"ds_flexera_api_hosts\" do\n   run_script $js_flexera_api_hosts, rs_optima_host"
    regex = /datasource.*do(\s)+.*request.*do(\s)+.*auth.*([\s\S])+end([\s\+])+end/

    # Print some debug info about diff patch
    # puts "Diff Patch:"
    # puts diff.patch
    # puts "---"

    # First check if the PT file has been manually validated and enabled for permission generation
    pt_file_enabled = permissions_verified_pt_file_yaml["validated_policy_templates"].select { |pt| pt.include?(file) }
    if pt_file_enabled.empty?
      # If the PT file has not been manually validated, then print an error message which will block the PR from being merged
      # This will help improve coverage as we touch more PT files
      fail "Policy Template file `#{file}` has **not** yet been enabled for automated permission generation.  Please help us improve coverage by [following the steps documented in `tools/policy_master_permission_generation/`](https://github.com/flexera-public/policy_templates/tree/master/tools/policy_master_permission_generation) to resolve this"
    elsif diff && diff.patch =~ regex
      # If the PT file has been manually validated, but there are new datasources, then print a warning message
      warn("Detected new request datasource in Policy Template file `#{file}`.  Please verify the README.md has any new permissions that may be required.")
    end
  end
end

# check for policy section comments
has_app_changes.each do |file|
  if file.end_with?(".pt") && !file.end_with?("_meta_parent.pt")
    file_contents = File.read(file)

    # Regex to test whether particular kinds of code blocks exist
    # We don't have to check for the entire block because fpt will generate an error if the block is not valid
    param_regex = /^parameter\s+"[^"]*"\s+do$/
    auth_regex = /^credentials\s+"[^"]*"\s+do$/
    pagination_regex = /^pagination\s+"[^"]*"\s+do$/
    escalation_regex = /^escalation\s+"[^"]*"\s+do$/
    cwf_regex = /^define\s+\w+\(\s*([$]\w+\s*,\s*)*([$]\w+\s*)?\)\s*(return\s+([$]\w+\s*,\s*)*([$]\w+\s*)?)?do$/

    # Regex to test whether the policy section comments exist
    param_comment_regex = /^\#{79}\n# Parameters\n\#{79}$/
    auth_comment_regex = /^\#{79}\n# Authentication\n\#{79}$/
    pagination_comment_regex = /^\#{79}\n# Pagination\n\#{79}$/
    datasource_comment_regex = /^\#{79}\n# Datasources & Scripts\n\#{79}$/
    policy_comment_regex = /^\#{79}\n# Policy\n\#{79}$/
    escalation_comment_regex = /^\#{79}\n# Escalations\n\#{79}$/
    cwf_comment_regex = /^\#{79}\n# Cloud Workflow\n\#{79}$/

    hash_string = "###############################################################################"

    if param_regex.match?(file_contents) && !param_comment_regex.match?(file_contents)
      fail "Policy Template file `#{file}` does **not** have a comment indicating where the Parameters begin. Please add a comment like the below before the parameters blocks:\n\n#{hash_string}<br>\# Parameters<br>#{hash_string}"
    end

    if auth_regex.match?(file_contents) && !auth_comment_regex.match?(file_contents)
      fail "Policy Template file `#{file}` does **not** have a comment indicating where the Authentication begins. Please add a comment like the below before the credentials blocks:\n\n#{hash_string}<br>\# Authentication<br>#{hash_string}"
    end

    if pagination_regex.match?(file_contents) && !pagination_comment_regex.match?(file_contents)
      fail "Policy Template file `#{file}` does **not** have a comment indicating where the Pagination begins. Please add a comment like the below before the pagination blocks:\n\n#{hash_string}<br>\# Pagination<br>#{hash_string}"
    end

    if !datasource_comment_regex.match?(file_contents)
      fail "Policy Template file `#{file}` does **not** have a comment indicating where the Datasources & Scripts begin. Please add a comment like the below before the datasources blocks:\n\n#{hash_string}<br>\# Datasources & Scripts<br>#{hash_string}"
    end

    if !policy_comment_regex.match?(file_contents)
      fail "Policy Template file `#{file}` does **not** have a comment indicating where the Policy begins. Please add a comment like the below before the policy block:\n\n#{hash_string}<br>\# Policy<br>#{hash_string}"
    end

    if escalation_regex.match?(file_contents) && !escalation_comment_regex.match?(file_contents)
      fail "Policy Template file `#{file}` does **not** have a comment indicating where the Escalations begin. Please add a comment like the below before the escalation blocks:\n\n#{hash_string}<br>\# Escalations<br>#{hash_string}"
    end

    if cwf_regex.match?(file_contents) && !cwf_comment_regex.match?(file_contents)
      fail "Policy Template file `#{file}` does **not** have a comment indicating where the Cloud Workflow begins. Please add a comment like the below before the cloud workflow blocks:\n\n#{hash_string}<br>\# Cloud Workflow<br>#{hash_string}"
    end
  end
end
