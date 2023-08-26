def isSubsequence(s, t):

    if len(s) == 0:
        return True

    def gen(str):
        for symb in str:
            yield symb
        yield 'True'

    s_symb = gen(s)
    deque = next(s_symb)

    for symb in t:
        if symb == deque:
            deque = next(s_symb)
            if deque == 'True':
                return True

    return False


print(isSubsequence("axc", "ahbgdc"))
