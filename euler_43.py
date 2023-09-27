from itertools import permutations

primes = [2,3,5,7,11,13,17]

def property(n):
    lstn = list(str(n))
#    print(lstn)
    for i in range(1,8):
#        print(int(lstn[i] + lstn[i+1] + lstn[i+2]))
        if (int(lstn[i] + lstn[i+1] + lstn[i+2]))%primes[i-1] != 0:
#            print("pass", i, lstn[i], primes[i-1])
            return False
#        else:
#            print("fail", i, lstn[i], primes[i-1])
    return True

if property(1406357289):
    print("ok")

perms = [''.join(p) for p in permutations('0123456789')]


ans = 0
for i in range(len(perms)):
    if property(perms[i]):
        ans += int(perms[i])

print("Answer: ", ans)
