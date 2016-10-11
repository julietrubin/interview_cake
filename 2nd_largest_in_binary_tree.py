

def get_largest_and_parent(root):
	parent_node = root 
	largest_node = root.right 

	while(largest_node.right ! = None){
		parent_node = current_node
		largest_node = partent_node.right
	}
	return largest_node, parent_node
	
def get_second_largest(root):
	largest_node, parent_node = get_largest_and_parent(root)
	if largest_node.left == None:
		return parent_node
		
	largest_node, parent = get_largest_and_parent(current_node.left)
	return largest_node