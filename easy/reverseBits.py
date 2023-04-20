def reverseBits(n):
    digits = "01"
    r = ""
    radix = 2
    while (n > 0):
        k = n % radix
        r = digits[k] + r
        n = n // radix

    binary_str = r.zfill(32)
    reverse_string = binary_str[::-1]
    return int(reverse_string, 2)