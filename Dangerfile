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

has_app_changes.each do |file|
 diff = git.diff_for_file(file)
 #message "diff.patch #{diff.patch}"
 if diff && diff.patch =~ /http/
   #urls = diff.patch.scan(URI.regexp)
   #urls.each  do |url|
   message "patch #{diff.patch}"
   diff.patch.scan(/^\+/).each do |line|
     message "line #{line}"
   end
 end
 #url = file.scan(URI.regexp)
  #message "url #{file.scan(URI.regexp)}"
  status = 404

  if (status == 404 )
    fail "The README link is not valid. #{file} "
  end
end

fail 'Please provide a summary of your Pull Request.' if github.pr_body.length < 10

fail 'Please add labels to this Pull Request' if github.pr_labels.empty?
