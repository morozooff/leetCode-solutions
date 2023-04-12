def merge(nums1, m, nums2, n):
    del nums1[m:len(nums1)]
    nums1.extend(nums2)
    nums1.sort()

nums1 = [1, 2, 3, 0, 0,0]
m = 3
nums2 = [2, 5, 8, 6]
n = 4

merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0

merge(nums1, m, nums2, n)
print(nums1)

