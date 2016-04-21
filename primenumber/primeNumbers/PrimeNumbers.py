import math
class PrimeNumbers:
    def __init__(self):
        self.primenum=[2]

    def __is_prime(self,num):
        for i in range(2,int(math.ceil(math.sqrt(num))+1)):
            if num % i == 0:
              return False
        return True

    def list_prime_numbers(self, end):
        if end < 1:
            return "error"
        i=2
        while len(self.primenum) < end:
            if self.__is_prime(i):
                self.primenum.append(i)
            i = i+1
        return self.primenum