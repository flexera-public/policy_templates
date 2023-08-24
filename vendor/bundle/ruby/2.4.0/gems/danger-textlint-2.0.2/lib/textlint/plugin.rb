# require "mkmf"
require "json"

module Danger
  # [Danger](http://danger.systems/ruby/) plugin for [textlint](https://textlint.github.io/).
  #
  # @example Run textlint and send violations as inline comment.
  #
  #          # Lint added and modified files only
  #          textlint.lint
  #
  # @example Keep severity until warning. It allows merging pull request if there are violations remaining.
  #
  #          textlint.max_severity = "warn"
  #          textlint.lint
  #
  # @example Max inline comment number. If you want disable this feature, please set nil. Default: nil
  #
  #          textlint.max_comment_num = 5
  #          textlint.lint
  #
  # @see  Kesin11/danger-textlint
  # @tags lint, textlint
  #
  class DangerTextlint < Plugin
    # .textlintrc path
    # @return [String]
    attr_accessor :config_file

    # Set max danger reporting severity
    # choice: nil or "warn"
    # @return [String]
    attr_accessor :max_severity

    # Set max danger reporting comment number
    # choice: nil or integer
    # @return [String]
    attr_accessor :max_comment_num

    # Execute textlint and send comment
    # @return [void]
    def lint
      return if target_files.empty?

      bin = textlint_path
      result_json = run_textlint(bin, target_files)
      errors = parse(result_json)
      send_comment(errors)
    end

    private

    def textlint_path
      local = "./node_modules/.bin/textlint"

      # NOTE: Danger using method_missing hack for parse 'warn', 'fail' in Dangerfile.
      # Same issue will occur 'message' when require 'mkmf'. Because 'mkmf' provide 'message' method.
      # Then, disable find executable textlint until danger fix this issue.

      # File.exist?(local) ? local : find_executable("textlint")
      raise "textlint not found in ./node_modules/.bin/textlint" unless File.exist?(local)

      local
    end

    def textlint_command(bin, target_files)
      command = "#{bin} -f json"
      command << " -c #{config_file}" if config_file
      return "#{command} #{target_files.join(' ')}"
    end

    def run_textlint(bin, target_files)
      command = textlint_command(bin, target_files)
      `#{command}`
    end

    def target_files
      ((git.modified_files - git.deleted_files) + git.added_files)
    end

    def parse(json)
      result = JSON(json)
      dir = "#{Dir.pwd}/"
      severity_method = {
        1 => "warn",
        2 => "fail"
      }

      result.flat_map do |file|
        file_path = file["filePath"]
        file["messages"].map do |message|
          severity = max_severity == "warn" ? 1 : message["severity"]
          {
            file_path: file_path.gsub(dir, ""),
            line: message["line"],
            severity: severity_method[severity],
            message: "#{message['message']}(#{message['ruleId']})"
          }
        end
      end
    end

    def send_comment(errors)
      limited_errors = errors
      if max_comment_num && limited_errors.size > max_comment_num
        limited_errors = limited_errors.first(max_comment_num)
        send("warn", "Textlint reported more than #{max_comment_num} problems, but danger-textlint doesn't to display all problems. Please run textlint in your machine and check all problems.")
      end

      limited_errors.each do |error|
        send(error[:severity], error[:message], file: error[:file_path], line: error[:line])
      end
    end
  end
end
