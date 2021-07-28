class TreeNode:
	def __init__(self,data):
		self.data = data
		self.children = []
		self.parent = None

	def add_child(self,child):
		child.parent = self
		self.children.append(child)

	def get_level(self):
		level = 0 
		p = self.parent
		while p:
			level += 1 
			p = p.parent
		return level

	def print_tree(self):
		spaces = ' ' * self.get_level() * 2 
		print(spaces+self.data)
		if self.children:
			for i in self.children:
				i.print_tree()

def product_tree():
	root = TreeNode("Courses")

	Science = TreeNode("Science")
	root.add_child(Science)
	Biology = TreeNode("Biology")
	Chemistry = TreeNode("Chemistry")
	Physics = TreeNode("Physics")
	Science.add_child(Biology)	
	Science.add_child(Chemistry)
	Science.add_child(Physics)
	return root

top = product_tree()
top.print_tree()