n=int(input("Enter some Number"))
def fib(x):
	if (x>0):
		x=fib(x-1)+fib(x-2)
	else:
		x=0	
	return x 
print(fib(n))
