import unittest
from app.calculator import Calculator

class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Correct result tests
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2,2)
        self.assertEqual(4,result)

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(10,2)
        self.assertEqual(8,result)

    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply(15,3)
        self.assertEqual(45,result)

    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide(100,5)
        self.assertEqual(20,result)

    # Test for when both args are not numbers
    def test_calculator_add_if_both_args_are_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    def test_calculator_subtract_if_both_args_are_not_numbers(self):
        self.assertRaises(ValueError, self.calc.subtract, [1,2,3], 'three')

    def test_calculator_multiply_if_both_args_are_not_numbers(self):
        self.assertRaises(ValueError, self.calc.multiply, { 'one': '1'}, '2')

    def test_calculator_divide_if_both_args_are_not_numbers(self):
        self.assertRaises(ValueError, self.calc.divide, (1,3,5), 'eleven')


    # Tests for when x is not a number
    def test_calculator_add_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    def test_calculator_subtract_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.subtract, (2,4), 3)

    def test_calculator_multiply_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.multiply, {'x': 'four'}, 3)

    def test_calculator_divide_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.divide, [15], 3)


    # Tests for when y is not a number
    def test_calculator_add_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')

    def test_calculator_subtract_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.subtract, 100, {'y': 'four'})

    def test_calculator_multiply_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.multiply, 65, [15])

    def test_calculator_divide_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.divide, 2, (1,))

    # Test divide_by_zero
    def test_calculator_divide_by_zero_returns_error_message(self):
        self.assertRaises(ZeroDivisionError,self.calc.divide, 15, 0)

if __name__ == '__main__':
    unittest.main()