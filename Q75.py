def maxSumOfThreeSubarrays(nums, k):
    n = len(nums)
    total = sum(nums[:k])
    left = [0] * n
    right = [0] * n
    for i in range(k, n):
        total += nums[i]
    left[k - 1] = sum(nums[:k])
    right[n - k] = sum(nums[n - k:])
    for i in range(k, n):
        left[i] = max(left[i - 1], sum(nums[i - k + 1:i + 1]))
    for i in range(n - k - 1, -1, -1):
        right[i] = max(right[i + 1], sum(nums[i:i + k]))
    return max(left + right)

print(maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2))
