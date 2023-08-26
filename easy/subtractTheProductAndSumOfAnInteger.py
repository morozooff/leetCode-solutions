class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        values = []
        while n > 0:
            values.append(n % 10)
            n = n // 10

        mult = 1
        for value in values:
            mult *= value

        return mult - sum(values)