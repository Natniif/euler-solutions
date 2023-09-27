from email.base64mime import header_length
import math

def is_prime(n):
    for j in range(2, int(n**0.5) + 1):
        if n%j == 0:
            return False
    return True

i = 0

for k in range(2, 1000000):
    if is_prime(k) == True:
        i += 1
        if i == 10001:
            print(k)





