vals = { "A":1 , "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H": 8, "I":9, "J": 10, "K": 11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q"
:17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z": 26}

def names_to_number(name):
    str_name = list(name)
    name_number = 0
    for i in range(len(name)):
        name_number += vals[str_name[i]] 
    return(name_number)



with open('names.txt') as f:
    names = f.read()

names = names.strip().split(',')
names = [x[1:-1] for x in names]
names.sort()

score = 0 

for i in range(len(names)):
    score += (i+1)* names_to_number(names[i])



print(score)

#with open("names.txt","r") as f: 
#    names = f.readlines()
#
#print(names.strip("")



#
#summ_value = 0
#for i in range(len(names)): 
#    summ_value += names_to_number(names[i])
#
#print(sum_value)
#
