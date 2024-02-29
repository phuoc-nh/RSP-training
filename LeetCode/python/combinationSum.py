# def combinationSum(candidates, target):
#     res = []
    
#     def backtrack(cur, total, i):
#         print(cur)
#         if total == target:
#             res.append(cur.copy())
#             return
        
#         if total > target or i >= len(candidates):
#             return
        
#         cur.append(candidates[i])
#         backtrack(cur, total+candidates[i], i)
#         cur.pop()
#         backtrack(cur, total, i+1)

#     backtrack([], 0, 0)
#     print(res)
#     return res

def combinationSum(candidates, target):
    ret = []
    dfs(candidates, target, [], ret)
    print(ret)
    return ret

def dfs(nums, target, path, ret):
    print(path)
    if target < 0:
        return 
    if target == 0:
        ret.append(path)
        return 
    for i in range(len(nums)):
        path.append(nums[i])
        dfs(nums[i:], target-nums[i], path, ret)
candidates = [2,3,6,7]
target = 7
combinationSum(candidates,target)