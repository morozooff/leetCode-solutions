def sortedSquares( nums):

    squares = []

    for num in nums:
        squares.append(num*num)

    return sorted(squares)


print(sortedSquares([-4,-1,0,3,10]))

