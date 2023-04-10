from collections import Counter

def isValid(s):
    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for bracket in s:
        if bracket in brackets:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != brackets[stack.pop()]:
            return False
    return len(stack) == 0


s = "()[]{}"
print(isValid(s))
s = "(){]"
print(isValid(s))
s = "{[]}"
print(isValid(s))
s = "{[}]"
print(isValid(s))

s = ''
print(isValid(s))