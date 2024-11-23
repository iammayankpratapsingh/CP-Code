def combinationSum3(k, n):
    def backtrack(start, k, n, path):
        if len(path) == k and n == 0:
            result.append(path)
            return
        for i in range(start, 10):
            if i > n:
                break
            backtrack(i + 1, k, n - i, path + [i])

    result = []
    backtrack(1, k, n, [])
    return result

print(combinationSum3(3, 7))
