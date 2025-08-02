#Assesment



list = ["!","@","#","$","%","^","&","*" ]
i = len(list)
N = 10 
j = 0
while(N < 25) & (j <= i-1 ):
    print(list[j],"-",N)
    N = N+2
    j = j+1


#######################################    


def solve(color):
    color = 'Green'
    nextcolor = 'currentState'
    if(color == "Red"):
        nextcolor = 'Green'
        print(nextcolor)
    elif(color == 'Green'):
        nextcolor = 'Yellow'
        print(nextcolor)

    else:

        nextcolor = 'Red'
        print(nextcolor)


solve('color')


######################################


list = ["!","@","#","$","%","^","&","*" ]
i = len(list)
N = 10 
j = 0
while(N < 25) & (j <= i-1 ):
    print(list[j],"-",N)
    N = N+2
    j = j+1

list1 = ["!","@","#","$","%","^","&","*" ]
i1 = len(list)
N1 = 10 
j1 = 0
while(N1 < 25) & (j1 <= i1-1 ):
    d ={
    list1[j1]: -N1
    }
    print(d)
    N1 = N1+2
    j1 = j1+1


print(d);


arr = [3,5,3,3,8,5,6]
 
 #print(arr)
 
n = len(arr)
 
dist = {}
 
for i in range(n):
    if arr[i] in dist:
      dist[arr[i]] = dist[arr[i]] + 1
    else:
      dist[arr[i]] = 1
   
   
     
  
      
       
    
      
     
     
     
print(dist)     
 
 
t = 0
 
 #for key in dist:
  # if(dist[key]==1):
   #  t = t + int(key)
     


  #print(t)

for key in dist:
   if(dist[key] == 1):
      t = t + int(key)


print(t)


#########################

string = 'wisfghtr'


din = {
   'w' : 0,
   'i' : 0,
   's' : 0,
   'h' : 0
}

print(din)

for i in range(len(string)):
   if string[i] in din:
      din[string[i]] = din[string[i]] + 1
   

print(din)

print(string[0])
meanValue = 9999

for key in din:
   if(din[key]<meanValue):
      meanValue = din[key]


print(meanValue)


















    




