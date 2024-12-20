def rob(nums):
    if not nums:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + (dp[i - 2] if i > 1 else 0))
    return dp[-1]

print(rob([2, 7, 9, 3, 1]))
