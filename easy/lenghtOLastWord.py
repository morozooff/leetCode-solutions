def lenghtOfLastWord(s):
    lst = s.split()
    return len(lst[len(lst)-1])





s = "Hello World"
print(lenghtOfLastWord(s))