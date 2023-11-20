class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
    
def insert(root, value):
    
    if not root:
        return Node(value)
    
    if root.value == value:
        return root
    elif root.value < value:
        root.right = insert(root.right, value)
    
    else:
        root.left = insert(root.left,value)
    return root
    

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
    

r = Node(50)
r =insert(r, 30)
r = insert(r, 20)

inorder(r)
        