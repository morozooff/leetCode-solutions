class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def findRang(num):
            result = []
            while num != 0:
                result.append(num % 10)
                num = num // 10
            return result

        result = []
        for i in range(left, right + 1):
            array = []
            dividers = findRang(i)
            for j in dividers:
                try:
                    k = i % j
                except ZeroDivisionError:
                    k = 1
                array.append(k)

            array = set(array)
            if array == {0}:
                result.append(i)

        return result
