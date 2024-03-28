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

### Outdated Terminology test
# Return false if no outdated terminology, such as RightScale, is found in the file
def general_outdated_terminology?(file)
  fail_message = ""

  # Store contents of file for direct analysis
  file_text = File.read(file)

  # Exclude files not worth checking
  if !file.include?("Dangerfile") && !file.include?(".dangerfile") && !file.start_with?("data/") && !file.start_with?("tools/")
    file_text.each_line.with_index do |line, index|
      line_number = index + 1
      test_line = line.strip.downcase

      if test_line.include?(" rs ") || test_line.include?(" rightscale ")
        fail_message += "Line #{line_number.to_s}: Reference to `RightScale` found. Recommended replacements: `Flexera`, `Flexera CCO`, `Flexera Automation`\n\n"
      end

      if test_line.include?(" optima ")
        fail_message += "Line #{line_number.to_s}: Reference to `Optima` found. Recommended replacements: `Flexera`, `Flexera CCO`, `Cloud Cost Optimization`\n\n"
      end
    end
  end

  fail_message = "**#{file}**\nOutdated terminology found. Please remove references to defunct internal names for products or services:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end
