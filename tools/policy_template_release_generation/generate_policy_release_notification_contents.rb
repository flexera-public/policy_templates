class Changelog
  attr_accessor :path, :version, :changes

  def initialize(path, version, changes)
    @path = path
    @version = version
    @changes = changes
  end
end

class PolicyTemplate
  attr_accessor :name, :path

  def initialize(name, path)
    @name = name
    @path = path
  end
end

# Manually set branches here (for now)
base_branch = 'origin/master'
head_branch = 'POL-847-policy-automated-updates-on-releases'

# Get a list of added and modified files

#`ENV['DANGER_GITHUB_PR_BASE_SA'] + '...' + 'ENV['DANGER_GITHUB_PR_HEAD_SHA']
#added_files = `git diff --name-only --diff-filter=A HEAD@{1} HEAD`.split("\n")
#modified_files = `git diff --name-only --diff-filter=M HEAD@{1} HEAD`.split("\n")
# changed_files = (added_files + modified_files).uniq

changed_files = `git diff --name-only #{base_branch} #{head_branch}`.split("\n")
# puts "These are the Modified Files: #{changed_files}"


# Initialize arrays to store Changelog objects and Policy Template objects
changelogs = []
policy_templates = []

# Process Changelog files
changed_files.each do |file|
  next unless file.match?(/CHANGELOG\.md$/) || file.match?(/\.pt$/) #Consider pulling README

  if file.match?(/CHANGELOG\.md$/) 
    changelog_content = File.read(file)
    version = changelog_content.match(/^##\s*v([\d.]+)/)&.captures&.first
    changes = []

    if version && !changelog_content.empty?
      # Caputre changes for the most recent version only
      latest_version_changes = changelog_content.scan(/^##\s*v#{version}[\s\S]*?(?=(?:^##\s*v\d+)|\z)/m)
      latest_version_changes.each do |version_changes|
        changes.concat(version_changes.scan(/^- (.+)/).flatten)
      end

      changelogs << Changelog.new(file, version, changes) if version && !changes.empty?
    end
  else
    # Capture policy template names
    pt_content = File.read(file)
    name = pt_content.match(/name "([^"]+)"/)&.captures&.first
    policy_templates << PolicyTemplate.new(name, file) if name
  end
end

# puts "This is the list of Changelogs: #{changelogs}"
# puts "This is the list of Policy Templates: #{policy_templates}"

# Create Notification Content Array
notification_content_array = []

# Match Changelog entries with Policy Templates based on paths
# and then push Changelog contents to Notification Content Array defined above
changelogs.each do |changelog|
  matching_template = policy_templates.find { |template| changelog.path.include?(File.dirname(template.path)) }
  if matching_template
    # puts "Changelog for Policy Template '#{matching_template.name}':"
    # puts "Updated Template Version '#{changelog.version}'"
    # puts changelog.changes
    # puts "Policy Template File Path: #{matching_template.path}"
    # puts "\n"

    notification_content_json = {
      activityTitle: matching_template.name,
      activitySubtitle: "Version: #{changelog.version}",
      facts: [{
        name: "Updates",
        value: changelog.changes
      }]
    }

    notification_content_array << notification_content_json

    # # Store Changelog content in Step Output
    # puts "::set-output name=changelog_content::#{changelog.changes.join}"
  else
    puts "No matching Policy Template found for Changelog Version #{changelog.version}"
  end
end

#Output Notification Content as a JSON string
puts changelog_json_array.to_json
