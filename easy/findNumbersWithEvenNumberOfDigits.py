class Solution:
    def findNumbers(self, nums):
        counter = 0
        for num in nums:
            qualifier = len(str(num))
            if qualifier % 2 == 0:
                counter += 1
            else:
                pass

        return counter