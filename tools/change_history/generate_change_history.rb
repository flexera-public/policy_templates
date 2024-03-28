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
    modified_files: client.pull_request_files(repo_name, pr.number).map(&:filename)
  }
end

# Construct final object
merged_prs = { "merged_prs": pr_list }

# Write the output JSON file to disk
File.open('data/change_history/change_history.json', 'w') {
  |file| file.write(JSON.pretty_generate(merged_prs) + "\n")
}

# Generate the README.md from the same information
File.open('HISTORY.md', 'w') do |file|
  file.puts "# #{repo_name} Change History\n"
  file.puts "## Description\n"
  file.puts "This document contains a full change history of this repository. Changes are sorted by date, with the most recent changes listed first. This functions as a universal changelog file for the entire repository.\n"
  file.puts "## History\n"

  pr_list.each do |pr|
    file.puts "### PR [##{pr[:number]}](#{pr[:pr_link]}): #{pr[:title]}\n"
    file.puts "- **Description**: #{pr[:description]}"
    file.puts "- **Labels**: #{pr[:labels].join(', ')}"
    file.puts "- **Created At**: #{pr[:created_at]}"
    file.puts "- **Merged At**: #{pr[:merged_at]}"
    file.puts "- **Modified Files**:"

    pr[:modified_files].each do |file_name|
      file.puts "  - `#{file_name}`"
    end

    file.puts ""
  end
end
