require 'json'

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

# Get a list of added and modified files
added_files = `git diff --name-only --diff-filter=A origin/master~1..origin/master`.split("\n")
modified_files = `git diff --name-only --diff-filter=M origin/master~1..origin/master`.split("\n")
changed_files = (added_files + modified_files).uniq

# Initialize arrays to store Changelog objects and Policy Template objects
changelogs = []
policy_templates = []

# Process Changelog files
changed_files.each do |file|
  next unless file.match?(/CHANGELOG\.md$/) || file.match?(/\.pt$/) #Consider pulling README as well

  if file.match?(/CHANGELOG\.md$/) 
    changelog_content = File.read(file)
    version = changelog_content.match(/^##\s*v([\d.]+)/)&.captures&.first
    changes = []

    if version && !changelog_content.empty?
      # Capture changes for the most recent version only
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

# Create Notification Content Array
all_notification_content_array = []

# Match Changelog entries with Policy Templates based on paths
# and then push Changelog contents to Notification Content Array defined above
changelogs.each do |changelog|
  matching_template = policy_templates.find { |template| changelog.path.include?(File.dirname(template.path)) }
  if matching_template

    # Format HTML for Notification API call
    # Replace backticks around words with HTML code tags
    formatted_changes = changelog.changes.map do |change|
      change.gsub(/`([^`]+)`/, '<code>\1</code>')
    end

    formatted_changes_html = formatted_changes.map { |change| "<li>#{change}</li>"}.join('')

    notification_content_json = {
      activityTitle: "<h2 style='font-size: 18px;'>#{matching_template.name}</h2>",
      facts: [{
        name: "Template Version",
        value: changelog.version
      },
      {
        name: "Policy Updates",
        value: "<ul>#{formatted_changes_html}</ul>"
      }]
    }

    all_notification_content_array << notification_content_json
  end
end

# Output Notification Content as a JSON string to be used directly in YAML workflow file
puts "Array: #{all_notification_content_array}"
all_notification_content = JSON.generate(all_notification_content_array).gsub('"', '\\"').gsub('\\\"', '\\\\\\\\\\"')
puts all_notification_content
