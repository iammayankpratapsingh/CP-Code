from itertools import permutations

def lexicographicalPermutations(s):
    return sorted([''.join(p) for p in permutations(s)])

print(lexicographicalPermutations("abc"))
