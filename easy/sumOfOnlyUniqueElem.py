class Solution:
    def sumOfUnique(self, nums: list) -> int:
        frequency = {}

        for num in nums:
            if num not in frequency.keys():
                frequency[num] = num
            else:
                frequency[num] = 0

        return sum(frequency.values())