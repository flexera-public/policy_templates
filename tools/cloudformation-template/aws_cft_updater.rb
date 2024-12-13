require "json"
require "time"
require "pathname"
require "digest"
require "fileutils"

# Method to test if two files are identical
def files_match?(file1, file2)
  lines1 = File.readlines(file1)
  lines2 = File.readlines(file2)

  # Remove line 3 since this contains the date the file was generated
  lines1.delete_at(2) if lines1.size > 2
  lines2.delete_at(2) if lines2.size > 2

  # Compare the remaining content
  Digest::SHA256.hexdigest(lines1.join) == Digest::SHA256.hexdigest(lines2.join)
end

# Define the directory containing the files
release_dir = "./releases"
rolling_path = "./rolling/FlexeraAutomationPolicies.template"
local_file_path = "./FlexeraAutomationPolicies.template"

# Unless the files are identical, create a new version.
unless files_match?(rolling_path, local_file_path)
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

  new_patch_version = (Integer(most_recent_version.split(".")[2]) + 1).to_s
  new_version = most_recent_version.split(".")[0] + "." + most_recent_version.split(".")[1] + "." + new_patch_version
  new_file_path = release_dir + "/FlexeraAutomationPolicies_v" + new_version + ".template"

  FileUtils.cp(rolling_path, new_file_path, verbose: true)
  FileUtils.cp(rolling_path, local_file_path, verbose: true)
end
