def rearrangeArray(nums):
    negatives = []
    positives = []

    for n in nums:
        if n < 0:
            negatives.append(n)
        else:
            positives.append(n)

    res = []

    for i in range(len(positives)):
        res.append(positives[i])
        res.append(negatives[i])
    print(res)
    
    return res

nums = [3,1,-2,-5,2,-4]
rearrangeArray(nums)