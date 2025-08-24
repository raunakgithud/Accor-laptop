#Binary_search
print("Brute_force")

print("------------------------------------------")

#The Brute Force Approach is a straightforward method to 
# solve problems by 
# trying all possible configurations or solutions.

#Characteristics:
#Simplicity: Very easy to implement
#Exhaustive: Checks all possible solutions without skipping any
#When to use:
#When the problem size is small
#When no efficient algorithm is known

print("Linear Search using Brute Force Approach")
def linear_search(list,target):
    for i in range(len(list)):
        if list[i] == target:
            print(f'index is:{i}')

num = [3,9,7,5,1,0,3] 

find = 1

finding = linear_search(list=num,target=find)
print(finding)

print("------------------------------------")

print("Binary Search is an efficient search technique that works on sorted lists.")

#How it works:
#Check the middle element of the sorted list.
#If the middle element equals the target, return its position.
#If the target is greater, discard the left half and continue searching in the right half.
#If the target is smaller, discard the right half and continue in the left half.
#Repeat until the target is found or the list segment is empty.

#Characteristics:
#Requires the list to be sorted
#Works by halving the search space each time
#Much faster than linear search for large datasets

print("binary search example")

def binary_search(num,element):
    low = 0
    high = len(num)
    mid = (low + high)//2
    while low <= high:
        if num[mid] == element:
            return mid
        elif element > mid:
            low = mid + 1
        else:
            high = mid -1

bs = binary_search(num=[23,34,56,78,102,104],element=34)

#list should be sorted for binary search
