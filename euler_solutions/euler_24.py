from itertools import permutations

lexigraphic_permutations = list(permutations("0123456789"))

solution = ''.join(lexigraphic_permutations[999999])

print(solution)
