class Solution:
    def maxProductDifference(self, nums: list) -> int:
        sort_nums = nums.sort(reverse=True)
        w, x = nums[0], nums[1]
        y, z = nums[len(nums) - 1], nums[len(nums) - 2]

        return (w * x) - (y * z)