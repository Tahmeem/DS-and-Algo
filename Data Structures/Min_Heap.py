class MinHeap:
	def __init__(self,capacity):
		self.storage = [0]*capacity #initialize array for heap
		self.capacity = capacity
		self.size = 0 

	def getParentIndex(self,index):
		return (index-1)//2 #Formula to get parent

	def getLeftChildIndex(self,index):
		return 2 * index + 1 

	def getRightChildIndex(self,index):
		return 2 * index + 2

	def hasParent(self,index):
		return self.getParentIndex(index) >= 0 

	def hasLeftChild(self,index):
		return self.getLeftChildIndex(index) < self.size 

	def hasRightChild(self,index):
		return self.getRightChildIndex(index) < self.size


	def parent(self,index):
		return self.storage[self.getParentIndex(index)]  

	def leftChild(self,index):
		return self.storage[self.getLeftChildIndex(index)]  

	def rightChild(self,index):
		return self.storage[self.getRightChildIndex(index)]

	def isFull(self):
		return self.size == self.capacity
	def swap(self,index1,index2):
		self.storage[index1],self.storage[index2] = self.storage[index2],self.storage[index1] 


	def heapifyUp(self):
		index = self.size - 1 
		while (self.hasParent(index) and self.parent(index) > self.storage[index]): #Comparing parent to current node
			self.swap(self.getParentIndex(index),index)
			index = self.getParentIndex(index)		


	def insert(self,data):
		if self.isFull():
			print("Full")
			return 
		self.storage[size] = data
		self.size += 1 
		self.heapifyUp()

			
	



