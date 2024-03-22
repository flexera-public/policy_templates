require 'find'

# The string to search for
old_string = '/rightscale/policy_templates/master/cost/flexera/cco/scheduled_reports/currency_reference.json'
# The string to replace it with
new_string = '/flexera-public/policy_templates/master/data/currency/currency_reference.json'

# Starting directory
dir = Dir.pwd

Find.find(dir) do |path|
  next unless File.file?(path) && path.end_with?('.pt')

  text = File.read(path)
  new_contents = text.gsub(old_string, new_string)

  # Only write to the file if there are changes to avoid unnecessary writes
  if text != new_contents
    File.open(path, "w") { |file| file.puts new_contents }
    puts "Updated: #{path}"
  end
end

puts "Finished processing files."
