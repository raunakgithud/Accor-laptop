#Heap--1138220234

print('Heap data structure')

#for max hepify assumes that its left and right nodes are already 
#max heap

def max_heapify(arr,i,n):
    largest = i
    left = 2*i
    right = 2*i + 1
    if left < n and arr[left] > arr[largest]:  
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i :
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,largest,n)


#insert an element to a heap 

def insert_heap(heap,key):
    heap.append(key)
    i = len(heap)-1
    while i > 0:
        parent = (i-1)//2
        if heap[parent] < heap[i]:
            heap[parent],heap[i] = heap[i],heap[parent] 
            i = parent
        else:
            break

heap1 =[11,9,8,3,2]

insert_heap(heap1,16)
print(heap1)
max_heapify(heap1,len(heap1),0)
print(heap1)


def extract_min_heap(heap):
    if len(heap) == 0:
        return None
    maximum = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    max_heapify(heap,len(heap,0))
    return maximum



#heap data structure is not at all good for searching
#T.C. for searching an element in a heap structure will
#take O(n) time 

def build_maxheap(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        max_heapify(arr,i,n)


a = [7,0,5,3,2,4]

print(build_maxheap(a))
print(a)

def heap_sort(arr):
    n = len(arr) - 1
    build_maxheap(arr)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        max_heapify(arr,i,n)

#find smallest k elements in the array 
#introducing mean heap to find the k smallest element in an
#unsorted 
#array

def smallest_kelements(arr,k):
    n = len(arr)
    max_heapify(arr,0,n)
    result = []
    for i in range(k):
        result.append(arr.pop())
    return result
a1 = [0,9,5,1,4,3]
print(smallest_kelements(a1,3))

from heapq import heappush,heappop
def prims_algorithm(graph):
    mst = []
    visited = set()
    min_heap = []
    start_vertex = 0
    visited.add(start_vertex)
    for edge in graph[start_vertex]:
        heappush(min_heap,edge) # edge: weight,start v , end v
    while min_heap:
        weight,u,v = heappop(min_heap)
        if v not in visited:
            visited.add(v)
            mst.append(u,v,weight)
            for next_edge in graph[v]:
                if next_edge not in visited:
                    heappush(min_heap,edge)
    return mst
                


    






