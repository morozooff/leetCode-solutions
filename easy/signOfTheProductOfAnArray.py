def arraySign(nums):
    result = 1
    for i in nums:
        result *= i
    print(result)
    if result == 0:
        return 0
    elif result > 0:
        return 1
    else:
        return -1