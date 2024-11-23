def combinationSum(candidates, target):
    result = []
    
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                backtrack(i, target - candidates[i], path + [candidates[i]])

    backtrack(0, target, [])
    return result

print(combinationSum([2, 3, 6, 7], 7))