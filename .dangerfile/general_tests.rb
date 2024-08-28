# DangerFile General Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: General
###############################################################################

#### Textlint test
# Return false if linter finds no problems
def general_textlint?(file)
  puts "*** " + Time.now.strftime("%H:%M:%S.%L") + " Testing file using text linter..."

  fail_message = ""

  # Run text lint and store results in log file
  `node_modules/.bin/textlint #{file} 1> textlint.log`

  if $?.exitstatus != 0
    error_list = `cat textlint.log`.split("\n")
    error_list.shift(2) # Remove first line since it just links to the filename in the local filesystem
    error_list = error_list.join("\n\n")

    fail_message = "Textlint errors found:\n\n#{error_list}"
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

### Spell check test
# Run the Danger spell checker on a file
def general_spellcheck?(file)
  puts "*** " + Time.now.strftime("%H:%M:%S.%L") + " Testing file using aspell spell checker..."

  fail_message = ""

  # Run aspell and store results in log file
  ignore_file = ".spellignore"

  command = %(
    awk '{print NR ": " $0}' #{file} |
    aspell --master=en_US --lang=en_US --ignore-case --mode=markdown list -l en |
    sort |
    uniq |
    grep -vFf #{ignore_file} |
    while read word; do
      awk -v word="$word" '{for (i=1; i<=NF; i++) if ($i == word) print "Line " NR ": " word}' #{file}
    done |
    sort -n -k2,2 1> aspell.log
  )

  if system(command)
    error_list = `cat aspell.log`
    fail_message = "Spelling errors found:\n\n#{error_list}"
  end

  return fail_message.strip if !fail_message.strip.empty?
  return false
end

### Markdown lint test
# Return false if linter finds no problems
def general_bad_markdown?(file)
  puts "*** " + Time.now.strftime("%H:%M:%S.%L") + " Testing file using markdown linter..."

  # Adjust testing based on which file we're doing
  case file
  when "README.md"
    mdl = `mdl -r "~MD007","~MD013","~MD024" #{file}`
  when "README_META_POLICIES.md"
    mdl = `mdl -r "~MD007","~MD013","~MD024" #{file}`
  when "tools/cloudformation-template/README.md"
    mdl = `mdl -r "~MD007","~MD013","~MD033","~MD034" #{file}`
  when ".github/PULL_REQUEST_TEMPLATE.md"
    mdl = `mdl -r "~MD002","~MD007","~MD013" #{file}`
  else
    mdl = `mdl -r "~MD007","~MD013" #{file}`
  end

  # Return the problems found if the mdl file is not empty. Otherwise, return false
  return "Markdown syntax errors found:\n\n#{mdl}" if !mdl.empty?
  return false
end

### Bad URL test
# Return false if no invalid URLs are found.
def general_bad_urls?(file, file_diff)
  puts "*** " + Time.now.strftime("%H:%M:%S.%L") + " Testing file for bad or invalid URLs..."

  # List of hosts to ignore in the analysis
  exclude_hosts = [
    'api.loganalytics.io',          'management.azure.com',
    'management.core.windows.net',  'login.microsoftonline.com',
    'oauth2.googleapis.com',        'www.googleapis.com',
    'image-charts.com',             'graph.microsoft.com',
    'www.w3.org',                   'tempuri.org',
    'us-3.rightscale.com',          'us-4.rightscale.com'
  ]

  regex = /(^\+)/
  fail_message = ""

  if file_diff && file_diff.patch =~ regex
    file_diff.patch.each_line.with_index do |line, index|
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

  fail_message = "Bad URLs found:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end

### Outdated Terminology test
# Return false if no outdated terminology, such as RightScale, is found in the file
def general_outdated_terminology?(file, file_lines)
  puts "*** " + Time.now.strftime("%H:%M:%S.%L") + " Testing file for outdated terminology..."

  fail_message = ""

  # Exclude files not worth checking
  if !file.include?("Dangerfile") && !file.include?(".dangerfile") && !file.start_with?("data/") && !file.start_with?("tools/")
    file_lines.each_with_index do |line, index|
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

  fail_message = "Outdated terminology found. Please remove references to defunct internal names for products or services:\n\n" + fail_message if !fail_message.empty?

  return fail_message.strip if !fail_message.empty?
  return false
end
