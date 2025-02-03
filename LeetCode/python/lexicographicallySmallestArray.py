from collections import deque
def lexicographicallySmallestArray(nums, limit: int):
    # build group number
    # [[1,1,2], [6,7], [18]]
    groups = []
    tag = {}
    for n in sorted(nums):
        if not len(groups) or abs(groups[-1][-1] - n) > limit:
            q = deque()
            q.append(n)
            # q.pp
            groups.append(q)
        else:
            groups[-1].append(n)
            
        tag[n] = len(groups) - 1
            
            
    res = []
    
    for n in nums:
        q = groups[tag[n]]
        res.append(q.popleft())
    # print(groups)
    # print(tag)
    # print(res)
    
    return res
            
    
    
    
    
nums = [1,7,6,18,2,1]
limit = 3
lexicographicallySmallestArray(nums, limit)