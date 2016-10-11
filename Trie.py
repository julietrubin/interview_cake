class Trie:
	def __init__(self):
		self._root = {}
	def add(self, item):
		current_dict = self._root
		for c in item:
			if not current_dict.get(c):
				current_dict[c] = {}
			current_dict = current_dict[c]
		current_dict['*'] = '*'
		
	def get(self, item):
		current_dict = self._root
		for c in item:
			if not current_dict.get(c):
				return False
			current_dict = current_dict[c]	
		if not current_dict.get('*'):
			return False
		return True