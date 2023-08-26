def firstUniqChar(s):
    frequency = {}
    for symb in s:
        if symb not in frequency:
            frequency[symb] = 1
        else:
            frequency[symb] += 1
    print(frequency)
    for symb_value in frequency:
        if frequency[symb_value] == 1:
            return s.index(symb_value)
    return -1