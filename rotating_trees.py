#Faculty Session 9 - BST and AVL trees
#https://students-old.masaischool.com/lectures/131107?tab=concepts

class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def insert(root,key):
        
        if root is None:
            return Node(key)
        if key < root.val :
            root.left = insert(root.left,key)  
        else :
            root.right = insert(root.right,key)
        
        return root      

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val , end=" ")
        inorder(root.right)


root = Node(10)
root.left = Node(9)
root.right = Node(11)

insert(root,key=19) 
insert(root,key=18)
print(inorder(root))
# deleting elements 

def find_min(root):
    while root.left is not None:
        root = root.left
    return root
print(find_min(root=Node(10)))


def delete_node(root,key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left,key)
    elif key > root.val :
        root.right = delete_node(root.right,key) 
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete_node(root.right,temp.val)
    return root

#AVL is a self balancing binary tree, with the 
#Balancing factor = height(root.left) - height(root.right) 
#A BST is balanced if balancing factor lies in {-1,0,1}
#4 types of rotatio for an avl to balancing
#ll : one right,lr: one left one right,rr: one left,rl: 1 right 1 left
           
#20 , 10, 5, 30, 40, 25, 22

node = Node(20)
#insert(node,10)
insert(node,5)
insert(node,30)
insert(node,40)
insert(node,25)
insert(node,22)
print(inorder(node))
print(node.left.val)
print(node.right.val)
print(inorder(node.right))
print(inorder(node.left))

class AVLNode:
    def __init__(self,value):
        self.val = value
        self.right = None
        self.left = None
        self.height = 1

def get_height(root):
    if not root:
        return 0
    return root.height
def get_balance(root):
    if root:
        return get_height(root.left) - get_height(root.right)
    return 0
def right_rotate(y):
    x = y.left
    z = x.right
    x.right = y
    y.left = z
    y.height = 1 + max(get_height(y.left),get_height(y.right))
    x.height = 1 + max(get_height(x.left),get_height(x.right))
    return x



#      y
#    x
#      z
# after rotate   
#    x
#       y
#    z
    

def let_rotate(x):
    y = x.right
    z = y.left
    y.left = x
    x.right = z #T2
    x.height = 1 + max(get_height(x.left),get_height(x.right))
    y.height = 1 + max(get_height(y.left),get_height(y.right))
    return y
     
#    x
#       y
#    z
# after rotate  
#      y
#    x
#      z

def AVLinsert(root,key):
    if root is None:
        return AVLNode(key)
    if key < root.val :
        root.left = AVLinsert(root.left,key)
    if key > root.val :
        root.right = AVLinsert(root.right,key)
    root.height = 1 + max(get_height(root.right), get_height(root.left))
    balance = get_balance(root)
    #LL
    if balance > 1 and key < root.left.val :
        return right_rotate(root)
    # RR
    if balance < -1 and key > root.right.val:
        return let_rotate(root)
    # LR
    if balance > 1 and key > root.left.val:
        root.left = let_rotate(root.left)
        return right_rotate(root)
    # RL
    if balance < -1 and key < root.right.val:
        root.right = right_rotate(root.right)
        return let_rotate(root)
    return root


R = AVLNode(90)
R.left = AVLNode(85)
R.right = AVLNode(110)
AVLinsert(R,150)
AVLinsert(R,70)
AVLinsert(R,67)
AVLinsert(R,120)
AVLinsert(R,48)

print(inorder(R))
print(inorder(R.left))
print(inorder(R.right))

