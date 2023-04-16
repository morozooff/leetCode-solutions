def containsDuplicate(nums):
    counter = {}
    isDuplicate = False
    for i in nums:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
            if counter[i] == 2:
                return True
    return  isDuplicate

nums = [1,2,3,4]
print(containsDuplicate(nums))

nums = [1,2,3,1]
print(containsDuplicate(nums))

nums = [3,1]
print(containsDuplicate(nums))
