def maximumHappinessSum(happiness, k):
    happiness.sort(reverse=True)
    print(happiness)
    
    res = 0
    for i in range(min(k, len(happiness))):
        res += max(0, happiness[i] - i)
    print(res)
    return res

happiness = [2,3,4,5]
k = 1
maximumHappinessSum(happiness, k)
