class Queue:
	def __init__(self):
		self._stack1 = []
		self._stack2 = []
	
	def enqueue(self, value):
		self._stack1.append(value)
		
	def dequeue(self):
		if len(self._stack2) == 0:
			if len(self._stack1) == 0:
				raise IndexError()
			self._stack1.reverse() 
			self._stack2 = self._stack1
			self._stack1 = []
			
		return self._stack2.pop()
			
		
		