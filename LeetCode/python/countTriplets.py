def countTriplets(arr):
    res = 0
    
    for i in range(len(arr) - 1):
        left = 0
        for j in range(i+1, len(arr)):
            left ^= arr[j-1]
            right = 0
            k = j
            while k < len(arr):
                right ^= arr[k]
                if  right == left:
                    res += 1
                k += 1
         
    #         print('===') 
    # print(res)
    return res


arr = [1,1,1,1,1]
countTriplets(arr)