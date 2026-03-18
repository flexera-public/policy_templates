# DangerFile README Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: README
###############################################################################

### Deprecated README test
# Utility method. Returns true if README is for a deprecated policy
def readme_deprecated?(file, file_lines)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing whether README file is deprecated..."

  file_lines.each do |line|
    return true if line.start_with?("## Deprecated")
  end

  return false
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

  fail_message += "```# Policy Name```\n" if !name_found
  fail_message += "```## What It Does```\n" if !what_it_does_found
  fail_message += "```## Input Parameters```\n" if !input_parameters_found
  fail_message += "```## Policy Actions```\n" if !policy_actions_found
  fail_message += "```## Prerequisites```\n" if !prerequisites_found
  fail_message += "```## Supported Clouds```\n" if !supported_clouds_found
  fail_message += "```## Cost```\n" if !cost_found

  fail_message = "[[Info](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md#readmemd)] README.md is missing required sections. Please make sure the following sections exist and are indicated with the below markdown. Spelling, spacing, and capitalization should conform to the below:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
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
      fail_message += "Line #{line_number.to_s}: What It Does out of order.\n"
      what_it_does_raised = true
    end

    if !how_it_works_raised && how_it_works_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number.to_s}: How It Works out of order.\n"
      how_it_works_raised = true
    end

    if !policy_savings_raised && policy_savings_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number.to_s}: Policy Savings Details out of order.\n"
      policy_savings_raised = true
    end

    if !input_parameters_raised && input_parameters_found && (!name_found || !what_it_does_found)
      fail_message += "Line #{line_number.to_s}: Input Parameters out of order.\n"
      input_parameters_raised = true
    end

    if !policy_actions_raised && policy_actions_found && (!name_found || !what_it_does_found || !input_parameters_found)
      fail_message += "Line #{line_number.to_s}: Policy Actions out of order.\n"
      policy_actions_raised = true
    end

    if !prerequisites_raised && prerequisites_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found)
      fail_message += "Line #{line_number.to_s}: Prerequisites out of order.\n"
      prerequisites_raised = true
    end

    if !supported_clouds_raised && supported_clouds_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found || !prerequisites_found)
      fail_message += "Line #{line_number.to_s}: Supported Clouds out of order.\n"
      supported_clouds_raised = true
    end

    if !cost_raised && cost_found && (!name_found || !what_it_does_found || !input_parameters_found || !policy_actions_found || !prerequisites_found)
      fail_message += "Line #{line_number.to_s}: Cost out of order.\n"
      cost_raised = true
    end
  end

  fail_message = "[[Info](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md#readmemd)] README.md sections are out of order. Sections should be in the following order: Policy Name, What It Does, How It Works, Policy Savings Details, Input Parameters, Policy Actions, Prerequisites, Supported Clouds, Cost\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
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
      if !line.start_with?(expected_credential_message)
        fail_message += "Line #{line_number.to_s}: README has invalid description for credentials section or description is not correctly located two lines below `## Prerequisites`. Credentials section should contain the following description text before the credential list:\n\n"
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

  if !credential_footnote
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
    aws_json_tester = /^\s{2}```json\n\s{2}\{\n\s{6}"Version": "2012-10-17",\n\s{6}"Statement": \[\n\s{10}\{\n\s{14}"Effect": "Allow",\n\s{14}"Action": \[\n[\s\S]*?\n\s{10}\}\n\s{6}\]\n\s{2}\}\n\s{2}```$/

    # JSON Test currently disabled pending decision on whether to include this in READMEs going forward

    # if !readme_text.match?(aws_json_tester)
    #   fail_message += "AWS permission JSON example missing or formatted incorrectly. JSON example should be formatted [like so](https://raw.githubusercontent.com/flexera-public/policy_templates/master/.dangerfile/examples/AWS_PERMISSION_JSON.md).\n\n"
    # end

    if !aws_permission_text[0].start_with?("- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:") && !aws_permission_text[0].start_with?("- [**Alibaba Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*)")
      fail_message += "Line #{aws_permission_line.to_s}: AWS permission statement does not use the standard text. Please make sure AWS permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:```\n\n"
    end

    aws_perm_tester = /`[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*:[a-zA-Z0-9]+`(?:[\*\u2020\u2021\u00a7\u2016\u00b6]+)?$/

    # Hash to track the presence of each footnote symbol in the permission list
    footnote_symbols = { "*" => false,  "†" => false, "‡" => false, "§" => false, "‖" => false, "¶" => false }
    permission_list_found = 0

    aws_permission_text.each_with_index do |line, index|
      line_number = index + aws_permission_line

      permission_list_found = 1 if index == 1 && line.start_with?("  - ")

      if permission_list_found == 1
        if !line.start_with?("  - ")
          permission_list_found = 2
        else
          footnote_symbols["*"] = true if line.strip.end_with?("*")
          footnote_symbols["†"] = true if line.strip.end_with?("\u2020")
          footnote_symbols["‡"] = true if line.strip.end_with?("\u2021")
          footnote_symbols["§"] = true if line.strip.end_with?("\u00a7")
          footnote_symbols["‖"] = true if line.strip.end_with?("\u2016")
          footnote_symbols["¶"] = true if line.strip.end_with?("\u00b6")

          permission_action = line.split("  - ")[1]

          if permission_action.nil? || !permission_action.match?(aws_perm_tester)
            fail_message += "Line #{line_number.to_s}: AWS permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
            fail_message += "```  - `rds:DeleteDBSnapshot`*```\n"
            fail_message += "```  - `ec2:TerminateInstances`†```\n"
            fail_message += "```  - `sts:GetCallerIdentity` ```\n"
            fail_message += "```  - `cloudtrail:LookupEvents` ```\n\n"
          end
        end
      end
    end

    # Check for missing footnotes for any symbols that were found in the permissions list
    footnote_symbols.each do |symbol, found|
      next unless found # Only check if the symbol was found in the permission list

      # Search for corresponding footnote explanation
      if symbol == "*"
        if !aws_permission_text.any? { |line| line.strip.start_with?("\\*") }
          fail_message += "Permission list contains a permission with an asterisk (*), but no corresponding footnote explaining it. Please add a footnote starting with `  \\* ` like so:\n\n"
          fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      else
        if !aws_permission_text.any? { |line| line.strip.start_with?(symbol) }
          fail_message += "Permission list contains a permission with a #{symbol} symbol, but no corresponding footnote explaining it. Please add a footnote starting with `  #{symbol} ` like so:\n\n"
          fail_message += "```  #{symbol} Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      end
    end

    # Check if no permission list was found
    if permission_list_found == 0 && !aws_permission_text[0].start_with?("- [**Alibaba Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*)")
      fail_message += "AWS permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the AWS permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
      fail_message += "```  - `rds:DeleteDBSnapshot`*```\n"
      fail_message += "```  - `ec2:TerminateInstances`†```\n"
      fail_message += "```  - `sts:GetCallerIdentity` ```\n"
      fail_message += "```  - `cloudtrail:LookupEvents` ```\n\n"
    end
  end

  if azure_permission_line
    if !azure_permission_text[0].start_with?("- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:") && !azure_permission_text[0].start_with?("- [**Azure Storage Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure) (*provider=azure_storage*)")
      fail_message += "Line #{azure_permission_line.to_s}: Azure permission statement does not use the standard text. Please make sure Azure permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:```\n\n"
    end

    azure_perm_tester = /^`Microsoft\.(?:[a-zA-Z]+|\*)\/(?:[a-zA-Z]+|\*)\/(?:[a-zA-Z]+|\*)(?:\/(?:[a-zA-Z]+|\*))*`(?:[\*\u2020\u2021\u00a7\u2016\u00b6]+)?$/

    # Hash to track the presence of each footnote symbol in the permission list
    footnote_symbols = { "*" => false,  "†" => false, "‡" => false, "§" => false, "‖" => false, "¶" => false }
    permission_list_found = 0

    azure_permission_text.each_with_index do |line, index|
      line_number = index + azure_permission_line

      permission_list_found = 1 if index == 1 && line.start_with?("  - ")

      if permission_list_found == 1
        if !line.start_with?("  - ")
          permission_list_found = 2
        else
          footnote_symbols["*"] = true if line.strip.end_with?("*")
          footnote_symbols["†"] = true if line.strip.end_with?("\u2020")
          footnote_symbols["‡"] = true if line.strip.end_with?("\u2021")
          footnote_symbols["§"] = true if line.strip.end_with?("\u00a7")
          footnote_symbols["‖"] = true if line.strip.end_with?("\u2016")
          footnote_symbols["¶"] = true if line.strip.end_with?("\u00b6")

          permission_action = line.split("  - ")[1]
          if permission_action.nil? || !permission_action.match?(azure_perm_tester)
            fail_message += "Line #{line_number.to_s}: Azure permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
            fail_message += "```  - `Microsoft.Compute/snapshots/delete`*```\n"
            fail_message += "```  - `Microsoft.Compute/snapshots/read` ```\n"
            fail_message += "```  - `Microsoft.Insights/metrics/read` ```\n\n"
          end
        end
      end
    end

    # Check for missing footnotes for any symbols that were found in the permissions list
    footnote_symbols.each do |symbol, found|
      next unless found # Only check if the symbol was found in the permission list

      # Search for corresponding footnote explanation
      if symbol == "*"
        if !azure_permission_text.any? { |line| line.strip.start_with?("\\*") }
          fail_message += "Permission list contains a permission with an asterisk (*), but no corresponding footnote explaining it. Please add a footnote starting with `  \\* ` like so:\n\n"
          fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      else
        if !azure_permission_text.any? { |line| line.strip.start_with?(symbol) }
          fail_message += "Permission list contains a permission with a #{symbol} symbol, but no corresponding footnote explaining it. Please add a footnote starting with `  #{symbol} ` like so:\n\n"
          fail_message += "```  #{symbol} Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      end
    end

    # Check if no permission list was found
    if permission_list_found == 0
      fail_message += "Azure permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the Azure permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
      fail_message += "```  - `Microsoft.Compute/snapshots/delete`*```\n"
      fail_message += "```  - `Microsoft.Compute/snapshots/read` ```\n"
      fail_message += "```  - `Microsoft.Insights/metrics/read` ```\n\n"
    end
  end

  if google_permission_line
    if !google_permission_text[0].start_with?("- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:")
      fail_message += "Line #{google_permission_line.to_s}: Google permission statement does not use the standard text. Please make sure Google permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:```\n\n"
    end

    google_perm_tester = /^`[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+(?:\.[a-zA-Z]+)*`(?:[\*\u2020\u2021\u00a7\u2016\u00b6]+)?$/

    # Hash to track the presence of each footnote symbol in the permission list
    footnote_symbols = { "*" => false,  "†" => false, "‡" => false, "§" => false, "‖" => false, "¶" => false }
    permission_list_found = 0

    google_permission_text.each_with_index do |line, index|
      line_number = index + google_permission_line

      permission_list_found = 1 if index == 1 && line.start_with?("  - ")

      if permission_list_found == 1
        if !line.start_with?("  - ")
          permission_list_found = 2
        else
          footnote_symbols["*"] = true if line.strip.end_with?("*")
          footnote_symbols["†"] = true if line.strip.end_with?("\u2020")
          footnote_symbols["‡"] = true if line.strip.end_with?("\u2021")
          footnote_symbols["§"] = true if line.strip.end_with?("\u00a7")
          footnote_symbols["‖"] = true if line.strip.end_with?("\u2016")
          footnote_symbols["¶"] = true if line.strip.end_with?("\u00b6")

          if !line.split("  - ")[1].match?(google_perm_tester)
            fail_message += "Line #{line_number.to_s}: Google permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
            fail_message += "```  - `resourcemanager.projects.get`*```\n"
            fail_message += "```  - `recommender.computeInstanceMachineTypeRecommendations.list`†```\n"
            fail_message += "```  - `compute.regions.list` ```\n"
            fail_message += "```  - `billing.resourceCosts.get` ```\n\n"
          end
        end
      end
    end

    # Check for missing footnotes for any symbols that were found in the permissions list
    footnote_symbols.each do |symbol, found|
      next unless found # Only check if the symbol was found in the permission list

      # Search for corresponding footnote explanation
      if symbol == "*"
        if !google_permission_text.any? { |line| line.strip.start_with?("\\*") }
          fail_message += "Permission list contains a permission with an asterisk (*), but no corresponding footnote explaining it. Please add a footnote starting with `  \\* ` like so:\n\n"
          fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      else
        if !google_permission_text.any? { |line| line.strip.start_with?(symbol) }
          fail_message += "Permission list contains a permission with a #{symbol} symbol, but no corresponding footnote explaining it. Please add a footnote starting with `  #{symbol} ` like so:\n\n"
          fail_message += "```  #{symbol} Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      end
    end

    # Check if no permission list was found
    if permission_list_found == 0
      fail_message += "Google permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the Google permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
      fail_message += "```  - `resourcemanager.projects.get`*```\n"
      fail_message += "```  - `recommender.computeInstanceMachineTypeRecommendations.list`†```\n"
      fail_message += "```  - `compute.regions.list` ```\n"
      fail_message += "```  - `billing.resourceCosts.get` ```\n\n"
    end
  end

  if flexera_permission_line
    if !flexera_permission_text[0].start_with?("- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:")
      fail_message += "Line #{flexera_permission_line.to_s}: Flexera permission statement does not use the standard text. Please make sure Flexera permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:```\n\n"
    end

    flexera_perm_tester = /^`[a-zA-Z0-9\-_\.]+`(?:[\*\u2020\u2021\u00a7\u2016\u00b6]+)?$/

    # Hash to track the presence of each footnote symbol in the permission list
    footnote_symbols = { "*" => false,  "†" => false, "‡" => false, "§" => false, "‖" => false, "¶" => false }
    permission_list_found = 0

    flexera_permission_text.each_with_index do |line, index|
      line_number = index + flexera_permission_line

      permission_list_found = 1 if index == 1 && line.start_with?("  - ")

      if permission_list_found == 1
        if !line.start_with?("  - ")
          permission_list_found = 2
        else
          footnote_symbols["*"] = true if line.strip.end_with?("*")
          footnote_symbols["†"] = true if line.strip.end_with?("\u2020")
          footnote_symbols["‡"] = true if line.strip.end_with?("\u2021")
          footnote_symbols["§"] = true if line.strip.end_with?("\u00a7")
          footnote_symbols["‖"] = true if line.strip.end_with?("\u2016")
          footnote_symbols["¶"] = true if line.strip.end_with?("\u00b6")

          if !line.split("  - ")[1].match?(flexera_perm_tester)
            fail_message += "Line #{line_number.to_s}: Flexera permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
            fail_message += "```  - `billing_center_viewer`*```\n\n"
          end
        end
      end
    end

    # Check for missing footnotes for any symbols that were found in the permissions list
    footnote_symbols.each do |symbol, found|
      next unless found # Only check if the symbol was found in the permission list

      # Search for corresponding footnote explanation
      if symbol == "*"
        if !flexera_permission_text.any? { |line| line.strip.start_with?("\\*") }
          fail_message += "Permission list contains a permission with an asterisk (*), but no corresponding footnote explaining it. Please add a footnote starting with `  \\* ` like so:\n\n"
          fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      else
        if !flexera_permission_text.any? { |line| line.strip.start_with?(symbol) }
          fail_message += "Permission list contains a permission with a #{symbol} symbol, but no corresponding footnote explaining it. Please add a footnote starting with `  #{symbol} ` like so:\n\n"
          fail_message += "```  #{symbol} Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      end
    end

    # Check if no permission list was found
    if permission_list_found == 0
      fail_message += "Flexera permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the Flexera permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
      fail_message += "```  - `billing_center_viewer`*```\n\n"
    end
  end

  fail_message = "[[Info](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md#prerequisites)] README.md has problems with how credential permissions are presented:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### README vs. API Call Permission Mismatch
# Compare the permissions listed in the README's Prerequisites section against
# those derived from the policy template's actual API calls.  Results are
# informational: mismatches are flagged as warnings because the derivation is
# automated and best-effort.
# Returns true if derived_perm is covered by any entry in readme_perms, either
# as an exact match or via a wildcard pattern.  A '*' in a README permission
# matches exactly one path segment (e.g. Microsoft.Insights/*/read covers
# Microsoft.Insights/metrics/read but not Microsoft.Insights/a/b/read).
def permission_covered?(derived_perm, readme_perms)
  readme_perms.any? do |readme_perm|
    if readme_perm.include?('*')
      regex = Regexp.new('\A' + Regexp.escape(readme_perm).gsub('\*', '[^/]+') + '\z', Regexp::IGNORECASE)
      regex.match?(derived_perm)
    else
      readme_perm.casecmp?(derived_perm)
    end
  end
end

#
# Relies on /tmp/policy_api_list.json being pre-generated by the CI workflow
# step that runs policy_api_list_generator.py --output-dir /tmp.  Returns false
# immediately when that file is absent (e.g. local Danger runs).
def readme_api_permission_mismatch?(file, file_lines)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing whether README permissions match derived API call permissions..."

  api_list_file = '/tmp/policy_api_list.json'
  return false unless File.exist?(api_list_file)

  begin
    api_data = JSON.parse(File.read(api_list_file))
  rescue JSON::ParserError
    return false
  end

  api_calls = api_data['api_calls']
  return false if api_calls.nil? || api_calls.empty?

  # Find API calls whose policy file lives in the same directory as this README
  readme_dir = File.dirname(file)
  policy_calls = api_calls.select { |c| File.dirname(c['policy_file'].to_s) == readme_dir }
  return false if policy_calls.empty?

  # Collect unique, non-empty derived permissions grouped by cloud provider
  derived_aws   = policy_calls.select { |c| c['api_service'] == 'AWS'   && !c['permission'].to_s.empty? }.map { |c| c['permission'] }.uniq.sort
  derived_azure = policy_calls.select { |c| c['api_service'] == 'Azure' && !c['permission'].to_s.empty? }.map { |c| c['permission'] }.uniq.sort
  derived_gcp   = policy_calls.select { |c| c['api_service'] == 'GCP'   && !c['permission'].to_s.empty? }.map { |c| c['permission'] }.uniq.sort

  return false if derived_aws.empty? && derived_azure.empty? && derived_gcp.empty?

  # Parse permissions listed in the README Prerequisites section
  readme_aws_perms   = []
  readme_azure_perms = []
  readme_gcp_perms   = []

  in_prereqs   = false
  in_aws       = false
  in_azure     = false
  in_gcp       = false
  in_perm_list = false

  file_lines.each do |line|
    in_prereqs = true if line.strip == '## Prerequisites'
    next unless in_prereqs

    # Stop at the next top-level section
    break if line.start_with?('## ') && line.strip != '## Prerequisites'

    # Detect the start of a cloud credential sub-section and reset state
    if line.start_with?('- [**')
      in_perm_list = false
      if line.include?('[**AWS') || line.include?('[**Alibaba')
        in_aws = true;  in_azure = false; in_gcp = false
      elsif line.include?('[**Azure') || line.include?('[**Azure Storage')
        in_aws = false; in_azure = true;  in_gcp = false
      elsif line.include?('[**Google')
        in_aws = false; in_azure = false; in_gcp = true
      else
        in_aws = false; in_azure = false; in_gcp = false
      end
    end

    # Activate permission-list scanning on the first indented list item
    in_perm_list = true  if (in_aws || in_azure || in_gcp) && line.start_with?('  - `')
    # Deactivate when we leave the contiguous indented list
    in_perm_list = false if in_perm_list && !line.start_with?('  - ')
    next unless in_perm_list

    # Extract the backtick-enclosed permission string and strip footnote symbols
    match = line.match(/`([^`]+)`/)
    next unless match

    perm = match[1].gsub(/[†‡§‖¶]+$/, '').strip
    readme_aws_perms   << perm if in_aws
    readme_azure_perms << perm if in_azure
    readme_gcp_perms   << perm if in_gcp
  end

  # Build mismatch lists in both directions
  missing_from_readme  = []
  missing_from_derived = []

  derived_aws.each   { |p| missing_from_readme  << "AWS: `#{p}`"   unless permission_covered?(p, readme_aws_perms) }
  derived_azure.each { |p| missing_from_readme  << "Azure: `#{p}`" unless permission_covered?(p, readme_azure_perms) }
  derived_gcp.each   { |p| missing_from_readme  << "GCP: `#{p}`"   unless permission_covered?(p, readme_gcp_perms) }

  # Wildcard permissions (e.g. Microsoft.Insights/*/read) are intentional and
  # are not expected to appear verbatim in the derived list, so skip them here.
  # Azure RBAC role names (e.g. 'Storage Blob Data Reader') contain neither '/'
  # nor ':' and cannot be matched against derived ARM permission strings; skip them.
  readme_aws_perms.each   { |p| missing_from_derived << "AWS: `#{p}`"   unless p.include?('*') || derived_aws.any?   { |d| d.casecmp?(p) } }
  readme_azure_perms.each { |p| missing_from_derived << "Azure: `#{p}`" unless p.include?('*') || (!p.include?('/') && !p.include?(':')) || derived_azure.any? { |d| d.casecmp?(p) } }
  readme_gcp_perms.each   { |p| missing_from_derived << "GCP: `#{p}`"   unless p.include?('*') || derived_gcp.any?   { |d| d.casecmp?(p) } }

  return false if missing_from_readme.empty? && missing_from_derived.empty?

  warn_message = "[[Info](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md#prerequisites)] Possible mismatch between README permissions and the permissions derived from the policy template's API calls. This check is automated and best-effort — false positives are possible, particularly for action-only permissions, write operations, or API call patterns the analyzer cannot fully resolve. Please review and update the README if needed.\n\n"

  if !missing_from_readme.empty?
    warn_message += "**Derived from API calls but not listed in README:**\n\n"
    missing_from_readme.each { |p| warn_message += "- #{p}\n" }
    warn_message += "\n"
  end

  if !missing_from_derived.empty?
    warn_message += "**Listed in README but not detected in API calls** *(write/delete permissions and action-only permissions are commonly found here)*:\n\n"
    missing_from_derived.each { |p| warn_message += "- #{p}\n" }
    warn_message += "\n"
  end

  return warn_message.strip
end
