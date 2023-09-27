def same_digits(a,b):
    lst_a = list(str(a))
    lst_b = list(str(b))
    if sorted(lst_a) == sorted(lst_b):
        return True
    return False

for i in range(1,1000000):
    if same_digits(i*2, i*3):
        if same_digits(i*3,i*4):
            if same_digits(i*4,i*5):
                if same_digits(i*5, i*6):
                    print(i)
                    break

