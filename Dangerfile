  require 'uri'
# DangerFile
# https://danger.systems/reference.html
changed_files = (git.added_files + git.modified_files)
has_app_changes = changed_files.select{ |file| file.end_with? "pt" }
has_new_policy_template = git.added_files.select{ |file| file.end_with? "pt" }
md_files = changed_files.select{ |file| file.end_with? "md" }

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

fpt = nil
has_app_changes.each do |file|
  fpt = `./fpt check #{file}`
  if fpt != nil
    fail fpt
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
  'www.googleapis.com'
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
         url_string = url.to_s.gsub(/\)|\.$/,'') #remove extra chars
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
         if ! res.code =~ /200|302/ #allow OK and temporary redirects such as login
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
 diff = git.diff_for_file(file)
 regex =/^\+category/
 if diff && diff.patch =~ regex
   diff.patch.each_line do |line|
     if line =~ regex
       category = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse
       if !categories.include?(category.downcase)
         fail "The Category is not valid: #{category}.  Valid Categories include #{categories.join(", ")}"
       end
    end
   end
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
    fail "#{file} '#{mdl}'"
  end
end

# check for lowercase files and directories
has_app_changes.each do |file|
  regex = /^[a-z]+$/g
  if file !~ regex
    fail "Policy Template path is not lowercase. #{file}"
  end
end

fail 'Please provide a summary of your Pull Request.' if github.pr_body.length < 10

fail 'Please add labels to this Pull Request' if github.pr_labels.empty?
