def minCost(colors: str, neededTime) -> int:
    i = 0
    res = 0
    while i < len(colors):
        if i + 1 < len(colors) and colors[i] != colors[i+1]:
            i += 1
            continue
        
        total = neededTime[i]
        maximum = neededTime[i]
        j = i + 1
        
        while j < len(colors) and colors[i] == colors[j]:
            total += neededTime[j]
            maximum = max(maximum, neededTime[j])
            j += 1
            
        res += total - maximum # keep biggest needed time only
        i = j
    print('res', res)
    return res
    
colors = "abaac"
neededTime = [1,2,3,4,5]

colors = "abc"
neededTime = [1,2,3]

colors = "aabaa"
neededTime = [1,2,3,4,1]

minCost(colors, neededTime)