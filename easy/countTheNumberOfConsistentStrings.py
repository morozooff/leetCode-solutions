class Solution:
    def countConsistentStrings(self, allowed, words):
        right_words_count = 0
        allowed_list = list(allowed)

        for word in words:
            if set(list(word)).issubset(allowed_list):
                right_words_count += 1

        return right_words_count