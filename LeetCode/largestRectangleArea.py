def largestRectangleArea(heights):
    stack = [] # id height
    maxArea = 0
    for i in range(len(heights)):
        h = heights[i]
        start = i
        while stack and stack[-1][1] > h:
            id, height = stack.pop()
            maxArea = max(maxArea, (i - id) * height)
            start = id
        
        stack.append((start, h))
    
    while len(stack):
        id, height = stack.pop()
        maxArea = max(maxArea, (len(heights) - id) * height)

    # print(maxArea)
    # print(stack) 
    return maxArea
    
heights = [2,1,5,6,2,3]

largestRectangleArea(heights)