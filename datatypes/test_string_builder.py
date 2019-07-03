import unittest
from string_builder import StringBuilder

class TestStringBuilder(unittest.TestCase):
	def test(self):
		string_builder = StringBuilder()
		string_builder.append("I ")
		string_builder.append("like ")
		string_builder.append("pi!")

		self.assertEqual(string_builder.toString(), "I like pi!")

if __name__ == '__main__':
	unittest.main()