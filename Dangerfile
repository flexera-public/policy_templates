# DangerFile
# https://danger.systems/reference.html
changed_files = (git.added_files + git.modified_files)
has_app_changes = changed_files.select{ |file| file.end_with? "pt" }
message "had total app_changes #{has_app_changes.length}"
# Changelog entries are required for changes to library files.
no_changelog_entry = !git.modified_files.include?("CHANGELOG.md")
if (has_app_changes.length != 0) && no_changelog_entry
  warn("No Changelog")
end

missing_doc_changes = git.modified_files.grep(/README.md/).empty?
if (has_app_changes.length != 0) && missing_doc_changes
  warn("No readme")
end

raise 'Please provide a summary of your Pull Request.' if github.pr_body.length < 10

raise 'Please add labels to this Pull Request' if github.pr_labels.empty?
