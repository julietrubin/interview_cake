
def reverse(st):
	st = list(st)
	for i in range(len(st)/2):
		end_index = len(st) - 1 - i
		temp = st[i]
		st[i] = st[end_index]
		st[end_index] = temp
	return ''.join(st)