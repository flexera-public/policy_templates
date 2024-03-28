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
policy_pr_list = pr_list.select { |pr| pr[:modified_files].any? { |file| file.match?(/\.pt\z/) } }.slice(0, 200)

File.open('HISTORY.md', 'w') do |file|
  file.puts "# #{repo_name} Change History\n\n"
  file.puts "## Description\n\n"
  file.puts "This document contains the last 200 policy template merges for the #{repo_name} repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 200 policy merges, is also available.\n\n"
  file.puts "## History\n\n"

  policy_pr_list.each do |pr|
    file.puts "### PR [##{pr[:number]}](#{pr[:pr_link]}): #{pr[:title]}\n\n"

    file.puts "#### Description\n\n"
    pr[:description].each_line { |line| file.puts "> #{line}" }

    file.puts "#### Metadata\n\n"

    file.puts "- **Labels**: #{pr[:labels].join(', ')}"
    file.puts "- **Created At**: #{pr[:created_at]}"
    file.puts "- **Merged At**: #{pr[:merged_at]}"

    if pr[:modified_files].length <= 10
      policy_list = pr[:modified_files].select { |file| file.include?(".pt") }.map do |pt_file|
        file_text = File.read(pt_file)
        file_text.split("\n")[0].strip.split('"')[1]
      end

      policy_list_string = policy_list.join(", ")
    else
      policy_list_string = "> 10 policies modified. Please review the [PR on Github](#{pr[:pr_link]}) for the full list."
    end

    file.puts "- **Modified Policies**: #{policy_list_string}"

    file.puts "\n"
  end
end
