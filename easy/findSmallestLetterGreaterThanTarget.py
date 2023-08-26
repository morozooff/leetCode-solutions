class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        comp_array = []
        letters_copy = set(letters)

        for i in letters_copy:
            if i > target:
                comp_array.append(i)

        if len(comp_array) == 0:
            return letters[0]
        else:
            return min(comp_array)
