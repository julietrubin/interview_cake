class Node:
	def __init__(self, left, right, value):
		self.left = left
		self.right = right
		self.value = value
		
def is_valid_binary_tree(root, greater_than_value, less_than_value):
	if root.left.value > root.value or root.right.value < root.value:
		return False
	if root.value > less_than_value or root.value < greater_than_value:
		return False
	left_is_valid = True if root.left.value == None or \
		is_valid_binary_tree(root.left, ,less_than_value)
	right_is_valid = True if root.right.value == None or \
		is_valid_binary_tree(root.right, )
	return left_is_valid and right_is_valid