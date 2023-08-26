class Solution:
    def uniqueOccurrences(self, arr):
        occurence = {}
        for value in arr:
            if str(value) not in occurence:
                occurence[str(value)] = 1
            elif str(value) in occurence:
                occurence[str(value)] += 1

        return len(occurence.values()) == len(list(set(occurence.values())))