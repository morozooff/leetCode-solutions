class Solution:
    def numberOfMatches(self, n: int) -> int:

        def isEven(n):
            if n % 2 == 0:
                return True

        match_counter = 0

        while n != 1:
            if isEven(n):
                n = n//2
                match_counter += n
            else:
                n = (n-1)//2
                match_counter += n
                n += 1

        return match_counter