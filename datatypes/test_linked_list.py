import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
	def test_add_node_and_first(self):
		linked_list = LinkedList()
		linked_list.add_node(1)

		self.assertEqual(linked_list.first().data, 1)

	def test_add_node_last(self):
		linked_list = LinkedList()
		linked_list.add_node(1)

		self.assertEqual(linked_list.last().data, 1)

	def test_add_node_last(self):
		linked_list = LinkedList()
		linked_list.add_node(1)
		linked_list.add_node(2)

		self.assertEqual(linked_list.last().data, 2)

	def test_find_value(self):
		linked_list = LinkedList()
		linked_list.add_node(1, 'a')
		linked_list.add_node(2, 'b')
		linked_list.add_node(3, 'c')
		linked_list.add_node(4, 'd')

		self.assertEqual(linked_list.find(3).key, 'c')

	def test_find_key(self):
		linked_list = LinkedList()
		linked_list.add_node(1, 'a')
		linked_list.add_node(2, 'b')
		linked_list.add_node(3, 'c')
		linked_list.add_node(4, 'd')

		self.assertEqual(linked_list.find_key('d').data, 4)

if __name__ == '__main__':
	unittest.main()