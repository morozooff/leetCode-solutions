def plusOne(digits):
    if digits[0] == 9:
        digits.insert(0, 0)
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            break
        else:
            digits[i] = 0
    if digits[0] == 0:
        digits.remove(0)
    return digits


digits = [9, 9, 9]
print(plusOne(digits))

digits2 = [9,8,7,6,5,4,3,2,1,0]
print(plusOne(digits2))