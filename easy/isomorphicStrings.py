def isIsomorphic(s, t):
    composion = {}
    for position in range(len(s)):
        if s[position] not in composion:
            if t[position] in composion.values():
                return False
            else:
                composion[s[position]] = t[position]
        else:
            if t[position] != composion[s[position]]:
                return False
            else:
                pass
    return True


s = 'badc'
t = 'baba'
print(isIsomorphic(s, t))
s = 'paper'
t = 'title'
print(isIsomorphic(s, t))