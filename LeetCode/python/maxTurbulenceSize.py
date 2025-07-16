def maxTurbulenceSize(arr):
    l = 0
    r = 1
    prev = ''
    res = 1
    
    while r < len(arr):
        if arr[r-1] > arr[r] and prev == '<':
            res = max(res, r - l + 1)
            r += 1
            prev = '>'
        elif arr[r-1] < arr[r] and prev == '>':
            res = max(res, r - l + 1)
            r += 1
            prev = '<'
        else:
            if arr[r-1] == arr[r]:
                l = r
                r += 1
                prev = ''
            else:
                res = max(res, 2)
                prev = '<' if arr[r-1] < arr[r] else '>'
                l = r - 1
                r += 1
            
    print('res', res)
    return res

arr = [4,8,12,16]

maxTurbulenceSize(arr)