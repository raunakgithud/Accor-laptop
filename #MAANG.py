 #MAANG

a = [2, 1, 4, 6]

arr = [
  [2, 4, 6, 8],
  [5, -1, 3, 7],
  [9, 10, 11, 12]
]

print(a)
print(arr)

#traversing all elements of the 2d array 

def traversing(arr,m,n):  #m is no of rows, n is no of col
    T = []
    S = 0
    for i in range(m):
        for j in range(n):
            T.append(arr[i][j])
            S += arr[i][j]
    return T,S


print(traversing(arr,3,4))

def fn(arr,n):  # diagonal traversing
    i = 0 
    j = n-1
    T = []
    S = 0
    while i< n and j >= 0:
        T.append(arr[i][j])
        S += arr[i][j]
        i += 1
        j -= 1
    return S,T

arr1 = [
  [1, 2, 3, 4],
  [4, 5, 6, 7],
  [7, 8, 9, 10],
  [10, 11, 12, 13]
]   

print(fn(arr1,4))  #opposite diagonal travers

def fndiag(arr,n):
    i = 0
    j = 0
    T= []
    s = 0
    while i < n and j < n:
        T.append(arr[i][j])
        s += arr[i][j]
        i += 1
        j += 1
    return T,s

print(fndiag(arr1,4))   #diagonal travers

#L shaped traversal of n*m traversal

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
] # 4*5 matrix n*m

def Ltraversal(arr,n,m):
    i = 0
    j = 1
    while i < n:   # can be used [for _ in range(n)] 
        print(arr[i][0])
        i += 1
    while j < m :  # [for _ in range(1,m)]
        print (arr[n-1][j],end=" ")
        j += 1


print(Ltraversal(matrix,4,5))

#Z shaped traversal 

matrix1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]  
# n*n matrix 5*5 matrix

def Ztraversal(arr,n):
    for i in range(n):
        print(arr[0][i],end=" ")
    i = 1
    j = n-2
    while i < n and j >= 1:
        print(arr[i][j],end = " ")
        i += 1
        j -= 1
    for i in range(1,n):
        print(arr[n-1][i],end=" ")    

print(Ztraversal(matrix1,5))

#N traversal
# matrix should be a square matrix 
def Ntraversal(arr,n):
    for i in range(n-1,0,-1):
        print(arr[i][0],end=" ")
    i = 0
    j = 0
    while i < n and j < n:
        print(arr[i][j],end = " ")
        i += 1
        j += 1
    #for i in range(n-2,0,-1):
    #    print(arr[i][n-1],end=" ")
    i = n-2
    while i >= 0 :
        print(arr[i][n-1],end=" ")
        i -= 1

matrix1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]  
print(Ntraversal(matrix1,5))

#spiral travarsal

spiral_matrix = [
  [1, 2, 3, 4, 5, 6],
  [7, 8, 9, 10, 11, 12],
  [13, 14, 15, 16, 17, 18],
  [19, 20, 21, 22, 23, 24],
  [25, 26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35, 36],
  [37, 38, 39, 40, 41, 42]
]  #n*m matrix 7*6

def spiral_travarsal(arr,n,m):
    top = 0
    bottom = n-1
    fist = 0
    last = m-1
    for i in range(fist,last+1,1):
        print(arr[top][i],end=" ")
    top += 1
    for i in range(top,bottom+1,1):
        print(arr[i][last],end=" ")
    last -= 1
    for i in range(last,fist,-1):
        print(arr[bottom][i],end=" ")
    bottom -= 1
    for i in range(bottom,top,-1):
        print(arr[i][fist],end=" ")
    fist += 1
                    
print(spiral_travarsal(spiral_matrix,7,6))        





















        

         


