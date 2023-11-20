class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
    
def insert(root, value):
    

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
    
        