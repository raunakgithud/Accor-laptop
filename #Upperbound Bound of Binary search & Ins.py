#Upperbound Bound of Binary search & Insertion Sort


#In a sorted array, lower bound and upper bound help us find the positions related to a target element x with respect to its occurrences.
#
#Lower Bound of x is the first position in the array where the element is greater than or equal to x.
#Upper Bound of x is the first position in the array where the element is strictly greater than x.
#Example: Given array A = [2, 2, 2, 2, 3, 4, 9, 100] and x = 2:
#
#Lower bound of 2 provides index 1 (first occurrence of 2).
#Upper bound of 2 provides index 5 (first element greater than 2 is 3 at index 5).

#Algorithm to find Upper bound

#The logic resembles binary search with a slight modification:
#
#Initialize low = 1, high = n + 1 (assuming 1-based indexing).
#While low < high:
#mid = floor((low + high)/2)
#If A[mid] <= x, set low = mid + 1
#Else set high = mid
#Return low
#If no element is greater than x, return -1 or the indicator for no upper bound.

def upperbound(a,n,x):
    low = 1
    high = n+1
    while low < high:
        mid = (low + high)//2
        if a[mid] <= x:
            low = mid + 1
        else:
            high = mid
    if low > n:
        return -1
    else:
        return low




#Insertion sort algorithm
def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key


#In-place sorting algorithm: Sorts data using only a small, constant amount of extra space beyond the original array.
#Example: Insertion Sort, Selection Sort, Bubble Sort
#Out-place sorting algorithm: Requires significant extra space for sorting.
#Example: Merge Sort (requires extra arrays)

#Insertion Sort is an in-place sorting algorithm.

arr = [7,0,5,6,1,3]
print(insertionsort(arr))

print(arr)
