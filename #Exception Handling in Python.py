#Exception Handling in Python

print("-------------------------------------")
#Sorting is the process of rearranging elements in a list 
# according 
# to a certain order (ascending or descending).

#Bubble Sort is one of the simplest sorting algorithms using 
#the brute force approach.
#It works by repeatedly swapping adjacent elements 
#if they are in the wrong order.
#It is an in-place algorithm (does not require extra space).
#It operates by comparing pairs of adjacent elements and swapping them if needed.
#After each full pass, the largest unsorted element "bubbles up" to its correct position.

# Buble short

A = [3,6,7,8,1,0,2]
print(A)
count = 0 
for j in range(len(A)-1):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
            count += 1
print(A)
print(count)


print("--------------------------------------------------")

print("Optimization of Buble sort")

l = [8,2,3,6,0,1]
c = 0
N = len(l)
for j in range(N-1):
    for i in range(N-1):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]  #pythonic swap
            c += 1
print(l)
print(c)

print("-----------------------------------")

print("Swaping two elements in python for sorting")

#Using a temporary variable:
#
#Store one element in a temporary variable.
#Assign the second element's value to the first element's position.
#Assign the temporary stored value to the second element's position.

#temp = x
#x = y
#
#y = temp

#Algorithm: A step-by-step procedure or formula to solve a problem, represented in an abstract way.
#Pseudo code: Writing the algorithm in a simplified, readable language resembling programming code but not following a strict syntax.
#Code: The actual implementation of the pseudo code in a specific programming language which can be compiled or interpreted.





