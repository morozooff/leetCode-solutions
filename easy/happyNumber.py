def convert(n):
    result = []
    while n > 0:
        result.append(n % 10)
        n //= 10
    result.reverse()
    return result


def isHappy(n):
    check_list = []
    result = False
    while n not in check_list:
        check_list.append(n)
        summa = 0
        for num in convert(n):
            summa += num * num
        if summa == 1:
            result = True
            break
        else:
            n = summa
    return result


print(isHappy(19))