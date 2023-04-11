def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = int((start+end)/2)
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess < target:
            start = mid + 1
        elif guess > target:
            end = mid - 1

    return end+1


nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))


target2 = 2
print(searchInsert(nums, target2))

target3 = 7
print(searchInsert(nums, target3))

target4 = 0
print(searchInsert(nums, target4))