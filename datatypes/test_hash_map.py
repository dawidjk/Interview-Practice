import unittest
from hash_map import HashMap

length = 3

class TestHashMap(unittest.TestCase):
	def test_put_and_get(self):
		hash_map = HashMap(length)

		hash_map.put("Hello", "there")
		hash_map.put("Hi", "stranger")
		hash_map.put("Welcome", "rando")
		hash_map.put("Enjoy", "your day")
		hash_map.put("Goodbye", ", till we meet again!")

		self.assertEqual(hash_map.get("Hello"), "there")
		self.assertEqual(hash_map.get("Welcome"), "rando")
		self.assertEqual(hash_map.get("Goodbye"), ", till we meet again!")

	def test_update(self):
		hash_map = HashMap(length)

		hash_map.put("Hello", "there")
		hash_map.put("Hi", "stranger")
		hash_map.put("Welcome", "rando")
		hash_map.put("Enjoy", "your day")
		hash_map.put("Goodbye", ", till we meet again!")

		hash_map.update("Hello", "Goodbye")
		hash_map.update("Goodbye", "Hello")

		self.assertEqual(hash_map.get("Hello"), "Goodbye")
		self.assertEqual(hash_map.get("Goodbye"), "Hello")

	def test_get_empty(self):
		hash_map = HashMap(length)

		hash_map.put("Hello", "there")
		hash_map.put("Hi", "stranger")
		hash_map.put("Welcome", "rando")
		hash_map.put("Enjoy", "your day")
		hash_map.put("Goodbye", ", till we meet again!")

		self.assertEqual(hash_map.get("Nothing is here"), None)

if __name__ == '__main__':
	unittest.main()