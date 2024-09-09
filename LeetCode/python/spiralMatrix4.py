def spiralMatrix(m, n, head):
    res = [[-1] * n for i in range(m)]
	
    top = 0
    right = n
    bot = m
    left = 0
    
    while head:
        # left to right
        for i in range(left, right):
            if not head:
                return res
            res[top][i] = head.val
            head = head.next
        top += 1
    
        # top to bottom
        for i in range(top, bot):
            if not head:
                return res
            res[i][right-1] = head.val
            head = head.next
        right -= 1
        # right to left
        for i in range(right-1, left - 1 , -1):
            if not head:
                return res
            res[bot-1][i] = head.val
            head = head.next
        bot -= 1
        # bottom to top
        for i in range(bot-1, top-1, -1):
            if not head:
                return res
            res[i][left] = head.val
            head = head.next
        left += 1
    return res
m = 3
n = 5
head = [3,0,2,6,8,1,7,9,4,2,5,5,0]

spiralMatrix(m, n, head)
