
def sum_previosly(num):
    result = 0
    for i in range(num):
        result += i
    return result


def missingNumber(nums):
    maxim = len(nums)
    full = sum_previosly(maxim) + maxim
    non_full = sum(nums)
    return full - non_full