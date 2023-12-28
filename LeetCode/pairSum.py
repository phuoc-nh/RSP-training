class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
            
        cur = self.head
        
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        
    def reverse(self, head):
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        return prev
    
    def endOfFirstHalf(self):
        cur = self.head
        slow = cur
        fast = cur
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def pairSum(self):
        endOfFirstHalfNode = self.endOfFirstHalf()
        reveredSecondHalf = self.reverse(endOfFirstHalfNode.next)
        self.print(reveredSecondHalf)
        cur = self.head
        maxSum = 0
        while reveredSecondHalf and cur:
            maxSum = max(maxSum, reveredSecondHalf.val + cur.val)
            cur = cur.next
            reveredSecondHalf = reveredSecondHalf.next
        print(maxSum)
        return maxSum
        # self.print(self.head)
        
    def print(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
            
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(5)
ll.pairSum()