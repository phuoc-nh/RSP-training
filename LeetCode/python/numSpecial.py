import copy

def numSpecial(mat):
    prefixSumRow = copy.deepcopy(mat)
    prefixSumCol = copy.deepcopy(mat)
    
    col = len(mat[0])
    row = len(mat)

    for i in range(row):
        for j in range(1,col):
            prefixSumRow[i][j] += prefixSumRow[i][j-1] 
            # print(prefixSumRow[i][j])

    for i in range(1, row):
        for j in range(col):
            prefixSumCol[i][j] += prefixSumCol[i-1][j]
    
    res = 0
    for i in range(row):
        for j in range(col):
            countOne = prefixSumRow[i][col-1] + prefixSumCol[row-1][j]
            if mat[i][j] == 1 and (countOne - 1 == 1):
                print(i, j)
                res += 1
    # print(res)       
    return res       


    # for p in prefixSumRow:
    #     print(p)
    # print('==========')
    # for x in prefixSumCol:
    #     print(x)
# mat = [
#     [1,1,0],
#     [0,0,1],
#     [1,0,0]
# ]
mat = [[1,0,0],[0,1,0],[0,0,1]]

numSpecial(mat)