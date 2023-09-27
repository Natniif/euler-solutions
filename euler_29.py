def powers(a,b):
    sequence = []
    if 2 <= a and 2 <= b: 
        for i in range(2,a+1):
            for j in range(2,b+1): 
                value = i**j
                if value not in sequence:
                    sequence.append(value)
    return(sequence)


print(len(powers(100,100)))                        
