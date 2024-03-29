from linked_list import LinkedList

class HashMap:
	def __init__(self, length):
		self.map = []
		self.length = length
		for x in range(0, length):
			self.map.append(LinkedList())

	def put(self, key, value):
		hashed = hash(key)
		self.map[hashed % self.length].add_node(value, key)

	def get(self, key):
		hashed = hash(key)
		found = self.map[hashed % self.length].find_key(key)

		if found is not None:
			return found.data
		
		return None

	def update(self, key, value):
		if self.get(key) is None:
			self.put(key, value)

		else:
			hashed = hash(key)
			self.map[hashed % self.length].find_key(key).data = value

if __name__ == '__main__':
	map = HashMap(10)
	map.put("Hello", "there")
	map.put("Hi", "stranger")
	map.put("Welcome", "rando")
	map.put("Enjoy", "your day")

	print("Enjoy: " + map.get("Enjoy"))
	print("Hello: " + map.get("Hello"))
