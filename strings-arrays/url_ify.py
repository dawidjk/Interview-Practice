import unittest

def url_ify(given, length):
	# loop  through string backwards
	# if character is not space, move as far back as possible
	# else, insert as far back and 0 then 2 then %
	to_modify = bytearray(given)
	write_space = len(to_modify) - 1

	for i in range(length - 1, 0, -1):
		if to_modify[i] is 32:
			to_modify[write_space] = '0'
			to_modify[write_space - 1] = '2'
			to_modify[write_space - 2] = '%'
			write_space -= 3

		else:
			to_modify[write_space] = to_modify[i]
			write_space -= 1

	return str(to_modify)

class TestURLify(unittest.TestCase):
	def test_empty_string(self):
		self.assertEqual(url_ify("", 0), "")

	def test_all_spaces(self):
		self.assertEqual(url_ify("         ", 4), "%20%20%20")

	def test_one_space(self):
		self.assertEqual(url_ify("Hello There  ", 11), "Hello%20There")

	def test_string_multiple_spaces(self):
		self.assertEqual(url_ify("Mr John Smith    ", 13), "Mr%20John%20Smith")

if __name__ == '__main__':
	unittest.main()
