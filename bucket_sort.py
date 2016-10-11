

def get_sorted_scores(unsorted_scores, highest_possible_score):
	count_list = [0] * (highest_possible_score + 1)
	
	for score in  unsorted_scores:
		count_list[score] += 1
		
	sorted_scores = []
	for i in range(len(count_list)):
		sorted_scores.extend([i] * count_list[i])
		
	return sorted_scores