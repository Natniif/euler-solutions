def sequence(n):
    length = 1
    number =n
    while number > 1:
        if number%2 ==0:
            number = number/2
            length += 1
        else:
            number = (3*number) + 1
            length += 1
    return length

print(sequence(13))

largest_number = 0
longest_sequence = 0

for i in range(1,1000001):
    if sequence(i) > longest_sequence:
        longest_sequence = sequence(i)
        largest_number = i
        print(largest_number)

print(largest_number)
