#practice heap assignment
#
## name = input()                  # Reading input from STDIN
## print('Hi, %s.' % name)         # Writing output to STDOUT
#
#
##k = input()
#arr = [1, 3, -1, -3, 5, 3, 6, 7]
#k = 3
#n = len(arr)
#ak = []
#i = 0
#j = 0
#while i < n:
#
#    while j < k:
#        ak.append[arr[i]]
#        i += 1 
#j += 1    
#        
#        
#    
# 

heap = [10, 9, 8, 4, 2, 5, 6]
n = len(heap)
i = 1
count = 0
while (2*i + 1) < n :
    if heap[2*i] < heap[2*i+1]:
        count += 1
    i+=1
#print(count)        
    
def heapcount(heap):
    n = len(heap)
    i = 1
    count = 0
    while (2*i + 1) < n :
     
     
     if heap[2*i] < heap[2*i+1]:

        count += 1
     i+=1
    return count

print(heapcount(heap))


#k = input()
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
n = len(arr)
ak = [[0]*(k)]*(n-k+1)
i = 0
j = 0
#while i+k-1 < n-1:
#   while j < i + k-1 :
#      ak[i][j] = arr[j]
#      j += 1
#   i += 1
#   i = j
print(ak)   
print(len(ak))
print(len(ak[0]))
i = 0
j = 0
l = len(ak)
w = len(ak[0])
while i < l :
   
   while j < w and k == i:
      ak[i][j] = arr[k]
      j += 1
      k += 1
   i += 1
   
print(ak)     
   


   
 




        
    
       

