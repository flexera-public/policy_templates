require 'rubygems'
require 'json'
require 'fileutils'
require 'octokit'
require 'uri'
require 'time'

# Configure connection to Github API
repo_name = "flexera-public/policy_templates"
branch = "master"
github_api_token = ENV["GITHUB_API_TOKEN"]
github_client = Octokit::Client.new(access_token: github_api_token)
github_client.auto_paginate = true

# Gather list of PRs via API and filter for ones merged into master.
# Also sort the list by date with the most recent PRs coming first
merged_pull_requests = github_client.pull_requests(repo_name, state: 'closed').select do |pr|
  pr.merged_at && pr.base.ref == 'master'
end.sort_by(&:merged_at).reverse

# Convert the API results into a simple object
pr_list = merged_pull_requests.map do |pr|
  {
    number: pr.number,
    title: pr.title,
    description: pr.body,
    labels: pr.labels.map(&:name),
    href: pr.html_url,
    created_at: pr.created_at,
    merged_at: pr.merged_at,
    modified_files: github_client.pull_request_files(repo_name, pr.number).map(&:filename)
  }
end

# Construct final object
merged_prs = { "merged_prs": pr_list }

# Write the output JSON file
File.open('data/change_history/change_history.json', 'w') {
  |file| file.write(JSON.pretty_generate(merged_prs) + "\n")
}

# Generate the HISTORY.md from the same data
# Only include PRs that actually modified policies
active_list_text = File.read("data/active_policy_list/active_policy_list.json")
active_list_json = JSON.parse(active_list_text)
active_policy_list = active_list_json[:policies]

policy_pr_list = pr_list.select { |pr| pr[:modified_files].any? { |file| file.match?(/\.pt\z/) } }.slice(0, 100)

File.open('HISTORY.md', 'w') do |file|
  file.puts "# #{repo_name} Policy Change History\n\n"
  file.puts "## Description\n\n"
  file.puts "This document contains the last 100 policy template merges for the #{repo_name} repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.\n\n"
  file.puts "## History\n\n"

  policy_pr_list.each do |pr|
    policy_name = "Not displayed due to PR with > 5 policies or no published policies. Please see [Github Pull Request](#{pr[:href]}) for these details."

    if pr[:modified_files].length <= 10
      modified_policies = []

      pr[:modified_files].each do |policy|
        active_entry = active_policy_list.find { |policy| policy[:file_name] == policy }
        modified_policies << active_entry if active_entry
      end

      if modified_policies.length <= 5
        policy_name = modified_policies.map do |policy| do
          "[#{policy[:name]}](https://github.com/flexera-public/policy_templates/tree/master/#{policy[:readme]})"
        end.join(", ")
      end
    end

    description = ""

    pr[:description].each_line do |line|
      if !line.include?("### Description") && !line.include?("### Contribution Check List") && !line.include?("New functionality has been documented in the README if applicable") && !line.include?("New functionality includes testing.") && !line.include?("New functionality has been documented in the README if applicable") && !line.include?("New functionality has been documented in CHANGELOG.MD")
        description += "> #{line.strip}\n"
      end
    end

    file.puts "### PR [##{pr[:number]}](#{pr[:href]}): #{pr[:title]}\n\n"
    file.puts "#### Description\n\n"
    file.puts "#{description.strip}\n\n"
    file.puts "#### Metadata\n\n"
    file.puts "- **Policies**: #{policy_name}\n"
    file.puts "- **Merged At**: #{pr[:merged_at]}\n"
    file.puts "\n---\n\n"
  end
end
