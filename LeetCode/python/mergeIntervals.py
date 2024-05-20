def mergeIntervals(intervals):
    intervals.sort()
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        
        
        curStart, curEnd = intervals[i]
        if curStart > res[-1][1]:
            res.append(intervals[i])
            continue
        
        prevStart, prevEnd = res.pop()
        res.append([prevStart, max(curEnd, prevEnd)])
        
    print(res)
    
    return res

intervals = [[1,4],[4,5]]
mergeIntervals(intervals)