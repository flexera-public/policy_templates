# Generate Change History
# This script generates the following files:
# data/change_history/change_history.json: Full history of the repository in JSON format
# HISTORY.md: Human readable history of the last 100 merges that impacted policies
#
# The script fetches incrementally: it loads any previously recorded pull requests from
# data/change_history/change_history.json and only asks the Github Search API for pull
# requests merged after the most recent one already on record. This avoids re-fetching and
# re-processing the entire pull request history (thousands of pull requests and growing) on
# every run, which does not scale and risks exhausting the Github API rate limit. Per-pull
# request calls (needed only to list modified files, since the Search API does not return
# them) are now limited to the small number of newly-merged pull requests instead of the
# entire history.
#
# If data/change_history/change_history.json does not exist or cannot be parsed, the script
# falls back to a full historical fetch to bootstrap the file. The Search API caps results at
# 1,000 per query, so it is not suitable for this initial bootstrap; the full Pull Requests API
# is used instead, exactly as this script originally worked.

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

change_history_file = 'data/change_history/change_history.json'

# Converts a Github API pull request (or search result) into the simple object stored in
# data/change_history/change_history.json. Always makes a dedicated call to fetch the list of
# modified files since neither the Search API nor the base pull request payload includes it.
def build_pr_entry(github_client, repo_name, pr, merged_at)
  {
    number: pr.number,
    title: pr.title,
    description: pr.body,
    labels: pr.labels.map(&:name),
    href: pr.html_url,
    created_at: pr.created_at,
    merged_at: merged_at,
    modified_files: github_client.pull_request_files(repo_name, pr.number).map(&:filename)
  }
end

# `merged_at` is a Time object for newly-fetched pull requests but a String once it has been
# through a JSON round trip (i.e. for previously recorded pull requests). Normalize to Time so
# both can be compared/sorted consistently.
def to_time(value)
  value.is_a?(String) ? Time.parse(value) : value
end

# Load any previously recorded pull requests so we can fetch incrementally instead of
# re-fetching the entire repository history on every run. Symbolize names so previously
# recorded and newly-fetched entries share the same (symbol) keys.
existing_prs = []
if File.exist?(change_history_file)
  begin
    existing_data = JSON.parse(File.read(change_history_file), symbolize_names: true)
    existing_prs = existing_data[:merged_prs] || []
  rescue JSON::ParserError
    existing_prs = []
  end
end

existing_pr_numbers = existing_prs.map { |pr| pr[:number] }
last_merged_at = existing_prs.map { |pr| to_time(pr[:merged_at]) }.max

new_pr_list = []

if last_merged_at.nil?
  # Bootstrap: no existing (or parseable) history found, so fetch the full set of pull
  # requests merged into master. Only happens once, when the file is first created.
  puts Time.now.strftime("%H:%M:%S.%L") + " * No existing change history found. Performing a full historical fetch..."

  merged_pull_requests = github_client.pull_requests(repo_name, state: 'closed').select do |pr|
    # Omit PRs triggered by this script to avoid an infinite loop
    pr.merged_at && pr.base.ref == branch
  end.sort_by(&:merged_at).reverse

  new_pr_list = merged_pull_requests.map { |pr| build_pr_entry(github_client, repo_name, pr, pr.merged_at) }
else
  # Incremental fetch: only ask the Github Search API for pull requests merged after the most
  # recently recorded merge. A one day buffer is subtracted from the cutoff to guard against
  # any clock skew or API eventual-consistency; pull requests we already have on record are
  # skipped below by number, so re-checking a small window of already-known pull requests is
  # harmless.
  cutoff = (last_merged_at - 86400).strftime('%Y-%m-%d')
  puts Time.now.strftime("%H:%M:%S.%L") + " * Existing change history found. Fetching pull requests merged on or after #{cutoff}..."

  query = "repo:#{repo_name} is:pr is:merged base:#{branch} merged:>=#{cutoff}"
  search_results = github_client.search_issues(query, per_page: 100)

  search_results.items.each do |pr|
    next if existing_pr_numbers.include?(pr.number)
    next unless pr.pull_request && pr.pull_request.merged_at

    new_pr_list << build_pr_entry(github_client, repo_name, pr, pr.pull_request.merged_at)
  end
end

puts Time.now.strftime("%H:%M:%S.%L") + " * Found #{new_pr_list.length} newly merged pull request(s)."

# Combine newly-found pull requests with the previously recorded ones (in case the incremental
# window above overlapped with pull requests we already have), then sort by merge date with the
# most recent pull requests coming first.
pr_list = (new_pr_list + existing_prs).uniq { |pr| pr[:number] }.sort_by { |pr| to_time(pr[:merged_at]) }.reverse

# Construct final object
merged_prs = { "merged_prs": pr_list }

# Write the data/change_history/change_history.json file
File.open(change_history_file, 'w') {
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
      labels << "Unpublished" if pr[:labels].include?("UNPUBLISHED")
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
