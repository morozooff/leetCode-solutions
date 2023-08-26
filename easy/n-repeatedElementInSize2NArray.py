class Solution:
    def repeatedNTimes(nums):
        n = len(nums)//2

        frequency = {}
        for elem in nums:
            if elem not in frequency:
                frequency[elem] = 1
            else:
                frequency[elem] += 1

            if frequency[elem] == n:
                return elem