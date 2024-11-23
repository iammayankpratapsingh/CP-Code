def subsets(nums):
    result = [[]]
    for num in nums:
        result += [item + [num] for item in result]
    return result

print(subsets([1, 2, 3]))
