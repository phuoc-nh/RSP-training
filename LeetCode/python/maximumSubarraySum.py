def maximumSubarraySum(nums, k):
    res = 0
    dup = {}
    leftId = 0
    for i in range(len(nums)):
        if nums[i] in dup.values():
            # remove until nums[i] is unique
            
            while nums[i] in dup.values():
                print(i, leftId)
                del dup[leftId]
                leftId += 1
            dup[i] = nums[i]
        else:
            dup[i] = nums[i]
            if len(dup.keys()) == k:
                res = max(sum(dup.values()), res)
            elif len(dup.keys()) > k:
                print(dup)
                print('>>>>',leftId)
                del dup[leftId]
                leftId += 1
                res = max(sum(dup.values()), res)
    print(res)
    return res
 
nums = [1,1,2]
k = 2

maximumSubarraySum(nums, k)