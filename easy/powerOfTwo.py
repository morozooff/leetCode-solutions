def isPowerOfTwo(n):
    if n == 0:
        return False
    if n == 1:
        return True

    if n % 2 == 0:
        isPT = isPowerOfTwo(n//2)
    else:
        isPT = False
    return isPT

print(isPowerOfTwo(16))
print(isPowerOfTwo(1))
print(isPowerOfTwo(0))
