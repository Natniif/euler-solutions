def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i ==0:
            return False
    return True

def circular(n):
    if is_prime(n):
        nstr = str(n)
        lstn = list(nstr)
        circular = []
        for i in range(1, len(lstn)):
            if i == lstn.index(max(lstn)):
                store = lstn[i]
                print(store)
                del lstn[i]
                lstn.insert(0,store)
                print(lstn)
                number = ''.join([str(x) for x in lstn])
                print(number)
                if is_prime(int(number)):
                    circular.append(number)

                else:
                    return False
                    break
            else:
                store = ''.join(lstn[i:-1])
                print(store)
                del lstn[i:-1]
                lstn.insert(0,store)
                print(lstn)
                number = ''.join([str(x) for x in lstn])
                print(number)
                if is_prime(int(number)):
                    circular.append(number)
    return True

if circular(197):
    print("Success!")


