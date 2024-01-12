# def ship(grid, shots):
#     ROWS = len(grid)
#     COLS = len(grid[0])

#     DIRECTIONS = [
#         (1,0),
#         (-1,0),
#         (0,1),
#         (0,-1)
#     ]
#     res = []
#     ATTACKED = 'Attacked'
#     for r, c in shots:
#         if grid[r][c] == '.':
#             res.append('Missed')
#             # grid[r][c] = ATTACKED
#         elif grid[r][c] == ATTACKED:
#             res.append('Already attacked')
#         else:
#             temp = grid[r][c]
#             grid[r][c] = ATTACKED   
            
#             isSunk = True
#             for dr, dc in DIRECTIONS:
#                 row = dr + r
#                 col = dc + c
#                 if 0 <= row < ROWS and 0 <= col < COLS:
#                     if grid[row][col] == temp:
#                         isSunk = False
            
#             if isSunk:
#                 res.append('Ship ' + temp + ' sunk')
#             else:
#                 res.append('Attacked ship ' + temp)
                
                    
#     print(res)      
#     return res

# grid = [[".",".","B","B","B"], 
#         [".",".",".",".","."], 
#         [".",".",".",".","."], 
#         [".",".",".",".","."], 
#         [".",".",".",".","."]]

# shots = [[0,0], 
#  [0,0], 
#  [0,4], 
#  [0,4]]

# ship(grid, shots)


def newHashMap(queryType, query):
    INSERT = 'insert'
    ADD_TO_VALUE = 'addToValue'
    ADD_TO_KEY = 'addToKey'
    GET = 'get'

    m = {}
    result = 0

    for i in range(len(query)):
        if queryType[i] == INSERT:
            m[query[i][0]] = query[i][1]
        elif queryType[i] == GET:
            result += m[query[i][0]] 
        elif queryType[i] == ADD_TO_VALUE:
            for k in m:
                m[k] = m[k] + query[i][0]
        else:
            newM = {}
            for k in m:
                newM[k+query[i][0]] = m[k]
                # del m[k]
            m = newM
        print('query', query[i])     
        print('queryType', queryType[i])     
        print('map', m)
        print('=====================')
        
    print('result', result)
    return result

queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
query = [[1, 2], [2, 3], [2], [1], [3]]

newHashMap(queryType, query)