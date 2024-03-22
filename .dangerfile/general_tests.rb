# DangerFile General Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: General
###############################################################################

### Spell check test
# Run the Danger spell checker on a file
def general_spellcheck?(file)
  # Import the ignore list from a file but ignore entries starting with #
  # This is so we can have comments in this file
  prose.ignored_words = File.readlines('.spellignore').map(&:chomp).select{ |entry| !entry.start_with?("#") }

  # Disable functionality to prevent a lot of pointless results
  prose.ignore_numbers = true
  prose.ignore_acronyms = true

  # Set language
  prose.language = "en-us"

  # Check spelling
  prose.check_spelling(file)
end

### Markdown lint test
# Return false if linter finds no problems
def general_bad_markdown?(file)
  # Adjust testing based on which file we're doing
  case file
  when "README.md"
    mdl = `mdl -r "~MD007","~MD013","~MD024" #{file}`
  when "tools/cloudformation-template/README.md"
    mdl = `mdl -r "~MD007","~MD013","~MD033","~MD034" #{file}`
  when ".github/PULL_REQUEST_TEMPLATE.md"
    mdl = `mdl -r "~MD002","~MD007","~MD013" #{file}`
  else
    mdl = `mdl -r "~MD007","~MD013" #{file}`
  end

  # Return the problems found if the mdl file is not empty. Otherwise, return false
  return "**#{file}**\nMarkdown syntax errors found:\n\n#{mdl}" if !mdl.empty?
  return false
end

### Bad URL test
# Return false if no invalid URLs are found.
def general_bad_urls?(file)
  # List of hosts to ignore in the analysis
  exclude_hosts = [
    'api.loganalytics.io',          'management.azure.com',
    'management.core.windows.net',  'login.microsoftonline.com',
    'oauth2.googleapis.com',        'www.googleapis.com',
    'image-charts.com',             'graph.microsoft.com',
    'www.w3.org',                   'tempuri.org',
    'us-3.rightscale.com',          'us-4.rightscale.com'
  ]

  diff = git.diff_for_file(file)
  regex = /(^\+)/
  fail_message = ""

  if diff && diff.patch =~ regex
    diff.patch.each_line.with_index do |line, index|
      line_number = index + 1

      if line =~ regex
        URI.extract(line,['http', 'https']).each do |url|
          # Skip excluded hosts
          next if exclude_hosts.include?(url.scan(URI.regexp)[0][3])

          # Clean up URL string and convert it into a proper URI object
          url_string = url.to_s.gsub(/[!@#$%^&*(),.?":{}|<>]/,'')
          url = URI(url_string)

          # Check for a valid host. Skip URLs that are dynamicly constructed and may not have a valid hostname.
          # Example: http://ec2. + $region + .awsamazon.com/... does not have a valid hostname to query.
          next if url.host !~ /(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)/

          # Make HTTP request to URL
          response = Net::HTTP.get_response(url)

          # Test again when the file isn't found and path includes tree/master
          # This is in case it is the README link or a new file included in the repo
          if response.code == '404' && url_string =~ /tree\/master/
            # Modify URL string and convert it back into a proper URI object
            url_string = url.to_s.gsub('tree/master',"tree/#{github.branch_for_head}").gsub(')','')
            url = URI(url_string)

            # Make HTTP request to URL again
            response = Net::HTTP.get_response(url) #make request
          end

          # Return error details if a proper response code was not received
          if response.code !~ /200|302/
            fail_message += "Line: #{line_number.to_s}\nURL: #{url_string}\nResponse Code: #{response.code}\n\n"
          end
        end
      end
    end
  end

  fail_message = "**#{file}**\nBad URLs found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

###############################################################################
# Methods: Ruby
###############################################################################

### Ruby lint test
# Return false if Ruby linter finds no problems
def general_ruby_errors?(file)
  linter = `ruby -c #{file}`

  # Return the problems found if applicable
  return "**#{file}**\nRuby linting found errors:\n\n#{linter}" if linter.strip != "Syntax OK"
  return false
end

### Rubocop lint test
# Return false if Rubocop linter finds no problems
def general_rubocop_problems?(file)
  linter = `rubocop #{file}`

  fail_message = ""

  linter.each_line do |line|
    fail_message += line.strip + "\n" if line.start_with?(file)
  end

  # Return the problems found if applicable
  return "**#{file}**\nRubocop linting found problems:\n\n#{fail_message}" if !fail_message.empty?
  return false
end

###############################################################################
# Methods: Python
###############################################################################

### Python lint test
# Return false if Python linter finds no problems
def general_python_errors?(file)
  linter = `pylint --errors-only #{file}`

  fail_message = ""

  linter.each_line do |line|
    fail_message += line.strip + "\n" if line.start_with?(file)
  end

  # Return the problems found if applicable
  return "**#{file}**\nPython linting found errors:\n\n#{fail_message}" if !fail_message.strip.empty?
  return false
end

###############################################################################
# Methods: JSON/YAML
###############################################################################

def general_json_bad_location?(file)
  fail_message = ""

  if file.start_with?("automation/") || file.start_with?("compliance/") || file.start_with?("cost/") || file.start_with?("operational/") || file.start_with?("saas/") || file.start_with?("security/")
    fail_message = "**#{file}**\nJSON file located inside policy directory. Please move JSON file to an appropriate subdirectory in `data/`"
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

def general_yaml_bad_location?(file)
  fail_message = ""

  if file.start_with?("automation/") || file.start_with?("compliance/") || file.start_with?("cost/") || file.start_with?("operational/") || file.start_with?("saas/") || file.start_with?("security/")
    fail_message = "**#{file}**\nYAML file located inside policy directory. Please move YAML file to an appropriate subdirectory in `data/`"
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

def general_json_errors?(file)
  linter = `jsonlint #{file}`

  # Return the problems found if applicable
  return "**#{file}**\nJSON linting found errors:\n\n#{linter}" if !linter.strip.empty?
  return false
end

def general_yaml_errors?(file)
  linter = `yaml-lint -q #{file}`

  # Return the problems found if applicable
  return "**#{file}**\nYAML linting found errors:\n\n#{linter}" if !linter.strip.empty?
  return false
end
