#rake task to generate file list until we version on each master commit
require 'rubygems'
require 'json'
require 'fileutils'

desc "One line task description"
task :generate_policy_list do
  FileUtils.mkdir_p 'dist'
  file_list = []
  Dir['**/*.pt'].each do |file|
    change_log = ::File.join(file.split('/')[0...-1].join('/'),'CHANGELOG.md')
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
      file_list<<{"name": @name, "file_name": file, "version": @version, "change_log": change_log }
    end
  end
  policies = {"policies": file_list }
  File.open('dist/active-policy-list.json', 'w') { |file| file.write(JSON.pretty_generate(policies)+"\n") }
end
