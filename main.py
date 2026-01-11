'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''

print("Hello World")

A = [2, 4, 6, 8, 10, 19]
B = [1, 2, 3, 4, 5, 11, 17, 19]

ina = 0
inb = 0

C = []

while ina < len(A) and inb < len(B):
    if A[ina] <= B[inb]:
        C.append(A[ina])
        ina += 1
    else:
        C.append(B[inb])
        inb += 1
        

C.extend(A[ina:])
C.extend(B[inb:])

print(C)







