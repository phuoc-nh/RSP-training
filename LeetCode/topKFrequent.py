from collections import Counter
import heapq
def topKFrequent(nums, k):
    count = [[] for i in range(len(nums) + 1)]
    counter = Counter(nums)
    
    for key, v in counter.items():
        count[v].append(key)
    
    res = []
    print(count)
    
    for i in range(len(count)-1, 0, -1):
        if count[i]:
            # res.append(count[i])
            for x in count[i]:
                res.append(x)
            if len(res) == k:
                return res

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
