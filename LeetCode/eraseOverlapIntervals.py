def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: (x[0], x[1]))
    res = [intervals[0]]
    print(intervals)
    count = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < res[-1][1]:
            count += 1
            if intervals[i][1] < res[-1][1]:
                res.pop()
                res.append(intervals[i])
        else:
            res.append(intervals[i])
            
    print(res)
    print(count)
    return count
    
    
intervals=[[1, 10], [2,5], [6,7]]
eraseOverlapIntervals(intervals)