class PolicyParser
  DEFINITION_REGEX = /^[[:blank:]]*define[[:blank:]]*([\w_\.]+)[[:blank:]]*\([@$\w _,]*\)[[:blank:]]*.*do/.freeze

  attr_reader :parsed_info,  :parsed_category, :parsed_name, :parsed_severity, :parsed_long_description, :parsed_short_description, :parsed_default_frequency

  def parse(file)
    source = File.read(file)

    # we assume that all of the metadata is before any declarations
    # especially RCL defines which are not parsable as Ruby
    source = source.split(DEFINITION_REGEX, 2).first
    instance_eval(source, file)
  end

  def info(**info)
    @parsed_info = info
  end

  def category(category)
    @parsed_category = category
  end

  def name(name)
    @parsed_name = name
  end

  def severity(severity)
    @parsed_severity = severity
  end

  def long_description(long_description)
    @parsed_long_description = long_description
  end

  def short_description(short_description)
    @parsed_short_description = short_description
  end

  def default_frequency(default_frequency)
    @parsed_default_frequency = default_frequency
  end

  def method_missing(symbol, *args, &block)
    # do nothing
  end
end
