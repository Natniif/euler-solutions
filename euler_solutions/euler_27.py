def prime(n): 
    for i in range(2,int(abs(n)**(0.5))+1):
        if n%i == 0: 
            return False 
    return True

def equation(n,a,b): 
    return(n**2 + a*n + b)

def consecutive_primes(a,b):
    n = 0
    largest = 0
    for i in range(1000):
        n = i**2 + i*a + b
        
        if prime(n) == False:
            largest = i - 1 
            break
        elif prime(n):
            i += 1
    return(largest)

print(consecutive_primes(1,41))


largest = 0
product = 0 
for i in range(-1000,1000):
    for j in range(-1000,1000):
            if largest < consecutive_primes(i,j):
                largest = consecutive_primes(i,j)
                product = i*j
    

print(product)

