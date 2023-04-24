def lastStoneWeight(stones):
    while len(stones) > 1:
        y = stones.pop(stones.index(max(stones)))
        x = stones.pop(stones.index(max(stones)))
        sub_stone = y - x
        if sub_stone != 0:
            stones.append(sub_stone)

    if len(stones) == 0:
        return 0
    else:
        return stones[0]

print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1]))