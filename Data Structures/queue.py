from collections import deque

example_queue = deque()

q.appendleft(5)
q.appendleft(6)
q.appendleft(10)

q.pop() #5

class Queue:
	def __init__(self):
		self.buffer = deque()

	def enqueue(self,val):
		self.buffer.appendleft(val)
	
	def dequeue(self):
		return self.buffer.pop()

	def is_empty(self):
		return len(self.buffer)== 0 

	def size(self):
		return len(self.buffer) 