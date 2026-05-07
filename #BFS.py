#BFS

print('introduction to BFS')

#breadth first search

#BFS uses a queue to maintain the order of nodes to visit next 
#(FIFO: First In, First Out).

#BFS example in python 

def bfs(graph,start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        print(vertex,end=' ')
        for neigh in graph[vertex]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)


graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'F'],
    'D': ['A', 'G'],
    'E': ['A'],
    'F': ['C'],
    'G': ['D', 'H', 'I'],
    'H': ['G'],
    'I': ['G']
}

bfs(graph,start='A')

#T O(V+E)
#S O(V)

#intro DFS

def dfs(graph,start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex,end = " ")
            visited.add(vertex)
            
        for neigh in graph[vertex]:
            if neigh not in vertex:
                stack.append(vertex)



#recursive DFS

def recursive_dfs(graph,vertex,visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex,end=' ')
    for neigh in graph[vertex]:
        if neigh not in visited:
            recursive_dfs(graph,neigh,visited)

#Recursive Fibonacci (Without DP)


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
#DP memoization

def dp_fib(n,memo = None):
    if memo is None:
        memo = [-1]*(n+1)
    if n <= 1:
        return n 
    if memo[n] != 1:
        return memo[n]
    memo[n] = dp_fib(n-1,memo) + dp_fib(n-2,memo) 
    return memo[n] 


print(dp_fib(10))


#linked list concept in brief
class node:
    def __init__(self,data):
        self.data = data
        self.next = None


#Linked List with Insertion at Head
class linklist:
    def __init__(self):
        self.head = None
    def insert_head(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node   


#https://students-old.masaischool.com/lectures/136361?tab=concepts

#Hashing

#Faculty Session 24 - Hashing

#https://aiven.io/tools/pg-playground

#hash take input and provide a op within a range n mod 5 
#will give op [0,1,2,4]
# uniformly distributed fast computation
# 
# low collision chance
#used to search an element not to insert or delete are on
# less priority
# 
# 37.55
# 
# collision of keys
# 
# collision resulution techniques
# chaining
# Linear probing
# quadretic probing 

#open addressing

# linear probing when collision occurs h(k)+i, h(k)is hash fn

#in Quadretic prob will use h(k) +i**2 when collision

print('Direct address table')

#example

max_size = 100
table = [0]*max_size

print(table)
key = [2,8,6,18,10]
for key in key:
    table[key] =1
print(table)

if table[18] == 1:
    print('element is there')

print('hash function is uniformly distributed')


m = 7
hashvalue = key % m

if key == 89:
    print(hashvalue)


#hash table impementation with hash fn
#A hash table is an array where elements are stored at 
#the index given by the hash function.

class hash:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
    def hash_fn(self,key):
        return key % self.size    
    def Insert(self,key):
        id = self.hash_fn(key)
        self.table[id] = key
    def search(self,key):
        id = self.hash_fn(key)
        if self.table[id] == key:
            return True
        return False

#Collision occurs when different keys hash to 
#the same index in the hash table.

#Collision resolution strategies:
#
#Chaining
#Open addressing (Linear probing, Quadratic probing)

#example

h = hash(10)
keys = [11,21,41,101,121]
for k in keys:
    h.Insert(k)

print(h.search(11))

#chaining
#In worst case (all keys in the same slot), 
#search degrades to O(n).

class hash_chaining:
    def __init__(self,size):
        self.size = size
        self.hasttable = [[ ] for _ in range(size)]
    def hash_fn(self,key):
        return key % self.size
    def insert(self,key):
        id = self.hash_fn(key)
        self.hasttable[id].append(key)
    def search(self,key):
        id = self.hash_fn(key)
        return key in self.hasttable[id]
    

#Open addressing probing
#Linar probing


class hash_Linearprobing:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
    def hash_fn(self,key):
        return key % self.size
    def Insert(self,key):
        id = self.hash_fn(key)
        i = 0 
        while self.table[(id + i) % self.size] is not None:
            
            i += 1
        self.table[(id + i) % self.size] = key
    def search(self,key):
        id = self.hash_fn(key) 
        i = 0 
        while self.table[(id + i) % self.size] is not None:
            if self.table[(id+i) % self.size] == key:
                return True
            i += 1
        return False

#Tutorial Session - 1 - Recurrence Relations
#Faculty Session 3 - Searching Algorithms 
#Recursion 
# 
def fact(n):
    if n == 1:
        return 1 
    else:
        return n* fact(n-1)
    
print(fact(6))

#searching algorithm
#linear search:
def linear_search(A,n,x):
    n = len(A)
    for i in range(n):
        if A[i] == x:
            return i
    return -1

#Greedy approach to find the maximum element, electing 
#max 3 no.s 

A = [6,8,9,12,15]
max = 3

A.sort(reverse=True)
selected = A[:max]

print(selected)

#do's for reduce time complexity

#Binary search algorithm

# array must be sorted
#will find the midle element mid = (0+n)//2

#binary search from psudo code:

def bst(A,s,n,x):  #start index is s end is n target x
    mid = (s+n)//2
    
    if A[mid] == x:
        return mid
    if A[mid] > x:
        return bst(A,s,mid-1,x)  #time complexity is getting reduced 
    if A[mid] < x:               #compared to iteration
        return bst(A,mid+1,n,x)
    return -1

arr = [1,2,7,8,12,14,15]

BSTarr = bst(arr,0,len(arr),8)

print(BSTarr)

#time complexity O(log n)
#space complexityO(logn) recurtion takes stack memory
##########################################################
#Faculty Session 4 - Lower/Upper Bound of Binary Search
##########################################################

#scenario 1
#array is sorted elements are repeatative
Arr = [2,4,6,6,8,11,19]
bstArr = bst(Arr,0,len(Arr),6)
print(bstArr)
aarr = [6,6,6,6,8,9,12,34]
#if target is 6 and we have to find the lowest index
#and we need the time complexity must not exceed O(log n)

#Lower bound of an element in an array

def LBBst(A,high,low,t): #complete iteration
    low = 1
    high = len(A) + 1
    while low < high :
        mid = (low + high)//2
        if A[mid] < t:
            low = mid + 1
        else:
            high = mid  #we have taken high = len(a) '+1' else
    return low

BSTaarr = LBBst(aarr,1,len(aarr)+1,4)
print(BSTaarr)
lbarr = LBBst(Arr,1,len(Arr)+1,5) 
print(lbarr)

#pthread method for deadlocks

#Osthrich algo
#Deadlock Ignorance
#RAG resource allocation graph


#Graph--BFS--DFS

graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]


    
    
from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque()
    queue.append(start)
    #queue.append(start)
    visited.add(start)
    while queue :
        vertex = queue.popleft()
        print(vertex,end=" ")
        for nei in graph[vertex]:
            if nei not in visited :
                visited.add(nei)
                queue.append(nei)

graph = {
    0 : [1,4,6],
    1 : [0,5],
    2 : [5,6],
    3 : [4,5,6],
    4 : [0,3],
    5 : [1,2,3],
    6 : [0,2,3]
}
print(bfs(graph,0))


    
    




        
                  
        





 






        
