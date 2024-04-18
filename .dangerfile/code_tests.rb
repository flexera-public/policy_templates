# DangerFile Code Tests
# See ./Dangerfile for more details

###############################################################################
# Methods: Ruby
###############################################################################

### Ruby lint test
# Return false if Ruby linter finds no problems
def code_ruby_errors?(file)
  linter = `ruby -c #{file}`

  # Return the problems found if applicable
  return "Ruby linting found errors:\n\n#{linter}" if linter.strip != "Syntax OK"
  return false
end

### Rubocop lint test
# Return false if Rubocop linter finds no problems
def code_rubocop_problems?(file)
  linter = `rubocop #{file}`

  fail_message = ""

  linter.each_line do |line|
    fail_message += line.strip + "\n" if line.start_with?(file)
  end

  # Return the problems found if applicable
  return "Rubocop linting found problems:\n\n#{fail_message}" if !fail_message.empty?
  return false
end

###############################################################################
# Methods: Python
###############################################################################

### Python lint test
# Return false if Python linter finds no problems
def code_python_errors?(file)
  linter = `pylint --errors-only #{file}`

  fail_message = ""

  linter.each_line do |line|
    fail_message += line.strip + "\n" if line.start_with?(file)
  end

  # Return the problems found if applicable
  return "Python linting found errors:\n\n#{fail_message}" if !fail_message.strip.empty?
  return false
end

###############################################################################
# Methods: JSON/YAML
###############################################################################

def code_json_bad_location?(file)
  fail_message = ""

  if file.start_with?("automation/") || file.start_with?("compliance/") || file.start_with?("cost/") || file.start_with?("operational/") || file.start_with?("saas/") || file.start_with?("security/")
    fail_message = "JSON file located inside policy directory. Please move JSON file to an appropriate subdirectory in `data/`"
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

def code_yaml_bad_location?(file)
  fail_message = ""

  if file.start_with?("automation/") || file.start_with?("compliance/") || file.start_with?("cost/") || file.start_with?("operational/") || file.start_with?("saas/") || file.start_with?("security/")
    fail_message = "YAML file located inside policy directory. Please move YAML file to an appropriate subdirectory in `data/`"
  end

  return fail_message.strip if !fail_message.empty?
  return false
end

def code_json_errors?(file)
  linter = `jsonlint #{file}`

  # Return the problems found if applicable
  return "JSON linting found errors:\n\n#{linter}" if !linter.strip.empty?
  return false
end

def code_yaml_errors?(file)
  linter = `yaml-lint -q #{file}`

  # Return the problems found if applicable
  return "YAML linting found errors:\n\n#{linter}" if !linter.strip.empty?
  return false
end
