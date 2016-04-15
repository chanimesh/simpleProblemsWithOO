class PrimeNumbers:
    def __init__(self):
        self.primenum=[]

    def is_divisible(self, divisor, dividend):
        if dividend % divisor == 0:
            return True
        return False

    def is_prime(self,num):
        for i in range(2,num):
            if self.is_divisible(i,num):
              return False
        return True

    def list_primenumbers(self,end):
        for i in range(2,end+1):
            if self.is_prime(i):
                self.primenum.append(i)
        return self.primenum