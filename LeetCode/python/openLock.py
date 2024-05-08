from queue import Queue
def openLock(deadends, target):
    
    def helper(lock):
        # '0000'
        res = []
        
        for i in range(4):
            digit = (int(lock[i]) + 1) % 10
            
            res.append(lock[0:i] + str(digit) + lock[i+1:])
            
            digit = 9 if lock[i] == '0' else int(lock[i])- 1
            res.append(lock[0:i] + str(digit) + lock[i+1:])
        return res

    # print(helper('1111'))

    visited = set()
    q = Queue()
    q.put(['0000', 0]) # initial lock and cur step
    
    while not q.empty():
        cuLock, cur = q.get()
        if cuLock == target:
            return cur
        for lock in helper(cuLock):
            if lock in deadends:
                continue
            if lock not in visited:
                q.put([lock, cur + 1])
                visited.add(lock)
    
    return -1


deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(openLock(deadends, target))