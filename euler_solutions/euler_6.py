a = list(range(1,101))

sum_a = sum(a)
sum_of_squares = 0

print(a[2]**2)

print(a)

i = 0
while i < 100:
    square = a[i]**2
    sum_of_squares += square
    i += 1

sum_a_squared = (sum_a)**2

print(sum_a_squared)
print(sum_of_squares)

print(sum_a_squared - sum_of_squares)
    
