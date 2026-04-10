# DangerFile Github Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: Github
###############################################################################

### Bad Github PR summary
# Verify that the pull request has properly formatted title
def github_pr_bad_title?(github)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing Github pull request for bad title..."

  pol_matcher = /^POL-\d{1,4} .+$/
  fopts_matcher = /^FOPTS-\d{1,4} .+$/
  foaa_matcher = /^FOAA-\d{1,4} .+$/

  return false if github.pr_title.match?(pol_matcher) || github.pr_title.match?(fopts_matcher) || github.pr_title.match?(foaa_matcher)

  fail_message = "### **Github Pull Request**\n[[Info](https://github.com/flexera-public/policy_templates/blob/master/CONTRIBUTING.md#4-make-a-pull-request)] Pull Request has improper title. Title should always begin with the JIRA ticket id, followed by a description, like in the following examples:\n\n"
  fail_message += "POL-123 Add New Feature\n"
  fail_message += "FOPTS-1000 Fixed Bug\n\n"
  fail_message += "FOAA-710 New Policy Template\n\n"
  fail_message.strip
end

### Missing Github PR summary
# Verify that the pull request has a summary
def github_pr_missing_summary?(github)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing Github pull request for missing summary..."
  return "### **Github Pull Request**\n[[Info](https://github.com/flexera-public/policy_templates/blob/master/CONTRIBUTING.md#4-make-a-pull-request)] Pull Request is missing summary. Please provide a summary of your Pull Request." if github.pr_body.length < 10
  false
end

### Missing Github PR labels
# Verify that the pull request has labels
def github_pr_missing_labels?(github)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing Github pull request for presence of labels..."
  return "### **Github Pull Request**\n[[Info](https://github.com/flexera-public/policy_templates/blob/master/CONTRIBUTING.md#4-make-a-pull-request)] Pull Request is missing labels. Please add labels to this Pull Request." if github.pr_labels.empty?
  false
end

### Missing Github PR Ready label
# Verify that the pull request has ready for review label
def github_pr_missing_ready_label?(github)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing Github pull request for READY-FOR-REVIEW label..."
  return "### **Github Pull Request**\n[[Info](https://github.com/flexera-public/policy_templates/blob/master/CONTRIBUTING.md#4-make-a-pull-request)] Pull Request is missing `READY-FOR-REVIEW` label. Please add this label if this Pull Request is ready for review.\n\nPlease note that this message may be a false positive if you've added the label after Dangerfile tests were run, since adding labels does not trigger them to run again. In these cases, simply ignore this message." unless github.pr_labels.include?("READY-FOR-REVIEW")
  false
end
