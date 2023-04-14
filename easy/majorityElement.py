def majorityElement(nums):
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1
    major = max(counter.values())

    for key, value in counter.items():
        if value == major:
            return key

nums = [3, 2, 3]
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
