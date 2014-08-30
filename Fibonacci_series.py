def fib(n):
	a, b = 0, 1
	while b < n:
		print(a,b)
		a, b = b, a+b
	return a,b	

max = 1000 # raw_input("Enter an integer: How high do you want to go?")

fibonacci = fib(int(max))

print fibonacci
