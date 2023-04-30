class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        start = 1
        end = num // 2
        while start <= end:
            middle = (start + end) // 2
            middle_2 = middle * middle
            if num == middle_2:
                return True
            elif middle_2 > num:
                end = middle - 1
            elif middle_2 < num:
                start = middle + 1

        return False