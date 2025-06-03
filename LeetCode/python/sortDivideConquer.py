def sortArray(nums):
	
    def merge(l, m, r):
        # print(l, m, r)
        left = nums[l:m+1]
        right = nums[m+1:r+1]
        
        print('lef', left)
        print('right', right)
        
        p1 = 0
        p2 = 0
        i = l
        
        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                nums[i] = left[p1]
                p1 += 1
            else:
                nums[i] = right[p2]
                p2 += 1
                
            i += 1
            
        while p1 < len(left):
            nums[i] = left[p1]
            i += 1
            p1 += 1
        
        while p2 < len(right):
            nums[i] = right[p2]
            i += 1
            p2 += 1
            
        
        
    # nums = [1,3,0,2]
    # l = 0, r = 4, m = 2
    # merge(0, 2, 4)
    
    # print(nums)
     
    def mergeSort(l, r):
        if l == r:
            return
        
        m = (l + r) // 2
        mergeSort(l, m)
        mergeSort(m+1, r)
        merge(l, m, r)
        
 
    mergeSort(0, len(nums)-1)
    
    print('nums', nums)
    return nums
         
	
    
nums = [5,1,1,2,0,0]
sortArray(nums)