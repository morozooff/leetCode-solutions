import random

class Solution:
    def sumZero(self, n):

        def generate_unique(array):
            digit = random.randint(-n, n)
            if digit in array or digit == 0:
                return generate_unique(array)
            else:
                return digit

        summ = 0
        result = []

        if n % 2 == 0:
            for num in range(n//2):
                value = generate_unique(result)
                antivalue = 0 - value
                result.append(value)
                result.append(antivalue)
        else:
            result.append(0)
            for num in range((n-1)//2):
                value = generate_unique(result)
                antivalue = 0 - value
                result.append(value)
                result.append(antivalue)

        return result