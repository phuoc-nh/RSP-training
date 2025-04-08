from collections import Counter
def minimumOperations(nums) -> int:
    counter = Counter(nums)
    print(counter)
    
    def allUnique(counter):
        for k in counter:
            if counter[k] > 1:
                return False
            
        return True
    
    res = 0 
    i = 0
    while not allUnique(counter) and i < len(nums):
        res += 1
        for j in range(3):
            if i < len(nums):
                counter[nums[i]] -= 1
                i += 1
    
    print(res)
            
    return res
    
    
    
nums = [1,2,3,4,2,3,3,5,7]
minimumOperations(nums)