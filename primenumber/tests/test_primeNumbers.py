import unittest
from  primeNumbers.PrimeNumbers import PrimeNumbers


class simpleTests(unittest.TestCase):

    def testing_with_eight(self):
        prime = PrimeNumbers()
        self.assertEqual(prime.list_primenumbers(8),[2,3,5,7])

    def testing_with_11(self):
        prime = PrimeNumbers()
        self.assertEqual(prime.list_primenumbers(11),[2,3,5,7,11])

    def test_is_divisible_4_by_2(self):
        prime= PrimeNumbers()
        self.assertEqual(prime.is_divisible(2,4),True)

    def test_isdivisible_7_3(self):
        prime=PrimeNumbers()
        self.assertEqual(prime.is_divisible(3,7),False)

    def test_is_prime_7(self):
        prime = PrimeNumbers()
        self.assertEqual(prime.is_prime(7),True)

    def test_is_prime_10(self):
        prime = PrimeNumbers()
        self.assertEqual(prime.is_prime(70),False)
