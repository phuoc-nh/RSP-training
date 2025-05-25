def findMedianSortedArrays(nums1, nums2) -> float:
    n = len(nums1) + len(nums2)
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1
    
    half = n // 2 # 5
    
    l2 = 0
    r2 = len(nums2) - 1
    
    while True:
        m2 = (l2 + r2) // 2
        m1 = half - (m2 + 1) - 1
        
        print('m2', m2)
        print('m1', m1)
        
        left1 = nums1[m1] if m1 >= 0 else float('-infinity')     
        left2 = nums2[m2] if m2 >= 0 else float('-infinity')     
        
        right1 = nums1[m1 + 1] if m1 + 1 < len(nums1) else float('infinity')
        right2 = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('infinity')
        
        if left1 <= right2 and left2 <= right1:
            print('left1', left1)
            print('left2', left2)
            print('right1', right1)
            print('right2', right2)
            
            if n % 2 == 1:
                print('res odd', min(right1, right2))
                return min(right1, right2)
            else:
                print('res even', (max(left1, left2) + min(right1, right2)) / 2)
                return (max(left1, left2) + min(right1, right2)) / 2
                        
        elif left2 > right1:
            r2 = m2 - 1
        elif left1 > right2:
            l2 = m2 + 1
        
            
            
    print(l2, r2)
    


nums1 = [1,2]
nums2 = [3,4]
res = findMedianSortedArrays(nums1, nums2)
print('res', res)
# total values is 10
# if the length is even
# find 2 values
# the idea is find the index1 and index2 where left values 1 & 2 equal to 4
# make sure the left part of nums1 is always smaller than the value mid + 1 in nums 2


        