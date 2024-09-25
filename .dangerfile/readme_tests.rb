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

  fail_message = "README.md is missing required sections. Please make sure the following sections exist and are indicated with the below markdown. Spelling, spacing, and capitalization should conform to the below:\n\n" + fail_message if !fail_message.empty?

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

  fail_message = "README.md sections are out of order. Sections should be in the following order: Policy Name, What It Does, How It Works, Policy Savings Details, Input Parameters, Policy Actions, Prerequisites, Supported Clouds, Cost\n\n" + fail_message if !fail_message.empty?

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

    credential_footnote = true if line.start_with?("The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.")

    aws_policy = true if (line.include?("AWS") || line.include?("aws")) && (line.include?("Credential") || line.include?("credential"))
    azure_policy = true if (line.include?("Azure") || line.include?("azure")) && (line.include?("Credential") || line.include?("credential")) && !line.include?("China") && !line.include?("china") && !line.include?("Graph") && !line.include?("graph")
    google_policy = true if (line.include?("Google") || line.include?("google") || line.include?("GCP") || line.include?("gcp")) && (line.include?("Credential") || line.include?("credential"))

    # Description check
    prereq_line_number = line_number if line.start_with?("## Prerequisites")

    if line_number == prereq_line_number + 2
      if !line.start_with?("This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).")
        fail_message += "Line #{line_number.to_s}: README has invalid description for credentials section or description is not correctly located two lines below `## Prerequisites`. Credentials section should contain the following description text before the credential list:\n\n"
        fail_message += "```This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).```\n\n"
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

    aws_permission_scanning = false if line.start_with?("- [") && (!line.include?("AWS") && !line.include?("aws"))
    aws_permission_scanning = false if azure_permission_scanning || google_permission_scanning || flexera_permission_scanning
    aws_permission_scanning = true if !line.start_with?("This Policy Template uses [Credentials]") && !aws_permission_stop_scanning && !aws_permission_scanning && prereq_line_number > 0 && (line.include?("[**AWS") || line.include?("[**aws"))
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
    flexera_permission_scanning = true if !line.start_with?("This Policy Template uses [Credentials]") && !flexera_permission_stop_scanning && !flexera_permission_scanning && prereq_line_number > 0 && (line.include?("[**Flexera") || line.include?("[**flexera")) && (!line.include?("AWS") && !line.include?("aws")) && (!line.include?("Azure") && !line.include?("azure")) && (!line.include?("Google") && !line.include?("google")) && !file.start_with?("saas/fsm/")
    flexera_permission_line = line_number if !flexera_permission_line && flexera_permission_scanning
    flexera_permission_text << line if flexera_permission_scanning
  end

  if !credential_footnote
    fail_message += "Permissions section missing footnote. Please make sure the following footnote is at the end of the permissions section of the README:\n\n"
    fail_message += "```The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.```\n\n"
  end

  if aws_policy && !aws_permission_line
    fail_message += "AWS permissions missing or incorrectly formatted. Please make sure AWS permissions begin with a list item like the following:\n\n"
    fail_message += "```- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:```\n\n"
  end

  if azure_policy && !azure_permission_line
    fail_message += "Azure permissions missing or incorrectly formatted. Please make sure Azure permissions begin with a list item like the following:\n\n"
    fail_message += "```- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:```\n\n"
  end

  if google_policy && !google_permission_line
    fail_message += "Google permissions missing or incorrectly formatted. Please make sure Google permissions begin with a list item like the following:\n\n"
    fail_message += "```- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:```\n\n"
  end

  if aws_permission_line
    aws_json_tester = /^\s{2}```json\n\s{2}\{\n\s{6}"Version": "2012-10-17",\n\s{6}"Statement": \[\n\s{10}\{\n\s{14}"Effect": "Allow",\n\s{14}"Action": \[\n[\s\S]*?\n\s{10}\}\n\s{6}\]\n\s{2}\}\n\s{2}```$/

    # JSON Test currently disabled pending decision on whether to include this in READMEs going forward

    # if !readme_text.match?(aws_json_tester)
    #   fail_message += "AWS permission JSON example missing or formatted incorrectly. JSON example should be formatted [like so](https://raw.githubusercontent.com/flexera-public/policy_templates/master/.dangerfile/examples/AWS_PERMISSION_JSON.md).\n\n"
    # end

    if !aws_permission_text[0].start_with?("- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:")
      fail_message += "Line #{aws_permission_line.to_s}: AWS permission statement does not use the standard text. Please make sure AWS permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:```\n\n"
    end

    aws_perm_tester = /`[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*:[a-zA-Z0-9]+`(?:[\*\u2020\u2021])?$/

    # Hash to track the presence of each footnote symbol in the permission list
    footnote_symbols = { "*" => false,  "†" => false, "‡" => false }

    # footnote_symbol_found = 0
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

          permission_action = line.strip.split(/\s{2}-\s+/)[1]
          if permission_action.nil? || !permission_action.match?(aws_perm_tester)
            fail_message += "Line #{line_number.to_s}: AWS permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
            fail_message += "```  - `rds:DeleteDBSnapshot`*```\n"
            fail_message += "```  - `ec2:TerminateInstances`†```\n"
            fail_message += "```  - `sts:GetCallerIdentity` ```\n"
            fail_message += "```  - `cloudtrail:LookupEvents` ```\n\n"
          end
        end
      end
      # footnote_symbol_found = 2 if footnote_symbol_found == 1 && line.start_with?('  \* ', '  † ', '  ‡ ')
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
          fail_message += "Permission list contains a permission with an #{symbol} symbol, but no corresponding footnote explaining it. Please add a footnote starting with `  #{symbol} ` like so:\n\n"
          fail_message += "```  #{symbol} Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
        end
      end
    end

    # Check if no permission list was found
    if permission_list_found == 0
      fail_message += "AWS permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the AWS permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
      fail_message += "```  - `rds:DeleteDBSnapshot`*```\n"
      fail_message += "```  - `ec2:TerminateInstances`†```\n"
      fail_message += "```  - `sts:GetCallerIdentity` ```\n"
      fail_message += "```  - `cloudtrail:LookupEvents` ```\n\n"
    end

    # if footnote_symbol_found == 1
    #   fail_message += "AWS permission list contains a permission with a footnote symbol (e.g., an asterisk, dagger or crossed dagger) but no footnote explaining why or the footnote is formatted incorrectly. The footnote should indicate what is special about these permissions; in most cases, this will be an explanation that the permission is optional and only needed for policy actions. Please add a footnote that begins with [space][space][backslash][footnote symbol][space] like so:\n\n"
    #   fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
    #   fail_message += "```  ‡ Only required if using Customer Managed KMS Key on Volumes mounted by EC2 Instance(s)```\n\n"
    # end
  end

  if azure_permission_line
    if !azure_permission_text[0].start_with?("- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:")
      fail_message += "Line #{azure_permission_line.to_s}: Azure permission statement does not use the standard text. Please make sure Azure permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:```\n\n"
    end

    azure_perm_tester = /^`Microsoft\.[a-zA-Z]+\/[a-zA-Z]+\/[a-zA-Z]+(?:\/[a-zA-Z]+)*`(?:[\*\u2020\u2021])?$/
    footnote_symbol_found = 0
    permission_list_found = 0

    azure_permission_text.each_with_index do |line, index|
      line_number = index + azure_permission_line

      permission_list_found = 1 if index == 1 && line.start_with?("  - ")

      if permission_list_found == 1
        if !line.start_with?("  - ")
          permission_list_found = 2
        else
          footnote_symbol_found = 1 if line.strip.end_with?("*", "\u2020", "\u2021")

          if !line.split("  - ")[1].match?(azure_perm_tester)
            fail_message += "Line #{line_number.to_s}: Azure permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
            fail_message += "```  - `Microsoft.Compute/snapshots/delete`*```\n"
            fail_message += "```  - `Microsoft.Compute/snapshots/read` ```\n"
            fail_message += "```  - `Microsoft.Insights/metrics/read` ```\n\n"
          end
        end
      end

      footnote_symbol_found = 2 if footnote_symbol_found == 1 && line.start_with?('  \* ', '  † ', '  ‡ ')
    end

    if permission_list_found == 0
      fail_message += "Azure permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the Azure permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
      fail_message += "```  - `Microsoft.Compute/snapshots/delete`*```\n"
      fail_message += "```  - `Microsoft.Compute/snapshots/read` ```\n"
      fail_message += "```  - `Microsoft.Insights/metrics/read` ```\n\n"
    end

    if footnote_symbol_found == 1
      fail_message += "Azure permission list contains a permission with a footnote symbol (e.g., an asterisk, dagger or crossed dagger) but no footnote explaining why or the footnote is formatted incorrectly. The footnote should indicate what is special about these permissions; in most cases, this will be an explanation that the permission is optional and only needed for policy actions. Please add a footnote that begins with [space][space][backslash][footnote symbol][space] like so:\n\n"
      fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n\n"
    end
  end

  if google_permission_line
    if !google_permission_text[0].start_with?("- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:")
      fail_message += "Line #{google_permission_line.to_s}: Google permission statement does not use the standard text. Please make sure Google permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:```\n\n"
    end

    google_perm_tester = /^`[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+(?:\.[a-zA-Z]+)*`(?:[\*\u2020\u2021])?$/
    footnote_symbol_found = 0
    permission_list_found = 0

    google_permission_text.each_with_index do |line, index|
      line_number = index + google_permission_line

      permission_list_found = 1 if index == 1 && line.start_with?("  - ")

      if permission_list_found == 1
        if !line.start_with?("  - ")
          permission_list_found = 2
        else
          footnote_symbol_found = 1 if line.strip.end_with?("*", "\u2020", "\u2021")

          if !line.split("  - ")[1].match?(google_perm_tester)
            fail_message += "Line #{line_number.to_s}: Google permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
            fail_message += "```  - `resourcemanager.projects.get`*```\n"
            fail_message += "```  - `recommender.computeInstanceMachineTypeRecommendations.list`†```\n"
            fail_message += "```  - `compute.regions.list` ```\n"
            fail_message += "```  - `billing.resourceCosts.get` ```\n\n"
          end
        end
      end

      footnote_symbol_found = 2 if footnote_symbol_found == 1 && line.start_with?('  \* ', '  † ', '  ‡ ')
    end

    if permission_list_found == 0
      fail_message += "Google permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the Google permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
      fail_message += "```  - `resourcemanager.projects.get`*```\n"
      fail_message += "```  - `recommender.computeInstanceMachineTypeRecommendations.list`†```\n"
      fail_message += "```  - `compute.regions.list` ```\n"
      fail_message += "```  - `billing.resourceCosts.get` ```\n\n"
    end

    if footnote_symbol_found == 1
      fail_message += "Google permission list contains a permission with a footnote symbol (e.g., an asterisk, dagger or crossed dagger) but no footnote explaining why or the footnote is formatted incorrectly. The footnote should indicate what is special about these permissions; in most cases, this will be an explanation that the permission is optional and only needed for policy actions. Please add a footnote that begins with [space][space][backslash][footnote symbol][space] like so:\n\n"
      fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n"
      fail_message += "```  † Only the permissions needed for the specific recommendations you're looking to produce are required. If using this policy only for idle recommendations, for example, `recommender.computeInstanceMachineTypeRecommendations.list` is not needed.```\n\n"
    end
  end

  if flexera_permission_line
    if !flexera_permission_text[0].start_with?("- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:")
      fail_message += "Line #{flexera_permission_line.to_s}: Flexera permission statement does not use the standard text. Please make sure Flexera permissions begin with the following text followed by a list:\n\n"
      fail_message += "```- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:```\n\n"
    end

    flexera_perm_tester = /^`[a-zA-Z0-9\-_\.]+`(?:[\*\u2020\u2021])?$/
    footnote_symbol_found = 0
    permission_list_found = 0

    flexera_permission_text.each_with_index do |line, index|
      line_number = index + flexera_permission_line

      permission_list_found = 1 if index == 1 && line.start_with?("  - ")

      if permission_list_found == 1
        if !line.start_with?("  - ")
          permission_list_found = 2
        else
          footnote_symbol_found = 1 if line.strip.end_with?("*", "\u2020", "\u2021")

          if !line.split("  - ")[1].match?(flexera_perm_tester)
            fail_message += "Line #{line_number.to_s}: Flexera permission list item formatted incorrectly. Please make sure all list items are formatted like the following examples:\n\n"
            fail_message += "```  - `billing_center_viewer`*```\n\n"
          end
        end
      end

      footnote_symbol_found = 2 if footnote_symbol_found == 1 && line.start_with?('  \* ', '  † ', '  ‡ ')
    end

    if permission_list_found == 0
      fail_message += "Flexera permission list missing or formatted incorrectly. Please ensure there is a list of permissions beneath the Flexera permission statement. Each list item should begin with [space][space][hyphen][space] like so:\n\n"
      fail_message += "```  - `billing_center_viewer`*```\n\n"
    end

    if footnote_symbol_found == 1
      fail_message += "Flexera permission list contains a permission with a footnote symbol (e.g., an asterisk, dagger or crossed dagger) but no footnote explaining why or the footnote is formatted incorrectly. The footnote should indicate what is special about these permissions; in most cases, this will be an explanation that the permission is optional and only needed for policy actions. Please add a footnote that begins with [space][space][backslash][footnote symbol][space] like so:\n\n"
      fail_message += "```  \\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.```\n\n"
    end
  end

  fail_message = "README.md has problems with how credential permissions are presented:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end
