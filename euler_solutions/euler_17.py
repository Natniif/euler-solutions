initDict1 = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                     11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
                                  18: "Eighteen", 19: "Nineteen",
                                               10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty",
                                                            90: "Ninety", 100: "Hundred", 1000: "Thousand"}

#loop through all numbers in 1000
#for each one create a number written out in a string
#at end of for loop create a long string with .append then find length and print
#if number only has one digit use last number(n)
#if three digits first digit uses hundreds(n) then second digit tens(n) and last number lastnumber(n)
#if three digits add and between hundred and tens
#if second last digit is 1 and last digit is not zero use teens(n)
#

written = []
for i in range(1,10):
    written.append(initDict1[i])

for i in range(10,20):
    written.append(initDict1[i])

for i in range(20,100,10):
    written.append(initDict1[i])
    for j in range(1,10):
        written.append(initDict1[i] + initDict1[j])

for i in range(1,10):
    for j in range(1,10): 
        written.append(initDict1[i] + initDict1[100] + "and" + initDict1[j])

for i in range(1,10):
    for j in range(20,100,10):
        written.append(initDict1[i] + initDict1[100] + "and" + initDict1[j])
        for k in range(1,10): 
            written.append(initDict1[i] + initDict1[100] + "and" + initDict1[j] + initDict1[k])

for i in range(1,10): 
    written.append(initDict1[i] + initDict1[100])

for h in range(1,10):
    for j in range(10,20):
        written.append(initDict1[h]+ initDict1[100] + "and" +  initDict1[j])


written.append(initDict1[1] + initDict1[1000])


print(written)


length = 0
for i in written: 
    length += len(i)

print(length)



#written_num =[] 
#for i in range(1,1001):
#    number = list(i)
#    individual_num = [] 
#    if i == 1000:
#         written_num.append("onethousand")
#         written_num.append(individual_num(i[0])
#    elif i > 99:
#        str_num = str(i)
#        individual_num.append(hundred(i[0]))
#        individual_num.append("and")
#        if i[1] ==1 and i[2] !=0:
#            individual_num.append(teen(i[1])
#    
#        written_num.append(individual_num)
#    elif i > 9:
#            if i[0] ==1 and i[1] !=0:
#            individual_num.append(teen(i[0])
#        else:
#            individual_num.append(tens(i[0])
#            individual_num.append(lastnum(i[1]))
#    
#        written_num.append(individual_num)
#    elif i < 10:
#        individual_num.append(lastnum(i))
#        written_num.append(individual_num)

#print(written_num)
#print(tens(4))
#print(lastnum(5))
#print(teen(6))
#print(hundred(6))


