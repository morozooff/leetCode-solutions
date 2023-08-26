class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_dict = {}
        candies = len(candyType)
        eat_permission = candies//2
        print(eat_permission )

        unique_candies= set(candyType)
        candy_count = len(unique_candies)

        result = candy_count - eat_permission

        if result <= 0:
            return candy_count
        else:
            return candy_count - result