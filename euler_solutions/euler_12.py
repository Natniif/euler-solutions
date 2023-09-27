def triangle_num(n):
    triangle = 0
    for i in range(1,n+1):
        triangle += i
    return(triangle)

def factors(n):
    num_of_factors =  0
    for j in range(1, int((n)**0.5 + 1)):
        if n%j ==0:
            num_of_factors += 2
        if j*j ==n:
            num_of_factors -= 1
    return num_of_factors




for i in range(50000):
    triangle = triangle_num(i)
    if factors(triangle) > 500:
        print("Answer:", triangle)
        break
