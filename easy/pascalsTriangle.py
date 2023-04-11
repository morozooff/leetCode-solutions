
# n - line, k - index
def c(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0

def generate(numRows):
    result = []
    for row in range(numRows):
        lst = [c(row, index) for index in range(row+1)]
        result.append(lst)
    return result

print(generate(30))
print(generate(4))
print(generate(3))
print(generate(2))
print(generate(1))
print(generate(0))
