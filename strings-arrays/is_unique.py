# Are all characters in a string unique?

import unittest

# Assuming ASCII
characters = 128

def is_unique_easy(string):
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
	def test_empty_easy(self):
		self.assertTrue(is_unique_easy(""))

	def test_true_easy(self):
		self.assertTrue(is_unique_easy("abczyx"))

	def test_false_easy(self):
		self.assertFalse(is_unique_easy("aabbcc"))

if __name__ == '__main__':
	unittest.main()