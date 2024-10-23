def max_product(nums):
    if not nums:
        return 0
    cur_max, cur_min = nums[0], nums[0]
    result = nums[0]
    for num in nums[1:]:
        if num < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(num, cur_max * num)
        cur_min = min(num, cur_min * num)
        result = max(result, cur_max)
    return result

if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print("Max Product Subarray:", max_product(nums))
