vals = { "A":1 , "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H": 8, "I":9, "J": 10, "K": 11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z": 26}


def word_to_number(word):
    word_str = list(word)
    word_val = 0
    for i in range(len(word_str)):
        word_val += vals[str(word_str[i])]

    return(word_val)

def is_triangle(n):
    if n < 0:
        return False
    sum_n = 0
    num = 1
    while sum_n <= n:
        sum_n += num
        if sum_n == n:
            return True
        num += 1
    return False


f = open('words.txt','r')
words = f.read()
words = words.strip()
words = words.split(',')
words = [i.replace('"', '') for i in words]

#print(words)

count = 0
for i in range(len(words)):
    if is_triangle(word_to_number(words[i])):
        count += 1

print("Answer: ", count)


