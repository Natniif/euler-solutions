def Palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False



def binary_list(n):
    binary = bin(n)
    binary_lst = list(binary)
    binary_lst.pop(0)
    binary_lst.pop(0)
    if Palindrome(binary_lst):
        return True
    return False

s = ['5','8','5']
if binary_list(585) and Palindrome(s):
    print("hello")

ans = 0


for i in range(1,1000000):
    list_i = list(str(i))
    if Palindrome(list_i) and binary_list(i):
        ans += i


print("Answer: ", ans)


