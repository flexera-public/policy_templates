# DangerFile README Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: README
###############################################################################

### Deprecated README test
# Utility method. Returns true if README is for a deprecated policy
def readme_deprecated?(file, file_lines)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing whether README file is deprecated..."
  file_lines.any? { |line| line.start_with?("## Deprecated") }
end

### Missing README Sections
# Verify that README file has all required sections
def readme_missing_sections?(file, file_lines)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing whether README file is missing required sections..."

  fail_message = ""

  # Flags for whether sections are found
  name_found = false
  what_it_does_found = false
  input_parameters_found = false
  policy_actions_found = false
  prerequisites_found = false
  supported_clouds_found = false
  cost_found = false

  file_lines.each_with_index do |line, index|
    name_found = true if index == 0 && line.start_with?("# ")
    what_it_does_found = true if line.start_with?("## What It Does")
    input_parameters_found = true if line.start_with?("## Input Parameters")
    policy_actions_found = true if line.start_with?("## Policy Actions")
    prerequisites_found = true if line.start_with?("## Prerequisites")
    supported_clouds_found = true if line.start_with?("## Supported Clouds")
    cost_found = true if line.strip == "## Cost"
  end

  fail_message += "```# Policy Name```\n" unless name_found
  fail_message += "```## What It Does```\n" unless what_it_does_found
  fail_message += "```## Input Parameters```\n" unless input_parameters_found
  fail_message += "```## Policy Actions```\n" unless policy_actions_found
  fail_message += "```## Prerequisites```\n" unless prerequisites_found
  fail_message += "```## Supported Clouds```\n" unless supported_clouds_found
  fail_message += "```## Cost```\n" unless cost_found

  fail_message = "[[Info](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md#readmemd)] README.md is missing required sections. Please make sure the following sections exist and are indicated with the below markdown. Spelling, spacing, and capitalization should conform to the below:\n\n" + fail_message unless fail_message.empty?

  return false if fail_message.empty?
  fail_message.strip
end

### Out of order README Sections
# Verify that README file has the various sections in the correct order
def readme_sections_out_of_order?(file, file_lines)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing whether README file sections are in the correct order..."

  fail_message = ""

  # Flags for whether sections are found
  name_found = false
  what_it_does_found = false
  how_it_works_found = false
  policy_savings_found = false
  input_parameters_found = false
  policy_actions_found = false
  prerequisites_found = false
  supported_clouds_found = false
  cost_found = false

  what_it_does_raised = false
  how_it_works_raised = false
  policy_savings_raised = false
  input_parameters_raised = false
  policy_actions_raised = false
  prerequisites_raised = false
  supported_clouds_raised = false
  cost_raised = false

  file_lines.each_with_index do |line, index|
    line_number = index + 1

    name_found = true if index == 0 && line.start_with?("# ")
    what_it_does_found = true if line.start_with?("## What It Does")
    how_it_works_found = true if line.start_with?("## How It Works")
    policy_savings_found = true if line.start_with?("### Policy Savings Details")
    input_parameters_found = true if line.start_with?("## Input Parameters")
    policy_actions_found = true if line.start_with?("## Policy Actions")
    prerequisites_found = true if line.start_with?("## Prerequisites")
    supported_clouds_found = true if line.start_with?("## Supported Clouds")
    cost_found = true if line.strip == "## Cost"

    if !what_it_does_raised && what_it_does_found && !name_found
      fail_message += "Line #{line_number}: What It Does out of order.\n"
      what_it_does_raised = true
    end

    if !how_it_works_raised && how_it_works_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number}: How It Works out of order.\n"
      how_it_works_raised = true
    end

    if !policy_savings_raised && policy_savings_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number}: Policy Savings Details out of order.\n"
      policy_savings_raised = true
    end

    if !input_parameters_raised && input_parameters_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number}: Input Parameters out of order.\n"
      input_parameters_raised = true
    end

    if !policy_actions_raised && policy_actions_found && (!name_found || !what_it_does_found || !input_parameters_found)
      fail_message += "Line #{line_number}: Policy Actions out of order.\n"
      policy_actions_raised = true
    end

    if !prerequisites_raised && prerequisites_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found)
      fail_message += "Line #{line_number}: Prerequisites out of order.\n"
      prerequisites_raised = true
    end

    if !supported_clouds_raised && supported_clouds_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found || !prerequisites_found)
      fail_message += "Line #{line_number}: Supported Clouds out of order.\n"
      supported_clouds_raised = true
    end

    if !cost_raised && cost_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found || !prerequisites_found)
      fail_message += "Line #{line_number}: Cost out of order.\n"
      cost_raised = true
    end
  end

  fail_message = "[[Info](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md#readmemd)] README.md sections are out of order. Sections should be in the following order: Policy Name, What It Does, How It Works, Policy Savings Details, Input Parameters, Policy Actions, Prerequisites, Supported Clouds, Cost\n\n" + fail_message unless fail_message.empty?

  return false if fail_message.empty?
  fail_message.strip
end

# Footnote symbols used in permission lists
CREDENTIAL_FOOTNOTE_SYMBOLS = ["*", "\u2020", "\u2021", "\u00a7", "\u2016", "\u00b6"].freeze

# Helper: validates the permission list within a credential section of a README.
# permission_text  - array of lines collected for this provider's credential section
# permission_line  - line number of the first line of permission_text (for error reporting)
# perm_tester      - regex that each permission item string must match
# provider_name    - e.g. "AWS", "Azure", "Google", "Flexera" (used in error messages)
# examples         - array of example permission strings shown in error messages
# skip_list_check  - when true, skip the "no permission list found" error (Alibaba case)
# Returns a fail_message fragment (empty string if no issues found).
def validate_permission_list(permission_text, permission_line, perm_tester, provider_name, examples, skip_list_check: false)
  fail_message = ""
  footnote_symbols = CREDENTIAL_FOOTNOTE_SYMBOLS.each_with_object({}) { |sym, h| h[sym] = false }
  permission_list_found = 0

  permission_text.each_with_index do |line, index|
    line_number = index + permission_line

    permission_list_found = 1 if index == 1 && line.start_with?("  - ")

    if permission_list_found == 1
      if !line.start_with?("  - ")
        permission_list_found = 2
      else
        CREDENTIAL_FOOTNOTE_SYMBOLS.each { |sym| footnote_symbols[sym] = true if line.strip.end_with?(sym) }

        permission_action = line.split("  - ")[1]
        if permission_action.nil? || !permission_action.match?(perm_tester)
          fail_message += "Line #{line_number}: #{provider_name} permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
          examples.each_with_index { |ex, i| fail_message += "```#{ex}```\n"; fail_message += "\n" if i == examples.length - 1 }
        end
      end
    end
  end

  footnote_symbols.each do |symbol, found|
    next unless found

    if symbol == "*"
      unless permission_text.any? { |l| l.strip.start_with?("\\*") }
        fail_message += "Permission list contains a permission with an asterisk (*), but no corresponding footnote explaining it. Please add a footnote starting with `  \\* ` like so:\n\n"
        fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
      end
    else
      unless permission_text.any? { |l| l.strip.start_with?(symbol) }
        fail_message += "Permission list contains a permission with a #{symbol} symbol, but no corresponding footnote explaining it. Please add a footnote starting with `  #{symbol} ` like so:\n\n"
        fail_message += "```  #{symbol} Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
      end
    end
  end

  if permission_list_found == 0 && !skip_list_check
    fail_message += "#{provider_name} permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the #{provider_name} permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
    examples.each_with_index { |ex, i| fail_message += "```#{ex}```\n"; fail_message += "\n" if i == examples.length - 1 }
  end

  fail_message
end

### README Credentials formatting
# Verify that README file has credentials in the proper formatting
def readme_invalid_credentials?(file, file_lines)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing whether README file has properly formatted credentials..."

  fail_message = ""

  prereq_line_number = -100

  aws_policy = false
  azure_policy = false
  google_policy = false

  aws_permission_line = nil
  azure_permission_line = nil
  google_permission_line = nil
  flexera_permission_line = nil

  aws_permission_text = []
  azure_permission_text = []
  google_permission_text = []
  flexera_permission_text = []

  aws_permission_scanning = false
  azure_permission_scanning = false
  google_permission_scanning = false
  flexera_permission_scanning = false

  credential_footnote = false

  file_lines.each_with_index do |line, index|
    line_number = index + 1
    expected_credential_footer = "The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers."
    credential_footnote = true if line.start_with?(expected_credential_footer)

    aws_policy = true if (line.include?("AWS") || line.include?("aws") || line.include?("Alibaba") || line.include?("alibaba")) && (line.include?("Credential") || line.include?("credential"))
    azure_policy = true if (line.include?("Azure") || line.include?("azure")) && (line.include?("Credential") || line.include?("credential")) && !line.include?("China") && !line.include?("china") && !line.include?("Graph") && !line.include?("graph")
    google_policy = true if (line.include?("Google") || line.include?("google") || line.include?("GCP") || line.include?("gcp")) && (line.include?("Credential") || line.include?("credential"))

    # Description check
    prereq_line_number = line_number if line.start_with?("## Prerequisites")

    if line_number == prereq_line_number + 2
      expected_credential_message = "This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s)."
      unless line.start_with?(expected_credential_message)
        fail_message += "Line #{line_number}: README has invalid description for credentials section or description is not correctly located two lines below `## Prerequisites`. Credentials section should contain the following description text before the credential list:\n\n"
        fail_message += "```"+expected_credential_message+"```\n\n"
      end
    end

    if line.start_with?("The [Provider-Specific Credentials") || (line.start_with?("#") && (aws_permission_scanning || azure_permission_scanning || google_permission_scanning || flexera_permission_scanning))
      aws_permission_scanning = false
      azure_permission_scanning = false
      google_permission_scanning = false
      flexera_permission_scanning = false

      aws_permission_stop_scanning = true
      azure_permission_stop_scanning = true
      google_permission_stop_scanning = true
      flexera_permission_stop_scanning = true
    end

    aws_permission_scanning = false if line.start_with?("- [") && (!line.include?("AWS") && !line.include?("aws") && !line.include?("Alibaba") && !line.include?("alibaba"))
    aws_permission_scanning = false if azure_permission_scanning || google_permission_scanning || flexera_permission_scanning
    aws_permission_scanning = true if !line.start_with?("This Policy Template uses [Credentials]") && !aws_permission_stop_scanning && !aws_permission_scanning && prereq_line_number > 0 && (line.include?("[**AWS") || line.include?("[**aws") || line.include?("[**Alibaba") || line.include?("[**alibaba"))
    aws_permission_line = line_number if !aws_permission_line && aws_permission_scanning
    aws_permission_text << line if aws_permission_scanning

    azure_permission_scanning = false if line.start_with?("- [") && (!line.include?("Azure") && !line.include?("azure"))
    azure_permission_scanning = false if aws_permission_scanning || google_permission_scanning || flexera_permission_scanning
    azure_permission_scanning = true if !line.start_with?("This Policy Template uses [Credentials]") && !azure_permission_stop_scanning && !azure_permission_scanning && prereq_line_number > 0 && (line.include?("[**Azure") || line.include?("[**azure")) && !line.include?("Azure China")
    azure_permission_line = line_number if !azure_permission_line && azure_permission_scanning
    azure_permission_text << line if azure_permission_scanning

    google_permission_scanning = false if line.start_with?("- [") && (!line.include?("Google Cloud Credential") && !line.include?("Google Cloud Credential"))
    google_permission_scanning = false if aws_permission_scanning || azure_permission_scanning || flexera_permission_scanning
    google_permission_scanning = true if !line.start_with?("This Policy Template uses [Credentials]") && !google_permission_stop_scanning && !google_permission_scanning && prereq_line_number > 0 && (line.include?("[**Google") || line.include?("[**google"))
    google_permission_line = line_number if !google_permission_line && google_permission_scanning
    google_permission_text << line if google_permission_scanning

    flexera_permission_scanning = false if line.start_with?("- [") && (!line.include?("Flexera") && !line.include?("flexera"))
    flexera_permission_scanning = false if aws_permission_scanning || azure_permission_scanning || google_permission_scanning
    flexera_permission_scanning = true if !line.start_with?("This Policy Template uses [Credentials]") && !flexera_permission_stop_scanning && !flexera_permission_scanning && prereq_line_number > 0 && (line.include?("[**Flexera") || line.include?("[**flexera")) && !line.include?("ITAM") && (!line.include?("AWS") && !line.include?("aws")) && (!line.include?("Azure") && !line.include?("azure")) && (!line.include?("Google") && !line.include?("google")) && !file.start_with?("saas/fsm/")
    flexera_permission_line = line_number if !flexera_permission_line && flexera_permission_scanning
    flexera_permission_text << line if flexera_permission_scanning
  end

  unless credential_footnote
    fail_message += "Permissions section missing footnote. Please make sure the following footnote is at the end of the permissions section of the README:\n\n"
    fail_message += "```The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.```\n\n"
  end

  if aws_policy && !aws_permission_line
    fail_message += "AWS permissions missing or incorrectly formatted. Please make sure AWS permissions begin with a list item like the following:\n\n"
    fail_message += "```- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:```\n\n"
  end

  if azure_policy && !azure_permission_line
    fail_message += "Azure permissions missing or incorrectly formatted. Please make sure Azure permissions begin with a list item like the following:\n\n"
    fail_message += "```- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:```\n\n"
  end

  if google_policy && !google_permission_line
    fail_message += "Google permissions missing or incorrectly formatted. Please make sure Google permissions begin with a list item like the following:\n\n"
    fail_message += "```- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:```\n\n"
  end

  if aws_permission_line
    aws_perm_tester = /`[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*:[a-zA-Z0-9]+`(?:[\*\u2020\u2021\u00a7\u2016\u00b6]+)?$/
    aws_examples = [
      "  - `rds:DeleteDBSnapshot`*",
      "  - `ec2:TerminateInstances`\u2020",
      "  - `sts:GetCallerIdentity` ",
      "  - `cloudtrail:LookupEvents` "
    ]
    is_alibaba = aws_permission_text[0].start_with?("- [**Alibaba Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*)")

    unless aws_permission_text[0].start_with?("- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:") || is_alibaba
      fail_message += "Line #{aws_permission_line}: AWS permission statement does not use the standard text. Please make sure AWS permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:```\n\n"
    end

    fail_message += validate_permission_list(aws_permission_text, aws_permission_line, aws_perm_tester, "AWS", aws_examples, skip_list_check: is_alibaba)
  end

  if azure_permission_line
    azure_perm_tester = /^`Microsoft\.(?:[a-zA-Z]+|\*)\/(?:[a-zA-Z]+|\*)\/(?:[a-zA-Z]+|\*)(?:\/(?:[a-zA-Z]+|\*))*`(?:[\*\u2020\u2021\u00a7\u2016\u00b6]+)?$/
    azure_examples = [
      "  - `Microsoft.Compute/snapshots/delete`*",
      "  - `Microsoft.Compute/snapshots/read` ",
      "  - `Microsoft.Insights/metrics/read` "
    ]

    unless azure_permission_text[0].start_with?("- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:") || azure_permission_text[0].start_with?("- [**Azure Storage Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure) (*provider=azure_storage*)")
      fail_message += "Line #{azure_permission_line}: Azure permission statement does not use the standard text. Please make sure Azure permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:```\n\n"
    end

    fail_message += validate_permission_list(azure_permission_text, azure_permission_line, azure_perm_tester, "Azure", azure_examples)
  end

  if google_permission_line
    google_perm_tester = /^`[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+(?:\.[a-zA-Z]+)*`(?:[\*\u2020\u2021\u00a7\u2016\u00b6]+)?$/
    google_examples = [
      "  - `resourcemanager.projects.get`*",
      "  - `recommender.computeInstanceMachineTypeRecommendations.list`\u2020",
      "  - `compute.regions.list` ",
      "  - `billing.resourceCosts.get` "
    ]

    unless google_permission_text[0].start_with?("- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:")
      fail_message += "Line #{google_permission_line}: Google permission statement does not use the standard text. Please make sure Google permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:```\n\n"
    end

    fail_message += validate_permission_list(google_permission_text, google_permission_line, google_perm_tester, "Google", google_examples)
  end

  if flexera_permission_line
    flexera_perm_tester = /^`[a-zA-Z0-9\-_\.]+`(?:[\*\u2020\u2021\u00a7\u2016\u00b6]+)?$/
    flexera_examples = [
      "  - `billing_center_viewer`*"
    ]

    unless flexera_permission_text[0].start_with?("- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:")
      fail_message += "Line #{flexera_permission_line}: Flexera permission statement does not use the standard text. Please make sure Flexera permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:```\n\n"
    end

    fail_message += validate_permission_list(flexera_permission_text, flexera_permission_line, flexera_perm_tester, "Flexera", flexera_examples)
  end

  fail_message = "[[Info](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md#prerequisites)] README.md has problems with how credential permissions are presented:\n\n" + fail_message unless fail_message.empty?

  return false if fail_message.empty?
  fail_message.strip
end
