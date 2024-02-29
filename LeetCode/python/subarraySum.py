# def subarraySum(nums, k):
#     res = 0
#     for i in range(len(nums)):
#         if nums[i] == k:
#             res += 1
#     for i in range(len(nums)):
#         temp = []
#         for x in range(i+1):
#             temp.append(nums[x])
#         # print(temp)
#         for j in range(i+1, len(nums), 1):
#             prefix = nums[j] + temp[j-1]
#             temp.append(prefix)
#             if prefix == k:
#                 res += 1
                
#     # print(res)
#     return res
def subarraySum(nums, k):
    res = 0
    curSum = 0
    prefixSums = {0:1}
    
    for num in nums:
        curSum += num
        diff = curSum - k
        res += prefixSums.get(diff, 0)
        prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
    print(res)
    return res
nums = [1,1,1]
k = 2
subarraySum(nums, k)