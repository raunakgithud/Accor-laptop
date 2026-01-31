'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")

#In a Max Heap, the value of each node is greater than or equal to the values of its children, with the maximum element at the root.
#In a Min Heap, the value of each node is smaller than or equal to the values of its children, with the minimum element at the root.
#Important properties:
#
#The tree is almost complete (filled from left to right).
#Height of the heap is O(log n).

def maxHeapify(arr, i, n):
    
    
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, n)

def buildmaxheap(arr):
    n = len(arr)
    for i in range(n//2 -1,-1,-1):
        maxHeapify(arr,i,n)
        
#build max heapify time complexity O(n)

import heapq

def smallest_k_elements(arr, k):
    heapq.heapify(arr)  # builds min heap in O(n)
    result = []
    for _ in range(k):
        result.append(heapq.heappop(arr))  # extract min
    return result


