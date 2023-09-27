def incorrect_frac(a,b): 
    lst_a = list(str(a))
    lst_b = list(str(b))
    #print(lst_a)
    #print(lst_b)
    if int(lst_a[1]) == 0 and int(lst_b[1]) == 0: 
        return False
    elif int(lst_a[0]) == int(lst_b[0]) and int(lst_a[1]) == int(lst_b[1]):
        return False
    else:
        for i in range(len(lst_a)):
            #print(i)
            for j in range(len(lst_a)):
                #print(j)
                if lst_a[j] == lst_b[i]:
                    lst_a.pop(j)
                    lst_b.pop(i)
                    #print(lst_a)
                    #print(lst_b)
                    if int(lst_a[0]) == 0 or int(lst_b[0]) == 0: 
                        return False
                        break
                    elif a/b == int(lst_a[0])/int(lst_b[0]):
                        return True 
                        break
                    break
            break
    return False

if incorrect_frac(11,13):
    print("hello")
else: 
    print("no")

    
numerator= []
denomenator = []
for i in range(11,100):
    #print("numerator",i)
    for j in range(11,100): 
        #print("denomenator", j)
        if incorrect_frac(i,j):
            numerator.append(i)
            denomenator.append(j)
            #print(numerator)
            #print(denomenator)

print(numerator, denomenator)            

top = 1
for i in range(len(numerator)):
    top *= numerator[i]     


bottom = 1
for i in range(len(denomenator)):
    bottom *= denomenator[i]

print(top, bottom)


frac = top/bottom
print(frac)


