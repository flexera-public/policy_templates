# DangerFile Github Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: Github
###############################################################################

### Bad Github PR summary
# Verify that the pull request has properly formatted title
def github_pr_bad_title?(github)
  fail_message = ""

  github.pr_title

  fail_message = "**Github Pull Request**\nPull Request is missing summary. Please provide a summary of your Pull Request." if .length < 10

  return fail_message.strip if !fail_message.empty?
  return false
end

### Missing Github PR summary
# Verify that the pull request has a summary
def github_pr_missing_summary?(github)
  fail_message = ""
  fail_message = "**Github Pull Request**\nPull Request is missing summary. Please provide a summary of your Pull Request." if github.pr_body.length < 10

  return fail_message.strip if !fail_message.empty?
  return false
end

### Missing Github PR labels
# Verify that the pull request has labels
def github_pr_missing_labels?(github)
  fail_message = ""
  fail_message = "**Github Pull Request**\nPull Request is missing labels. Please add labels to this Pull Request." if github.pr_labels.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end
