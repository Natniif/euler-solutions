def divisible(n):
    i = 2
    while i < 21:
        if n%i ==0:
            i += 1
        else:
            return False
    return True

print(divisible(232792560))

"""
smallest = 100088888
for k in range(2549, 232792562):
    if k < smallest and divisible(k):
        smallest = k
    
print("Anser:", smallest)


a =50000

i = 2

while i < 21:
    if a%i == 0:
        i += 1
    else:
        a = a + 1
        i =2

print(a)
"""
    
            
        
    
