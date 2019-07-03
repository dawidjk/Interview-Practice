import unittest

# Assuming ASCII 128 characters
characters = 128

def palindrome_permutation(string):
	count = [0] * characters
	# Make string lowercase/uppercase if you want to ignore case
	# Can also limit to 26 lowercase characters

	for letter in string:
		count[ord(letter)] += 1

	odds_seen = 0

	for letter in string:
		if count[ord(letter)] % 2 is 1:
			if odds_seen < ((len(string) + 1) % 2) + 1:
				odds_seen += 1
			else:
				return False

	return True

class TestPalindromePermutation(unittest.TestCase):
	def empty_string(self):
		self.assertTrue(palindrome_permutation(""))

	def one_char(self):
		self.assertTrue(palindrome_permutation("1"))

	def two_char_true(self):
		self.assertTrue(palindrome_permutation("11"))

	def two_char_false(self):
		self.assertFalse(palindrome_permutation("12"))

	def full_palindrome(self):
		self.assertTrue(palindrome_permutation("taco cat"))

	def long_string_not(self):
		self.assertFalse(palindrome_permutation("abcdef ghisdfqaaa"))

if __name__ == '__main__':
	unittest.main()
