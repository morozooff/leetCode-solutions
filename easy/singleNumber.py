def singleNumber(nums):
    stack = []
    for i in range(len(nums)):
        if nums[i] in stack:
            stack.remove(nums[i])
            continue
        stack.append(nums[i])
    return stack[0]