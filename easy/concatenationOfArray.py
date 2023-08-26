def getConcatenation(nums) :
    duplicate = nums.copy()
    nums.extend(duplicate)
    return nums

nums = [1, 2, 1]
print(getConcatenation(nums))