class Solution:
    def findCenter(self, edges: list) -> int:
        intersection = set(edges[0])&set(edges[1])
        return list(intersection)[0]