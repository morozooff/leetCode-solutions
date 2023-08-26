class Solution:
    def sumBase(self, n: int, k: int) -> int:

        def from_10_to_k(n, k):
            new = ''

            while n > 0:
                remainder = n % k
                new = str(remainder) + new
                n = n // k

            return new

        summ = 0
        new_num = from_10_to_k(n, k)

        for num in new_num:
            summ += int(num)

        return summ
