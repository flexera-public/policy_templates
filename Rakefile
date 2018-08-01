#rake task to generate file list until we version on each master commit
require 'rubygems'
require 'json'
require 'fileutils'

desc "One line task description"
task :generate_policy_list do
  file_list = []
  FileUtils::mkdir_p 'dist'
  Dir['**/*.pt'].each do |file|
    if !file.match(/test_code/)
      f = File.read(file)
      f.each_line do |line|
        if line =~ /^name/
          @name = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse
          puts @name
        end
        if line =~ /long_description/
          if line =~ /Version/
            @version = line.split(':').last.strip.chomp("\"")
          end
        end
      end
      file_list<<{"name": @name, "file_name": file, "version": @version }
    end
  end
  policies = {"policies": file_list }
  File.open('dist/active-policy-list.json', 'w') { |file| file.write(JSON.pretty_generate(policies)) }
end
