#heapassignment

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
n = len(arr)
ak = [[0]*(k)]*(n-k+1)

print(ak)   
#print(len(ak))
#print(len(ak[0]))

l = len(ak)
w = len(ak[0])

i = 0
j = 0

while i < l:
    
    #print(z,end="' ")
    

    while j < w:
        ak[i][j] =  arr[i+j]
        
        j+=1
        #print(j,end="* ")

    i+=1
    #print(i,end=" -")    
print(ak)

for i in range(l):
    for j in range(w):
        ak[i][j] = arr[i+j]

print(ak)

def fn(arr,n,k):
    ak = [[0]*(k)]*(n-k+1)
    l = len(ak)
    w = len(ak[0])
    i = 0
    while i < l:
        j = 0
        while j < w:
            ak[i][j] = arr[i+j]
            j += 1
        i += 1
    return ak        

print(fn(arr,len(arr),3))

print(max(arr))


#from collections import deque
#
## Input
#n, k = map(int, input().split())
#arr = list(map(int, input().split()))
#
#dq = deque()
#result = []
#
#
#
#for i in range(n):
#
#    # Remove elements out of current window
#    while dq and dq[0] <= i - k:
#        dq.popleft()
#
#    # Remove smaller elements from back
#    while dq and arr[dq[-1]] < arr[i]:
#        dq.pop()
#
#    dq.append(i)
#
#    # Window starts producing answers
#    if i >= k - 1:
#        result.append(arr[dq[0]])
#
## Output
#print(*result)






