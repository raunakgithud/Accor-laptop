#merge_sort

print('merge_sort')

#merging tw sorted array in a single array 

A = [2, 4, 6, 8, 10, 19]
B = [1, 2, 3, 4, 5, 11, 17, 19]

inA = 0
inB = 0
C = []
while inA < len(A) and inB < len(B):
    if A[inA] <= B[inB]:
     C.append(A[inA])
     inA += 1
else:
    C.append(B[inB])
    inB  += 1

C.extend(A[inA:])
C.extend(B[inB:])

print (C)



