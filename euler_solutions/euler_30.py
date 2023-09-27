sum_of_fifth = 0
for i in range(2,2000000): 
    string = str(i)
    sum_of_powers =0
    for j in string:
        sum_of_powers +=int(j)**5
    if sum_of_powers == i:
        sum_of_fifth += sum_of_powers

print(sum_of_fifth)

