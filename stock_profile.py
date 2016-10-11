from decimal import Decimal


def best_profile(stock_array):
	max_profile = 0
	# we keep track of smallest so we can find the difference of that and a future price
	lowest_price = Decimal('Infinity')
	
	
	for price in stock_array:
		if price < lowest_price:
			lowest_price = price
		elif price - lowest_price > max_profile:
			# this price might be less than the max_price 
			# but still have a greater profile if we have found a new lowest_price
			max_profile = price - lowest_price
		
	return max_profile