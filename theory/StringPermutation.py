def permutation(arr, l, r):
    if l == r:
        print(''.join(arr))
    else:
        for i in range(l, r):
            arr[l], arr[i] = arr[i], arr[l]
            permutation(arr, l+1, r)
            arr[l], arr[i] = arr[i], arr[l]

arr = ['A', 'B', 'C']

permutation(arr, 0, len(arr))    