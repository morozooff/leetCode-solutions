from collections import defaultdict


def removeDuplicates(nums):
    unique_nums = sorted(list(set(nums)))
    k = len(unique_nums)
    count = {
    }
    for i in range(len(unique_nums)):
        nums[i] = unique_nums[i]
    return k


nums = [-1,0,0,0,0,3,3]

print(removeDuplicates(nums))
print(nums)
