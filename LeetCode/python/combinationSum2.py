def combinationSum2(candidates, target):
    res = []

    def backtrack(index,cur, total):
        if total > target:
            return
        if total == target:
            res.append(cur)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue

            backtrack(index + 1, cur + [candidates[i]], total + candidates[i])

    candidates.sort()
    backtrack(0, [], 0)
    print(res)
    return res

candidates=[10,1,2,7,6,1,5]
target = 8
combinationSum2(candidates, target)