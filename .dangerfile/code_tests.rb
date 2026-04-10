# DangerFile Code Tests
# See ./Dangerfile for more details

# Policy category top-level directories — kept in sync with POLICY_CATEGORY_DIRS in Dangerfile
POLICY_DIRS = %w[automation/ compliance/ cost/ operational/ saas/ security/].freeze

###############################################################################
# Methods: Ruby
###############################################################################

### Ruby lint test
# Return false if Ruby linter finds no problems
def code_ruby_errors?(file)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing Ruby file using standard linter..."

  linter = `ruby -c #{file}`

  # Return the problems found if applicable
  return false if linter.strip == "Syntax OK"
  "Ruby linting found errors:\n\n#{linter}"
end

### Rubocop lint test
# Return false if Rubocop linter finds no problems
# Currently not in use due to extremely verbose and thorough output
# def code_rubocop_problems?(file)
#   puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing Ruby file using Rubocop linter..."

#   linter = `rubocop #{file}`

#   fail_message = ""

#   linter.each_line do |line|
#     fail_message += line.strip + "\n" if line.start_with?(file)
#   end

#   # Return the problems found if applicable
#   return "Rubocop linting found problems:\n\n#{fail_message}" if !fail_message.empty?
#   return false
# end

###############################################################################
# Methods: Python
###############################################################################

### Python lint test
# Return false if Python linter finds no problems
def code_python_errors?(file)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing Python file using pylint linter..."

  linter = `pylint --errors-only #{file}`

  fail_message = ""

  linter.each_line do |line|
    fail_message += line.strip + "\n" if line.start_with?(file)
  end

  # Return the problems found if applicable
  return false if fail_message.strip.empty?
  "Python linting found errors:\n\n#{fail_message}"
end

###############################################################################
# Methods: JSON/YAML
###############################################################################

def code_json_bad_location?(file)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing JSON file location..."
  return "JSON file located inside policy directory. Please move JSON file to an appropriate subdirectory in `data/`" if POLICY_DIRS.any? { |dir| file.start_with?(dir) }
  false
end

def code_yaml_bad_location?(file)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Testing YAML file location..."
  return "YAML file located inside policy directory. Please move YAML file to an appropriate subdirectory in `data/`" if POLICY_DIRS.any? { |dir| file.start_with?(dir) }
  false
end

def code_json_errors?(file)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Linting JSON file..."

  linter = `jsonlint #{file}`

  # Return the problems found if applicable
  return false if linter.strip.empty?
  "JSON linting found errors:\n\n#{linter}"
end

def code_yaml_errors?(file)
  puts Time.now.strftime("%H:%M:%S.%L") + " *** Linting YAML file..."

  linter = `yaml-lint -q #{file}`

  # Return the problems found if applicable
  return false if linter.strip.empty?
  "YAML linting found errors:\n\n#{linter}"
end
