import sys

if len(sys.argv) == 1:
	try:
		n = int(raw_input("Enter an integer: "))
	except ValueError:
		print "Enter a valid integer"
			
elif len(sys.argv) >1:
		try:
			n = int(sys.argv[1])

		except ValueError:
			print "No valid integer! will use 100 ..." 
			n = 100
print "Fizz buzz counting up to ", n
my_list = [i for i in range(0,n+1)]
print my_list
for i in range(1,n+1):
	if i % 3 == 0 and i % 5 != 0:
		my_list[i] = "fizz"
	if i % 5 == 0 and i % 3 != 0:
		my_list[i] = "buzz"
for i in range(0,n+1):
	print my_list[i], "\n"
