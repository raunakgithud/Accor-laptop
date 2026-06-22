#asymptotic-notation 
# n0 ∈ N  and n >= n0
#f (n) ≤ c.g(n)             f (n) = O(g(n))  upper bound
#f (n) ≥ c.g(n)             f (n) = Ω(g(n))  Lower bound 
#c1.g(n) ≤ f(n) ≤ c2.g(n)   f (n) = Θ(g(n))  tight bound

#mathemetical equation that defines an equation 
#recursively 
# T(n) = T(n/2) + c
#master theorem 
#T(n) = aT(n/b) + f(n)  # f(n) = O(n**c)
#if c <= log b(a) then T(n) = theta(n ** log b(a))
#if c = log b(a) then T(n) = omega(n**log b(a)(log n))
#if c > log b(a) then T(n) = theta(f(n))

print('recurrsion')

#Node1 -- Node2
# |       |
#Node3 -- Node4

graph = {
    'Node1' : ['Node2','Node3'],
    'Node2' : ['Node1','Node4'],
    'Node3' : ['Node1','Node4'],
    'Node4' : ['Node2','Node3']
}

print(graph)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)  # Divide step
        merge_sort(right)  # Divide step

        i = j = k = 0
        # Merge step
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

ex1 = [9,0,4,6,2,11]
print(merge_sort(ex1))


#BST 

class node:
    def __init__(self,key):
        node.right = None
        node.left = None
        node.val = key


def insert(root,value):
    if root is None:
        return node(value)
    elif root.val > value:
        root.left = insert(root.left,value) 
    else:
        root.right = insert(root.right,value)
    return root

def search(root,value):
    if root is None or root.val == value:
        return root
    elif root.val > value:
        return search(root.left,value)
    else:
        return search(root.right,value)


root = node(23)
root.left = node(21)
root.right = node(31)

print(search(root,33))     
print(insert(root=root,value=37))    


#Upperbound and lower bound of Bynary Search
#lower bound is 1st possition arr[i] >= x
#Upper bound is 1st possition arr[i] > x
#1 base indexing low = 1 high = n+1

def upper_bound(A,n,x):
    low = 1
    high = n + 1
    while low < high:
        mid = (low + high)//2
        if A[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low

def lower_bound(A,n,x):
    low = 1
    high = n + 1
    while low < high:
        mid = (low + high)//2
        if A[mid] < x:
            low = mid + 1
        else:
            high = mid
    if low > n:
        return -1        
    return low

A = [2, 2, 2, 2, 3, 4, 9, 100] #and x = 2        

print(upper_bound(A,len(A)+1,2))
print(lower_bound(A,len(A)+1,2))


#Insertion sort algorithm 

ar = [5, 2, 4, 6, 1, 3]
def insertaion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i -1 

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

insertaion_sort(ar)
print(ar)
#T.C = O(n^2)


#partition

       
ex2 = [3, 6, 8, 10, 1, 2, 1]
#def partition(arr,low,high):
#    pivot = arr[high]
#    i = low -1
#    for j in range(low,high):
#        if arr[j] < pivot:
#            i += 1
#            arr[i],arr[j] = arr[j],arr[i]
#    arr[i+1],arr[high] = arr[high],arr[i+1]
#    return i+1

def partition(arr,low,high):
    pivot = arr[high]
    i = low -1
    for j in range(low,high):
        if arr[j] < pivot:
            i+= 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[high],arr[i+1] = arr[i+1],arr[high]
    return i+1
        

index = partition(ex2,0,len(ex2)-1) 
print(index)
print(ex2)

#quick_sort
def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

quick_sort(ex2,0,len(ex2)-1)
print(ex2)        

import random as rm

def randomized_partition(arr,low,high):
    pivot_index = rm.randint(low,high)
    arr[pivot_index],arr[high] = arr[high],arr[pivot_index]
    return partition(arr,low,high)
def randomized_quick_sort(arr,low,high):
    if low < high:
        pi = randomized_partition(arr,low,high)
        randomized_quick_sort(arr,low,pi-1)
        randomized_quick_sort(arr,pi+1,high)

#Backtracking
#subset sum problem 
def subset_sum(arr,n,target):
    if target == 0 :
        return True
    if n == 0 and target != 0:
        return False
    if arr[n-1] > target:
        return subset_sum(arr,n-1,target)
    return subset_sum(arr,n-1,target) or subset_sum(arr,n-1,target-arr[n-1])





#def maxCandy(candy,target):
#    l = []
#    
#        
#    i = 0
#    n = 1
#    while target >= 0 and i < len(candy)-1:
#            
#        if n*candy[i] < target:
#            l.append(candy[i])
#            target -= n*candy[i]
#        if target > candy[i+1]:
#            n += 1
#        else:
#            i += 1 
#    

def maxCandy(candy,target):
    for price in candy:
        while target >= price:  
            if target > 0:
             target -= price
             return price
    return maxCandy(candy,target)

page = [10,12]
problem = 32
def notebook(page,problem):
    l = []
    n = 1
    i = 0
    while problem > 0:
        if problem >= n*page[i]:
            problem -= n*page[i]
            l.append(page[i])
            n += 1
        else:
            problem += page[i]
            n = 1
            i += 1     
    if problem != 0:
        return -1
    return len(l)  

#notebook(page,problem)        
            
def notebook(page,problem):
    l = []
    n = 1
    i = 0
    while problem > 0:
        if problem >= n*page[i]:
            problem -= n*page[i]
            l.append(page[i])
            n += 1
        else:
            problem += page[i]
            n = 1
            i += 1     
    if problem != 0:
        return -1
    for i in range(len(l)):
        print(l[i],end=" ") 

   


    
    
    
    
#candy = [2, 3, 6, 7]
#target = 7
#
#i = 0
#l = []
#while target != 0 :
#    if target > candy[i]:
#        l.append(candy[i])
#        target -= candy[i]
##    else:
##        target += candy[i]
##        l.pop()
## ######################################################### 
#i=0
#if target != 0:
#
#    while target != 0 :
#
#        while target >= candy[i]:
#            l.append(candy[i])
#        target -= candy[i]
#    target += candy[i]
#    l.pop()
#    i += 1        
###########################################################
# 
    


    

    

    #target += candy[i]#backtrack
    #l.pop()
    
    #i += 1
    #while target >= candy[i]:
    #    target -= candy[i]
    #    l.append(candy[i])


   
          
#print(l)            
#def maxCandy(candy,target):
#    l = []
#    n = 1
#    i = 0
#    while target >= 0:
#        if target >= n*candy[i]:
#            target -= n*candy[i]
#            l.append(candy[i])
#            n += 1
#        else:
#            target += candy[i]
#            
#            n = 1
#            i += 1
#    for j in range(len(l)):
#        print(l[j],end= " ")


#print(maxCandy(candy,target))

def maxcan(candy,target):
    n = 1
    i = 0
    l = []
    if target != 0 :
         while target >= candy[i]:
             target -= n*candy[i]
             l.append(candy[i])
         n += 1 
         target += candy[i]
         l.pop()
         n = 1
         i += 1
         while target >= candy[i]:
             target -= n*candy[i]
             l.append(candy[i])
         return l       


candy = [2, 3, 6, 7]
target = 7  
def maxc(candy,low,high,target):
    l =[]
    if low < high and target >= candy[low]:
        
        while target >= candy[low]:
            l.append(candy[low])
        target -= candy[low]
        return l
    target += candy[low]
    low += 1
    l.pop()
    l =maxc(candy,low,high,target)

#print(maxc(candy=candy,low=0,high=len(candy),target=target))
def newmaxc(candy,low,high,target):
    l = []
    if target == 0:
        l.append(candy[low])
        return
    for i in range(low,high):
        if target < candy[i]:
            break
        l.append(candy[i])
        newmaxc(candy,i,high,target=target-candy[i])
        l.pop()
candy1 = [2, 3, 6, 7]
target1 = 7             
#print(newmaxc(candy=candy1,low=0,high=len(candy1)-1,target=target1))        
           

def maxpage(pages,low,high,problem):
    result = []
    if problem == 0:
        result.append(pages[low])
        return len(result)
    while low < high:
        if problem < page[low]:
            break
        result.append(pages[low])
        problem -= pages[low]
        low += 1

        maxpage(pages,low,high,problem)
        result.pop()
    return -1    

def subs(A,N,K,diff):
    low = 0
    high = N-1
    sub = []
    while low <= high:
        if len(sub) < K:
            sub.append(A[low])
        low += 1
    for i in range(K):
        if max(sub[i],sub[i+1]) - min(sub[i],sub[i+1]) == diff:
            return True
    return False            
A = [1, 2, 1]  
diff = 1
k = 2      
print(subs(A,3,2,1))  


    








          

    
    

        


                       

                
                
                
            
                
                
            
            
          





            


 




        
candy = [2, 3, 6, 7]#[2, 3, 5]#
target = 7#8#
n = 1
i = 0
l = []
if target != 0 :
    while target >= candy[i]:
        target -= candy[i]
        l.append(candy[i])
    

    target += candy[i]#backtrack
    l.pop()
    #n = 1
    i += 1
    while target >= candy[i]:
        target -= candy[i]
        l.append(candy[i])


for i in range(len(l)):
  print(l[i],end = " ")
          
 



    


