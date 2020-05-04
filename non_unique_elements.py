from collections import Counter

data = [1, 2, 3, 1, 3]


def checkio(data: list) -> list:
    dup = {k for k, v in Counter(data).items() if v > 1}
    res = [l for l in data if l in dup]
    return res
