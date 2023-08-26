class Solution:
    def replaceDigits(self, s: str) -> str:

        def shift(symb, shift_value):
            ascii_num = ord(symb)
            new_symb = chr(ascii_num + shift_value)
            return new_symb

        new_s = ''

        def isEven(num):
            return num%2==0

        for i in range(len(s)):
            if isEven(i):
                current_symb = s[i]
                new_s += current_symb
            else:
                new_s += shift(current_symb, int(s[i]))

        return new_s