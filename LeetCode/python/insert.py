def insert(intervals, newInterval):
    res = []
    
    for interval in intervals:
        if interval[0] > newInterval[1] or interval[1] < newInterval[0]:
            res.append(interval)
            continue
        newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        
        # if interval[1] >= newInterval[0]: # compare end with start new interval
        #     newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        #     print('new interval', newInterval)
        # else:
        #     res.append(interval)
            
    print(res)
    print(newInterval)
    res.append(newInterval)
    return sorted(res)
    

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# [[1,2],[3,10],[12,16]]
insert(intervals, newInterval)