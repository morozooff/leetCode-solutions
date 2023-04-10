value = {1: 1, 2: 2}
def climbStairs(n):
    if n in value:
        return value[n]
    else:
        value[n] = climbStairs(n-1) + climbStairs(n-2)
        return value[n]

print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
