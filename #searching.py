#searching
#Indexing in Lists:

#
#Indexing is the way to find the position of elements in a list. In Python, indexing starts from 0.
#The first element is at index 0.
#The second element is at index 1, and so on.
#Searching an Element (Linear Search):
#
#To find the position of an element in a list, we can iterate through the list and compare each element with the target element until we find it.
#
#Algorithm Steps:
#
#Iterate over the list from index 0 to the end.
#Compare the element at the current index with the target element.
#If they match, return the index.
#If the end of list is reached without finding the element, return -1 to indicate the element is not found.
#Code Example:
#
list = [56,98,34,23,12,45,67]
target = int(input("please enter the element"))
index = 0
#for i in range(len(list)):
#    if list[i] == target:
#        print(i)
#
#        print(list[i])


for i in range(len(list)):
    if list[i] == target:
        print(f"index value is {i} for targrt{target}")

    #else:
       # print("target is not there")


#Steps of Selection Sort:
#
#Start with an unsorted list.
#Assume the first element is the minimum.
#Loop through the unsorted list to find the actual minimum.
#Append the minimum to a new sorted list.
#Remove the minimum from the unsorted list.
#Repeat until the unsorted list is empty.   
# 
# 

print("----------------")
print(list)   #Start with an unsorted list.
   #Assume the first element is the minimum.
#for i in range(len(list)):
#    if (list[i]<min):
#        min = list[i]
#print(min)
count =0
list_sort = []
l = len(list)
while(len(list)>0): #Repeat until the unsorted list is empty. 
    min = list[0] #Assume the first element is the minimum.
    for i in range(len(list)):
        if(min>list[i]):  #Loop through the unsorted list to find the actual minimum.
            min = list[i]
    list_sort.append(min)  #Append the minimum to a new sorted list.
    list.remove(min)  #Remove the minimum from the unsorted list.
    
print(list_sort)
print(list)


#matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]
#
#print(matrix)

#Matrix Operations Using Nested Loops:
#
#To perform element-wise operations between two matrices of the same size, you can use nested loops.
#
#Outer loop iterates over rows.
#Inner loop iterates over columns.
#Example: Matrix Addition:

X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

print("Addition Result:")
for row in result:
    print(row)
#Similarly, you can change the operator to -, *, or / for subtraction, multiplication, or division respectively.
#
#Using List Comprehension:

# Subtraction
result = [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("matrix:")
print(matrix)
rows = len(matrix)
cols = len(matrix[0])

transpose = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

print("Transpose of matrix:")
for row in transpose:
    print(row)
print("------------------------------")
import numpy as np

# Create NumPy arrays from lists
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

Y = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

#Other Features:
#
#Random matrix generation: np.random.randint(low, high, size=(rows,cols))
#
#Creating zero matrices: np.zeros((rows, cols))
#
#Transpose: np.transpose(matrix) or matrix.T
#
#Matrix multiplication (dot product): np.dot(X, Y)
#
#Cross product: np.cross(X, Y)
#
#Delete row or column: np.delete(matrix, index, axis) (axis=0 for rows, axis=1 for columns)
#
#Adding Rows or Columns:

# To add a column to a matrix
new_col = np.array([[1], [2], [3]])
X_new = np.hstack((X, new_col))
print("-------------------")
A = [2, 3, 4, 5]

# Square each element
squared = [val**2 for val in A]

print(squared)  # Output: [4, 9, 16, 25]

print(new_col)



    
            


    

    


    
    