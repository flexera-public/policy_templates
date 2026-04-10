# DangerFile Changelog Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: Changelog
###############################################################################

### Deprecated CHANGELOG test
# Utility method. Returns true if CHANGELOG is for a deprecated policy
def changelog_deprecated?(file, file_lines)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing whether CHANGELOG file is deprecated..."

  file_lines.any? do |line|
    line.include?("Deprecated: This policy template is no longer being updated") ||
      line.include?("Deprecated: This policy is no longer being updated")
  end
end

### Bad CHANGELOG Formatting test
# Verify that CHANGELOG is formatted correctly
# This only covers details that won't be picked up by the Markdown linter
def changelog_bad_formatting?(file, file_lines)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing whether CHANGELOG file is formatted correctly..."

  fail_message = ""

  # Regex to test proper formatting of version numbers
  version_tester = /^\d+\.\d+(\.\d+)?$/

  file_lines.each_with_index do |line, index|
    line_number = index + 1

    if line_number == 1
      if line.chomp != "# Changelog"
        fail_message += "Line #{line_number}: Invalid first line. The first line should always be: # Changelog\n"
      end
    else
      if line.strip.start_with?("#")
        if !line.start_with?("## v")
          fail_message += "Line #{line_number}: Invalid hash. Hash (#) should always precede a version number formatted like so: `## v1.0`\n"
        elsif !line.split("v")[1].match?(version_tester)
          fail_message += "Line #{line_number}: Invalid version number. Version numbers should always consist of two or three integers separated by periods. Valid examples: `1.0` `2.3.76` `11.5`\n"
        end
      elsif line.strip.start_with?("-")
        if !line.start_with?("- ") && !line.start_with?("  - ")
          fail_message += "Line #{line_number}: Invalid list formatting. List items under a version number should always begin with `- ` followed by some text explaining the change. Secondary items on a sublist should begin with `  - `.\n"
        end
      elsif !line.strip.empty?
        fail_message += "Line #{line_number}: Invalid content. After the first line, CHANGELOG files should only have version numbers preceded by `##`, changes preceded by `-`, and empty lines.\n"
      end
    end
  end

  return false if fail_message.empty?
  ("[[Info](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md#changelogmd)] CHANGELOG.md has formatting problems. Please correct the below:\n\n" + fail_message).strip
end
