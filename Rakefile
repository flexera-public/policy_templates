#rake task to generate file list until we version on each master commit
require 'rubygems'
require 'json'
require 'fileutils'

desc "One line task description"
task :generate_policy_list do
  FileUtils.mkdir_p 'dist'
  file_list = []
  Dir['**/*.pt'].reject{ |f| f['msp/'] }.each do |file|
    change_log = ::File.join(file.split('/')[0...-1].join('/'),'CHANGELOG.md')
    readme = ::File.join(file.split('/')[0...-1].join('/'),'README.md')
    if !file.match(/test_code/)
      f = File.open(file, "r:bom|utf-8")
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
        if line =~ /short_description/
          @description = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse.split('.').first
        end
        if line =~ /category \"(compliance|cost|operational|security|saas management)\"/i
          @category = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse
          @category = @category.gsub(" ","_")
          @category = @category.downcase
        end
        if line =~ /severity/
          @severity = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse
        end
      end
      file_list<<{
        "name": @name,
        "file_name": file,
        "version": @version,
        "change_log": change_log,
        "description": @description,
        "category": @category,
        "severity": @severity,
        "readme": readme
      }
    end
  end
  policies = {"policies": file_list }
  File.open('dist/active-policy-list.json', 'w') { |file| file.write(JSON.pretty_generate(policies)+"\n") }
end
