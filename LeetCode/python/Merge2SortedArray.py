arr1 = [1,6,10,12, 13,20]
arr2 = [2, 5, 7, 100, 102,300]

res = []

i1 = 0
i2 = 0

while i1 < len(arr1) and i2 < len(arr2):
    if arr1[i1] <= arr2[i2]:
        res.append(arr1[i1])
        i1 += 1
    else:
        res.append(arr2[i2])
        i2 += 1

if i1 < len(arr1):
    for i in range(i1, len(arr1)):
        res.append(arr1[i])

if i2 < len(arr2):
    for i in range(i2, len(arr2)):
        res.append(arr2[i])
print(res)