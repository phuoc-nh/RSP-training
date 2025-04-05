def minimumOperations():
    def calOperations(numbers):
        sortedNumb = sorted(numbers)
        operations = 0
        indexMap = {}
        for i in range(len(numbers)):
            indexMap[numbers[i]] = i
        
        for i in range(len(numbers)):
            if numbers[i] != sortedNumb[i]:
                operations += 1
                j = indexMap[sortedNumb[i]]
                indexMap[numbers[i]] = indexMap[sortedNumb[i]]
                numbers[i], numbers[j] = numbers[j], numbers[i]
                
                # print(numbers)
                # print(indexMap)
                
                # print("________")            
                
        # print(operations)
        
        return operations
    
    
    
numbers = [7,6,5,4]

minimumOperations(numbers)