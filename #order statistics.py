#order statistics

print('order statistics')

print('quick select algo')

#to find nth smallest element in O(1) time

# pivot and partitioning function

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


array = [1,9,15,2,3,6]
k = partition(array,0,len(array)-1)
print(k)

def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

q = quick_sort(array,0,len(array)-1)

print(array)

#Randomized quick sort

import random

def random_partition(arr,low,high):
    pivot_index = random.randint(low,high)
    arr[pivot_index],arr[high] = arr[high],arr[pivot_index]
    return partition(arr,low,high)

def randomized_quicksort(arr,low,high):
    if low < high:
        pi = random_partition(arr,low,high)
        randomized_quicksort(arr,low,pi-1)
        randomized_quicksort(arr,pi+1,high)

def quick_select(arr,low,high,k):  #k th smallest element
    if low == high:
        return arr[low]
    pivot_i = random_partition(arr,low,high)
    if  k -1 ==  pivot_i:
        return pivot_i
    if k -1 > pivot_i :
        return quick_select(arr,pivot_i+1,high,k)
    if k -1 < pivot_i:
        return quick_select(arr,low,pivot_i+1,k) 
         

#######################################################

#######################################################
#Greedy method 

print("Greedy method")

# Greedy coin change example

coins = [10,5,2,1]

print(coins)

def min_coins(x):
    count = 0
    a = []
    for coin in coins:
        while x >= coin:
            x -= coin
            a.append(coin)
            count += 1
    return count , a    

print(min_coins(7))
print(min_coins(9))

#https://students-old.masaischool.com/lectures/132161?tab=concepts

# CIA   confidentiality  Integrity  availablity
print('graph basics')
#kruskals algo for MST

#edge = sorted(edges, key = lambda e:e.weight)
#parent = [i for i in range(n)]
#
#def find(x):
#    if parent[x] != x:
#        parent[x] = find(parent[x])
#    return parent[x]
#def union(x,y):
#    parent[find(x)] = find(y) 
#
#mst = []
#for edge in egdes:
#    u,v = weight.u, weight.v
#    if find(u) != find(v):
#        

coins = [10,5,2,1]
min = 1000
max = 0
for i in range(len(coins)):
    if max < coins[i] :
        max = coins[i]
    if min > coins[i]:
        min = coins[i]
print(min,max) 

# G is a weighted graph 
# g = (v,e)
# T = @
# e' = {e1,e2,e3,...}
# tree must not have acycle graph can have

parent = [i for i in range(6)]
print(parent)

#Union find data structure for cycle detection 
#Used in kruskal's algorihm to detect cycles 


#https://students-old.masaischool.com/lectures/132162?tab=notes
#Faculty Lecture 14 - Heap Data Structure

#heap sort will resolve the sorting time complexity to O(nlog n)
#and space complexity to O(1)

#ith  root, 2ith left subtree, 2i + 1the right
#key of a node must be greater than or eq to the key of the 
#child node at Max Heap
#Max Heapify
#MaxHeap height is "log n"  so heapify tc = O(log n)

class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
# Tree structure:
#            16
#          /    \
#        14      10
#       /  \    /  \
#      8    7  9    3
#     / \  
#    2   4
#   /
#  1
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1  # zero-based index
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def insert(heap, key):
    heap.append(key)  # Insert at the end
    i = len(heap) - 1
    # Bubble up
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] < heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break


def extract_max(heap):
    if len(heap) == 0:
        return None
    maximum = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    max_heapify(heap, len(heap), 0)
    return maximum


#Faculty Lecture 15 - Prims algo and huffman coding
#https://students-old.masaischool.com/lectures/132774?tab=notes




  




