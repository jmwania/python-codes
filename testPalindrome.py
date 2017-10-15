import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):

	def test_with_punctuation_and_spaces(self):
		self.assertEqual(is_palindrome("A Toyota's a Toyota"),True)
	def test_case_1(self):
		self.assertEqual(is_palindrome("race car"),True)
	def test_case_2(self):
		self.assertEqual(is_palindrome("Red rum, sir, is murder"),True)
	def test_case_3(self):
		self.assertEqual(is_palindrome("Eva, can I see bees in a cave?"),True)
	def test_case_4(self):
		self.assertEqual(is_palindrome("No lemon, no melon"),True)
	def test_false_1(self):
		self.assertEqual(is_palindrome("selfless"),False)
	def test_false_2(self):
		self.assertEqual(is_palindrome("sentences"),False)
	def test_non_string_input(self):
		self.assertEqual(is_palindrome(123321),False)
	def test_list_input(self):
		self.assertEqual(is_palindrome(["racecar","Ava"]),False)

if __name__ == '__main__':
	unittest.main()