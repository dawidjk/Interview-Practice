# Check to see if two strings are a permutation of one another
import unittest
import sys
import os
sys.path.append(os.path.abspath('../datatypes'))
from hash_map import HashMap

hash_map_length = 128

def check_permutation(one, two):
	if len(one) != len(two):
		return False

	hash_map = HashMap(hash_map_length)

	for char in one:
		quantity = hash_map.get(char)

		if quantity is None:
			hash_map.put(char, 1)
		else:
			hash_map.update(char, quantity + 1)

	for char in two:
		quantity = hash_map.get(char)

		if quantity is None:
			return False
		else:
			hash_map.update(char, quantity - 1)

	for char in one:
		if hash_map.get(char) is not 0:
			return False

	return True


class TestCheckPermutation(unittest.TestCase):
	def test_check_empty_both(self):
		self.assertTrue(check_permutation("", ""))

	def test_check_empty_one(self):
		self.assertFalse(check_permutation("abc", ""))
		self.assertFalse(check_permutation("", "abc"))

	def test_check_equal(self):
		self.assertTrue(check_permutation("hello", "ollhe"))

	def test_check_not_equal(self):
		self.assertFalse(check_permutation("Let's get this bread", "Nah, I'm on a low carb diet"))


if __name__ == '__main__':
	unittest.main()

