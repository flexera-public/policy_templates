class Changelog
  attr_accessor :version, :changes

  def initialize(name, version, changes)
    @name = name
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
base_branch = 'master'
head_branch = 'POL-847-policy-automated-updates-on-releases'
puts "Base branch #{base_branch}"

# Get a list of added and modified files

#`ENV['DANGER_GITHUB_PR_BASE_SA'] + '...' + 'ENV['DANGER_GITHUB_PR_HEAD_SHA']
#added_files = `git diff --name-only --diff-filter=A HEAD@{1} HEAD`.split("\n")
#modified_files = `git diff --name-only --diff-filter=M HEAD@{1} HEAD`.split("\n")

# added_files = `git diff --name-only #{base_branch}..#{head_branch} --diff-filter=A`.split("\n")
# modified_files = `git diff --name-only #{base_branch}..#{head_branch} --diff-filter=M`.split("\n")
# puts "These are the Added Files: #{added_files}"
# puts "These are the Modified Files: #{modified_files}"
# changed_files = (added_files + modified_files).uniq
changed_files = `git diff --name-only #{base_branch} #{head_branch}`.split("\n")
puts "These are the Modified Files: #{changed_files}"


# Initialize arrays to store Changelog objects and Policy Template objects
cumulative_changelogs = []
policy_templates = []

# Process Changelog files
changed_files.each do |file|
  next unless file.match?(/CHANGELOG\.md$/)

  changelog_content = File.read(file)
  version = changelog_content.match(/^##\s*v([\d.]+)/)&.captures&.first
  changes = []

  if version && !changelog_content.empty?
    # Caputre cahnges for the most recent version only
    latest_version_changes = changelog_content.scan(/^##\s*v#{version}[\s\S]*?(?=(?:^##\s*v\d+)|\z)/m)
    latest_version_changes.each do |version_changes|
      changes.concat(version_changes.scan(/^- (.+)/).flatten)
    end

    cumulative_changelogs << Changelog.new(file, version, changes) if version && !changes.empty?
  end
end

puts "This is the list of Changelogs: #{cumulative_changelogs}"

# # Process Policy Template files
# policy_template_files.each do |pt_file|
#   pt_content = File.read(pt_file)
#   name = pt_content.match(/name "([^"]+)"/)&.captures&.first
#   policy_templates << PolicyTemplate.new(name, pt_file) if name
# end

# # Match Changelog entries with Policy Templates based on paths
# changelogs.each do |changelog|
#   matching_template = policy_templates.find { |template| changelog.path.include?(template.name.downcase) }
#   if matching_template
#     puts "Changelog for Policy Template '#{matching_template.name}':"
#     puts changelog.changes
#     puts "Policy Template File Path: #{matching_template.path}"
#     puts "\n"
#   else
#     puts "No matching Policy Template found for Changelog Version #{changelog.version}"
#   end
# end
