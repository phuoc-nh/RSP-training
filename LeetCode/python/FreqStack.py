# class FreqStack:

#     def __init__(self):
#         self.stack = []
#         self.count = {}
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         self.count[val] = self.count.get(val, 0) + 1
    
#     def pop(self) -> int:
#         # print(self.count)    
#         # print(self.stack)
#         maxCount = max(self.count.values())
#         listMax = []
        
#         for c in self.count:
#             if self.count[c] == maxCount:
#                 listMax.append(c)
                
#         for i in range(len(self.stack)-1, -1, -1):
#             numb = self.stack[i]
#             if numb in listMax:
#                 self.stack.pop(i)
#                 self.count[numb] -= 1
#                 if self.count[numb] == 0:
#                     del self.count[numb]
#                 # remove ith number
#                 # reduce count
#                 return numb
                
class FreqStack:
# map counter to stack of value
# use a variable to track max count

# put use max count variable to detech which list to remove
# remove the top
# check if need to decrease max count
# if list to be removed empty -> decrease max count
    def __init__(self):
        self.countVal = {}
        self.maxCount = 0
        self.valCount = {}

    def push(self, val: int) -> None:
        if val not in self.valCount:
            self.valCount[val] = 0
        
        self.valCount[val] += 1
        curCount = self.valCount[val]

        if curCount > self.maxCount:
            self.maxCount = curCount
        
        if curCount not in self.countVal:
            self.countVal[curCount] = []

        self.countVal[curCount].append(val)


    def pop(self) -> int:
        self.countVal[self.maxCount].pop()
        if len(self.countVal[self.maxCount]) == 0:
            self.maxCount -= 1


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()

a = [5,7,5,7,4,5]
for x in a:
    obj.push(x)
    
res = obj.pop()
print(res)

res = obj.pop()
print(res)

res = obj.pop()
print(res)

res = obj.pop()
print(res)