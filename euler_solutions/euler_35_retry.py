def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i ==0:
            return False
    return True

def circular(n):
    if is_prime(n):
        lst = list(str(n))
        # print(''.join(lst))
        if len(lst) > 1:
            for i in range(len(lst) - 1):
                store = lst[0]
                lst.pop(0)

                lst.append(store)
                test = ''.join(lst)
                # print(test)
                if is_prime(int(test)) == False:
                    # print('not prime')
                    return False
            return True
            
        else:
            return True
    return False
            
circular(23)




ans = 0
for i in range(1,1_000_000):
    if circular(i):
        ans += 1
        print(i)


print(ans)
