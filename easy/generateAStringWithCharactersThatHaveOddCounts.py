class Solution:
    def generateTheString(self, n: int) -> str:
        min_half = n // 2
        max_half = min_half
        margin = n - (max_half + min_half)

        if max_half % 2 == 0 and min_half % 2 == 0:
            min_half -= 1
            max_half += 1

        if min_half < 0:
            max_half = 0
            min_half = 0

        return ('a' * max_half) + ('b' * min_half) + ('c' * margin)