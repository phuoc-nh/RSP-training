# swap 0 with 1 to make contiguous sub array of ones
# maintain a window of size ones
# calculate one in current window
# calculate max one in each window
# return ones - max one 

def minSwaps(nums):
    n = len(nums)
    ones = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1

    curOnes = 0
    maxOnes = 0
    l = 0
    for r in range(2 * n):
        if nums[r % n] == 1:
            curOnes += 1
        if r - l + 1 > ones:
            if nums[l % n] == 1:
                curOnes -=1
            l += 1
        maxOnes = max(maxOnes, curOnes)
    
    return ones - maxOnes

nums = [1,0,0,1,1,0]