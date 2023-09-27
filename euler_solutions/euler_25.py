def fibonacci(n):
    fib = [3,1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return(sum(fib))        

for i in range(1,1000000) :
    if len(str(fibonacci(i))) == 1000:
        print(i+2)
        break



