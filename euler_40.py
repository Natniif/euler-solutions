def list_maker(n):
    number = [int(x) for x in str(n)]
    return(number)

print(list_maker(10))




num = []
for i in range(1,1000000):
    number = list_maker(i)
    for j in range(len(number)):
        num.append(number[j])

print(num[0]*num[9]*num[99]*num[999]*num[9999]*num[99999]*num[999999])


