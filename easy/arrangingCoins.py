def arrangeCoins(n):
    counter = -1
    i = 1
    while n >= 0:
        counter += 1
        n -= i
        i += 1
    return counter