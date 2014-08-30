# Default is "World" if no variable provided on command line
# Author: Neocles Leontis / nleontis@gmail.com

name = ARGV.first || "World"

puts "Hello, #{name}!"
