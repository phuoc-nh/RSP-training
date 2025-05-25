# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
        
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid point by fast and slow pointer
        # reverse last half of the linkedList from mid point
        # merge 2 list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        # reverse ll
        second = slow.next
        slow.next = None
        prev = None


        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

  
        first, second = head, prev

        # while first:
        #     print('firs', first.val)
        #     first = first.next

        # while second:
        #     print('second', second.val)
        #     second = second.next
        first, second = head, prev
        
        while second:
            print('second first', second)
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
	
            
            print(second)
            print(second.next)
            # first, second = tmp1, tmp2
            first = tmp1
            second = tmp2
            print('second after', second)
            
        	# print(second)

        # print

        # while second:
        #     tmp1, tmp2 = first.next, second.next
        #     first.next = second
        #     second.next = tmp1
        #     first, second = tmp1, tmp2
        #     if second:
        #         print('second', second.val)
        #         print('second.', second.next)
        
        # while head:
        #     print(head.val)
        #     head= head.next

        
            
head = ListNode(1)
cur = head
cur.next = ListNode(2)
cur = cur.next
cur.next = ListNode(3)
cur = cur.next

cur.next = ListNode(4)
cur = cur.next
cur.next = ListNode(5)

sol = Solution()

sol.reorderList(head)