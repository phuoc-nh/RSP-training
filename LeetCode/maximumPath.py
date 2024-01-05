def maximumPath(values):
    matrixTriangle = []
    n = 1
    curIndex = 0
    while curIndex < len(values):
        el = []
        for i in range(n):
            if i + curIndex < len(values):
                el.append(values[i + curIndex])
        curIndex += n
        
        matrixTriangle.append(el)
        n += 1
    # print(n)
    
    for m in matrixTriangle:
        for i in range(n-1-len(m)):
            m.append(0)

    for i in range(len(matrixTriangle) - 2, -1,-1):
        for j in range(len(matrixTriangle[i])-1):
            # if j < len(matrixTriangle[i]) - 1:
            print(j+1)
            matrixTriangle[i][j] = max(matrixTriangle[i+1][j] + matrixTriangle[i][j], matrixTriangle[i+1][j+1] + matrixTriangle[i][j])
    
    # print(matrixTriangle)    
    return matrixTriangle[0][0]
values = [1,2,3,4,5,6,7,8,9,10]
maximumPath(values)