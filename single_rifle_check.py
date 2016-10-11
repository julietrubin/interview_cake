

def is_single_rifle(cards):
	# start at 0 because this is before the first card
	half1_marker = 0
	# if there actually is a second pile of cards this will be updated in the first for loop
	half2_marker_start = half2_marker = None
	
	for card in cards:
		if card - 1 == half1_marker:
			half1_marker += 1
		elif not half2_marker:
			# we found the half2 starting card
			half2_marker_start = card
			half2_marker = card
		elif card - 1 == half2_marker:
			half2_marker += 1
		else:			
			return False
			
	return (half2_marker_start == None) or (half1_marker + 1 == half2_marker_start)
	
print is_single_rifle([])
print is_single_rifle([1,2,3])
print is_single_rifle([1,2,3,4,7,5,8,6])
print is_single_rifle([3,1,4,2,5])
print is_single_rifle([1,2,3,7,8])
print is_single_rifle([7,8, 1,2,3,4,5,9,6])