def maxArea(height) -> int:
    
    l = 0 
    r = len(height) - 1
    
    res = 0
    print(l, r)
    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    print(res)
    return res


height = [1,8,6,2,5,4,8,3,7]
maxArea(height)