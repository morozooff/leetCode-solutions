class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        summ = 0
        char_list = list(chars)
        for word in words:
            char_list_for_comparision = char_list.copy()
            result = ''
            for symb in word:
                if symb in char_list_for_comparision:
                    result += str(symb)
                    char_list_for_comparision.remove(symb)

            if len(result) == len(word):
                summ += len(word)
                #char_list = char_list_for_comparision
            else:
                pass

        return summ

words = ["cat", "bt", "hat", "tree"]
chars = "atach"