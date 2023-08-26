class Solution:
    def reverseWords(self, s: str) -> str:
        result_string = ''
        words = s.split()
        for word in words:
            result_string = result_string + word[::-1]+' '

        return result_string.strip()