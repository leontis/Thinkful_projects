# Default is "World" if no variable provided on command line
# This is an unwanted but committed change
name = ARGV.first || "World"

puts "Hello, #{name}!"
