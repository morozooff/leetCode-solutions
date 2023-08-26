class Solution:
    def findRelativeRanks(self, score):

        def hoar_sort(nums):
            if len(nums) <= 1:
                return nums
            else:
                q = nums[len(nums) // 2]
                s_nums = []
                m_nums = []
                e_nums = []
                for num in nums:
                    if num > q:
                        s_nums.append(num)
                    elif num < q:
                        e_nums.append(num)
                    else:
                        m_nums.append(num)
            return hoar_sort(s_nums) + m_nums + hoar_sort(e_nums)

        sort_score = hoar_sort(score)
        result = []

        for unique in score:
            score_index = sort_score.index(unique)
            if score_index == 0:
                result.append("Gold Medal")
            elif score_index == 1:
                result.append("Silver Medal")
            elif score_index == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(score_index + 1))

        return result
