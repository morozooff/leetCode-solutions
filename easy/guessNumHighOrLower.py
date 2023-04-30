# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start<=end:
            middle = (start+end)//2
            guesstion = guess(middle)
            print(guesstion)
            if guesstion == 0:
                return middle
            elif guesstion == 1:
                start = middle + 1
            elif guesstion == -1:
                end = middle - 1