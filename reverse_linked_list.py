class Node:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right
		
		
def reverse_linked_list(head):
	current_node = head
	
	previous = None
	while current_node:
		temp = current_node.right
		current_node.right = previous
		
		previous = current_node
		current_node = temp
	return previous
		
		
		
1 -> 2 -> 3  ->