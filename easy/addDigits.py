def addDigits(num):
    while num >= 10:
        b = list(map(int, str(num)))
        num = sum(b)

    return num