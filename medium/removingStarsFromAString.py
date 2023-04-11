# this is solution without f-string
def removeStars(s):
    stack = []
    for i in s:
        if i == "*":
            stack.pop()
            continue
        stack.append(i)
    return ''.join(stack)


# this is beauty solution on Py3 with f-string
def removeStars3(s):
    while '*' in s:
        s = s[:s.index("*")-1] + s[s.index("*")+1:]
    return s

s = "leet**cod*e"
print(removeStars3(s))

s = "leet**cod*e"
print(removeStars(s))