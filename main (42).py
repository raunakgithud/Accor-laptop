'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''



print("Hello World")

print(float('-inf')) 

#recursive approach

def cutrod(p,n):
    if n == 0 :
        return 0
    q = float('inf')
    for i in range(1,n+1):
        q = max(q,p[i] + cutrod(p,n-i))
    return q    
        
    
    
#dynamic programing

def memocutrod(p,n,r):
    if r[n] >= 0:
        return r[n]
    q = float('inf')
    if n == 0:
        q= 0
    else:
        for i in range(1,n+1):
            q = max(q, p[i] + memocutrod(p,n-i,r))
    return q
    
    
# Bottom-up DP for LCS

def LCS(A, B):
    m = len(A)
    n = len(B)
    L = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if A[i] == B[j]:
                L[i][j] = 1 + L[i+1][j+1]
            else:
                L[i][j] = max(L[i+1][j], L[i][j+1])
    return L[0][0]

# Example usage
print(LCS("PRATEEK", "PARST"))  # Output: 3

#Subsequences include "PRA", "PTEK", "PT".
#Substrings include "PRA", "RATE", "TEEK".
    
    

#greedy technique to merge two BSTs

class treenode:
    def _init_(self,val = 0, left = None,right = None):
        self.val = val
        self.right = right
        self.left = left


def inorder(root,arr):
    if root :
        inorder(root.left,arr)
        arr.append(root.val)
        inorder(root.right,arr)
        
        
def merge(arr1,arr2):
    merge = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j] :
            merge.append(arr1[i])
            i += 1 
        else :
            merge.append(arr2[j])
            j += 1 
        if arr1[i] == arr2[j]:
            merge.append(arr1[i])
            i += 1 
            j += 1 
    merge.extend(arr1[i:])
    merge.extend(arr2[j:])
    return merge
    
    
def sortedaraytoBST(arr,start,end):
    if start > end : 
        return None
    mid = (start + end)//2
    root = treenode(arr[mid])
    root.left = sortedaraytoBST(arr,start,mid-1)
    root.right = sortedaraytoBST(arr,mid+1,end)
    return root
    
def mergeBST(ar1,ar2):
    ar1,ar2 = [],[]
    inorder(root1,ar1)
    inorder(root2,ar2)
    merged  = merge(ar1,ar2)
    return sortedaraytoBST(merged,0,len(merged)-1)
    
    
    
    
        
    
        
        