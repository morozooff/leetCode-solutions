# O(n) solution
def removeElement(nums, val):
    nums[:] = [i for i in nums if i != val]
    return len(nums)

# O(n^2)
# this is fast solution on leetcode, but on practice whith big data its not better solution
def removeElement_O(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

nums = [3,2,2,3]
val = 3

print(removeElement(nums, val))
print(nums)

nums1 = [0,1,2,2,3,0,4,2]
val1 = 2

print(removeElement(nums1, val1))
print(nums1)