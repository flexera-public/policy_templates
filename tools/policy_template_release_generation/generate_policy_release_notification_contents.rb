class Changelog
  attr_accessor :version, :changes

  def initialize(version, changes)
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

# Get a list of added and modified files

#`ENV['DANGER_GITHUB_PR_BASE_SA'] + '...' + 'ENV['DANGER_GITHUB_PR_HEAD_SHA']
#added_files = `git diff --name-only --diff-filter=A HEAD@{1} HEAD`.split("\n")
#modified_files = `git diff --name-only --diff-filter=M HEAD@{1} HEAD`.split("\n")

added_files = `git diff --name-only #{base_branch} #{head_branch} --diff-filter=A`.split("\n")
modified_files = `git diff --name-only #{base_branch} #{head_branch} --diff-filter=M`.split("\n")
puts "These are the Added Files: #{added_files}"
puts "These are the Modified Files: #{modified_files}"
changed_files = (added_files + modified_files).uniq

# Initialize arrays to store Changelog objects and Policy Template objects
changelogs = []
policy_templates = []

# # Process Changelog files
# changelog_files.each do |changelog_file|
#   changelog_content = File.read(changelog_file)
#   version = changelog_content.match(/^##\s*v([\d.]+)/)&.captures&.first
#   changes = changelog_content.scan(/^- (.+)/).flatten
#   changelogs << Changelog.new(version, changes) if version && !changes.empty?
# end

puts "This is the list of Changelogs"

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
