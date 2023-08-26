def reverseString(s):
    s = list(s)
    left = 0
    rigth = len(s) - 1

    while left < rigth:
        s[left], s[rigth] = s[rigth], s[left]
        left += 1
        rigth -= 1

reverseString("МИЭТ")