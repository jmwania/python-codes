"""test for switch reverser function"""
import unittest
from switchReverser import switch_reverser


class TestSwitchReverser(unittest.TestCase):
    """Class to test switch reverser"""

    def test_word_only_list(self):
        """Method to test for word-only list"""
        myList = ["Centaurs", "Hocruxes", "Muggles"]
        result = ["CENTAURS", "HOCRUXES", "MUGGLES"]
        self.assertEqual(switch_reverser(myList), result)

    def test_integer_only_list(self):
        """Method to test for integer-only list"""
        myList = [1, 2, 3, 4, 5]
        result = [5, 4, 3, 2, 1]
        self.assertEqual(switch_reverser(myList), result)

    def test_mixed_list(self):
        """Method to test a list with both integers and words"""
        myList = [1, 2, "Muggles", "Hogwarts"]
        self.assertEqual(switch_reverser(myList), myList)


if __name__ == '__main__':
    unittest.main()
