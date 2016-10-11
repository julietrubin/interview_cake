"""
Write a function that takes an integer flight_length (in minutes) and an array of integers movie_lengths (in minutes) 
and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:
Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory

"""

def get_two_movies(flight_length, movie_lengths):
	movie_length_by_remaining_length = {}
	# populate the movie_length_by_remaining_length dict
	for movie_length in movie_lengths:
		remaining_length = flight_length - movie_length
		# this check assures that we don't write over another movie with the same length 
		if remaining_length == movie_length and movie_length_by_remaining_length.get(remaining_length):
			return True
		movie_length_by_remaining_length[remaining_length] = movie_length
		
	for movie_length in movie_lengths:
		second_movie_length = movie_length_by_remaining_length.get(movie_length)
		# we already check for the case that there are two movies with the same length when populating the dict
		if second_movie_length and second_movie_length != movie_length:
			return True
	return False