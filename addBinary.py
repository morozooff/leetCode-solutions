def addBinary(a, b):
    result = ''
    temp = 0
    if len(a) != len(b):
        a = a.zfill(len(b))
        b = b.zfill(len(a))

    for i in range(len(a)-1, -1, -1):
        result += str((int(a[i]) + int(b[i]) + temp) % 2)
        temp = (int(a[i]) + int(b[i]) + temp) // 2
    if temp != 0:
        result += str(temp)

    return result[::-1]


a = "11"
b = "1"

print(addBinary(a, b))

a1 = "1010"
b1 = "1011"
print(addBinary(a1, b1))

a2 = '0'
b2 = '0'
print(addBinary(a2, b2))

a2 = '1'
b2 = '1'
print(addBinary(a2, b2))

a2 = '0000'
b2 = '0000'
print(addBinary(a2, b2))

a1 = "1010"
b1 = "1011"

print(bin(int(a1, 2)+int(b1, 2))[2:])