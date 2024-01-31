def NestedIterator(nestedList):
    res = []
    
    def recursion(cur):
        if type(cur) == int:
            print()
            res.append(cur)        
            return
        
        for i in range(len(cur)):
            recursion(cur[i])
    recursion(nestedList)
    print(res)
    
    
nestedList = [[1,1],2,[1,1]]

NestedIterator(nestedList)