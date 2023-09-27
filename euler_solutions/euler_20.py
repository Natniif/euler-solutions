def factorial(n):
    factorial = 1
    i = n
    while i >0: 
        factorial *= i
        i -= 1

    return(factorial)    
        
hundred = factorial(100)

sum_of_digits = 0
for i in str(hundred):
    sum_of_digits += int(i) 


print(sum_of_digits)
