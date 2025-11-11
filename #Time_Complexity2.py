#Time_Complexity2

#linear search
def linear_search(arr,target):
    N = len(arr)
    for i in range(N):
        if target == arr[i]:
            return i
    return-1


arr1 = [1,2,5,7,4,8]
search = 5
ls = linear_search(arr=arr1,target=search)

print(ls)

if ls != -1:
    print(ls)
else:
    print("target not found")


#Binary search

#Binary Search is an efficient search algorithm that works only on a sorted array. It uses the divide and conquer strategy.
#
#The algorithm compares the target value to the middle element of the sorted array.
#If they are equal, the search is complete.
#If target is less than the middle element, the search continues in the left half.
#If target is greater, the search continues in the right half.
#Time complexity is O(log n).
#Key Point: The array must be sorted for binary search to work correctly.

#iterative binary_search

def I_banary_search(array,t):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) //2
        if array[mid] == t:
            return mid
        elif array[mid] < t:
            low = mid + 1
        else:
            high = mid -1

    return -1
#recursive binary search
def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return recursive_binary_search(arr, target, low, mid - 1)


#Space Complexity:
#
#Iterative binary search uses O(1) space.
#Recursive binary search uses O(log n) space due to the call stack.
#==========================================================
#Sorting algorythm and time complexity

#Selection Sort:
#
#Finds the minimum element and swaps it with the first element; repeats for next positions.
#Time Complexity: O(n^2).

#Merge Sort:
#
#Divides the array into two halves, recursively sorts each half, then merges.
#Time Complexity: O(n log n).
#Uses recursion and divide and conquer approach.

#====================================================
print("=====selection_sorting==========")

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i] 
        





arr2 = [3,9,2,5,1,7,0]

selection_sort(arr=arr2)
print(arr2)

#=================merge sort=============================#

def merge_sort(arr):
    if len(arr) > 1:
        mid_arr = len(arr)//2
        left_arr = arr[:mid_arr]
        rigt_arr = arr[mid_arr:]
        merge_sort(left_arr)
        merge_sort(rigt_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(rigt_arr):
            if left_arr[i] < rigt_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = rigt_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(rigt_arr):
            arr[k] = rigt_arr[j]
            j += 1
            k += 1


print('========merge_sort=================')

#Recurrence relations and time complexity

#Recurrence Relations are equations that define sequences 
#recursively and are used to analyze the time complexity of 
#recursive algorithms such as merge sort and recursive 
# binary search.

#They express the running time of an algorithm 
#in terms of the running time of smaller inputs.
#Example: For merge sort, the time complexity satisfies the recurrence: T(n) = 2T(n/2) + O(n) where 2T(n/2) is the time to sort two halves, and O(n) for merging.
#
#Techniques to solve recurrence relations include:
#
#Master Theorem
#Substitution Method
#Recursion Tree Method
#Understanding these helps in mathematically deriving time complexities for recursive algorithms.













