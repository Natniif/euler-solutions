import math
#
#def recurring_cycle_length(n): 
#    count = 0 
#    fraction = str(1/n)
#    if math.isinf(n): 
#        for i in fraction: 
#            for j in range(1,100): 
#                if fraction(i) == fraction(j):
#                    print(i,j)
#                    for k in range(i-j):
#                        if fraction(i + k) == fraction(j + k):
#                            count += 1
#                        else: 
#                            break
#    return(count)
#


def recurring_cycle_length(n):
    fraction = str(1/n)    
    frac_lst = list(fraction)
    frac_lst.pop(0)
    frac_lst.pop(0)
    print(frac_lst)
    for i in frac_lst:
        for j in range(len(frac_lst)):
             
#There is a way to do this with primes i think from googling but cba rn 

print(recurring_cycle_length(7))
#print(1/6)
