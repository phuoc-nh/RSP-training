class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def addNode(self, value):
        cur = self.head
        if not cur:
            self.head = Node(value)
            return
        while cur.next != None:
            cur = cur.next
        cur.next = Node(value)
    
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        self.head = prev
    def print(self):
        cur = self.head
        while cur:
            print(cur.value, end=" ")
            cur = cur.next

ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(0)
ll.print()
ll.reverse()
print()
ll.print()
        
    