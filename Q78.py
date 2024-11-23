def mergeStones(stones, K):
    n = len(stones)
    if (n - 1) % (K - 1) != 0:
        return -1
    dp = [[[float('inf')] * n for _ in range(n)] for _ in range(n)]
    for length in range(K):
        for start in range(n - length):
            end = start + length
            dp[start][end][length] = sum(stones[start:end+1]) if length + 1 == K else 0
    return dp[0][n - 1][0]

print(mergeStones([3, 5, 1, 2, 6], 3))
