#test

#Loops and Lists
N = 4
l1 =[]
l2 =[]
l3 = []
l4 = []
count = 1
while (count<= N*N):
    for i in range(1,N+1):
        l1.append(i)
    for i in range(N+1,N+5):
        l2.append(i)
    for i in range(N+5,N+9):
        l3.append(i)
    for i in range(N+9,N*N+1):
        l4.append(i)

    count +=1
print(l1)
print(l2)
print(l3)
print(l4)


