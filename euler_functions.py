from itertools import permutations


class NumFunctions:
    def __init__(self,number: int):
        self.number = number
        self.string = str(number)
    def is_prime(self):

        for i in range(2,int(self.number**0.5) + 1):
            if self.number%i == 0:
                return False
        return True

    def all_primes_in_range(self):
        '''This is called the sieve of Eratosthenes and creates a boolean array of numbers (True and False) in the range of the 
        number and returns all numbers in array that are true'''
        #run validations on number
        assert self.number>=0, f"{self.number} is not a positive number, make sure to input is positive number"

        prime = [True for i in range(self.number + 1)]
        primes = [] 
        p = 2
        while p * p <= self.number:
        # If prime[p] is not
        # changed, then it is a prime
            if (prime[p] == True):
                # Updating all multiples of p to false as they have a factor
                for i in range(p * p, self.number+1, p):
                    prime[i] = False
            p += 1
     
        # Print all prime numbers
        for p in range(2, self.number+1):
            if prime[p]:
                primes.append(p)

        return primes

    def factors(self):
        factors = []
        for i in range(1,self.number + 1):
            if self.number%i ==0 and self.number not in factors:
                factors.append(i)
        


    def is_factor(self, num2):
        x = factors(self.number)
        if num2 in x:
            return True
        return False

    def nth_prime(self):
        #run validations on number
        assert self.number>=0, f"{self.number} is not a positive number, make sure to input is positive number"

        if self.number == 1:
            return 2
        count = 1
        num = 3
        while count <= self.number:
            number = NumFunctions(num)
            if number.is_prime():
                count += 1
                if count == self.number:
                    return num
            num += 2
        
    def num_permutations(self):
        return [''.join(p) for p in permutations(self.string)] 


class StringFunctions: 
    def __init__(self,string):
        self.string = string
        self.len = len(string)
        
    def str_permutations(self):
        return [''.join(p) for p in permutations(self.string)] 



if __name__ == '__main__':
    test_num = NumFunctions(23)
    if test_num.is_prime():
        print('hell')
    print(test_num.all_primes_in_range())
    print(test_num.num_permutations())
    print(test_num.nth_prime())

