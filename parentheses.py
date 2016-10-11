import sys

openers = ['(', '{', '[']
closers = [')', '}', ']']
openers_to_closers = { '(': ')', '{': '}', '[': ']'}

def properly_nested(code_string):
	opener_closer_stack = []
	for c in code_string:
		if c in openers:
			opener_closer_stack.append(c)
		elif c in closers:
			if len(opener_closer_stack) == 0:
				return False
			opener = opener_closer_stack.pop(len(opener_closer_stack)-1)
			if openers_to_closers[opener] != c:
				return False
	return 	len(opener_closer_stack) == 0:
	
print properly_nested(sys.argv[1]) 