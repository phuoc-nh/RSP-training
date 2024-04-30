class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        
    def insert(self, node):
        last = self.right.prev
        last.next = node
        node.prev = last
        
        node.next = self.right
        self.right.prev = node
        
    def get(self, key: int) -> int:
        
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            
            return self.cache[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode
        
        if len(self.cache) > self.capacity:
            lru  = self.left.next
            self.remove(lru) 
            del self.cache[lru.key]
        self.debug()
        
    def debug(self):
        for k in self.cache:
            print('key', self.cache[k].value)
        print('=============')
# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)

print('>>>',obj.get(1))

obj.put(3,3)
print('>>>',obj.get(2))