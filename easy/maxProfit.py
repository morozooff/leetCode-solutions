def maxProfit(prices):
    diff = 0
    lp = 0
    rp = 1
    while rp != len(prices):
        if prices[lp] > prices[rp]:
            lp += 1
            continue
        elif prices[rp] - prices[lp] > diff:
            diff = prices[rp] - prices[lp]
        rp += 1
    return diff

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
print("__________________")
prices = [1,2,4]
print(maxProfit(prices))
print("__________________")
prices = [7,6,4,3,1]
print(maxProfit(prices))
print("__________________")
prices = [1, 2]
print(maxProfit(prices))

prices = [2,1,2,1,0,1,2]
print(maxProfit(prices))
