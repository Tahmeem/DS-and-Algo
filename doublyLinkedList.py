class Node:
	def __init__(self,data):
		self.data = data
		self.nref = None
		self.pref = None

class doublyLinkedList:
	def __init__(self):
		self.head = None 

	def insertEmpty(self,data):
		if self.head == None:
			newNode = Node(data)
			self.head = newNode
		else:
			return 

	def insertStart(self,data):
		if self.head == None: #Empty list 
			newNode = Node(data)
			self.head = newNode 
			return 
		newNode = Node(data)
		newNode.nref = self.head
		self.head.pref = newNode
		self.head = newNode

	def insertEnd(self,data):
		if self.head == None: #Empty list 
			newNode = Node(data)
			self.head = newNode 
			return 	
		n = self.head
		while n.nref:
			n = n.nref 

		newNode = Node(data)
		n.nref = newNode
		newNode.pref = n 

	def insertafterItem(self, x, data):
		if self.head == None:
			return
		else:
			m = self.head
			while n:
				if n.data == x:
					break 
				n = n.nref
			if n:
				print("Not available")
				return
			else:
				newNode = Node(data)
				newNode.pref = n
				newNode.nref = n.nref
				if n.nref:
					n.nref.pref = newNode
				n.nref = newNode 
