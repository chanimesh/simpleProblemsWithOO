import unittest
from  primeNumbers.PrimeNumbers import PrimeNumbers


class simpleTests(unittest.TestCase):

    def __init__(self):
        prime = PrimeNumbers()

    def test_list_primenumberrs_with_non_prime_end(self):
        prime = PrimeNumbers()
        self.assertEqual(prime.list_primenumbers(8),[2,3,5,7])

    def test_list_primenumberrs_with_prime_end(self):
        self.assertEqual(self.prime.list_primenumbers(11),[2,3,5,7,11])

    def test_is_divisible_with_zero_remainder(self):
        self.assertEqual(self.prime.is_divisible(2,4),True)

    def test_is_divisible_with_non_zero_remainder(self):
        self.assertEqual(self.prime.is_divisible(3,7),False)

    def test_is_prime_with_prime(self):
        self.assertEqual(self.prime.is_prime(7),True)

    def test_is_prime_with_non_prime(self):
        self.assertEqual(self.prime.is_prime(70),False)
