def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    buy, sell, cooldown = [-prices[0]] * 2 + [0]
    for i in range(1, n):
        buy = max(buy, cooldown - prices[i])
        sell = max(sell, buy + prices[i])
        cooldown = max(cooldown, sell)
    return sell

print(maxProfit([1, 2, 3, 0, 2]))
