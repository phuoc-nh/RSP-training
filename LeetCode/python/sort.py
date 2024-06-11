def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print(arr)
arr = [5,2,1,3,9,0,4,5,6]

# bubbleSort(arr)

def selectionSort(arr):
    
    for i in range(len(arr)):
        kmin = i
        for j in range(i, len(arr)):
            if arr[j] < arr[kmin]:
                kmin = j
        
        if kmin != i:
            arr[kmin], arr[i] = arr[i], arr[kmin]
            
    print(arr)
    

# selectionSort(arr)

def insertSort(arr):
    for i in range(len(arr)):
        k = i
        while k > 0 and arr[k-1] > arr[k]:
            arr[k-1], arr[k] = arr[k], arr[k-1]
            k -= 1
            
    print(arr)
    
insertSort(arr)
            
    
