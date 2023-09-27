from itertools import permutations

def prod(n):
    lst_n = list(str(n))
    print(lst_n)
    bang = 1
    for i in range(len(lst_n)):
        bang *= lst_n[i] 
    return(bang)

print(prod(3))

numbers = [1,2,3,4,5,6,7,8,9]

nums = ([a for a in permutations(numbers)])

largest = 0
highest = 987654322
lowest = 123456789
product = []
for i in range(1, 200):
    concantated_prod = 0
    for j in range(1,5):
        concantated_prod += i*j
        if concantated_prod > lowest:
            product.append(concantated_prod)


print(product)

print(largest)
