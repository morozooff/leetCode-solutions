def moveZeroes(nums):
    stack = []
    iterator = 0

    while iterator != len(nums):
        if nums[iterator] == 0:
            stack.append(nums.pop(iterator))
            print(stack)
        else:
            iterator += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)