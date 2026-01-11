'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''

print("Hello World")

def partition(arr,low,high):
    pivot = arr[high]
    i = low -1 
    for j in range(low,high):
        if arr[i] < pivot:
            i += 1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1 
    
arr = [3, 6, 8, 10, 1, 2, 1]
print(arr)
p = partition(arr,0,len(arr)-1)

print(arr)

print(p)

def quik_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quik_sort(arr,low,pi-1)
        quik_sort(arr,pi+1,high)
        

arr1 = [10, 7, 8, 9, 1, 5]






quik_sort(arr1,0,len(arr1)-1)
print(arr1)


import random

def randomize_partition(arr,low,high):
    pivot_index = random.randint(low,high)
    arr[pivot_index],arr[high] = arr[high],arr[pivot_index]
    return partition(arr,low,high)


def randomize_quick_sort(arr,low,high):
    pi = randomize_partition(arr,low,high)
    randomize_quick_sort(arr,low,pi-1)
    randomize_quick_sort(arr,pi+1,high)
    
    




        




    
    