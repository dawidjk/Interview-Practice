import unittest
from array_list import ArrayList

values_add = 10

class TestArrayList(unittest.TestCase):
	def test_add(self):
		array_list = ArrayList()

		for i in range(0, values_add):
			array_list.add(i)

		self.assertEqual(array_list.length, values_add)

	def test_remove(self):
		array_list = ArrayList()

		for i in range(0, values_add):
			array_list.add(i)

		for i in range(0, values_add/2):
			array_list.remove(i)

		self.assertEqual(array_list.length, values_add/2)

	def test_remove_value(self):
		array_list = ArrayList()

		for i in range(0, values_add):
			array_list.add(i)

		for i in range(0, values_add/2):
			array_list.remove_value(i)

		self.assertEqual(array_list.length, values_add/2)

	def test_get(self):
		array_list = ArrayList()

		for i in range(0, values_add):
			array_list.add(i)

		for i in range(0, values_add):
			self.assertEqual(array_list.get(i), i)

if __name__ == '__main__':
	unittest.main()