# Generate Change History
# This script generates the following files:
# data/change_history/change_history.json: Full history of the repository in JSON format
# HISTORY.md: Human readable history of the last 100 merges that impacted policies

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
  # Omit PRs triggered by this script to avoid an infinite loop
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

# Write the data/change_history/change_history.json file
File.open('data/change_history/change_history.json', 'w') {
  |file| file.write(JSON.pretty_generate(merged_prs) + "\n")
}

# Read the active policy JSON to assist in gathering policy metadata
active_list_text = File.read("data/active_policy_list/active_policy_list.json")
active_list_json = JSON.parse(active_list_text)
active_policy_list = active_list_json["policies"]

# Only include last 100 PRs that actually modified policies and aren't automated
# Initial slice of 1000 is to reduce the workload of the rest of the filtering
policy_pr_list = pr_list.slice(0, 1000).select do |pr|
  pr[:modified_files].any? { |file| file.strip.end_with?(".pt") } && !pr[:title].include?("Update Meta Parent Policy Templates")
end.slice(0, 100)

# Generate the HISTORY.md file
File.open('HISTORY.md', 'w') do |file|
  # Build header
  file.puts "# Published Policy Change History\n\n"
  file.puts "## Description\n\n"
  file.puts "This document contains the last 100 policy template merges for the `#{repo_name}` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.\n\n"
  file.puts "## History\n\n"

  # Build entries for each change
  policy_pr_list.each do |pr|
    # Find labels that indicate the type of change
    labels = []

    if pr[:labels] && pr[:labels].any?
      labels << "New Policy Template" if pr[:labels].include?("NEW POLICY TEMPLATE")
      labels << "Major Update" if pr[:labels].include?("MAJOR UPDATE")
      labels << "Minor Update" if pr[:labels].include?("MINOR UPDATE")
      labels << "Bug Fix" if pr[:labels].include?("BUG FIX")
    end

    # We only display the names if <= 5 published policies were modified
    policy_name = "Not displayed due to PR with > 5 policies. Please see [Github Pull Request](#{pr[:href]}) for these details."

    # Logic to find the names of modified policies and generate links to their readmes
    if pr[:modified_files].length <= 10
      modified_policies = []

      pr[:modified_files].each do |policy|
        active_entry = active_policy_list.find { |active_policy| active_policy["file_name"] == policy }
        modified_policies << active_entry if active_entry

        # If full path is not found in active policy list, search for just the filename
        if !active_entry
          active_entry = active_policy_list.find { |active_policy| active_policy["file_name"].include?(policy.split('/')[-1]) }
          modified_policies << active_entry if active_entry
        end
      end

      if modified_policies.length > 0 && modified_policies.length <= 5
        policy_name = modified_policies.map do |policy|
          "[#{policy["name"]}](https://github.com/flexera-public/policy_templates/tree/master/#{policy["readme"]})"
        end.join(", ")
      end

      # If we found no modified policies that are in the active JSON list, assume they are unpublished
      if modified_policies.length == 0
        policy_name = "Not displayed due to PR with no published policies. Please see [Github Pull Request](#{pr[:href]}) for details about unpublished policies."
      end
    end

    # Clean up the description to remove known extraneous elements for readability
    description = ""

    pr[:description].each_line.with_index do |line, index|
      break if line.include?("Contribution Check List")
      break if line.include?("Link to Example Applied Polic") # Covers singular and plural
      next if line.include?("### Description")
      next if description.empty? && line.strip.empty?

      formatted_line = "> #{line}".strip
      description += "#{formatted_line}\n"
    end

    # Write entry to file
    file.puts "### PR [##{pr[:number]}](#{pr[:href]}): #{pr[:title]}\n\n"
    file.puts "*#{labels.join(", ")}*\n\n" if labels.any?
    file.puts "#### Description\n\n"
    file.puts "#{description.strip}\n\n"
    file.puts "#### Metadata\n\n"
    file.puts "- **Policies**: #{policy_name}\n"
    file.puts "- **Merged At**: #{pr[:merged_at]}\n"
    file.puts "\n---\n\n"
  end
end
