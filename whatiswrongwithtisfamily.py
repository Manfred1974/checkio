from collections import defaultdict

def is_family(tree):
    anscestor = defaultdict(set)
    for father, son in tree:
        if father == son: return False
        if father in anscestor[son]: return False
        if son in anscestor[father]: return False
        if anscestor[father] & anscestor[son]: return False
        anscestor[son] |= {father} | anscestor[father]
    adam = [person for person in anscestor if not anscestor[person]]
    return len(adam) == 1


def is_family(tree):
    i = 1
    n = 1
    print("x")
    while (i < len(tree)):
        k = 0
        while (k < i):
            subtree = tree[i]
            subtree2 = tree[k]
            if (((subtree2[0] == subtree[0]) or (subtree2[0] == subtree[1]) or (subtree2[1] == subtree[0]))):
                n += 1
            if (subtree2[1] == subtree[1]):
                return False
            k += 1
        i += 1

    if (n == len(tree)):
        return True
    else:
        return False

