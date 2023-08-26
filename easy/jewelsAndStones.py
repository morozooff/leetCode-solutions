class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        types_jewels = list(jewels)
        result = 0
        for jewel in types_jewels:
            result += stones.count(jewel)
        return result
