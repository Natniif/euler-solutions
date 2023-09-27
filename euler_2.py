y = 1 
x = 0

next = 0
ans = 0 

while next<4000000:
    next = x + y
    x = y 
    y = next
    if next%2 == 0: 
        ans += next; 
        
print("the answer is:" , ans) 
