import time
start = time.time()

def is_prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            return False
    return True

def factors(num):
    factors = []
    for i in range(2,num + 1):
        if num%i ==0 and num not in factors:
            factors.append(i)
    return factors

# finds number of prime factors
def prime_fac(n):
    facs = factors(n)
    num = 0
    for i in range(len(facs)):
        if is_prime(facs[i]):
            num += 1
    return num



def prime_fac(number):
    """function which will return
    the number of prime factors"""
    i = 2
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)
# need to start from a number 
j = 2*3*5*7


while True:
    if prime_fac(j) == 4:
        j += 1
        if prime_fac(j) == 4:
            j += 1
            if prime_fac(j) ==4 :
                j += 1
                if prime_fac(j) == 4:
                    print(j-3)
                    break
    j += 1


end = time.time()
print(end - start)

# this is shit!!!!
# try:
#     for i in range(643,1000):
#         first = factors(i) 
#         for x in range(len(first)):
#             primes1 = 0
#             if is_prime(first[x]):
#                 primes1 += 1
#
#             if primes1 != 3:
#                 break
#             elif primes1 == 3:
#                 second = factors(i+1)
#                 for y in range(len(second)):
#                     primes2 = 0
#                     if is_prime(second[y]):
#                         primes2 += 1 
#                     
#                     if primes2 != 3:
#                         break
#                     else:
#                         third = factors(i + 2)
#                         for p in range(len(third)):
#                             primes3 = 0
#                             if is_prime(third[p]):
#                                 primes3 += 1
#                             if primes3 != 3:
#                                 break
#                             else:
#
#                                 #
#                                 # fourth = factors(i+3)
#                                 # for k in range(len(fourth)):
#                                 #     if is_prime(fourth[k]) == False:
#                                 #         i += 1
#                                 #         break
#                                 #     else:
#                                 #         ans = i
#                                 raise StopIteration
# except StopIteration:
#     print(i)
#
#         
