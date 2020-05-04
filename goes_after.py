def goes_after(word: str, first: str, second: str) -> bool:
    res = tuple(word)
    if word == '':
        return False
    else:
        try:
            for i in range(len(res)):
                f = res[i]
                s = res[i+1]
                while first == f and second == s:
                    True
                    break
                else:
                    return False
        except IndexError:
            pass

    for i in res:
        f = res.index(i), i
        s = res.index(i + 1), i
        if first == i and second == e:
            return True

    for i in range(len(word)):
        if first = word[i]