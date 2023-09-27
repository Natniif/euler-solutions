def divisors(n): 
    divisor = 0
    for i in range(1, int(n/2)+1):
        if n%i ==0:
            divisor += i
    return(divisor)

def abundant_number(n): 
    if divisors(n) > n:
        return True
    return False

def sum_of_divisors(n):
    for i in range(1,n//2):
        if abundant_number(i):
            if abundant_number(n-i):
                return True
    return False


sum_of_false = 0
for i in range(28123):
    if sum_of_divisors(i) == False:
        sum_of_false += i 
        print(sum_of_false)

print(sum_of_false)


#
# abundant_nums = []
# for i in range(int(28124/2)): 
#     if abundant_number(i):
#         abundant_nums.append(i)
#
#
# all_sums = []
# for i in range(len(abundant_nums)):
#     for j in range(len(abundant_nums)):
#         all_sums.append(abundant_nums[i] + abundant_nums[j])
#
#
# sum1 = 0
# for i in range(len(all_sums)): 
#     sum1 += all_sums[i]
#
# sum2 = 0
# for i in range(1,28123): 
#     sum2 += i
#
# print(sum1)
# print(sum2)
#
# print(sum2 - sum1)
#




#
#def is_sum_in_list(n,num_list):
#    for n1 in num_list:
#        for n2 in num_list:
#            if n1 + n2 == n:
#                return True
#    return False
#
#
##list_of_sums_of_abundants = []
##for k in range(len(abundant_nums)):
##    for l in range(len(abundant_nums)):
##       list_of_sums_of_abundants.append(abundant_nums[k] + abundant_nums[l])
##
#
#not_sum_of_abundants = 0
#
#for i in abundant_nums:
#    for j in range(i,len(abundant_nums)):
#        
#         
#
#
#print(not_sum_of_abundants)        
