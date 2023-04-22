def get_dividend( dividend, divisor):
    while dividend % divisor == 0:
        dividend //= divisor
    return dividend


def isUgly( n) :
    if n <= 0:
        return False
    ugly_div = [2, 3, 5]

    # n = self.get_dividend(n, 2)
    for elem in [2, 3, 5]:
        n = get_dividend(n, elem)

    return n == 1

print(isUgly(7))