class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        def divider(num):
            num_parts = []

            while num >= 1:
                num_parts.append(num%10)
                num = num//10

            return num_parts


        frequency ={}

        for num in range(lowLimit, highLimit+1):
            num_parts = divider(num)
            sum_of_digits = sum(num_parts)

            if sum_of_digits not in frequency.keys():
                frequency[sum_of_digits] = 1
            else:
                frequency[sum_of_digits] += 1

        return max(frequency.values())