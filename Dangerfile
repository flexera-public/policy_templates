# DangerFile
# https://danger.systems/reference.html
changed_files = (git.added_files + git.modified_files)
do_something changed_files.select{ |file| file.end_with? "pt" }
has_app_changes = changed_files
# Changelog entries are required for changes to library files.
no_changelog_entry = !git.modified_files.include?("CHANGELOG.md")
if has_app_changes && no_changelog_entry
  warn("Any changes to library code should be reflected in the Changelog. Please consider adding a note there and adhere to the [Changelog Guidelines](https://github.com/Moya/contributors/blob/master/Changelog%20Guidelines.md).")
end

missing_doc_changes = git.modified_files.grep(/README.md/).empty?
if has_app_changes && missing_doc_changes
  warn("Any changes to library code should be reflected in the Changelog. Please consider adding a note there and adhere to the [Changelog Guidelines](https://github.com/Moya/contributors/blob/master/Changelog%20Guidelines.md).")
end

raise 'Please provide a summary of your Pull Request.' if github.pr_body.length < 10

raise 'Please add labels to this Pull Request' if github.pr_labels.empty?