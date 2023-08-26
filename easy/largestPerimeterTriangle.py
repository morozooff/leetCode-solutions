def largestPerimeter( nums):
    sorted_nums = sorted(nums, reverse=True)
    result = 0

    while len(sorted_nums) >= 3:
        comparing = sorted_nums[0:3]
        if comparing[0] + comparing[1] > comparing[2] and comparing[1] + comparing[2] > comparing[0] and comparing[2] + \
                comparing[0] > comparing[1]:
            result = sum(comparing)
            break
        else:
            sorted_nums.pop(0)
    return result

print(largestPerimeter([1,2,1,10]))