def hammingWeight(n):
    binary_string = str(bin(n))
    counter = 0
    for bit in binary_string:
        if bit == '1':
            counter += 1
        else:
            pass

    return counter

print(hammingWeight(11111111111111111111111111111101))