import heapq
import math

def maxKelements(nums, k):
    nums = [-i for i in nums]
    
    heapq.heapify(nums)
    score = 0
    for i in range(k):
        el = -heapq.heappop(nums) # log(n) get head heap and have to restructure
        print('el', el)
        score += el
        heapq.heappush(nums, -math.ceil(el/3)) # heap push is log(n)
    print(score)
    return score
nums = [1,10,3,3,3]
k = 3
maxKelements(nums, k)