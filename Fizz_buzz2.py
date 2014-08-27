import sys

def divisible(a,b):
	"""I determine if a is divisible by and return True or False """  
	#print "I'm a function. My name is {}".format(divisible.__name__)
	if a%b == 0:
		return True
	else:
		return False	

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
	if divisible(i,3) and not divisible(i,5):
		my_list[i] = "fizz"
	if divisible(i,5) and not divisible(i,3):
		my_list[i] = "buzz"
	if divisible(i,5) and divisible(i,3):
		my_list[i] = "fizz-buzz"

if __name__ == '__main__':
	
for i in range(0,n+1):
	print my_list[i], "\n"
