def pythag_check(a,b,p):
    try:
        c = (a**2 + b**2)**0.5
        if a + b + c == p:
            return True
        else: 
            return False
    except ValueError:
        print('input has to be an intiger')

def number_of_solutions(p):
    ans = 0
    for i in range(p//2):
        for j in range(p//2):
            
            if pythag_check(i,j,p):
                ans += 0.5
                
    return ans

max = 0
ans = 0
for p in range(3,1000):
    if number_of_solutions(p) > max:
        max = number_of_solutions(p)
        ans = p

print(ans)

