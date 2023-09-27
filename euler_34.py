def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return(fact)


def curious(n):
    str_n = str(n) 
    num  = [int(i) for i in str(n)]
    #print(num)
    total = 0
    for i in range(len(num)):
        total += factorial(int(num[i]))
        #print(total)
    if total == n:
        return True
    return False 

sum = 0
for i in range(3,100000):
    if curious(i):
        sum += i


print(sum)
