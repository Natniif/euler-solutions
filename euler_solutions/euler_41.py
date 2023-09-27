import itertools

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

# def uses_digits(n):
#     list_n = list(str(n))
#     numbers = []
#     for i in range(1,len(list_n)+1):
#         numbers.append(str(i))
#     list_n.sort()
#     if list_n == numbers:
#         return True
#     return False

largest = 0

ten = list(itertools.permutations('1234567'))
print(''.join(ten[1]))
print(len(ten))

for i in range(len(ten)):
    num = int(''.join(ten[i]))
    if num % 2 == 0:
        pass
    else:

        if is_prime(int(num)):
            print('found', num)
            if num > int(largest):
                largest = num 

print("Answer: ", largest)

