from collections import Counter

def permuteUnique(nums):
    def backtrack(path, counter):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in counter:
            if counter[num] > 0:
                counter[num] -= 1
                backtrack(path + [num], counter)
                counter[num] += 1

    result = []
    counter = Counter(nums)
    backtrack([], counter)
    return result

print(permuteUnique([1, 1, 2]))
