import unittest
import newPrime

class TestPrime(unittest.TestCase):

    def test_prime(self):
        self.assertEqual(newPrime.is_prime(10), False)
        self.assertEqual(newPrime.is_prime(999), False)
        self.assertEqual(newPrime.is_prime(79), True)
        self.assertEqual(newPrime.is_prime(2), True)
        self.assertEqual(newPrime.is_prime(1007), False)
        self.assertEqual(newPrime.is_prime(7), True)

if __name__ == '__main__':
    unittest.main()