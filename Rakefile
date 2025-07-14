require 'rubygems'
require 'json'
require 'fileutils'
require 'octokit'
require 'uri'
require 'time'
require_relative '.dangerfile/policy_parser'

# The list of policies is consumed by the tools/policy_sync/policy_sync.pt
# and the docs.rightscale.com build to generate the policies/user/policy_list.html
# the file is uploaded to S3 during a merge to master deploy step in .travis.yml
desc "Create a list of active policies to be published to the Public Policy Catalog"

task :generate_policy_list do
  # Preparation for getting information from Github repository
  repo_name = "flexera-public/policy_templates"
  branch = "master"
  github_api_token = ENV["GITHUB_API_TOKEN"]
  github_client = Octokit::Client.new(access_token: github_api_token)

  # Get the list of recommended policy templates
  generally_recommended_templates_json = File.read('data/active_policy_list/generally_recommended_templates.json')
  generally_recommended_templates = JSON.parse(generally_recommended_templates_json)
  # generally_recommended_template_names is all the PT Names for all the providers in generally_recommended_templates
  generally_recommended_template_names = []
  generally_recommended_templates.each do |key, value|
    generally_recommended_template_names.concat(value)
  end

  FileUtils.mkdir_p 'dist'
  file_list = []

  Dir['**/*.pt'].each do |file|
    change_log = ::File.join(file.split('/')[0...-1].join('/'), 'CHANGELOG.md')
    readme = ::File.join(file.split('/')[0...-1].join('/'), 'README.md')
    updated_at = nil

    f = File.open(file, "r:bom|utf-8")

    pp = PolicyParser.new
    pp.parse(file)

    if pp.parsed_info
      version = pp.parsed_info[:version]
      provider = pp.parsed_info[:provider]
      service = pp.parsed_info[:service]
      policy_set = pp.parsed_info[:policy_set]
      recommendation_type = pp.parsed_info[:recommendation_type]
      publish = pp.parsed_info[:publish]
      deprecated = pp.parsed_info[:deprecated]
      hide_skip_approvals = pp.parsed_info[:hide_skip_approvals]


      # 'publish' defaults to true unless explicitly set to false
      # 'deprecated' defaults to false unless explicitly set to true
      publish = !(publish == 'false' || publish == false)
      deprecated = deprecated == 'true' || deprecated == true
      # 'hide_skip_approvals' defaults to false unless explicitly set to true
      hide_skip_approvals = hide_skip_approvals == 'true' || hide_skip_approvals == true
    end

    # Get version from long description
    if version.nil? && pp.parsed_long_description =~ /Version/
      version = pp.parsed_long_description.split(':').last.strip.chomp("\"")
    end

    # Skip policy if the version isn't supplied or if version is '0.0'
    if !version || version == '0.0' || !publish
      puts "Skipping #{pp.parsed_name} because publish flag set to a value other than 'true'"
    else
      # Get datetime for last time file was modified
      commits = github_client.commits(repo_name, branch, path: file)
      updated_at = commits.first.commit.author.date.utc.iso8601 if !commits.empty?
      generally_recommended = generally_recommended_template_names.include?(pp.parsed_name) && !deprecated

      puts "Adding #{pp.parsed_name}"

      file_list << {
        "name": pp.parsed_name,
        "file_name": file,
        "version": version,
        "change_log": change_log,
        "description": pp.parsed_short_description,
        "category": pp.parsed_category,
        "severity": pp.parsed_severity,
        "readme": readme,
        "provider": provider,
        "service": service,
        "policy_set": policy_set,
        "recommendation_type": recommendation_type,
        "updated_at": updated_at,
        "generally_recommended": generally_recommended,
        "deprecated": deprecated,
        "hide_skip_approvals": hide_skip_approvals
      }
    end
  end

  # Sort the file list by Policy Template Name
  # This minimizes output diffs between runs
  file_list = file_list.sort_by { |pt| pt[:name] }

  # Construct final object
  policies = { "policies": file_list }

  # Write the output JSON file to disk
  File.open('dist/active-policy-list.json', 'w') {
    |file| file.write(JSON.pretty_generate(policies) + "\n")
  }
end
