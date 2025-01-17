def xorAllNums(nums1, nums2) -> int:
    xorNums2 = nums2[0]
    len2 = len(nums2)
    for i in range(1, len2):
        xorNums2 ^= nums2[i]
        
    for i in range(len(nums1)):
        if len2 % 2 == 1:
            nums1[i] ^= xorNums2
        else:
            nums1[i] = 0 ^ xorNums2
            
    res = nums1[0]
    for i in range(1, len(nums1)):
        res ^= nums1[i]
    print(res)
    
    return res
    
nums1 = [2,1,3]
nums2 = [10,2,5,0]

xorAllNums(nums1, nums2)