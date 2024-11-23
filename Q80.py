def longestArithSeqLength(A):
    n = len(A)
    dp = [{} for _ in range(n)]
    max_len = 2
    for i in range(1, n):
        for j in range(i):
            diff = A[i] - A[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            max_len = max(max_len, dp[i][diff])
    return max_len

print(longestArithSeqLength([3, 6, 9, 12]))
