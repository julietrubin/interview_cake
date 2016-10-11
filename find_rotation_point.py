def get_rotation_index(dictionary_list):	
	start_index = 0
	end_index = len(dictionary_list) - 1
	while(True):
		if end_index - start_index == 0:
			# base case only one index left
			return start_index
				
		# when there are only two indexes left, mid index will be the same at start_index
		mid_index = (end_index - start_index) / 2 + start_index
		if dictionary_list[mid_index] > dictionary_list[end_index]:
			start_index = mid_index + 1
		elif dictionary_list[mid_index] < dictionary_list[start_index]:
			end_index = mid_index - 1
		else:
			return start_index