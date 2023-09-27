def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i ==0:
            return False
    return True
    
primes = []
for i in range(2,10000):
    if is_prime(i):
        primes.append(i)


sum_of_primes = []
consec_count = []

for i in range(len(primes)):
    for j in range(i+1,i + len(primes[i:])):
        if is_prime(sum(primes[i:j])):
            if sum(primes[i:j]) < 1000000:
                consec_count.append(len(primes[i:j]))
                sum_of_primes.append(sum(primes[i:j]))
         
         


max_count = max(consec_count)
biggest_sum = sum_of_primes[consec_count.index(max_count)]

print(biggest_sum)

