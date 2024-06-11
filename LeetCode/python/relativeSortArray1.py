from collections import Counter
def relativeSortArray(arr1, arr2):
    a1 = []
    counter1 = Counter(arr1)
    for k in arr2:
        if k in counter1:
            for i in range(counter1[k]):
                a1.append(k)
            del counter1[k]

    for k, v in sorted(counter1.items()):
        for i in range(v):
            a1.append(k)
    return a1
            
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSortArray(arr1, arr2))