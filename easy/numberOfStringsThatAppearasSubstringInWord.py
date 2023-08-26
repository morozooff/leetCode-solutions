class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        def isSubstring(pattern, word):
            if pattern in word:
                return True

        counter = 0

        for pattern in patterns:
            if isSubstring(pattern, word):
                counter += 1

        return counter