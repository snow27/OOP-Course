from itertools import permutations


def possible_permutations(elements):
    perm = permutations(elements)
    for p in perm:
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]

