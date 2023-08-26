class Solution:
    def bitwiseComplement(self, n: int) -> int:
        trans = str(bin(n))
        real_part = trans[2:len(trans)]
        result = ''
        for symb in real_part:
            if symb == '1':
                result = result + '0'
            else:
                result = result + '1'
        result_str = '0b' + result

        return int(result_str, 2)