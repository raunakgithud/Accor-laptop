#searching_algo_Binary-search

print('--searching--')

def binary_search(a,p,q,x):
    if p>q:
        return -1
    mid = (p+q)//2
    if a[mid] == x:
        return mid
    if a[mid] > x:
        return binary_search(a,p,mid-1,x)
    if a[mid] < x:
        return binary_search(a,mid+1,q,x)
    

#finding the first occurence of an element in an sorted array
array = [3, 6, 8, 8, 8, 12, 15] #find the 1st occurence of 8
#using binary search recursively to find lower bound of x
def lower_bound(a,x):
    low,high = 0,len(a)
    while low < high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

#alternate approaches,check if previous element is < target

def fist_occurence(arr,x):
    pos = lower_bound(arr,x)
    if pos < len(arr)  and arr[pos] == x :
        return pos
    return -1

#Faculty Session 5 - Upperbound Bound of Binary search & Insertion Sort

A = [2, 2, 2, 2, 3, 4, 9, 100] # upper and lower bound of 2

def upper_bound(arr,x):
    low,high = 1,len(arr)+1
    while low < high:
        mid = (low + high)//2
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low

print(lower_bound(A,2))
print(upper_bound(A,2))


#insertion sort algorithm

def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i - 1
        while j>=0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
            

        

    
        