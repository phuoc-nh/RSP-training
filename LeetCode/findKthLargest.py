def findKthLargest(nums, k):
    k = len(nums) - k
    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p+=1
        
        nums[p], nums[r] = nums[r], nums[p]
        
        if p > k:
            return quickSelect(l, p-1)
        elif p < k:
            return quickSelect(p+1, r)
        else: return nums[p]

    return quickSelect(0, len(nums)-1)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums, k))