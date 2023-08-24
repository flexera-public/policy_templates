# https://docs.microsoft.com/en-us/azure/devops/pipelines/build/variables
require "uri"
require "danger/request_sources/github/github"

module Danger
  # ### CI Setup
  #
  # Add a script step:
  #
  # ```shell
  #   #!/usr/bin/env bash
  #   bundle install
  #   bundle exec danger
  # ```
  #
  # ### Token Setup
  #
  # Add the `DANGER_GITHUB_API_TOKEN` to your environment variables.
  #
  class AzurePipelines < CI
    def self.validates_as_ci?(env)
      # AGENT_ID is being used by AppCenter as well, so checking here to make sure AppCenter CI doesn't get a false positive for AzurePipelines
      # Anyone working with AzurePipelines could provide a better/truly unique env key to avoid checking for AppCenter
      !Danger::Appcenter::validates_as_ci?(env) &&
      env.key?("AGENT_ID") &&
      env["BUILD_REPOSITORY_PROVIDER"] != "TfsGit"
    end

    def self.validates_as_pr?(env)
      return env["BUILD_REASON"] == "PullRequest"
    end

    def supported_request_sources
      @supported_request_sources ||= [
        Danger::RequestSources::GitHub,
        Danger::RequestSources::GitLab,
        Danger::RequestSources::BitbucketServer,
        Danger::RequestSources::BitbucketCloud
      ]
    end

    def initialize(env)
      self.pull_request_id = env["SYSTEM_PULLREQUEST_PULLREQUESTNUMBER"] || env["SYSTEM_PULLREQUEST_PULLREQUESTID"]
      self.repo_url = env["BUILD_REPOSITORY_URI"]
      self.repo_slug = env["BUILD_REPOSITORY_NAME"]
    end
  end
end
