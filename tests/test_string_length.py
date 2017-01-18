import unittest

from main.string_length import string_length

class Length(unittest.TestCase):
	def test_if_int(self):
		self.assertTrue(string_length('abafsh'), str)
	def test_if_list_greater_than_one(self):
		b = string_length(['gamber'])
		if (len(b) > 1) & (isinstance(b, list)):
			self.assertGreater(string_length(9, 1))
			self.assertIsinstance(string_length(['getev']), list)

if __name__ == '__main__':
	unittest.main()