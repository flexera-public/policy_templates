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

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Sorting files for testing..."

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
changed_readme_files = changed_files.select{ |file| file.end_with?("/README.md") && (file.start_with?("automation/") || file.start_with?("compliance/") || file.start_with?("cost/") || file.start_with?("operational/") || file.start_with?("saas/") || file.start_with?("security/")) }
# Changed Changelog files.
changed_changelog_files = changed_files.select{ |file| file.end_with?("/CHANGELOG.md") }
# Changed MD files other than the above.
changed_misc_md_files = changed_files.select{ |file| file.end_with?(".md") && !file.end_with?("/CHANGELOG.md") && !file.start_with?("HISTORY.md") && !(file.end_with?("/README.md") && (file.start_with?("automation/") || file.start_with?("compliance/") || file.start_with?("cost/") || file.start_with?("operational/") || file.start_with?("saas/") || file.start_with?("security/"))) }
# Changed JSON files.
changed_json_files = changed_files.select{ |file| file.end_with?(".json") }
# Changed YAML files.
changed_yaml_files = changed_files.select{ |file| file.end_with?(".yaml") || file.end_with?(".yml") }
# New Policy Template files. Ignore meta policy files.
new_pt_files = git.added_files.select{ |file| file.end_with?(".pt") && !file.end_with?("meta_parent.pt") }

###############################################################################
# File Loading
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Loading file-based assets..."

permissions_yaml = YAML.load_file('tools/policy_master_permission_generation/validated_policy_templates.yaml')

###############################################################################
# Github Pull Request Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing Github pull request..."

test = github_pr_bad_title?(github); warn test if test
test = github_pr_missing_summary?(github); fail test if test
test = github_pr_missing_labels?(github); fail test if test
test = github_pr_missing_ready_label?(github); message test if test

###############################################################################
# Modified Important Files Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing if important files were modified..."

modified_important_files = changed_dangerfiles + changed_dot_files + changed_config_files
modified_important_files = modified_important_files.join("\n")

# Consolidate changed files into a single warning to save space
warn "### **Important Files Modified**\n\nPlease make sure these modifications were intentional and have been tested. These files are necessary for configuring the Github repository and managing automation.\n\n" + modified_important_files.strip if !modified_important_files.empty?

###############################################################################
# All Files Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed files..."

changed_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  warnings = []
  failures = []

  # Perform a basic text lint on all changed files
  test = general_textlint?(file); warnings << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Ruby File Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed Ruby files..."

# Perform a lint check on changed Ruby files
changed_rb_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Raise error if code errors found
  test = code_ruby_errors?(file); failures << test if test

  # Rubocop linting currently disabled. It is *very* verbose.
  #test = code_rubocop_problems?(file); warn test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Python File Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed Python files..."

# Perform a lint check on changed Python files
changed_py_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Raise error if code errors found
  test = code_python_errors?(file); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# JSON/YAML File Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed JSON files..."

changed_json_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Look for out of place JSON files
  test = code_json_bad_location?(file); failures << test if test

  # Lint test JSON files
  test = code_json_errors?(file); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed YAML files..."

changed_yaml_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Look for out of place YAML files
  test = code_yaml_bad_location?(file); failures << test if test

  # Lint test YAML files
  test = code_yaml_errors?(file); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# README Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed README.md files..."

# Check README.md for issues for each file
changed_readme_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Don't run tests against deprecated READMEs
  unless readme_deprecated?(file, file_lines)
    # Run aspell spell check on file
    test = general_spellcheck?(file); warnings << test if test

    # Raise warning if outdated terminology found
    test = general_outdated_terminology?(file, file_lines); warnings << test if test

    # Raise error if the file contains any bad urls
    test = general_bad_urls?(file, file_diff); failures << test if test

    # Raise error if improper markdown is found via linter
    test = general_bad_markdown?(file); failures << test if test

    # Raise error if README is missing required sections
    test = readme_missing_sections?(file, file_lines); failures << test if test

    # Raise error if README sections are out of order
    test = readme_sections_out_of_order?(file, file_lines); failures << test if test

    # Raise error if README credentials are formatted incorrectly
    test = readme_invalid_credentials?(file, file_lines); failures << test if test
  end

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# CHANGELOG Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed CHANGELOG.md files..."

# Check CHANGELOG.md for issues for each file
changed_changelog_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Don't run tests against deprecated CHANGELOGs
  unless changelog_deprecated?(file, file_lines)
    # Raise error if the file contains any bad urls
    test = general_bad_urls?(file, file_diff); failures << test if test

    # Raise error if improper markdown is found via linter
    test = general_bad_markdown?(file); failures << test if test

    # Raise error if CHANGELOG is incorrectly formatted
    test = changelog_bad_formatting?(file, file_lines); failures << test if test
  end

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Misc. Markdown Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed misc MD files..."

# Check Markdown files for issues for each file
changed_misc_md_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Run aspell spell check on file
  test = general_spellcheck?(file); warnings << test if test

  # Raise warning if outdated terminology found
  test = general_outdated_terminology?(file, file_lines); warnings << test if test

  # Raise error if the file contains any bad urls
  test = general_bad_urls?(file, file_diff); failures << test if test

  # Raise error if improper markdown is found via linter
  test = general_bad_markdown?(file); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Policy Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed Policy Template files..."

# Check policies for issues for each file
changed_pt_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  # Run policy through various methods that test for problems.
  # These methods will return false if no problems are found.
  # Otherwise, they return the warning or error message that should be raised.
  warnings = []
  failures = []

  # Preread file to avoid reading it multiple times for each method
  file_parsed = PolicyParser.new
  file_parsed.parse(file)
  file_text = File.read(file)
  file_lines = File.readlines(file)
  file_diff = git.diff_for_file(file)

  # Raise error if policy is deprecated but missing deprecated field in info() block
  test = policy_missing_deprecated_field?(file, file_parsed); failures << test if test

  # Raise error if policy changed but changelog has not been
  test = policy_unmodified_changelog?(file, changed_changelog_files); failures << test if test

  # Raise error if policy and changelog do not have matching version numbers
  test = policy_changelog_mismatch?(file, file_parsed); failures << test if test

  # Run policy through fpt testing. Only raise error if there is a syntax error.
  test = policy_fpt_syntax_error?(file); failures << test if test

  # Don't run remaining tests against deprecated policies
  unless policy_deprecated?(file, file_parsed)
    # Raise error if policy is not in a valid directory within the repo directory structure
    test = policy_bad_directory?(file); failures << test if test

    # Raise warning if policy changed but readme has not been
    rd_test = policy_unmodified_readme?(file, changed_readme_files); warnings << rd_test if rd_test

    # Raise error if policy is not in the master permissions file.
    # Raise warning if policy is in this file, but datasources have been added.
    # Only raise the above warning if the more general warning about updating the README doesn't exist.
    test = policy_missing_master_permissions?(file, permissions_yaml); failures << test if test
    ds_test = policy_new_datasource?(file, file_diff, permissions_yaml); warnings << ds_test if ds_test && !test && !rd_test

    # Raise error if policy filename/path contains any uppercase letters
    test = policy_bad_filename_casing?(file); failures << test if test

    # Raise error if policy short_description is missing valid README link
    test = policy_bad_readme_link?(file, file_parsed); failures << test if test

    # Raise warning if policy won't be published
    test = policy_unpublished?(file, file_parsed); warnings << test if test

    # Raise warning if policy's name has changed
    test = policy_name_changed?(file, file_diff); warnings << test if test

    # Raise warning if outdated terminology found
    test = general_outdated_terminology?(file, file_lines); warnings << test if test

    # Raise error if the file contains any bad urls
    test = general_bad_urls?(file, file_diff); failures << test if test

    # Raise warning if policy contains invalid indentation
    test = policy_bad_indentation?(file, file_lines); warnings << test if test

    # Raise error if policy contains multiple blank lines
    test = policy_consecutive_empty_lines?(file, file_lines); failures << test if test

    # Raise errors or warnings if bad metadata is found
    test = policy_bad_metadata?(file, file_parsed, "name"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "short_description"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "long_description"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "category"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "default_frequency"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "severity"); failures << test if test
    test = policy_bad_metadata?(file, file_parsed, "info"); failures << test if test

    # Raise errors or warnings if bad info block metadata is found
    if !test
      info_test = policy_missing_info_field?(file, file_parsed, "version"); failures << info_test if info_test
      info_test = policy_missing_info_field?(file, file_parsed, "provider"); failures << info_test if info_test
      info_test = policy_missing_info_field?(file, file_parsed, "service"); warnings << info_test if info_test
      info_test = policy_missing_info_field?(file, file_parsed, "policy_set"); warnings << info_test if info_test
    end

    # Raise error if policy version number does not use semantic versioning
    test = policy_nonsemantic_version?(file, file_parsed); failures << test if test

    # Raise error if there is a mismatch between the policy's credentials and the README
    test = policy_readme_missing_credentials?(file, file_lines); failures << test if test

    # Raise error if policy sections are out of order
    test = policy_sections_out_of_order?(file, file_lines); failures << test if test

    # Raise error of code blocks exist in policy that aren't used anywhere
    test = policy_orphaned_blocks?(file, file_lines, "parameter"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "credentials"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "pagination"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "datasource"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "script"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "escalation"); failures << test if test
    test = policy_orphaned_blocks?(file, file_lines, "define"); failures << test if test

    # Raise error if policy blocks are not grouped together by type
    test = policy_blocks_ungrouped?(file, file_lines); failures << test if test

    # Report on missing policy section comments
    test = policy_missing_section_comments?(file, file_text, "parameter"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "credentials"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "pagination"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "datasource"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "policy"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "escalation"); failures << test if test
    test = policy_missing_section_comments?(file, file_text, "cwf"); failures << test if test

    # Report on invalidly named code blocks
    test = policy_bad_block_name?(file, file_lines, "parameter"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "credentials"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "pagination"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "datasource"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "script"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "policy"); failures << test if test
    test = policy_bad_block_name?(file, file_lines, "escalation"); failures << test if test

    # Report on invalid/deprecated code blocks
    test = policy_deprecated_code_blocks?(file, file_lines, "permission"); warnings << test if test
    test = policy_deprecated_code_blocks?(file, file_lines, "resources"); warnings << test if test

    # Report on missing fields in code blocks
    fields_to_check = [
      { block: "parameter", fields: ["type", "category", "label", "description"] },
      { block: "credentials", fields: ["schemes", "tags", "label", "description"] },
      { block: "escalation", fields: ["automatic", "label", "description"] }
    ]

    fields_to_check.each do |item|
      item[:fields].each do |field|
        test = policy_block_missing_field?(file, file_lines, item[:block], field); failures << test if test
      end
    end

    # Raise warning, not error, if parameter block is missing a default field.
    # This is because there are occasionally legitimate reasons to not have a default
    test = policy_block_missing_field?(file, file_lines, "parameter", "default")

    if test
      warnings << test + "\n\nWhile not required, it is recommended that every parameter have a default value unless user input for that parameter is required and too specific for any default value to make sense"
    end

    # Raise warning, not error, if a datasource and the script it calls have mismatched names.
    # Warning because there are occasionally legitimate reasons to do this.
    test = policy_ds_js_name_mismatch?(file, file_lines); warnings << test if test

    # Raise error if run_script statements with incorrect parameter ordering are found
    test = policy_run_script_incorrect_order?(file, file_lines); failures << test if test

    # Raise error if code blocks have fields in improper order
    test = policy_block_fields_incorrect_order?(file, file_lines, "parameter"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "credentials"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "pagination"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "datasource"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "script"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "policy"); failures << test if test
    test = policy_block_fields_incorrect_order?(file, file_lines, "escalation"); failures << test if test

    # Raise error if recommendation policy is missing required export fields
    test = policy_missing_recommendation_fields?(file, file_lines, file_parsed, "required"); failures << test if test

    # Raise warning if recommendation policy is missing recommended export fields
    test = policy_missing_recommendation_fields?(file, file_lines, file_parsed, "recommended"); warnings << test if test

    # Raise error if policy has outdated links
    test = policy_outdated_links?(file, file_lines); failures << test if test

    # Raise warning if policy has any datasources using http instead of https
    test = policy_http_connections?(file, file_lines); warnings << test if test

    # Raise warning if improper spacing between comma-separated items found
    test = policy_bad_comma_spacing?(file, file_lines); warnings << test if test

    # Raise error if policy has console.log() statements
    test = policy_console_log?(file, file_lines); failures << test if test
  end

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end

###############################################################################
# Meta Policy Testing
###############################################################################

puts Time.now.strftime("%H:%M:%S.%L") + " * " + " Testing all changed Meta Parent Policy Template files..."

# Check meta policies for issues for each file
changed_meta_pt_files.each do |file|
  puts Time.now.strftime("%H:%M:%S.%L") + " ** " + " Testing " + file + "..."

  # Run meta policy through various methods that test for problems.
  # These methods will return false if no problems are found.
  # Otherwise, they return the warning or error message that should be raised.
  warnings = []
  failures = []

  # Run policy through fpt testing. Only raise error if there is a syntax error.
  test = policy_fpt_syntax_error?(file, "meta"); failures << test if test

  # Output final list of failures and warnings
  fail "### **#{file}**\n\n#{failures.join("\n\n---\n\n")}" if !failures.empty?
  warn "### **#{file}**\n\n#{warnings.join("\n\n---\n\n")}" if !warnings.empty?
end
