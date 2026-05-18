#Two_pointer

print('mang')
# remove duplicates
a = [1,2,2,2,3,4,4]
def unique(a):
    i = 0
    for j in range(1,len(a),1):
        if a[i] != a[j]:
            i += 1
            a[i] = a[j]
    for k in range(i):
        print(a[k], end=",")        
    return i+1        
              
    
print(unique(a))    

def merge(a1,a2):
    i = j = 0
    k = 0
    marr = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            marr[k] = a1[i]
            i += 1
            k += 1
        else:
            marr[k] = a2[j]
            k += 1
            j += 1
    while i < len(a1):
        marr[k] = a1[i]
        k += 1
        i += 1
    while j < len(a2):
        marr[k] = a2[j]
        k += 1
        j += 1

    return marr                    
a1 = [1, 3, 5, 7 ]
#a2 = [2 ,4, 6 ,8 ,9 ]
#print(merge(a1,a2))
arr = [2 ,4, 6 ,8 ,9 ] 
def max_water(arr):
    n = len(arr)
    a = []
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j] and i > j:
                a.append(arr[i]*(i-j))
            else:
                a.append((min(arr[j],arr[i]))*(max(i,j)-min(i,j)))
    c = 0 
    for i in range(len(a)):
        if c < a[i]:
            c = a[i]
    return c,a


        


print(max_water(arr))

#def maxwater(arr):
#    i = 0
#    j = len(arr) -1 
#
#    while i < j :
#        area = (j-i)*max(arr[i],arr[j])
#        if arr[i] < arr[j]:
#            i += 1
#        else:
#            j -= 1
#                

def if_sortednRotated(arr):
  count = 0
  n  = len(arr)
  for i in range(n-1):
    if arr[i] > arr[i+1] :
      count += 1 
  if count < 0 :
    return 'No'
  return 'Yes'

case = [3, 4, 7, 9, 1, 2]
print(if_sortednRotated(case))


