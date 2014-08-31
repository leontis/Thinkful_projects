# Default is "World" if no variable provided on command line
# Author: Neocles Leontis / nleontis@gmail.com

name = ARGV.first || "World"

puts "What's your name?"
my_name = gets.strip

puts "Hello, #{name}!"
