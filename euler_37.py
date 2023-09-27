def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(0.5)) + 1):
        if n%i == 0:
            return False 
    return True 

def all_prime_right(n):
    lst_n = list(str(n))
    length1 = len(lst_n)
    if is_prime(n):
        for i in range(length1-1, 0, -1):
            length = len(lst_n)
            num =   ''.join([str(j) for j in lst_n])
            num_int = int(num)
            if is_prime(num_int):
                lst_n.pop(length-1)
                num2 = ''.join([str(j) for j in lst_n])
                num2_int = int(num2)
                if is_prime(num2_int) == False:
                    return False
                    break
            else:
                return False
                break
        return True


def all_prime_left(n):
    lst_n = list(str(n))
    length = len(lst_n)
    if is_prime(n):
        for i in range(0,length -1):
            num =   ''.join([str(j) for j in lst_n])
            num_int = int(num)
            if is_prime(num_int):
                lst_n.pop(0)
                num2 = ''.join([str(j) for j in lst_n])
                num2_int = int(num2)
                if is_prime(num2_int) == False:
                    return False
                    break
            else:
                return False
                break
        return True

truncable_primes = []
sum_of_truncable_primes = 0

for i in range(10,1000000):
    if all_prime_left(i) and all_prime_right(i):
        truncable_primes.append(i)
        sum_of_truncable_primes += i

print(truncable_primes, sum_of_truncable_primes)
    
