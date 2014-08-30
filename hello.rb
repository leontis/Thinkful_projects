# Default is "World" if no variable provided on command line

name = ARGV.first || "World"

puts "Hello, #{name}!"
