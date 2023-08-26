class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        array_of_founded_indixies = []
        for num_symb in range(len(s)):
            if s[num_symb] == c:
                array_of_founded_indixies.append(num_symb)

        for num_symb in range(len(s)):
            difference_list = [abs(num_symb - index) for index in array_of_founded_indixies]
            result.append(min(difference_list))

        return result