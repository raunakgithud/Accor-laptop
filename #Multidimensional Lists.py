#Multidimensional Lists

list = [12,34,56,65,43,2,3,4,102]
print(list)
list_sort = []
while (len(list)>0):
    min = list[0]
    for i in range(len(list)):
        if (list[i]<min):
            min = list[i]

    list_sort.append(min)
    list.remove(min)


print(list_sort)

print("-----------------------------------")
colors = ['red','blue','green','yellow','red']
colors_select = ""
while (colors_select != "quite"):
    colors_select = input("color please")
    if(colors.count(colors_select)>=1):
        print("color is exist")
    else:
        print("color doesnt exists")

##--------------------------
print("----------------------")

import numpy as np

list_mat = np.array(list_sort)

print(list_mat)

print(np.arange(5,5))

print("-----------------------")

#multidimentional list dot product

l = [1,2,3,6,8]
add = 0
for i in range(len(l)):
    add += l[i]


print(add)

print("------------------------------")

l1 =[1,5,8,9,3]
l2 =[8,5,3,1,4]

#sum of products is dot product

sum = 0
if(len(l1) == len(l2)):
    for i in range(len(l1)):
        sum += l1[i]*l2[i]


print(sum)  # dot product is a scaler value

print("------------------------")

# matrix multiplication 

r1 = [2,1,4]
r2 = [6,3,1]
r3 = [9,7,1]

s1 = [3,7,2]
s2 = [8,2,6]
s3 = [2,8,1]

A = []
B = []

A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

summ = [[0,0,0],[0,0,0],[0,0,0]]

if(len(A)==len(B)):
    for i in range(len(A)):
        if(len(A[i])==len(B[i])):
            for j in range(len(A[i])):
                summ[i][j] = A[i].B[j]

print(summ)

print("-------------------------")

#def minimumOfThree(a,b,c):
  # write your code here
a = 11
b = 3
c = 17
num = 999
for i in (a,b,c):
  if(num>i):
    num = i
print(num)

    









    
    

