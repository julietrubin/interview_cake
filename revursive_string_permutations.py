

def get_permutations(input_string):
	if len(input_string) == 1:
		return [input_string]
		
	perm_list = []
	for i in range(len(input_string)):	
		for perm in get_permutations(input_string[:i] + input_string[i+1:]):
			perm_list.append(input_string[i] + perm)
		
	return perm_list