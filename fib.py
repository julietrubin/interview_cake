"""
Write a function fib() that a takes an integer n and returns the nth fibonacci ↴ number.
Let's say our fibonacci series is 0-indexed and starts with 0. 
fib(0) # => 0
fib(1) # => 1
fib(2) # => 1
fib(3) # => 2
fib(4) # => 3

Use a memoize approach.
"""


def fib(n):
	fib_list = []
	
	fib_list[0] = 0
	fib_list[1] = 1
	for i in range(2, n+1):
		fib_list[i] = fib_list[i-1] + fib_list[i-2]
	return fib_list[n+1]