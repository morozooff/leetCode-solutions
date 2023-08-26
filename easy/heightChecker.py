class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        pairs = list(zip(heights, expected))
        counter = 0
        for height, require in pairs:
            if height != require:
                counter += 1

        return counter