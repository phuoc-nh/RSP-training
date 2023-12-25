from sortedcontainers import SortedList

def countSmaller(nums):
    sl = SortedList([])
    result = []

    for i in range(len(nums) -1,-1,-1):
        idx = sl.bisect_left(nums[i])
        result.append(idx)
        sl.add(nums[i])

    result.reverse()
    # print(result)
    return result
nums = [5,2,6,1]
countSmaller(nums)