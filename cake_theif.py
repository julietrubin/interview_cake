# https://www.interviewcake.com/question/java/cake-thief
def max_duffel_bag_value(cake_tuples, capacity):
	# create a dict because we only care about the highest values for a given weight and we want to 
	# access the value in constant time 
	cake_dict = {}
	for weight, value in cake_tuples:
		if value > cake_dict.get(weight, None):
			cake_dict[weight] = value	
	return cake_dict
	# keep track of the highest value for capacity at a given index
	# we are using a bottom up approach here 			
	capacity_list = [0]
	for i in range(1, capacity + 1):
		# we initialize the capacity to the highest value of the previous capacity 
		capacity_list.append(capacity_list[i-1])
		for weight in cake_dict.keys():
			adding_value = i - weight
			if adding_value >= 0:
				capacity_list[i] = max(capacity_list[adding_value] + cake_dict.get(weight), capacity_list[i])
				
	return capacity_list[-1]
			
			
print max_duffel_bag_value([(4, 150), (5,200)], 8)
			