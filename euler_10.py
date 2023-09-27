def is_prime(n):
    for i in range(2,int(n**(0.5))  + 1):
        if n%i ==0:
            return False
    return True

sum_of_primes = 0
for j in range(2,2000000):
    if is_prime(j):
        sum_of_primes += j

print("Answer: ", sum_of_primes)

