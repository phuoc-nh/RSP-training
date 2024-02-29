from queue import Queue

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def constructBinaryTree(arr, i, n):
    root = None
    if i < n:
        root = Node(arr[i])
        root.left = constructBinaryTree(arr, i * 2 + 1, n)
        root.right = constructBinaryTree(arr, i * 2 + 2, n)
        
    return root


def inorderTraverse(root):
    if root:
        inorderTraverse(root.left)
        print(root.value, end=" ")
        inorderTraverse(root.right)
    
def buildTreeIter(arr):
    root = Node(arr[0])
    
    q = Queue()
    q.put(root)
    i = 1
    while i < len(arr):
        node = q.get()
        if i < len(arr):
            node.left = Node(arr[i])
            i += 1
            q.put(node.left)
        if i < len(arr):
            node.right = Node(arr[i])
            i += 1
            q.put(node.right)

    return root
def insertNode(root, value):
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if not node.left:
            node.left = Node(value)
            break
        else:
            q.put(node.left)
        
        if not node.right:
            node.right = Node(value)
            break
        else:
            q.put(Node.right)

# Delete node
# Pick delete node and pick last node
# Swap 2 nodes
# Delete last node

def deleteNode(root, value):
    q = Queue()
    q.put(root)

    deleteNode = None
    cur = None
    
    while not q.empty():
        cur = q.get()
        if cur.value == value:
            deleteNode = cur
        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)
    
    deleteNode.value = cur.value
    deletLastNode(cur)
     
def deletLastNode(root, node):
    q = Queue()
    q.put(root)
    
    while not q.empty():
        cur = q.get()
        if cur is node:
            cur = None
            return
        if cur.left:
            if cur.left is node:
                cur.left = None
                return
            else:
                q.put(cur.left)
        
        if cur.right:
            if cur.right is node:
                cur.right = None
                return
            else:
                q.put(cur.right)
    
def goodNodes(root):
    res = 0
    def dfs(root, curMax):
        if not root:
            return None
        if root.value >= curMax:
            curMax = root.value
            res += 1
        dfs(root.left, curMax)
        dfs(root.right, curMax)    

    dfs(root, root.value)
    print(res)
    return res
arr = [3,1,4,3,null,1,5]
root = buildTreeIter(arr)
print(root)
