require 'uri'
require_relative 'tools/lib/policy_parser'
# DangerFile
# https://danger.systems/reference.html
# get list of old names that were renamed
renamed_files = (git.renamed_files.collect{|r| r[:before]})
# get list of all files changes minus the old files renamed
# remove list of renamed files to prevent errors on files that don't exist
changed_files = (git.added_files + git.modified_files - renamed_files)
has_app_changes = changed_files.select{ |file| file.end_with? "pt" }
has_new_policy_template = git.added_files.select{ |file| file.end_with? "pt" }
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
  'us-4.rightscale.com',
  'demo.flexnetmanager.com',
  'wstunnel1-1.rightscale.com'
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

# check for valid category values.
# must be one of the following categories
# when adding a new category update the Rakefile generate_policy_list task and
# docs.rightscale.com/policies/users/policy_list.html.shim also.
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

# check markdown of .md files with markdown lint
# .md files should follow these rules https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md
mdl = nil
md_files.each do |file|
  if file == 'README.md'
    # MD024  Multiple headers with the same content
    # MD013 disable line length
    mdl = `mdl -r "~MD024","~MD013" #{file}`
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
textlint.lint
