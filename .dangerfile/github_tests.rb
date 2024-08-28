# DangerFile Github Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: Github
###############################################################################

### Bad Github PR summary
# Verify that the pull request has properly formatted title
def github_pr_bad_title?(github)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** " + " Testing Github pull request for bad title..."

  fail_message = ""

  pol_matcher = /^POL-\d{1,4} .+$/
  fopts_matcher = /^FOPTS-\d{1,4} .+$/

  if !github.pr_title.match?(pol_matcher) && !github.pr_title.match?(fopts_matcher)
    fail_message = "### **Github Pull Request**\nPull Request has improper title. Title should always begin with the JIRA ticket id, followed by a description, like in the following examples:\n\n"
    fail_message += "POL-123 Add New Feature\n"
    fail_message += "FOPTS-1000 Fixed Bug\n\n"
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Missing Github PR summary
# Verify that the pull request has a summary
def github_pr_missing_summary?(github)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** " + " Testing Github pull request for missing summary..."

  fail_message = ""
  fail_message = "### **Github Pull Request**\nPull Request is missing summary. Please provide a summary of your Pull Request." if github.pr_body.length < 10

  return fail_message.strip if !fail_message.empty?
  return false
end

### Missing Github PR labels
# Verify that the pull request has labels
def github_pr_missing_labels?(github)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** " + " Testing Github pull request for presence of labels..."

  fail_message = ""
  fail_message = "### **Github Pull Request**\nPull Request is missing labels. Please add labels to this Pull Request." if github.pr_labels.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Missing Github PR Ready label
# Verify that the pull request has ready for review label
def github_pr_missing_ready_label?(github)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** " + " Testing Github pull request for READY-FOR-REVIEW label..."

  fail_message = ""
  fail_message = "### **Github Pull Request**\nPull Request is missing `READY-FOR-REVIEW` label. Please add this label if this Pull Request is ready for review.\n\nPlease note that this message may be a false positive if you've added the label after Dangerfile tests were run, since adding labels does not trigger them to run again. In these cases, simply ignore this message." if !github.pr_labels.include?("READY-FOR-REVIEW")

  return fail_message.strip if !fail_message.empty?
  return false
end
