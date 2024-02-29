from collections import Counter
def singleNumber(nums):
    c = Counter(nums)
    for num in nums:
        if c[num] == 1:
            return num


nums = [4,1,2,1,2]
print(singleNumber(nums))
    