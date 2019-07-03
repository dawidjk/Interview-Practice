from array_list import ArrayList

class StringBuilder:
	def __init__(self):
		self.list = ArrayList()

	def append(self, string):
		self.list.add(string)

	def toString(self):
		# This doesn't mimick well in python
		return "".join(self.list.get())
