def kidsWithCandies(candies, extraCandies):
    result = []
    for i in candies:
        if i + extraCandies >= max(candies):
            result.append(True)
        else:
            result.append(False)
    return result

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))