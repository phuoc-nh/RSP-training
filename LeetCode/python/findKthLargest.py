def findKthLargest(nums, k):
    k = len(nums) - k
    def quickSelect(l, r):
        pivot = nums[r]
        p = l
        
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        # finally move pivot to p pointer
        nums[p], nums[r] = nums[r], nums[p]
        
        if k == p:
            return nums[p]      
        elif k < p:
            return quickSelect(l, p - 1)
        else:
            return quickSelect(p+1, r)
    
    res = quickSelect(0, len(nums) - 1)
    # print(res)
    return res
    

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))