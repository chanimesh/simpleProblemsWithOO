import unittest
from primeNumbers.PrimeNumbers import PrimeNumbers


class simpleTests(unittest.TestCase):

    def setUp(self):
        self.prime = PrimeNumbers()

    def test_list_prime_numbers_with_one(self):
        self.assertEqual(self.prime.list_prime_numbers(1), [2])

    def test_list_prime_numbers_with_more_than_one(self):
        self.assertEqual(self.prime.list_prime_numbers(3), [2, 3, 5])

    def test_list_prime_numbers_with_more_than_two(self):
        self.assertEqual(self.prime.list_prime_numbers(5), [2, 3, 5, 7, 11])

    def test_list_prime_numbers_with_negative_number(self):
        self.assertEqual(self.prime.list_prime_numbers(-1), "error")