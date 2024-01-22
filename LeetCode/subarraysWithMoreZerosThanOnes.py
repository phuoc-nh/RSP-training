from collections import Counter
def subarraysWithMoreZerosThanOnes(nums):
    nums = [i if i else -1 for i in nums]
    n = len(nums)
    presum = [0] * (n + 1)
    for i in range(1, n+1):
        presum[i] = presum[i-1] + nums[i-1]
    print('presum', presum)
    cnt = Counter()
    res = 0
    mod = 1000000007
    for i in range(n+1):
        cnt[presum[i]] += 1
        print('cnt', cnt)
        # res += sum([v for k, v in cnt.items() if k < presum[i]]) % mod
        for k, v in cnt.items():
            print('k, presum',k, presum[i])
            print('v', v)
            if k < presum[i]:
                res += v
        print('res', res)
        print('==========')
    return res % mod

nums = [0,1,1,0,1]
subarraysWithMoreZerosThanOnes(nums)