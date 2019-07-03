# Are all characters in a string unique?

import unittest

# Assuming ASCII
characters = 128

def is_unique(string):
	seen = [0] * characters

	if len(string) > characters:
		return False

	for letter in string:
		val = ord(letter)

		if seen[val] is 1:
			return False

		seen[val] += 1

	return True

class TestIsUnique(unittest.TestCase):
	def is_unique(self):
		self.assertTrue(is_unique_easy(""))

	def is_unique(self):
		self.assertTrue(is_unique_easy("abczyx"))

	def is_unique(self):
		self.assertFalse(is_unique_easy("aabbcc"))

if __name__ == '__main__':
	unittest.main()