#def concatenate(x):
#    for i in x:
#        
#    str_a = str(a)
#    str_b = str(b)
#    str_c = str(c)
#    return(str_a + str_b + str_c)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def same_digits(a,b):
    orda = sorted(str(a))
    ordb = sorted(str(b))
    if orda == ordb:
        return True
    return False
        
ans = []

nums = list(range(1000, 9999))


for i in range(len(nums)):
    if is_prime(nums[i]):
        print('hit', nums[i])
        for j in range(i+1, len(nums)):
            if same_digits(nums[i], nums[j]) and is_prime(nums[j]):
                print('hit', nums[j])
                dist = nums[j] - nums[i]
                for k in range(j+1, len(nums)):
                    if same_digits(nums[k], nums[j]) and is_prime(nums[k]) and dist == nums[k] - nums[j]:
                        ans.append(nums[i])
                        ans.append(nums[j])
                        ans.append(nums[k])
#
# for i in range(len(nums)):
#     count = 1
#     prime = []
#     for j in range(i+1,len(nums)):
#         if same_digits(nums[i],primes[j]):
#             if nums[i] not in prime:
#                 count +=1 
#                 prime.append(str(nums[j]))
#                 if str(nums[i]) not in primes:
#                    prime.append(str(nums[i]))
#
#                 elif count == 3:
#                     print(prime)
#                     answer = ''.join(prime)
#                     ans.append(answer)
#
# test
print(ans)
            
