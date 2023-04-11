def romanToInt(s):
    romanDict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    counter = {
        'I': 0,
        'V': 0,
        'X': 0,
        'L': 0,
        'C': 0,
        'D': 0,
        'M': 0
    }
    roman = list(s)
    print(roman)
    for i in range(len(roman)-1, -1, -1):
        if roman[i] in romanDict:
            if i == 0:
                counter[roman[i]] += 1
            elif romanDict[roman[i]] <= romanDict[roman[i - 1]]:
                counter[roman[i]] += 1
            elif romanDict[roman[i]] > romanDict[roman[i - 1]]:
                counter[roman[i]] += 1
                counter[roman[i-1]] -= 2
            else:
                print("что-то не так")
        else:
            exit(0)
    result = 0
    for i in counter:
        result += counter[i] * romanDict[i]
    return result

s = 'LIVIII'
romanToInt(s)
