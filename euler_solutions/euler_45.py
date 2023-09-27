def is_triangle(n):
    if n < 0:
        return False
    sum_n = 0
    num = 1
    while sum_n <= n:
        sum_n += num
        if sum_n == n:
            return True
        num += 1
    return False

def is_pentagon(n):
    if (1 + (24*n+1)**0.5)%6 == 0:
        return True
    return False

def is_hexagon(N):
    val = 8 * N + 1
    x = 1 + sqrt(val)
 
    # Calculate the value for n
    n = x / 4
 
    # Check if n - floor(n)
    # is equal to 0
    if ((n - int(n)) == 0):
        return True
    else:
        return False


for i in range(25000, 30000):
    hexagon = i*(2*i - 1)
    if is_triangle(hexagon):
        if is_pentagon(hexagon):
            print(hexagon)
            break
#
#for i in range(20000, 30000):
#    triangle = i*(i + 1)/2
#    for j in range(20000, 30000):
#        pentagon = j*(3*j -1)/2
#        if triangle == pentagon:
#            for k in range(20000, 30000):
#                hexagon = k*(2*k -1)
#                if triangle == pentagon == hexagon: 
#                    ans = (i*(i + 1)/2)
#                    print("Answer: ",ans) 
#                    break
