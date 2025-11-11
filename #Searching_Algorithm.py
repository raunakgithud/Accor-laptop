#Searching_Algorithm


#The searching problem can be defined both informally and formally:
#
#Informal Definition: Given a list or array A of n elements (not necessarily sorted) and an element x to search, we want to find if x is present and if so, at which index.
#Formal Definition: Input is an array A and element x. Output is an index i such that A[i] == x, or -1 if x is not in A.
#In this context, indexing is typically assumed to start from 1 for the sake of algorithm explanation, and the focus is on algorithmic logic rather than programming language syntax.

#Concept: Linear Search iterates through each element of the array from start to end, comparing each element with the target x until it finds a match or reaches the end.

def linear_search(A,x):
    n = len(A)
    for i in range(n):
        if A[i] == x:
            return i


print("function created successfully")

arr = [1,9,0,5,4,3]
ex = linear_search(arr,3)
print(ex)

#Binary_search algorithm
#Example: For array A = [1, 3, 0, 0, -4, -2, 10, 11, 100] and X = 0 the search will check elements in order until it finds 0 at index 3 or 4.
#
#Time Complexity:
#
#Best Case: O(1) when the element is at the first position.
#Worst Case: O(n) when the element is at the end or not present.
#Average Case: O(n), deriving average by summing comparisons done per possible position and dividing by n.
#Space Complexity: O(1) as it only uses constant extra space.
#
#This is a simple, straightforward method suitable for unsorted arrays.

#function BinarySearch(A, p, q, x):
#  if p > q:
#    return -1
#  mid = floor((p + q) / 2)
#  if A[mid] == x:
#    return mid
#  else if A[mid] > x:
#    return BinarySearch(A, p, mid - 1, x)
#  else:
#    return BinarySearch(A, mid + 1, q, x)


#Concept: Binary Search efficiently searches for an element x in a sorted array A of size n by repeatedly dividing the search interval in half.
#
#Key Requirements:
#
#The array must be sorted (in increasing or decreasing order).
#Random access is required to quickly access the middle element.
#Algorithm Idea:
#
#Find the middle element of the array.
#Compare middle element with x.
#If equal, return middle index.
#If x is smaller, repeat search on left sub-array.
#If x is larger, repeat search on right sub-array.
#Continue this process until the element is found or the sub-array size reduces to zero.
#Pseudocode:
#
#function BinarySearch(A, p, q, x):
#  if p > q:
#    return -1
#  mid = floor((p + q) / 2)
#  if A[mid] == x:
#    return mid
#  else if A[mid] > x:
#    return BinarySearch(A, p, mid - 1, x)
#  else:
#    return BinarySearch(A, mid + 1, q, x)





