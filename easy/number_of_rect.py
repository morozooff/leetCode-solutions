class Solution:
    def countGoodRectangles(self, rectangles: list) -> int:

        frequency = {}

        for rectangle in rectangles:
            less_part = min(rectangle)

            if less_part in frequency.keys():
                frequency[less_part] += 1
            else:
                frequency[less_part] = 1

        largest_square_key = max(frequency.keys())

        return frequency[largest_square_key]