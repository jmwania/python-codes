"""Tests for longer string function"""
import unittest
from longestWord import longer_word


class TestLongerString(unittest.TestCase):
    """Class to test longer string function"""

    def test_string_1_is_string(self):
        """Method to test if str1 is a string"""
        str1 = 2
        str2 = "Mammoth"
        self.assertEqual(longer_word(str1, str2), "All inputs must be string")

    def test_string_2_is_string(self):
        """Method to test if str2 is a string"""
        str1 = "Mammoth"
        str2 = 456.36
        self.assertEqual(longer_word(str1, str2), "All inputs must be string")

    def test_for_equal_length_strings(self):
        """Method to test if both strings are equal"""
        str1 = "Andela"
        str2 = "Andela"
        result = str1 + "\n" + str2
        self.assertEqual(longer_word(str1, str2), result)

    def test_for_longer_string_1(self):
        str1 = "Thor"
        str2 = "Iron Man"
        self.assertEqual(longer_word(str1, str2), str2)

    def test_for_longer_string_2(self):
        str1 = "My Feelings"
        str2 = "Kiki Challenge"
        self.assertEqual(longer_word(str1, str2), str2)


if __name__ == '__main__':
    unittest.main()
