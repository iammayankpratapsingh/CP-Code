def two_sum(nums, target):
    num_map = {}
    result = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            result.append((complement, num))
        num_map[num] = i
    return result

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Pairs with Target Sum:", two_sum(nums, target))
