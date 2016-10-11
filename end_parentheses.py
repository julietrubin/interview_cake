

def find_index_closing_parenthesis(beginning_index, sentence):
	parenthesis_count = sentence.count('(', 0, beginning_index + 1)
	end_paren_count = 0 
	i = len(sentence)
	while end_paren_count < parenthesis_count:
		i -= 1		
		if sentence[i] == ')':
			end_paren_count += 1	
	print i
			
