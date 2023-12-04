def combination_sum(candidates, target):
    def backtrack(start, end, target, path):
        if target == 0:
            results.append(path)
            return
        if target < 0:
            return
        for i in range(start, end):
            backtrack(i, end, target - candidates[i], path + [candidates[i]])

    results = []
    backtrack(0, len(candidates), target, [])
    return results
