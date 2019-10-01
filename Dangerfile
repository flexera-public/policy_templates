  require 'uri'
# DangerFile
# https://danger.systems/reference.html
changed_files = (git.added_files + git.modified_files)
has_app_changes = changed_files.select{ |file| file.end_with? "pt" }
has_new_policy_template = git.added_files.select{ |file| file.end_with? "pt" }

# Changelog entries are required for changes to library files.
no_changelog_entry = (changed_files.grep(/[\w]+CHANGELOG.md/i)+changed_files.grep(/CHANGELOG.md/i)).empty?
if (has_app_changes.length != 0) && no_changelog_entry
  fail "Please add a changelog"
end

missing_doc_changes = (changed_files.grep(/[\w]+README.md/i)+changed_files.grep(/README.md/i)).empty?
if (has_app_changes.length != 0) && missing_doc_changes
  warn("Should this include readme changes")
end

if (has_new_policy_template.length != 0) && missing_doc_changes
  fail "A README.md is required for new templates"
end

# checks for broken links in the any file
# exclude api and auth hostnames
exclude_hosts = [
  'api.loganalytics.io',
  'management.azure.com',
  'login.microsoftonline.com',
  'oauth2.googleapis.com',
  'www.googleapis.com'
]
changed_files.each do |file|
 diff = git.diff_for_file(file)
 regex =/(^\+).+?(http|https):\/\/[a-zA-Z0-9.\/?=_-]*.+/
 if diff && diff.patch =~ regex
   diff.patch.each_line do |line|
     if line =~ regex
       URI.extract(line,['http','https']).each do |uri|
         next if exclude_hosts.include?(uri.scan(URI.regexp)[0][3])
         uri = URI(uri)
         uri_string = uri.to_s.gsub(')','')
         message "Checking URI #{uri_string}"
         res = Net::HTTP.get_response(uri)
         if res.code != '200'
           fail "The URI is not valid: #{uri_string} in #{file} Status: #{res.code}"
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
changed_files.each do |file|
 diff = git.diff_for_file(file)
 regex =/^\+category/

 #message diff.patch
 if diff && diff.patch =~ regex

   diff.patch.each_line do |line|
     #message line
     if line =~ regex
       category = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse
       if !categories.include?(category.downcase)
         fail "The Category is not valid: #{category}.  Valid Categories include #{categories.join(", ")}"
       end
    end
   end
 end
end


fail 'Please provide a summary of your Pull Request.' if github.pr_body.length < 10

fail 'Please add labels to this Pull Request' if github.pr_labels.empty?
