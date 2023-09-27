def pentagon(n):
    pentagon = (n*(3*n-1))/2
    return(pentagon)

def is_pentagon(n):
    if (1 + (24*n+1)**0.5)%6 == 0:
        return True
    return False

pentagons = []
for i in range(2200): 
    pentagons.append(pentagon(i))


ans = 100000000

for i in range(1,2200):
    for j in range(1,2200):
        if is_pentagon(abs(int(pentagons[i] - pentagons[j]))):
            #print(abs(pentagons[i] - pentagons[j]))
            if is_pentagon(int(pentagons[i] + pentagons[j])) :
                print(pentagons[i] + pentagons[j],i,j)
                if abs(int(pentagons[i] - pentagons[j])) < ans and j != i:
                    ans = abs(int(pentagons[i] - pentagons[j]))
                    print("strike", i, j, ans)



print('Answer:' , ans)
