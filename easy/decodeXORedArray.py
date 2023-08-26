class Solution:
    def decode(self, encoded: list, first: int) -> list:

        original = [first]

        for value in encoded:
            current_original_element = original[len(original)-1]
            original.append(current_original_element^value)

        return original