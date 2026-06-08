#IRP-slidding window

def sliding_windwo(arr,n,k):
    beg,sum,count = 0,0,0
    for end in range(n):
        sum += arr[end]
        while sum < k and beg <= end:
            sum -= arr[beg]
            beg += 1
        count += 1
    return count

#largest substring with k repeating characters
#'aaabb'

def longest(s,k):
    N = len(s)
    d = {}
    for i in range(N):
        d[s[i]] = 0
        count = 0
    for i in range(N):
        for key in d:
            if s[i] == key:
                d[key] += 1
            if d[key] >= k:
                print(key, end=" ")    
                
         
                

print(longest(s='aaabb',k=3))
print(longest(s='ababb',k=2))

def isvalid(subs,k):
    charfreq = {}
    for i in range(len(subs)):
        charfreq[subs[i]] = 0
        for key in charfreq:
            if key == subs[i]:
                charfreq[key] += 1
                if charfreq[key] < k:
                    return False
                return True
    

def longest_sub(s,k):
    maxlen = 0
    for start in range(len(s)):
        for end in range(start,len(s),1):
            subs = s[start:end]
            while subs:
                maxlen = max(maxlen,end - start)
    return maxlen                

import os
nonse = os.urandom(16)
print(nonse.hex())


#Low lwbwl design
#Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already sorted
        for j in range(0, n - i - 1):

            # Swap if current element is greater than next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
#            
#Selection Sort works by:
#
#Finding the smallest element
#Swapping it with the first unsorted element
#Repeating for the remaining array
#

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        # Assume current position has minimum element
        min_index = i

        # Find the minimum element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


