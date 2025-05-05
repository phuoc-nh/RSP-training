def findClosestElements(arr, k: int, x: int):
        l = 0 
        r = k
        
        for i in range(k, len(arr)):
            print("abs(arr[l] - x)", abs(arr[l] - x), l)
            print('abs(arr[i] - x)', abs(arr[i] - x), i)
            if abs(arr[i] - x) < abs(arr[l] - x) :
                # if arr[i] != arr[l]:
                #     continue
                l += 1
                r += 1
            elif abs(arr[i] - x) == abs(arr[l] - x):
                if arr[i] > arr[l]:
                    continue
                
                l += 1
                r += 1
            print('..``')
        print(arr[l:r])
        print(l, r)
        return arr[l:r]

arr = [0,0,0,1,3,5,6,7,8,8]

k = 2
x = 2

# arr = [1,1,2,3,4,5]
# k = 4
# x = -1

# arr = [1,1,1,10,10,10]

# k = 1
# x = 9

# arr = [1,2,3,4,5]
# k = 4
# x = 3


findClosestElements(arr, k, x)