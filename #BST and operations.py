#BST and operations 
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

        #pass


def bst_search(root,key):
    if root is None or root.val == key:
        return root
    if key < root.val :
        return bst_search(root.left,key)
    if key > root.val :
        return bst_search(root.right,key)        

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val,end = " ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end= " ")        

root = Node(100)
root.left = Node(90)
root.right = Node(110)
root.left.left = Node(85)
root.left.right = Node(95)
root.right.left = Node(105)
root.right.right = Node(115) 
print(bst_search(root,90))  
print(inorder(root))
print(inorder(root=root.right))
print(postorder(root))
print(preorder(root=root.left))

def bst_insert(root,key):
    if root is None:
        return Node(key)
    if key < root.val :
        root.left = bst_insert(root.left,key)
    if key > root.val :
        root.right = bst_insert(root.right,key)


Root = Node(10)
Root.left = Node(8)
Root.right = Node(12)
bst_insert(Root,15)
bst_insert(Root,9)
bst_insert(Root,10)
bst_insert(Root,8)
bst_insert(Root,25)
bst_insert(Root,6)
bst_insert(Root,1)

print(inorder(Root.left))

