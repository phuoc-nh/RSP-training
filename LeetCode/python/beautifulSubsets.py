def beautifulSubsets(nums, k):
    res = [0]
    def recursion(i, cur):
        if len(cur) == 1:
            res[0] += 1
        
        for j in range(i+1, len(nums)):
            flag = True
            for n in cur:
                if abs(n - nums[j]) == k:
                    flag = False
                    break
            # print(cur, nums[j])
            if flag:
                cur.append(nums[j])
                res[0] += 1
                recursion(j, cur)
                cur.pop()
            
    for i in range(len(nums)):
        recursion(i, [nums[i]])
        
    # print(res)
    return res[0]

nums = [4,2,5,9,10,3]
k = 1

# nums = [2,4,6]
# k = 2
beautifulSubsets(nums, k)