class ArrayList:
	def __init__(self):
		self.length = 0
		self.allocated = 1
		self.array = [None]
		self.resize_factor = 2

	def add(self, data):
		if self.length == self.allocated:
			self.allocated = self.resize_factor * self.allocated
			temp = [None] * self.allocated

			for i in range(0, self.length):
				temp[i] = self.array[i]

			self.array = temp

		self.array[self.length] = data
		self.length += 1

	def remove(self, index):
		if index > self.length:
			return

		for i in range(index, self.length):
			self.array[i - 1] = self.array[i]

		self.array[self.length] = None
		self.length -= 1

	def remove_value(self, to_remove):
		for i in range(0, self.length):
			if self.array[i] == to_remove:
				self.remove(i)

	def get(self, index):
		if index > self.length:
			return None

		return self.array[index]

	def get(self):
		to_return = []

		for i in range(0,self.length):
			to_return.append(self.array[i])

		return to_return

	def length(self):
		return self.length

