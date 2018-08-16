"""Test for pig latin"""
import unittest
from pigLatin import pig_latin_converter


class TestPigLatinConverter(unittest.TestCase):
    """Class to test pig latin converter"""

    def test_empty_string(self):
        word = ""
        self.assertEqual(pig_latin_converter(
            word), "String should not be empty")

    def test_pig_latin_1(self):
        """Test 1 for pig latin"""
        word = "will"
        result = "illway"
        self.assertEqual(pig_latin_converter(word), result)

    def test_pig_latin_2(self):
        """Test 2 for pig latin"""
        word = "dog"
        result = "ogday"
        self.assertEqual(pig_latin_converter(word), result)

    def test_pig_latin_3(self):
        """Test 3 for pig latin"""
        word = "category"
        result = "ategorycay"
        self.assertEqual(pig_latin_converter(word), result)

    def test_pig_latin_4(self):
        """Test 4 for pig latin"""
        word = "chatter"
        result = "atterchay"
        self.assertEqual(pig_latin_converter(word), result)

    def test_pig_latin_5(self):
        """Test 5 for pig latin"""
        word = "trash"
        result = "ashtray"
        self.assertEqual(pig_latin_converter(word), result)

    def test_pig_latin_6(self):
        """Test 6 for pig latin"""
        word = "andela"
        result = "andelaway"
        self.assertEqual(pig_latin_converter(word), result)

    def test_pig_latin_7(self):
        """Test 7 for pig latin"""
        word = "electrician"
        result = "electricianway"
        self.assertEqual(pig_latin_converter(word), result)


if __name__ == '__main__':
    unittest.main()
