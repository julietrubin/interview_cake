import itertools

def number_of_ways(amount, denominations):
	return_list = []
	for denominator in denominations:
		if amount == denominator:
			return_list.append([denominator])
		elif denominator < amount:
			for way in number_of_ways(amount - denominator, denominations):
				if way != None:
					way.append(denominator)
					return_list.append(way)
	# we want to remove dublicate combinations
	return_list =  sorted([sorted(comb) for comb in return_list])
	return list(k for k,_ in itertools.groupby(return_list))