def findTheDifference(s, t):


    while len(t) != 1:

        if t[0] in s:
            rem_elem = t[0]
            t.remove(rem_elem)
            s.remove(rem_elem)

    return str(t)

print(findTheDifference("abcd", "abcde"))