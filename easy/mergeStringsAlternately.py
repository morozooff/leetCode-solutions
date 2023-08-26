class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        alternating_string = ''
        max_length = max(len(word1), len(word2))

        for i in range(max_length):
            if i < len(word1):
                print(i)
                alternating_string += word1[i]
            else:
                pass

            if i < len(word2):
                alternating_string += word2[i]
            else:
                pass

        return alternating_string