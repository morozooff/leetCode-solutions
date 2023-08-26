class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        pattern = list('balloon')
        tested = list(text)
        counter = 0
        flag = True

        while True:
            current_pattern = pattern.copy()
            for symb in pattern:
                if symb in tested:
                    tested.remove(symb)
                    current_pattern.remove(symb)
                else:
                    flag = False
                    break

            if flag:
                counter += 1
            else:
                break

        return counter
