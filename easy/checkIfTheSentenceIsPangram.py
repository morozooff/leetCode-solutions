class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        frequency = {}

        for symbol in sentence:
            if symbol  not in frequency.keys():
                frequency[symbol] = 1

        if len(frequency) == 26:
            return True
        else:
            return False