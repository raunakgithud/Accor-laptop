#Merge_sort

#time complexity O(nlogn)///Given two sorted arrays A and B of 
#size n, the goal is to merge them into a single 
#sorted array C of size 2n containing all elements 
#from A and B.


a = [4,7,8,3,2,9]
b = [9,1,78,32,98,33,54] 
indexa = 0
indexb = 0
c = []
print(c)
while indexa < len(a) and indexb < len(b):
    if a[indexa] <= b[indexb]:
        c.append(a[indexa])
        indexa += 1
    else:
        c.append(b[indexb])
        indexb += 1

c.extend(a[indexa:])
c.extend(b[indexb:])
print(c)# both a and b are not 

# Merge two sorted arrays A and B
A = [2, 4, 6, 8, 10, 19]
B = [1, 2, 3, 4, 5, 11, 17, 19]

# Initialize pointers
indexA = 0
indexB = 0
C = []

while indexA < len(A) and indexB < len(B):
    if A[indexA] <= B[indexB]:
        C.append(A[indexA])
        indexA += 1
    else:
        C.append(B[indexB])
        indexB += 1

# Copy remaining elements
C.extend(A[indexA:])
C.extend(B[indexB:])

print(C)  # Output: [1, 2, 2, 3, 4, 4, 5, 6, 8, 10, 11, 17, 19, 19]

#time complexity is O(n)

#Merge sort is a divide and conquer, recursive sorting algorithm that sorts an unsorted array efficiently in O(n log n) time.


#If array size is 1 or less, it is already sorted.
#Divide the array into two halves.
#Recursively sort each half using merge sort.
#Merge the two sorted halves using the merge procedure described above.

def merge(arr):
    n = len(arr)
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    i = j = k = 0
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

merge(a)
print(a)
array = [99,76,43,23,97]
merge(array)
print(array)
print(merge(array))

#Time Complexity:
#
#Recurrence: T(n) = 2T(n/2) + O(n)
#Using Master theorem, time complexity is O(n log n)
#Space Complexity:
#
#Merge sort uses O(n) extra space due to the temporary arrays used during merging.
#The recursion call stack uses O(log n) space.
#Total space complexity is O(n).

#Merge sort recurrence relation:
#
#T(n) = 2*T(n/2) + cn
#Divides the problem into two subproblems of size n/2.
#Merging step takes O(n) time.
#Solving the Recurrence (Master Theorem):
#
#a = 2 (number of recursive calls)
#b = 2 (each subproblem is size n/2)
#f(n) = cn (time to merge)
#n^(log_b a) = n^(log_2 2) = n
#Since f(n) = O(n), f(n) matches n^(log_b a)
#Case 2 of Master theorem applies:
#T(n) = Theta(n log n)
#Therefore, Merge Sort runs in O(n log n) time for best, worst, and average cases.
#
#This time complexity does not depend on the initial order of the array because the algorithm always divides the array and merges regardless of the input.

