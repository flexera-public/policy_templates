# DangerFile
# https://danger.systems/reference.html
# Tests located in .dangerfile directory

###############################################################################
# Required Libraries
###############################################################################

require 'uri'
require 'yaml'

###############################################################################
# Required External Files
###############################################################################

require_relative '.dangerfile/policy_parser'
require_relative '.dangerfile/github_tests'
require_relative '.dangerfile/general_tests'
require_relative '.dangerfile/code_tests'
require_relative '.dangerfile/readme_tests'
require_relative '.dangerfile/changelog_tests'
require_relative '.dangerfile/policy_tests'

###############################################################################
# File Sorting
###############################################################################

# Create lists of files based on specific attributes for testing
# Renamed Files.
renamed_files = git.renamed_files.collect{ |r| r[:before] }
# Changed Files. Ignores renamed files to prevent errors on files that don't exist
changed_files = git.added_files + git.modified_files - renamed_files
# Changed Dangerfile
changed_dangerfiles = changed_files.select{ |file| file == "Dangerfile" || file.start_with?(".dangerfile/") }
# Changed Dot Files
changed_dot_files = changed_files.select{ |file| file.start_with?(".") && !file.start_with?(".dangerfile/") }
# Changed Config Files
config_files = ["Gemfile", "Gemfile.lock", "Rakefile", "package.json", "package-lock.json"]
changed_config_files = changed_files.select{ |file| config_files.include?(file) }
# Changed Ruby files.
changed_rb_files = changed_files.select{ |file| file.end_with?(".rb") || file == "Dangerfile" || file == "Rakefile" }
# Changed Python files.
changed_py_files = changed_files.select{ |file| file.end_with?(".py") }
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
# Changed JSON files.
changed_json_files = changed_files.select{ |file| file.end_with?(".json") }
# Changed YAML files.
changed_yaml_files = changed_files.select{ |file| file.end_with?(".yaml") || file.end_with?(".yml") }
# New Policy Template files. Ignore meta policy files.
new_pt_files = git.added_files.select{ |file| file.end_with?(".pt") && !file.end_with?("meta_parent.pt") }

###############################################################################
# Github Pull Request Testing
###############################################################################

test = github_pr_bad_title?(github); warn test if test
test = github_pr_missing_summary?(github); fail test if test
test = github_pr_missing_labels?(github); fail test if test
test = github_pr_missing_ready_label?(github); message test if test

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
# Modified Important Files Testing
###############################################################################

modified_file_warnings = ""

changed_dangerfiles.each do |file|
  modified_file_warnings += "#{file}: Dangerfile or related file has been modified! Please ensure changes were intentional, have been tested, and do not break existing tests.\n\n"
end

changed_dot_files.each do |file|
  modified_file_warnings += "#{file}: Dot file has been modified! Please make sure these modifications were intentional and have been tested. Dot files are necessary for configuring the Github repository and managing automation.\n\n"
end

changed_config_files.each do |file|
  modified_file_warnings += "#{file}: Config file has been modified! Please make sure these modifications were intentional and have been tested. Config files are necessary for configuring the Github repository and managing automation.\n\n"
end

# Consolidate changed files into a single warning to save space
warn "**Important Files Modified**\n\n" + modified_file_warnings.strip if !modified_file_warnings.empty?

###############################################################################
# Ruby File Testing
###############################################################################

# Perform a lint check on changed Ruby files
changed_rb_files.each do |file|
  test = code_ruby_errors?(file); fail test if test

  # Rubocop linting currently disabled. It is *very* verbose.
  #test = code_rubocop_problems?(file); warn test if test
end

###############################################################################
# Python File Testing
###############################################################################

# Perform a lint check on changed Python files
changed_py_files.each do |file|
  test = code_python_errors?(file); fail test if test
end

###############################################################################
# JSON/YAML File Testing
###############################################################################

changed_json_files.each do |file|
  # Look for out of place JSON files
  test = code_json_bad_location?(file); fail test if test

  # Lint test JSON files
  test = code_json_errors?(file); fail test if test
end

changed_yaml_files.each do |file|
  # Look for out of place YAML files
  test = code_yaml_bad_location?(file); fail test if test

  # Lint test YAML files
  test = code_yaml_errors?(file); fail test if test
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

  # Raise error if policy short_description is missing valid README link
  test = policy_bad_readme_link?(file); fail test if test

  # Raise warning if policy won't be published
  test = policy_unpublished?(file); warn test if test

  # Raise warning if policy's name has changed
  test = policy_name_changed?(file); warn test if test

  # Raise error if the file contains any bad urls
  test = general_bad_urls?(file); fail test if test

  # Run policy through fpt testing. Only raise error if there is a syntax error.
  test = policy_fpt_syntax_error?(file); fail test if test

  # Raise warning if policy contains invalid indentation
  test = policy_bad_indentation?(file); warn test if test

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

  # Raise error if policy and changelog do not have matching version numbers
  test = policy_changelog_mismatch?(file); fail test if test

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

  # Raise error if code blocks have fields in improper order
  test = policy_block_fields_incorrect_order?(file, "parameter"); fail test if test
  test = policy_block_fields_incorrect_order?(file, "credentials"); fail test if test
  test = policy_block_fields_incorrect_order?(file, "pagination"); fail test if test
  test = policy_block_fields_incorrect_order?(file, "datasource"); fail test if test
  test = policy_block_fields_incorrect_order?(file, "script"); fail test if test
  test = policy_block_fields_incorrect_order?(file, "policy"); fail test if test
  test = policy_block_fields_incorrect_order?(file, "escalation"); fail test if test

  # Raise error if recommendation policy is missing required export fields
  test = policy_missing_recommendation_fields?(file, "required"); fail test if test

  # Raise warning if recommendation policy is missing recommended export fields
  test = policy_missing_recommendation_fields?(file, "recommended"); warn test if test

  # Raise error if policy has invalid Github links in datasources
  test = policy_bad_github_datasources?(file); fail test if test

  # Raise warning if policy has any datasources using http instead of https
  test = policy_http_connections?(file); warn test if test

  # Raise warning if improper spacing between comma-separated items found
  test = policy_bad_comma_spacing?(file); warn test if test

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
