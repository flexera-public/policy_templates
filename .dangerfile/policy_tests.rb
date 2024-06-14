# DangerFile Policy Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: Policy
###############################################################################

### Deprecated test
# Utility method. Returns true if policy is deprecated and false if it isn't
def policy_deprecated?(file)
  pp = PolicyParser.new
  pp.parse(file)

  info = pp.parsed_info

  deprecated = false

  if !info[:deprecated].nil?
    deprecated = true if info[:deprecated].downcase == "true"
  end

  return true if deprecated
  return false
end

### Deprecated without info flag test
# Returns true if policy is described as deprecated in short_description
# but lacks deprecated field in info() block
def policy_missing_deprecated_field?(file)
  pp = PolicyParser.new
  pp.parse(file)

  info = pp.parsed_info
  short_description = pp.parsed_short_description

  fail_message = ""

  if short_description.downcase.include?("deprecated")
    if info[:deprecated].nil?
      fail_message = "Policy is deprecated but has no `deprecated` field in the info() block. Please add the following line to the info() block: deprecated: \"true\""
    elsif info[:deprecated].downcase != "true"
      fail_message = "Policy is deprecated but `deprecated` field in the info() block is not set to `true`. Please set this field to `true`."
    end
  else
    if !info[:deprecated].nil?
      if info[:deprecated].downcase == "true"
        fail_message = "Policy is deprecated does not mention this in the `short_description`. Please add the following to the `short_description`:\n\n`**Deprecated: This policy is no longer being updated.**`"
      end
    end
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Nested directory test
# Return false if policy is correctly sorted within the directory structure
def policy_bad_directory?(file)
  fail_message = ""
  parts = file.split('/')

  valid_base_dirs = ["automation", "compliance", "cost", "operational", "saas", "security", "tools"]

  if !valid_base_dirs.include?(parts[0])
    fail_message += "Policy is not located in a valid base directory. All policies should be in one of the following directories: " + valid_base_dirs.join(', ') + "\n\n"
  end

  if (parts[1].include?('.pt') || parts[2].include?('.pt')) && parts[0] != "tools"
    fail_message += "Policy is not located within a subdirectory specific to the cloud provider or service it is applicable for. For example, AWS cost policies should be in the `/cost/aws` subdirectory, Azure operational policies in the `/operational/azure` subdirectory, etc.\n\n"
  end

  if (parts[1] == 'flexera' && parts[3].include?('.pt')) && parts[0] != "tools"
    fail_message += "Flexera policy is not contained in a subdirectory specific to the Flexera service it is for. For example, Flexera CCO cost policies should be in the `/cost/flexera/cco` subdirectory.\n\n"
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Unmodified README test
# Verify that .pt file also has an updated README
def policy_unmodified_readme?(file, changed_readme_files)
  fail_message = ""

  # Get file path for readme file
  file_sections = file.split('/')
  file_sections.pop
  readme_file_path = file_sections.join('/') + "/README.md"

  if !File.exist?(readme_file_path)
    fail_message = "Policy template has no README.md file. Please create this file and document the policy's functionality within."
  elsif !changed_readme_files.include?(readme_file_path)
    fail_message = "Policy template updated but associated README.md file has not been. Please verify that any necessary changes have been made to the README."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Unmodified CHANGELOG test
# Verify that .pt file also has an updated CHANGELOG
def policy_unmodified_changelog?(file, changed_changelog_files)
  fail_message = ""

  # Get file path for changelog file
  file_sections = file.split('/')
  file_sections.pop
  changelog_file_path = file_sections.join('/') + "/CHANGELOG.md"

  if !File.exist?(changelog_file_path)
    fail_message = "Policy template has no CHANGELOG.md file. Please create this file and document the policy's version changes within."
  elsif !changed_changelog_files.include?(changelog_file_path)
    fail_message = "Policy template updated but associated CHANGELOG.md file has not been. Please increment version number and update CHANGELOG.md accordingly."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Policy syntax error test
# Return false if no syntax errors are found using fpt.
def policy_fpt_syntax_error?(file, meta_policy = "child")
  fail_message = ""
  fpt = `[ -x ./fpt ] && ./fpt check #{file} | grep -v Checking`

  if !fpt.empty?
    if meta_policy == "meta"
      fail_message = "fpt has detected errors in meta policy. Please fix the issues in the child policy or in the meta policy generation tools that are causing these errors:\n\n#{fpt}"
    else
      fail_message = "fpt has detected errors in policy:\n\n#{fpt}"
    end
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Filename Casing test
# Verify that the filename is in lowercase
def policy_bad_filename_casing?(file)
  fail_message = ""

  if file.match?(/[A-Z]/)
    fail_message = "Policy template name and file path should be in lowercase. Please remove any uppercase [A-Z] characters."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### README Link test
# Verify that the readme in the short_description is valid
def policy_bad_readme_link?(file)
  fail_message = ""

  pp = PolicyParser.new
  pp.parse(file)
  short_description = pp.parsed_short_description

  file_path = file.split('/')
  file_path.pop
  file_url = "https://github.com/flexera-public/policy_templates/tree/master/" + file_path.join('/')

  url_regex = /https:\/\/[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:\/[^\s]*[^\s)])?/
  url_list = short_description.scan(url_regex)

  good_urls = 0
  bad_urls = 0

  url_list.each do |url|
    if url.include?("github.com")
      bad_urls += 1 if url != file_url && url != file_url + "/"
      good_urls += 1 unless url != file_url && url != file_url + "/"
    end
  end

  if bad_urls > 0 || good_urls == 0
    fail_message = "Policy `short_description` is missing a valid link to the policy README. Please ensure that the following link is present in the `short_description`:\n\n#{file_url}/"
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Publish test
# Return false if policy info block is missing publish field or publish is set to a value other than "false"
def policy_unpublished?(file)
  pp = PolicyParser.new
  pp.parse(file)

  info = pp.parsed_info

  fail_message = ""

  if !info[:publish].nil?
    if info[:publish].downcase == "false"
      fail_message = "Policy will not be published in the public catalog. If this is not the intended behavior, remove the `publish` field from the policy's info metadata block."
    end
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Name change test
# Return false if policy's name has not changed
def policy_name_changed?(file)
  # Get the diff to see only the new changes
  diff = git.diff_for_file(file)

  fail_message = ""

  diff.patch.each_line do |line|
    if line.start_with?('-name "')
      fail_message = "Policy's name has been changed. Please ensure that this is intentional and that the README has been updated accordingly."
      break
    end
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Bad Indentation test
# Verify that everything is properly indented
def policy_bad_indentation?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Message to return of test fails
  fail_message = ""

  indent_level = 0
  code_block = false
  eos_block = false
  define_block = false

  policy_code.each_line.with_index do |line, index|
    break if line.strip.start_with?('# Meta Policy [alpha]') # Break out of definition when enounter meta policy code at the bottom
    next if line.strip.start_with?('#') # Skip comment lines

    line_number = index + 1
    indentation = line.match(/\A\s*/).to_s.length

    # Skip blocks of EOS/EOF text and define blocks, since these contain arbitrarily spaced code/text
    code_block = false if code_block && line.strip == "EOS" || line.strip == "EOF"
    eos_block = false if eos_block && line.strip == "EOS" || line.strip == "EOF"
    define_block = false if define_block && line.start_with?("end")

    if !code_block && !define_block && !eos_block
      indent_level -= 2 if line.strip == "end" || line.strip == ")"

      if indentation != indent_level && !line.strip.empty? && line.strip != "EOS" && line.strip != "EOF"
        fail_message += "Line #{line_number.to_s}: Expected indentation of #{indent_level.to_s} spaces but found #{indentation} spaces.\n"
      end

      indent_level += 2 if line.strip.end_with?(" do") || line.start_with?("info(")

      # We only check EOS blocks if they are for the code field
      code_block = true if line.include?("<<-") && line.include?("code")
      eos_block = true if line.include?("<<-") && !line.include?("code")
      define_block = true if line.start_with?("define ") && line.strip.end_with?(" do")

    # If we're within one of these blocks, at least make sure we're 2 spaces indented
    elsif (code_block || define_block) && indentation < 2 && !line.strip.empty?
      fail_message += "Line #{line_number.to_s}: Expected indentation of at least two spaces within code/text block.\n"
    end
  end

  fail_message = "Policy Template has indentation issues. Code should be indented with 2 spaces inside each do/end block, info() block, and EOS block, with additional spacing for nested blocks as appropriate:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Consecutive Empty Lines test
# Verify that the policy does not have multiple blank lines in a row
def policy_consecutive_empty_lines?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Message to return of test fails
  fail_message = ""

  blank_lines_count = 0
  blank_line_number = nil

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    blank_lines_count += 1 if line.strip.empty?
    blank_line_number = line_number if line.strip.empty? && blank_lines_count == 1

    fail_message += "Line #{blank_line_number.to_s}\n" if !line.strip.empty? && blank_lines_count > 1

    blank_lines_count = 0 if !line.strip.empty?
    blank_line_number = nil if !line.strip.empty?
  end

  fail_message = "Policy Template has consecutive empty lines. Code blocks and other code constructs should never be separated by more than one empty line:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Metadata test
# Return false if policy metadata has missing or problematic field
def policy_bad_metadata?(file, field_name)
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

  fail_message = ""

  if field_name == "name"
    fail_message += "Please add a name field.\n\n" if !name
    fail_message += "Please add a value other than an empty string to the name field.\n\n" if name && name == ""
  end

  if field_name == "short_description"
    fail_message += "Please add a short_description field.\n\n" if !short_description
    fail_message += "Please add a value other than an empty string to the short_description field.\n\n" if short_description && short_description == ""
  end

  if field_name == "long_description"
    fail_message += "Please add a long_description field with an empty string as its value.\n\n" if !long_description
    fail_message += "Please make the long_description field an empty string.\n\n" if long_description && long_description != ""
  end

  if field_name == "category"
    fail_message += "Please add a category field.\n\n" if !category
    fail_message += "The Category is not valid: #{category}. Valid Categories include #{categories.join(', ')}\n\n" if category && !categories.include?(category.downcase)
    fail_message += "The First letter of Category is not capitalized: #{category}.\n\n" if category !~ /^[A-Z]/
  end

  if field_name == "default_frequency"
    fail_message += "Please add a default_frequency field.\n\n" if !default_frequency
    fail_message += "The default_frequency is not valid: #{default_frequency}. Valid frequencies include #{frequencies.join(', ')}\n\n" if default_frequency && !frequencies.include?(default_frequency)
  end

  if field_name == "severity"
    fail_message += "Please add a severity field.\n\n" if !severity
    fail_message += "The severity is not valid: #{severity}. Valid severities include #{severities.join(', ')}\n\n" if severity && !severities.include?(severity)
  end

  if field_name == "info"
    fail_message += "Please add an info field.\n\n" if info.nil?
  end

  fail_message = "Bad #{field_name} metadata found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Info block test
# Return false if policy info block has missing or problematic fields
def policy_missing_info_field?(file, field_name)
  pp = PolicyParser.new
  pp.parse(file)

  info = pp.parsed_info

  fail_message = ""

  if info.nil?
    fail_message += "Please add the info field.\n\n" if info.nil?
  else
    if field_name == "version"
      fail_message += "Please add version to the info field.\n\n" if info[:version].nil?
    end

    if field_name == "provider"
      fail_message += "Please add provider to the info field.\n\n" if info[:provider].nil?
    end

    if field_name == "service"
      fail_message += "Should this include service in the info field?\n\n" if info[:service].nil?
    end

    if field_name == "policy_set"
      fail_message += "Should this include policy_set in the info field?\n\n" if info[:policy_set].nil?
    end
  end

  fail_message = "Bad #{field_name} info metadata field found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Semantic Version Test
# Return false if policy's version number is compliant with semantic versioning
def policy_nonsemantic_version?(file)
  fail_message = ""

  semantic_regex = /^\d+\.\d+\.\d+$/

  pp = PolicyParser.new
  pp.parse(file)
  policy_version = pp.parsed_info[:version] if pp.parsed_info

  if !policy_version.match?(semantic_regex)
    fail_message = "Policy template version number is not compliant with [semantic versioning](https://github.com/flexera-public/policy_templates/blob/master/VERSIONING.md). Please update the version number accordingly."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Changelog Version Test
# Return false if policy's version number matches the latest entry in the CHANGELOG
def policy_changelog_mismatch?(file)
  fail_message = ""

  # Derive path to CHANGELOG file from file name/path
  file_parts = file.split('/')
  file_parts.pop
  changelog_file = file_parts.join('/') + "/CHANGELOG.md"

  # Store contents of file for direct analysis
  changelog_text = File.read(changelog_file)

  # Get version number from policy
  policy_version = nil

  pp = PolicyParser.new
  pp.parse(file)
  policy_version = pp.parsed_info[:version] if pp.parsed_info

  # Get version number from changelog
  changelog_version = nil

  if changelog_text && changelog_text.split("\n")[2].start_with?("## v")
    changelog_version = changelog_text.split("\n")[2].split('v')[1].strip
  end

  # We ignore situations where one of the values is missing.
  # Other tests will catch that.
  if policy_version && changelog_version && policy_version != changelog_version
    fail_message = "Version number in policy template does not match latest version number in `CHANGELOG.md`. Please review both files to make sure they are correct and aligned with each other."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### README Credential Test
# Return false if policy's README has documentation for all of the credentials in the policy itself
def policy_readme_missing_credentials?(file)
  fail_message = ""

  # Derive path to CHANGELOG file from file name/path
  file_parts = file.split('/')
  file_parts.pop
  readme_file = file_parts.join('/') + "/README.md"

  # Store contents of files for direct analysis
  policy_code = File.read(file)
  readme_text = File.read(readme_file)

  # Find out which providers have credentials in the policy
  pol_flexera_credential = false
  pol_aws_credential = false
  pol_azure_credential = false
  pol_google_credential = false
  pol_oracle_credential = false

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    if line.start_with?("credentials ")
      pol_flexera_credential = true if line.include?("flexera")
      pol_aws_credential = true if line.include?("aws")
      pol_aws_credential = true if line.include?("amazon")
      pol_azure_credential = true if line.include?("azure") && !line.include?("china")
      pol_google_credential = true if line.include?("google")
      pol_google_credential = true if line.include?("gcp")
      pol_google_credential = true if line.include?("gce")
      pol_oracle_credential = true if line.include?("oracle")
      pol_oracle_credential = true if line.include?("oci")
    end
  end

  # Find out which providers have credentials in the README
  readme_flexera_credential = false
  readme_aws_credential = false
  readme_azure_credential = false
  readme_google_credential = false
  readme_oracle_credential = false

  flexera_regex = /(?i)(?=.*flexera)(?=.*credential)(?=.*provider=flexera).*/
  aws_regex = /(?i)(?=.*aws)(?=.*credential)(?=.*provider=aws).*/
  azure_regex = /(?i)(?=.*azure)(?=.*credential)(?=.*provider=azure_rm).*/
  google_regex = /(?i)(?=.*google)(?=.*credential)(?=.*provider=gce).*/
  oracle_regex = /(?i)(?=.*oracle)(?=.*credential)(?=.*provider=oracle).*/

  readme_text.each_line.with_index do |line, index|
    line_number = index + 1

    readme_flexera_credential = true if line.strip.match?(flexera_regex)
    readme_aws_credential = true if line.strip.match?(aws_regex)
    readme_azure_credential = true if line.strip.match?(azure_regex) && !line.include?("Azure China")
    readme_google_credential = true if line.strip.match?(google_regex)
    readme_oracle_credential = true if line.strip.match?(oracle_regex)
  end

  # Check for mismatches between policy and README.md
  if pol_flexera_credential && !readme_flexera_credential && !file.start_with?("saas/fsm/")
    fail_message += "Policy contains Flexera credential but this credential either missing from or incorrectly formatted in the associated `README.md` file.\n\n"
  end

  if pol_aws_credential && !readme_aws_credential
    fail_message += "Policy contains AWS credential but this credential either missing from or incorrectly formatted in the associated `README.md` file.\n\n"
  end

  if pol_azure_credential && !readme_azure_credential
    fail_message += "Policy contains Azure credential but this credential either missing from or incorrectly formatted in the associated `README.md` file.\n\n"
  end

  if pol_google_credential && !readme_google_credential
    fail_message += "Policy contains Google credential but this credential either missing from or incorrectly formatted in the associated `README.md` file.\n\n"
  end

  if pol_oracle_credential && !readme_oracle_credential
    fail_message += "Policy contains Oracle credential but this credential either missing from or incorrectly formatted in the associated `README.md` file.\n\n"
  end

  if !pol_flexera_credential && readme_flexera_credential && !file.start_with?("saas/fsm/")
    fail_message += "Policy's `README.md` file contains documentation for a Flexera credential that does not exist or is incorrectly named in the policy.\n\n"
  end

  if !pol_aws_credential && readme_aws_credential
    fail_message += "Policy's `README.md` file contains documentation for an AWS credential that does not exist or is incorrectly named in the policy.\n\n"
  end

  if !pol_azure_credential && readme_azure_credential
    fail_message += "Policy's `README.md` file contains documentation for an Azure credential that does not exist or is incorrectly named in the policy.\n\n"
  end

  if !pol_google_credential && readme_google_credential
    fail_message += "Policy's `README.md` file contains documentation for a Google credential that does not exist or is incorrectly named in the policy.\n\n"
  end

  if !pol_oracle_credential && readme_oracle_credential
    fail_message += "Policy's `README.md` file contains documentation for an Oracle credential that does not exist or is incorrectly named in the policy.\n\n"
  end

  fail_message = "Policy Template's credentials and `README.md` documentation do not match:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Section order test
# Return false if policy sections are in the correct order.
def policy_sections_out_of_order?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Message to return of test fails
  fail_message = ""

  # Report back 'true' if policy sections are not properly ordered based on blocks
  found_metadata = false
  found_parameters = false
  found_credentials = false
  found_pagination = false
  found_datasources = false
  found_policy = false
  found_escalations = false
  found_cwf = false

  # Ensure that each type of error is only reported once
  metadata_fail = false
  parameters_fail = false
  credentials_fail = false
  datasources_fail = false
  policy_fail = false
  escalations_fail = false

  # Failsafe for meta policy code which won't be in the correct order by design
  found_meta = false

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    found_meta = true if line.strip.start_with?('# Meta Policy [alpha]')

    if !found_meta
      found_metadata = true if line.start_with?('name ')
      found_parameters = true if line.strip.start_with?('parameter ') && line.strip.end_with?('do')
      found_credentials = true if line.strip.start_with?('credentials ') && line.strip.end_with?('do')
      found_pagination = true if line.strip.start_with?('pagination ') && line.strip.end_with?('do')
      found_datasources = true if line.strip.start_with?('datasource ') && line.strip.end_with?('do')
      found_policy = true if line.strip.start_with?('policy ') && line.strip.end_with?('do')
      found_escalations = true if line.strip.start_with?('escalation ') && line.strip.end_with?('do')
      found_cwf = true if line.strip.start_with?('define ') && line.strip.end_with?('do')

      if !metadata_fail && !found_metadata && (found_parameters || found_credentials || found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before metadata\n\n"
        metadata_fail = true
      end

      if !parameters_fail && !found_parameters && (found_credentials || found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before parameter\n\n"
        parameters_fail = true
      end

      if !credentials_fail && !found_credentials && (found_pagination || found_datasources || found_policy || found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before credentials\n\n"
        credentials_fail = true
      end

      if !datasources_fail && !found_datasources && (found_policy || found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before datasources\n\n"
        datasources_fail = true
      end

      if !policy_fail && !found_policy && (found_escalations || found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before policy block\n\n"
        policy_fail = true
      end

      if !escalations_fail && !found_escalations && (found_cwf)
        fail_message += "Line #{line_number.to_s}: Invalid blocks found before escalations\n\n"
        escalations_fail = true
      end
    end
  end

  fail_message = "Policy Template does not have code blocks in the correct order.\nCode blocks should be in the following order: Metadata, Parameters, Credentials, Pagination, Datasources & Scripts, Policy, Escalations, Cloud Workflow, Meta Policy\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Orphaned block test
# Return false if code blocks of the specified block_name are all referenced elsewhere in the policy
def policy_orphaned_blocks?(file, block_name)
  # Store failure message
  fail_message = ""

  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Get a full list of names for all of the blocks of the specified type
  block_list = []

  policy_code.each_line.with_index do |line, index|
    if line.start_with?(block_name + " ")
      block_list << line.split('"')[1] if block_name != "define"
      block_list << line.split("(")[0].split(" ")[1] if block_name == "define"
    end
  end

  block_list.each do |block|
    reference_found = false

    policy_code.each_line.with_index do |line, index|
      if !line.start_with?(block_name + " ") && line.include?(block)
        reference_found = true
        break
      end
    end

    fail_message += "#{block}\n" if !reference_found
  end

  fail_message = "Orphaned `#{block_name}` code blocks found. Blocks that are not used anywhere in the policy should be removed:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Block grouping test
# Return false if code blocks are all grouped together by type.
def policy_blocks_ungrouped?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  # Store failure message
  fail_message = ""

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

    policy_code.each_line.with_index do |line, index|
      line_number = index + 1

      found_meta = true if line.strip.start_with?('# Meta Policy [alpha]')

      if !found_meta
        # If we've found the block we're testing, and then other blocks,
        # and then found the block we're testing again, return error
        if line.start_with?(block) && line.strip.end_with?('do') && found_other_blocks
          fail_message += "Line #{line_number.to_s}: Unsorted #{block.strip} code block found\n"
          found_block = false
          found_other_blocks = false
        end

        # Once we've found the block we're testing, start looking for other blocks
        if found_block
          block_names.each do |other_block|
            if other_block != block
              found_other_blocks = true if line.start_with?(other_block) && line.strip.end_with?('do')
            end
          end
        end

        found_block = true if line.start_with?(block) && line.strip.end_with?('do')
      end
    end
  end

  fail_message = "Ungrouped code blocks found. Code blocks should be grouped together in sections by type e.g. all parameter blocks should be next to each other, all credentials blocks should be next to each other, etc. with the exception of Meta Policy code:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Section comment test
# Return false if all required policy section comments are present.
def policy_missing_section_comments?(file, section_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

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
  if block_regex.match?(policy_code) && !comment_regex.match?(policy_code)
    hash_string = "###############################################################################"
    fail_message += "Policy Template does **not** have a comment indicating where the #{pretty_name} section begins. Please add a comment like the below before the parameters blocks:\n\n#{hash_string}<br>\# #{pretty_name}<br>#{hash_string}\n\n"
  end

  fail_message = "Missing policy section comments:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Bad block name test
# Return false if no invalidly named code blocks are found.
def policy_bad_block_name?(file, block_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

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

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1
    fail_message += "Line #{line_number.to_s}\n" if block_regex.match?(line)
  end

  fail_message = "Invalidly named #{block_name} blocks. Please ensure all #{block_name} blocks have names that begin with `#{proper_name}`:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Deprecated block test
# Return false if no deprecated blocks are found.
def policy_deprecated_code_blocks?(file, block_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  permission_regex = /^permission\s+"[^"]*"\s+do$/
  resources_regex = /^resources\s+"[^"]*",\s+type:\s+"[^"]*"\s+do$/

  fail_message = ""

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1
    fail_message += "Line #{line_number.to_s}: Permission block found\n" if permission_regex.match?(line)
    fail_message += "Line #{line_number.to_s}: Resources block found\n" if resources_regex.match?(line)
  end

  fail_message = "Deprecated #{block_name} blocks found. It is recommended that the policy be refactored to no longer use these code blocks:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Missing block field test
# Return false if specified field is not missing from any of the specified blocks.
def policy_block_missing_field?(file, block_name, field_name)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  present = false
  line_number = nil

  policy_code.each_line.with_index do |line, index|
    # Check if we're entering the block
    if line.strip.start_with?(block_name + ' ') && line.strip.end_with?('do')
      present = false
      line_number = index + 1
    end

    # Check for the field if we're in a block
    present = true if line_number && line.strip.start_with?(field_name + ' ')

    # For default field, and default value not present, check for comment declaring no default value
    # This is to avoid false errors for parameters that require user input
    present = true if !present && field_name == "default" && line.strip.start_with?('# No default value, user input required')

    # When we reach the end of a block, check if field was present
    if line.strip == 'end' && line_number
      fail_message += "Line #{line_number.to_s}\n" unless present
      line_number = nil
    end
  end

  # After looping through all lines, check if we found any missing fields
  if !fail_message.empty?
    # Construct resulting fail message with block name and line numbers
    fail_message = "#{block_name} code blocks with missing `#{field_name}` field found. Please add the `#{field_name}` field to these blocks:\n\n" + fail_message + "\n"
    # If we're checking for default field, add a note about comment `# No default value, user input required`
    if field_name == "default" && !fail_message.empty?
      fail_message += "Optionally, you can add a comment within the #{block_name} code blocks to indicate that the parameter requires user input and avoid this message.\n\n - `# No default value, user input required`"
    end
    # Return resulting fail message
    return fail_message.strip
  else
    # If we didn't find any missing fields, return false
    return false
  end
end

### Datasource/script name matching test
# Return message if datasource and script do not have matching names. Otherwise, return false
def policy_ds_js_name_mismatch?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""
  ds_name = nil
  js_name = nil
  line_number = nil
  found_mismatches = []

  policy_code.each_line.with_index do |line, index|
    # Stop doing the check once we hit the Meta Policy section
    if line.strip.start_with?('# Meta Policy [alpha]')
      break
    # When we find a datasource, store its name
    elsif line.strip.start_with?("datasource ") && line.strip.end_with?('do')
      name_test = line.match(/"([^"]*)"/)
      ds_name = name_test[1] if name_test
      line_number = index + 1
    # When we find a run_script, store its name and compare to datasource
    elsif line.strip.start_with?("run_script ")
      name_test = line.match(/run_script \$([a-zA-Z0-9_]+)/)
      js_name = name_test[1] if name_test

      if ds_name != nil && js_name != nil
        if ds_name[3..-1] != js_name[3..-1]
          found_mismatches << {
            line_number: line_number,
            ds_name: ds_name[3..-1],
            js_name: js_name[3..-1]
          }

          #fail_message += "Line #{line_number.to_s}: #{ds_name} / #{js_name}\n"
        end
      end

      # Reset all variables to start the process over for the next datasource we find
      ds_name = nil
      js_name = nil
      line_number = nil
    end
  end

  # Filter out mismatches where the javascript block is referenced by multiple datasources
  js_name_counts = found_mismatches.each_with_object(Hash.new(0)) do |item, counts|
    counts[item[:js_name]] += 1
  end

  filtered_mismatches = found_mismatches.reject do |item|
    js_name_counts[item[:js_name]] > 1
  end

  filtered_mismatches.each do |mismatch|
    fail_message += "Line #{mismatch[:line_number]}: ds_#{mismatch[:ds_name]} / js_#{mismatch[:js_name]}\n"
  end

  fail_message = "Datasources and scripts with mismatched names found. These names should match; for example, a datasource named ds_currency should be paired with a script named js_currency. This convention should only be ignored when the same script is called by multiple datasources. The following datasource/script pairs have mismatched names:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Script parameter order test
# Return message if script parameters are not in the correct order. Otherwise, return false
def policy_run_script_incorrect_order?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""
  ds_name = nil

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    # Stop doing the check if we've reached the meta policy section
    break if line.strip.start_with?('# Meta Policy [alpha]') # Break out of definition when enounter meta policy code at the bottom

    if line.strip.start_with?("datasource ") && line.strip.end_with?('do')
      name_test = line.match(/"([^"]*)"/)
      ds_name = name_test[1] if name_test
    end

    disordered = false
    val_index = -5

    if line.strip.start_with?("run_script")
      # Store a list of all of the parameters for the run_script
      parameters = line.strip.sub('run_script ', '').split(',').map(&:strip)

      # Remove the first item because it's just the name of the script itself
      script_name = parameters.shift

      val_found = false       # Whether we've found a iter_item or val() parameter
      ds_found = false        # Whether we've found a datasource parameter
      param_found = false     # Whether we've found a parameter parameter
      constant_found = false  # Whether we've found a constant, like rs_org_id
      value_found = false     # Whether we've found a raw value, like a number or string

      parameters.each_with_index do |parameter, index|
        if parameter.include?("iter_item") || parameter.include?("val(")
          val_found = true
          val_index = index
          disordered = true if ds_found || param_found || constant_found || value_found
        elsif index == val_index + 1
          # Do nothing, since splitting by , is going to split functions like val() into two entries
        elsif parameter.start_with?('$ds')
          ds_found = true
          disordered = true if param_found || constant_found || value_found
        elsif parameter.start_with?('$param')
          param_found = true
          disordered = true if constant_found || value_found
        elsif /[A-Za-z]/.match(parameter[0]) # If parameter starts with a letter
          constant_found = true
          disordered = true if value_found
        else # Assume a raw value, like a number or string, if none of the above
          value_found = true
          val_index = index if parameter.start_with?("val(")
        end
      end
    end

    fail_message += "Line #{line_number.to_s}: #{ds_name} / run_script #{script_name}\n" if disordered
  end

  fail_message = "run_script statements found whose parameters are not in the correct order. run_script parameters should be in the following order: script, val(iter_item, *string*), datasources, parameters, variables, raw values:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Code block field order test
# Return message if fields for the specified code block type are not in the proper order
def policy_block_fields_incorrect_order?(file, block_type)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  field_list = []
  correct_order = nil
  testing_block = false
  sub_block = false
  export_block = false
  field_block = false
  block_line_number = 0
  block_names = [ block_type ]
  block_id = ""
  policy_id = nil

  case block_type
  when "parameter"
    correct_order = [ "type", "category", "label", "description", "allowed_values", "allowed_pattern", "min_value", "max_value", "default" ]
  when "credentials"
    correct_order = [ "schemes", "label", "description", "tags", "aws_account_number" ]
  when "pagination"
    correct_order = [ "get_page_marker", "set_page_marker" ]
  when "datasource"
    correct_order = [ "auth", "pagination", "verb", "scheme", "host", "path", "query", "header", "body", "body_field", "ignore_status" ]
  when "script"
    correct_order = [ "parameters", "result", "code" ]
  when "policy"
    correct_order = [ "summary_template", "detail_template", "check", "escalate", "hash_include", "hash_exclude", "export" ]
    block_names = [ "  validate", "  validate_each" ]
  when "escalation"
    correct_order = [ "automatic", "label", "description", "email", "run" ]
  end

  if correct_order
    block_names.each do |block_name|
      policy_code.each_line.with_index do |line, index|
        line_number = index + 1

        break if line.strip.start_with?('# Meta Policy [alpha]') # Break out of definition when enounter meta policy code at the bottom

        policy_id = line.split('"')[1] if line.start_with?("policy ")

        if testing_block && !sub_block && !export_block && !line.strip.start_with?("end") && !line.strip.start_with?("request do") && !line.strip.start_with?("result do")
          sub_block = true if line.strip.end_with?(" do") || line.include?("<<-")
          export_block = true if line.strip == "export do"
          field_list << line.strip.split(" ")[0]
        elsif !sub_block && !export_block && line.strip.start_with?("end")
          filtered_list = field_list.select { |item| correct_order.include?(item) }
          order_indices = filtered_list.map { |item| correct_order.index(item) }

          if order_indices != order_indices.sort
            if policy_id && block_type == "policy"
              fail_message += "Line #{block_line_number.to_s}: policy \"#{policy_id}\" #{block_name.strip}\n"
            else
              fail_message += "Line #{block_line_number.to_s}: #{block_name} \"#{block_id}\"\n"
            end
          end

          testing_block = false
          sub_block = false
          export_block = false
          field_list = []
        elsif sub_block && !export_block && (line.strip == "end" || line.include?("EOS") || line.include?("EOF"))
          sub_block = false
        elsif export_block
          export_block = false if line.strip == "end" && !field_block
          field_block = true if line.strip.start_with?("field") && line.strip.end_with?(" do")
          field_block = false if line.strip  == "end" && field_block
        end

        if line.start_with?(block_name + " ") && line.strip.end_with?(" do")
          testing_block = true
          sub_block = false
          export_block = false
          field_list = []

          block_line_number = line_number
          block_id = line.split('"')[1]
        end
      end
    end
  end

  fail_message = "#{block_type} code blocks found with out of order fields.\nFields should be in the following order: " + correct_order.join(", ") + "\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Recommendation policy export field test
# Return message if required recommendation policy fields are missing
def policy_missing_recommendation_fields?(file, field_type)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  pp = PolicyParser.new
  pp.parse(file)
  info = pp.parsed_info

  if field_type == "required"
    required_fields = [ "accountID", "accountName", "resourceID", "recommendationDetails", "service", "savings", "savingsCurrency", "id" ]
  end

  if field_type == "recommended"
    required_fields = [ "resourceName", "region", "tags" ]
  end

  if !info[:recommendation_type].nil?
    fields_found = []
    export_block = false
    export_line = nil
    field_block = false

    export_info = []

    policy_code.each_line.with_index do |line, index|
      line_number = index + 1

      if line.strip.start_with?("export do")
        export_block = true
        export_line = line_number
      end

      if export_block && !field_block && line.strip.start_with?("end")
        export_block = false

        export_info << {
          "line": export_line,
          "list": fields_found
        }

        export_line = nil
        fields_found = []
      end

      if export_block && !field_block && line.strip.start_with?("field")
        fields_found << line.strip.split('"')[1]
        field_block = true
      end

      field_block = false if field_block && line.strip.start_with?("end")
    end

    export_info.each do |export|
      missing_fields = []

      required_fields.each do |field|
        missing_fields << field if !export[:list].include?(field)
      end

      if missing_fields.length > 0
        fail_message += "Line #{export[:line].to_s}: " + missing_fields.join(", ") + "\n"
      end
    end
  end

  fail_message = "Recommendation policy has export that is missing #{field_type} fields. These fields are scraped by the Flexera platform for dashboards:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end


### Improper Comma Spacing Test
# Return false if all comma separated items have a space between them like so: one, two, three
def policy_bad_comma_spacing?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    if line.include?(",") && !line.include?("allowed_pattern") && !line.include?('= ","') && !line.include?("(',')") && !line.include?('(",")') && !line.include?("jq(")
      if line.strip.match(/,\s{2,}/) || line.strip.match(/\s,/) || line.strip.match(/,[^\s]/)
        fail_message += "Line #{line_number.to_s}: Possible invalid spacing between comma-separated items found.\nComma separated items should be organized as follows, with a single space following each comma: apple, banana, pear\n\n"
      end
    end
  end

  fail_message = "Issues with comma-separation found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Outdated Links
# Return false if no outdated links are found
def policy_outdated_links?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  within_datasource = false
  github_host = false
  datasource_line = nil

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    if line.include?("https://image-charts.com")
      fail_message += "Line #{line_number.to_s}: Direct link to `image-charts.com` found. Please replace `https://image-charts.com/chart?` with `https://api.image-charts-auth.flexeraeng.com/ic-function?rs_org_id={{ rs_org_id }}&rs_project_id={{ rs_project_id }}&`.\n\n"
    end

    if line.start_with?("datasource ")
      within_datasource = true
      datasource_line = line_number
    end

    if within_datasource && line.start_with?("end")
      within_datasource = false
      github_host = false
    end

    if within_datasource
      github_host = true if line.strip.start_with?('host "raw.githubusercontent.com"')

      if github_host && line.strip.start_with?("path ")
        if line.include?("/policy_templates/")
          if !line.include?("/flexera-public/policy_templates/master/")
            fail_message += "Line #{datasource_line.to_s}: Datasource has outdated or incorrect Github path. Please update `path` field to point to `/flexera-public/policy_templates/master/`.\n\n"
          else
            file_path = line.split("/master/")[1].split('"')[0]

            if !File.exist?(file_path)
              fail_message += "Line #{datasource_line.to_s}: Datasource has invalid link to Github asset. The file `#{file_path}` does not appear to exist. Please make sure the `path` field points to a valid file.\n\n"
            end
          end
        end
      end
    end
  end

  fail_message = "Invalid links found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Insecure HTTP Test
# Return false if all datasources use HTTPS instead of HTTP
def policy_http_connections?(file)
  # Store contents of file for direct analysis
  policy_code = File.read(file)

  fail_message = ""

  within_datasource = false
  within_script = false
  within_cwf = false

  policy_code.each_line.with_index do |line, index|
    line_number = index + 1

    within_datasource = true if line.start_with?("datasource ")
    within_script = true if line.start_with?("script ")
    within_cwf = true if line.start_with?("define ")

    within_datasource = false if within_datasource && line.strip == "end"
    within_script = false if within_script && (line.strip == "EOS" || line.strip == "EOF")
    within_cwf = false if within_cwf && line.strip == "end"

    if within_datasource
      if line.strip.start_with?("scheme ") && line.strip.split('"')[1] == "http"
        fail_message += "Line #{line_number.to_s}: Datasource `scheme` field is configured to use insecure `http` connection instead of `https`. Please consider using `https` instead.\n\n"
      end
    end

    if within_script
      if line.include?("scheme") && line.include?(":") && line.include?("http") && !line.include?("https")
        fail_message += "Line #{line_number.to_s}: Script found where `scheme` field may be configured to use insecure `http` connection instead of `https`. Please consider using `https` instead.\n\n"
      end
    end

    if within_cwf
      if line.include?("https") && line.include?(":") && line.include?("false") && !line.include?("true")
        fail_message += "Line #{line_number.to_s}: Cloud Workflow found where `https` field may be set to `false`. Please consider using `https` instead.\n\n"
      end
    end
  end

  fail_message = "Insecure `http` connections found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Master permissions test
# Return false if master permissions have been recorded for the policy
def policy_missing_master_permissions?(file, permissions_yaml)
  # Get the diff to see only the new changes
  diff = git.diff_for_file(file)

  fail_message = ""

  # Use regex to look for blocks that have a "datasource", "request", and "auth" sections of the datasource
  # Example String:
  #   "diff --git a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\nindex 14b3236f..bf6a161d 100644\n--- a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n+++ b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n@@ -193,6 +193,16 @@ datasource \"ds_applied_policy\" do\n   end\n end\n \n+datasource \"ds_applied_policy_test_will_be_removed_later\" do\n+  request do\n+    auth $auth_flexera\n+    host rs_governance_host\n+    path join([\"/api/governance/projects/\", rs_project_id, \"/applied_policies/\", policy_id])\n+    header \"Api-Version\", \"1.0\"\n+    header \"Test\", \"True\"\n+  end\n+end\n+\n # Get region-specific Flexera API endpoints\n datasource \"ds_flexera_api_hosts\" do\n   run_script $js_flexera_api_hosts, rs_optima_host"
  regex = /datasource.*do(\s)+.*request.*do(\s)+.*auth.*([\s\S])+end([\s\+])+end/

  # First check if the PT file has been manually validated and enabled for permission generation
  pt_file_enabled = permissions_yaml["validated_policy_templates"].select { |pt| pt.include?(file) }

  if pt_file_enabled.empty? && !file.start_with?("saas/fsm/")
    # If the PT file has not been manually validated, then print an error message which will block the PR from being merged
    # This will help improve coverage as we touch more PT files
    fail_message = "Policy Template file has **not** yet been enabled for automated permission generation. Please help us improve coverage by [following the steps documented in `tools/policy_master_permission_generation/`](https://github.com/flexera-public/policy_templates/tree/master/tools/policy_master_permission_generation) to resolve this."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### New datasource test
# Return false if no new datasources are found.
def policy_new_datasource?(file, permissions_yaml)
  # Get the diff to see only the new changes
  diff = git.diff_for_file(file)

  fail_message = ""

  # Use regex to look for blocks that have a "datasource", "request", and "auth" sections of the datasource
  # Example String:
  #   "diff --git a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\nindex 14b3236f..bf6a161d 100644\n--- a/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n+++ b/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt\n@@ -193,6 +193,16 @@ datasource \"ds_applied_policy\" do\n   end\n end\n \n+datasource \"ds_applied_policy_test_will_be_removed_later\" do\n+  request do\n+    auth $auth_flexera\n+    host rs_governance_host\n+    path join([\"/api/governance/projects/\", rs_project_id, \"/applied_policies/\", policy_id])\n+    header \"Api-Version\", \"1.0\"\n+    header \"Test\", \"True\"\n+  end\n+end\n+\n # Get region-specific Flexera API endpoints\n datasource \"ds_flexera_api_hosts\" do\n   run_script $js_flexera_api_hosts, rs_optima_host"
  regex = /datasource.*do(\s)+.*request.*do(\s)+.*auth.*([\s\S])+end([\s\+])+end/

  # First check if the PT file has been manually validated and enabled for permission generation
  pt_file_enabled = permissions_yaml["validated_policy_templates"].select { |pt| pt.include?(file) }

  if diff && diff.patch =~ regex && !pt_file_enabled.empty?
    # If the PT file has been manually validated, but there are new datasources, then print a warning message
    fail_message = "Detected new request datasource(s) in Policy Template file. Please verify the README.md has any new permissions that may be required."
  end

  return fail_message.strip if !fail_message.empty?
  return false
end
