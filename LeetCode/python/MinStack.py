class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
            
            return
        
        if self.stack[-1][0] > val:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][0]))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())

obj.pop()
print(obj.top())

print(obj.getMin())