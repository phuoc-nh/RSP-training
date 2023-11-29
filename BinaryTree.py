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
        traverse(root.left)
        print(root.value, end=" ")
        traverse(root.right)

def inorderTraverse(root):
    if root:
        traverse(root.left)
        print(root.value, end=" ")
        traverse(root.right)
    
def buildTreeIter(arr):
    root = Node(arr[0])

    q = Queue()
    q.put(root)
    i = 1
    
    while i < len(arr):
        node = q.get()
        node.left = Node(arr[i])
        i += 1
        q.put(node.left)

        node.right = Node(arr[i])
        i += 1
        q.put(node.right)
    
    return root

def insertNode(root, value):
    q = Queue()
    q.put(root)
    
    while not q.empty():
        cur = q.get()
        
        if not cur.left:
            cur.left = Node(value)
            break
        else:
            q.put(cur.left)

        if not cur.right:
            cur.right = Node(value)
            break
        else:
            q.put(cur.right)

# Delete node
# Pick delete node and pick last node
# Swap 2 nodes
# Delete last node

def deleteNode(root, value):
    if not root:
        return
    
    deleteNode = None
    cur = None
    q = Queue()
    q.put(root)

    while not q.empty():
        cur = q.get()
        if cur.value = value:
            deleteNode = cur
        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)
    
    if deleteNode:
        temp = cur.value
        deleteLastNode(root, cur)
        deleteNode.value = temp
    
def deletLastNode(root, node):
    q = Queue()
    q.put(root)

    while not q.empty():
        cur = q.get()
        if cur is node:
            cur = None
            return

        if cur.right:
            if cur.right is node:
                cur.right = None
                return
            else:
                q.put(cur.right)
        
        if cur.left:
            if cur.left is node:
                cur.left = None
                return
            else:
                q.put(cur.left)
    

arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
# root = constructBinaryTree(arr, 0, len(arr))
# traverse(root)

# root = buildTreeIter(arr)
# traverse(root)

node1 = Node(1)
node2 = Node(2)
print(node1 is node1)
