def dailyTemperatures(temperatures):
    s = []
    res = [0 for i in range(len(temperatures))]
    for i, temp in enumerate(temperatures):
        if len(s) == 0:
            s.append([i, temp])
        else:
            print('.>>>', s[-1][1])
            while len(s) and s[-1][1] < temp:
                curI, curTemp = s.pop()
                res[curI] = i - curI
            s.append([i, temp])

    print(res)
    return res

temperatures = [73,74,75,71,69,72,76,73]
dailyTemperatures(temperatures)
