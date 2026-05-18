#Tree travarsal
print('Tutorial Session - 15 - Linked List II')
#Binary search tree
#linear search insertion(O(1))   search O(n)
#binary search insertion(O(n))   search O(log n)
#intriducing binary search tree ds for
# insertion and search is in O(log n)
#at lebel l the no of nodes will be 2**(l-1)
#Faculty Session 8 - Binary Search Trees

#search algo in BST 

class node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

        

def BST_search(root,key):
    if root is None or root.value == key:
        return root
    elif key < root.value:
        return BST_search(root.left, key)
    else:
        return BST_search(root.right,key)
    

#bst insertion 

def insert_bst(root,key):
    if root is None:
        return node(key)
    if key < root.key :
        root.left =  insert_bst(root.left,key)
    if key > root.key :
        root.right = insert_bst(root.left,key) 
       

#deletion of a node from BST
#case 1 leaf node
#case 2 single child  
#case 3  minimum from the right subtree or maximum from the 
# left subtree
        
def inordetree(root):
    if root:
        inordetree(root.left) 
        print(root.key,end=" ")
        inordetree(root.right)

root = node(10)
root.right = node(20)
root.left = node(8)
root.left.left = node(6)
root.left.right = node(9)
root.right.left = node(15)
root.right.right = node(500)


print(inordetree(root))

def preordertree(root):
    if root:
        print(root.key , end= " ")
        preordertree(root.left)
        preordertree(root.right)

print(preordertree(root))
def postordertree(root):
    if root:
        postordertree(root.left)
        postordertree(root.right)
        print(root.key , end = " ")

print(postordertree(root))


#Deletion in BST



def minvaluenode(node):
    current = node
    while current.left:
        current = current.left  # for BST root.left < root
    return current    

def deletnode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left = deletnode(root.left, key)
    elif key > root.key:
        root.right = deletnode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        #node with two children 
        temp = minvaluenode(root.right)
        root.key = temp.key
        root.right = deletnode(root.right,temp.key)
    return root


Root = node(100)
insert_bst(Root,90)
insert_bst(Root,200)
insert_bst(Root,250)
insert_bst(Root,95)
insert_bst(Root,85)
#print(inordetree(100))
#print(preordertree(100))



