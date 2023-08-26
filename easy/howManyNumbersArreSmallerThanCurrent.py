class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []

        for num1 in nums:
            counter = 0

            for num2 in nums:
                if num1 > num2:
                    counter += 1
                else:
                    pass
            result.append(counter)

        return result