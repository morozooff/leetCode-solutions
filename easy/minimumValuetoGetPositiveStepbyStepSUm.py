class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if nums[0] < 0:
            startValue = abs(nums[0]) + 1
        else:
            startValue = 1

        while True:
            value_list = []
            pointer = startValue

            for num in nums:
                res = pointer + num
                if res > 0:
                    pointer = res
                    value_list.append(res)
                    continue
                else:
                    break

            if len(nums) == len(value_list):
                return startValue

            startValue += 1