from collections import Counter

def findErrorNums(nums):
    res = []
    total = sum(nums)
    actualTotal = int((len(nums) * (len(nums) + 1)) / 2)
    c = Counter(nums)
    for k in c:
        if c[k] > 1:
            res.append(k)
            if actualTotal > total:
                res.append(k + actualTotal - total)
            else:
                res.append(k - (total - actualTotal))
    print(res)
    return res

nums = [1,2,2,4]
findErrorNums(nums)