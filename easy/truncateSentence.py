class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splitted_s = s.split(' ')
        new_s = ''

        for i in range(k):
            new_s += splitted_s[i] + ' '

        return new_s.strip()