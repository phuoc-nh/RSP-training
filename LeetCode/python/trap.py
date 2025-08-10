def trap(height) -> int:
    n = len(height)
    leftMax = [0 for i in range(n)]
    for i in range(1, n):
        leftMax[i] = max(height[i-1], leftMax[i-1])
    
    rightMax = [0 for i in range(n)]
    for i in range(n-2, -1, -1):
        rightMax[i] = max(height[i+1], rightMax[i+1])
    
    print(leftMax)
    print(rightMax)
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(height)