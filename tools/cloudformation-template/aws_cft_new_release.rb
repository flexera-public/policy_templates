require "json"
require "time"
require "pathname"
require "digest"
require "fileutils"

# Method to test if two files are identical
def files_match?(file1, file2)
  Digest::SHA256.file(file1).hexdigest == Digest::SHA256.file(file2).hexdigest
end

# Define the directory containing the files
release_dir = "./releases"
local_file_path = "./FlexeraAutomationPolicies.template"

# Get a list of all template files in the directory
files = Dir.entries(release_dir).select { |file| file =~ /FlexeraAutomationPolicies_v(\d+\.\d+\.\d+)\.template$/ }

# Extract version numbers and map them to their corresponding files
file_versions = files.map do |file|
  match = file.match(/v(\d+\.\d+\.\d+)/)
  [file, match[1]] if match
end.compact

# Find the most recent version
most_recent = file_versions.max_by { |_, version| Gem::Version.new(version) }
most_recent_file, most_recent_version = most_recent
most_recent_path = File.join(release_dir, most_recent_file)

# Unless the files are identical, create a new version.
unless files_match?(local_file_path, most_recent_path)
  new_minor_version = (Integer(most_recent_version.split(".")[1]) + 1).to_s
  new_version = most_recent_version.split(".")[0] + "." + new_minor_version + ".0"
  new_file_path = release_dir + "/FlexeraAutomationPolicies_v" + new_version + ".template"

  FileUtils.cp(local_file_path, new_file_path, verbose: true)
end
