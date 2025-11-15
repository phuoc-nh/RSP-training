def removeCoveredIntervals(intervals) -> int:
    intervals.sort()
    count = 0
    
    stack = []
    stack.append(intervals[0])
    
    for i in range(1, len(intervals)):
        prev = stack[-1]   
        cur = intervals[i]
        
        if cur[0] > prev[1]:
            stack.pop()
            stack.append(cur)
        else:
            if cur[1] <= prev[1]:
                count += 1
            else:
                stack.pop()
                stack.append(cur)
    
    return len(intervals) - count

    
intervals = [[1,4],[2,3]]

res = removeCoveredIntervals(intervals)
print(res)