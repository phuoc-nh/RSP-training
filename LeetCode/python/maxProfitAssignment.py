def maxProfitAssignment(difficulty, profit, worker):
    diff_pro = []
    for i in range(len(difficulty)):
        diff_pro.append((difficulty[i], profit[i]))
    
    diff_pro.sort()
    
    res = 0 
    i = 0
    cur = 0
    for w in worker:
        while i < len(diff_pro) and w >= diff_pro[i][0]:
            cur = max(cur, diff_pro[i][1])
            i += 1
            
        res += cur
    print(res)
    return res

difficulty = [85,47,57]
profit = [24,66,99]
worker = [40,25,25]

maxProfitAssignment(difficulty, profit, worker)