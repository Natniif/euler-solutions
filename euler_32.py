def is_pandigital(m1,m2,p):
    obj = ['1','2','3','4','5','6','7','8','9']
    nums = []
    lstm1 = list(str(m1))
    lstm2 = list(str(m2))
    lstp = list(str(p))


    for i in range(len(lstm1)):
        nums.append(lstm1[i])
    for j in range(len(lstm2)):
        nums.append(lstm2[j])
    for k in range(len(lstp)):
        nums.append(lstp[k])
    
    nums.sort()
    if nums == obj: 
        return True 
    else: 
        return False


sum_of_products = []
for i in range(1, 100):
    for j in range(1,1000):
        k = i*j
        if is_pandigital(i,j,k):
            if k not in sum_of_products:
                sum_of_products.append(k)

for i in range(1, 9):
    for j in range(1,10000):
        k = i*j
        if is_pandigital(i,j,k):
            if k not in sum_of_products:
                sum_of_products.append(k)



print(sum_of_products)
answer = 0
for i in range(len(sum_of_products)):
    answer += sum_of_products[i]    

print("Answer: ", answer)


