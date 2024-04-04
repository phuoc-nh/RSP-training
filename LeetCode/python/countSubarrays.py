def countSubarrays(nums, k):
  j = 0
  count = 0
  counter = {}
  maxCount = 0
  for i in range(len(nums)):
    counter[nums[i]] = counter.get(nums[i], 0) + 1
    maxCount = max(counter[nums[i]], maxCount)

    while maxCount == k and j < len(nums):
      # print('j', j)
      # print('i', i)
      # print('maxCount', maxCount)
      count += 1
      count += len(nums) - 1 - i
      # print('>>',len(nums) - 1 - i)
      print('>>',counter)
      print('>>',maxCount)
      print('i',i)
      print('j',j)
      if counter[nums[j]] == maxCount:
        maxCount -= 1
      
      counter[nums[j]] = counter.get(nums[j], 0) - 1
      if counter[nums[j]] == 0:
        del counter[nums[j]]
      # update maxCount
      j += 1
      
  print(count)
  return count

nums = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]
k = 2
countSubarrays(nums, k)