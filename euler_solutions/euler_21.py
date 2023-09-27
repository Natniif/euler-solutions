def divisors(n): 
    sum_of_divisors  = 0
    for i in range(1,int(n/2) + 1) :
        if n%i == 0:
            sum_of_divisors += i
    return(sum_of_divisors)

sum_of_amicable = 0
for i in range(1,10000):
    if i  == divisors(divisors(i)):
        if i != divisors(i):
            sum_of_amicable = sum_of_amicable + divisors(i) 

print(sum_of_amicable)

