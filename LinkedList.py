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
        
    def search(self, value):
        if not self.head:
            print('Not found')
            return
        
        cur = self.head
        while cur:
            if cur.value == value:
                print('YES')
                return
            else:
                cur = cur.next        
        print('Not found')
    
    def delete(self, value):
        if not self.head:
            print('Not found to delete')

        if self.head.value == value:
            self.head = self.head.next
            return        

        cur = self.head
        while cur:
            if cur.next and cur.next.value == value:
                print('value', value)
                print('cur', cur.value)
                print('cur.next', cur.next.value)
                cur.next = cur.next.next
                return
            cur = cur.next

        print('Not found node to delete')
        
    def insertAtIndex(self, value, index):
        if index > self.length():
            print('Out of range')
            return
        
        if index == 0:
            cur = self.head
            self.head = Node(value)
            self.head.next = cur
            return

        count = 0
        cur = self.head
        while cur:
            if count + 1 == index:
                temp = cur.next
                cur.next = Node(value)
                cur.next.next= temp
                return
            cur = cur.next
            count += 1

    def updateNthNode(self, value, index):
        if index > self.length():
            print('Out of range')
            return
        cur = self.head
        count = 0
        while cur:
            if index == count:
                cur.value = value
                return
            cur = cur.next
            count += 1

    def length(self):
        len = 0
        cur = self.head
        while cur:
            len += 1
            cur = cur.next
        
        return len
    
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
# ll.updateNthNode(12, 0)
ll.reverse()
# ll.delete(210)
ll.print()
# print()
# print(ll.length())
# print()
# ll.print()
# ll.search(9)        
    